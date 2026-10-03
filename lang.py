"""Localization. XLSlock was originally written for Czech users, but an English version was needed too. Switch languages via 'current_lang'."""

current_lang = "en" # "cs" or "en"

bapp_texts = {
    "feedback_text_public": {
        "cs": """V případě problémů nebo nejasností budu ráda za email na <b>codebysophia@gmail.com</b> 
        ideálně s co nejpřesnějším popisem a snímky obrazovky. 
        Můžete zasílat i poděkování :), také vítám návrhy na další aplikace.""",
        "en": """In case of problems or questions, please send me an email at <b>codebysophia@gmail.com</b> 
        ideally with a detailed description and screenshots. 
        You can also send thanks :), and I also welcome suggestions for new apps."""
    },

    "xlslock_name": {"cs": "XLSLOCK - Odemčení Excel souboru", "en": "XLSLOCK - Unlock Excel files"},

    "error_title": {"cs": "Chyba", "en": "Error"},

    "invalid_format": {
        "cs": "Nepodporovaný formát souboru! Přidej Excel soubor (*.xls, *.xlsx, *.xlsm)",
        "en": "Unsupported file format! Please provide an Excel file (*.xls, *.xlsx, *.xlsm)"
    },

    "success_title": {"cs": "Úspěch", "en": "Success"},

    "xlslock_instructions": {
        "cs": """<h2>Instrukce k odemčení zaheslovaného Excel souboru</h2>
        <p> <b> Program odstraní ochranu heslem, kdy není možné upravovat listy. Na některé typy zaheslování nefunguje. </b> </p>
        <p>1. Přetáhni soubor do okna nebo klikni na tlačítko <b>'Vyber soubor k odemčení'</b> a zvol Excel soubor, který chceš odemknout.</p>
        <p>2. Jakmile vybereš soubor, klikni na <b>'Odemknout soubor'</b> a aplikace odemkne ochranu listů v souboru.</p>
        <p>3. Odemčený soubor bude uložen jako kopie s předponou <b>'unlocked_'</b> do původní složky.</p>
        <p>{feedback}</p>""",
        "en": """<h2>Instructions for unlocking a password-protected Excel file</h2>
        <p><b>The program removes sheet protection when editing is not possible due to a password. It does not work with some types of password protection.</b></p>
        <p>1. Drag and drop the file into the window or click the <b>'Select file to unlock'</b> button and choose the Excel file you want to unlock.</p>
        <p>2. Once you have selected the file, click <b>'Unlock file'</b> and the application will remove the sheet protection from the file.</p>
        <p>3. The unlocked file will be saved as a copy with the prefix <b>'unlocked_'</b> in the original folder.</p>
        <p>{feedback}</p>"""
    },

    "select_file_to_unlock": {
        "cs": "Vyber soubor k odemčení",
        "en": "Select file to unlock"
    },

    "no_file_to_unlock_label": {
        "cs": "<b>NEBYL VYBRÁN SOUBOR K ODEMČENÍ</b>",
        "en": "<b>NO FILE HAS BEEN SELECTED TO BE UNLOCKED.</b>"
    },

    "unlock_file_btn": {"cs": "ODEMKNOUT SOUBOR", "en": "UNLOCK FILE"},

    "file_path_length_info": {
        "cs": "Délka cesty souboru je {path_length} znaků.",
        "en": "The file path length is {path_length} characters."
    },

    "long_file_name_error": {
    "cs": (
        "Název souboru (včetně nadřazených složek) je příliš dlouhý! "
        "Celková délka je nyní {path_length} znaků. "
        "Odeberte z názvu nebo cesty alespoň {extra_chars} znaků."
    ),
    "en": (
        "The file name (including parent folders) is too long! "
        "The total length is now {path_length} characters. "
        "Remove at least {extra_chars} characters from the name or path."
    )
    },

    "file_to_unlock_label": {
        "cs": "<b>Soubor k odemčení: {file_name}</b>",
        "en": "<b>File to unlock: {file_name}</b>"
    },

    "processing_file": {
        "cs": "Zpracovávám soubor: {file}",
        "en": "Processing file: {file}"
    },

    "unlocked_file_exists": {
        "cs": "Soubor s názvem unlocked_ již existuje, změněno na: {unlocked_file}",
        "en": "File with unlocked_ prefix already exists, name changed to {unlocked_file}"
    },

    "file_copy_created": {
        "cs": "Vytvořena kopie souboru jako {unlocked_file}",
        "en": "File copy created as {unlocked_file}"
    },

    "file_renamed": {
        "cs": "Soubor '{old_file}' byl přejmenován na '{new_file}'",
        "en": "File '{old_file}' has been renamed to '{new_file}'"
    },

    "file_unlocked_successfully": {
        "cs": "Soubor byl úspěšně odemknut a uložen jako {unlocked_file}.",
        "en": "File has been successfully unlocked and saved as {unlocked_file}"
    },

    "no_file_to_unlock": {
        "cs": "Nebyl vybrán žádný soubor k odemknutí!",
        "en": "No file to be unlocked has been selected!"
    },

    "folder_not_exists": {
        "cs": "Složka {folder} neexistuje!",
        "en": "Folder {folder} doesn't exist!"
    }
}


# Return translated text for the given key based on current_lang
def t(key, **kwargs):
    global current_lang
    try:
        text = bapp_texts[key][current_lang]
        if kwargs:
            return text.format(**kwargs)
        return text
    except KeyError:
        return key