#  XLSlock – Excel Sheet Unlocker
xlslock is a PySide6-based application that allows users to unlock password-protected Excel sheets by removing sheetProtection entries from the workbook’s XML structure.
The original file is never modified directly – the app creates a copy (unlocked_...) and applies the unlocking process there.
This tool is especially useful when dealing with Excel sheets that are locked but you still need to edit them.

Features
Drag & drop support – quickly load a locked Excel file.
File dialog support – choose locked files manually.
Logo & instructions displayed in the main window for user guidance.
Unlock button – automatically processes the file:
Copies the original file.
Converts it into a .zip.
Removes all <sheetProtection> tags from xl/worksheets/*.xml.
Recompresses and renames back into Excel format.
File safety – the original file is untouched. The unlocked version is saved as:
unlocked_<original_filename>.xlsx
unlocked_<original_filename>_1.xlsx (if already exists)
Error handling – warnings for:
Invalid file format (non-Excel).
Path length exceeding Windows limitations.
Missing worksheet folder in archive.
GUI feedback – success/error messages shown in dialogs.
