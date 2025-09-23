from PySide6 import QtWidgets
import os
import zipfile
import shutil
import lang

def unlock_files(locked_file): # Converts Excel file to .zip a removes sheetProtection
    if locked_file:
        print(lang.t("processing_file", file=locked_file))
            
        # Copy original file
        locked_file_path = os.path.join(locked_file)
        locked_file_dir, locked_file_name = os.path.split(locked_file_path)
        unlocked_file = os.path.join(locked_file_dir, f"unlocked_{locked_file_name}")
        
        # Check if unlocked file already exists, and add a number suffix if it does
        if os.path.exists(unlocked_file):
            base_name, ext = os.path.splitext(locked_file_name)
            counter = 1
            while os.path.exists(unlocked_file):
                unlocked_file = os.path.join(locked_file_dir, f"unlocked_{base_name}_{counter}{ext}")
                counter += 1
            print(lang.t("unlocked_file_exists", unlocked_file=unlocked_file))
        
        # Copy the file with the appropriate name
        shutil.copy(locked_file, unlocked_file)
        print(lang.t("file_copy_created", unlocked_file=unlocked_file))
        
        # Rename copy as .zip file
        unlocked_zip = f"{unlocked_file}.zip"
        os.rename(unlocked_file, unlocked_zip)
        print(lang.t("file_renamed", old_file=unlocked_file, new_file=unlocked_zip))
        
        # Process .zip file
        process_zip_file(unlocked_zip)
        QtWidgets.QMessageBox.information(None, lang.t("success_title"), lang.t("file_unlocked_successfully", unlocked_file=unlocked_file)) # Success information
    else:
        message = lang.t("no_file_to_unlock")
        print(message)
        QtWidgets.QMessageBox.warning(None, lang.t("error_title"), message)

# Functions for xlslock - App to unlock protected Excel files
def extract_zip(zip_file, target_folder): # Extract .zip file in a folder
    print(f"Extracting file: {zip_file}")
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(target_folder)
        print(f"File {zip_file} has been extracted to folder {target_folder}")

def find_and_remove_sheetProtection(source_folder): # Finds .xml files in xl/worksheets/ folder and removes sheetProtection tags
    worksheets_folder = os.path.join(source_folder, 'xl', 'worksheets')
    
    if not os.path.exists(worksheets_folder):
        message = lang.t("folder_not_exists", folder=worksheets_folder)
        print(message)
        QtWidgets.QMessageBox.warning(None, lang.t("error_title"), message)
        return
    
    for file in os.listdir(worksheets_folder):
        if file.endswith('.xml'):
            file_path = os.path.join(worksheets_folder, file)
            print(f"Processing XML file: {file_path}")
            edit_xml(file_path)

def edit_xml(file_path): # Removes sheetProtection tags from a .xml file
    print(f"Loading XML file: {file_path}")
    
    # Load contents of .xml file as text
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()
    
    # remove all sheetProtection tags (including those on more rows)
    while '<sheetProtection' in contents:
        start = contents.find('<sheetProtection')
        end = contents.find('/>', start) + 2  # Find the end of a tag
        contents = contents[:start] + contents[end:]  # Removes sheetProtection tag
    
    # Save edited content back into the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(contents)
    
    print(f"File {file_path} has been edited and saved.")

def compress_to_zip(source_folder, final_zip): # Recompression to .zip
    print(f"Compressing folder {source_folder} back into ZIP file {final_zip}")
    shutil.make_archive(final_zip.replace('.zip', ''), 'zip', source_folder)
    print(f"Folder {source_folder} has been compressed back into {final_zip}")

def process_zip_file(zip_file): # Convert to .zip file, remove sheetProtection and reconvert to original file type
    target_folder = zip_file.replace('.zip', '')
    
    # Extract .zip file
    extract_zip(zip_file, target_folder)
    
    # Find and remove sheetProtection tags
    find_and_remove_sheetProtection(target_folder)
    
    # Recompress to .zip
    compress_to_zip(target_folder, zip_file)
    
    # Remove temporary folder after success
    shutil.rmtree(target_folder)
    print(f"Temporary folder {target_folder} has been deleted")
    
    # Rename back to original format (remove .zip)
    original_file = zip_file.replace('.zip', '')
    os.rename(zip_file, original_file)
    print(f"File renamed back to {original_file}")