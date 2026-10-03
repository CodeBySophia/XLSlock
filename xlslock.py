from PySide6 import QtWidgets, QtGui, QtCore
import config
import xlslock_fn
import win_size_pos
import os
import ctypes
import lang
import sys

# App to unlock protected Excel files
class xlslock(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.locked_file = None # Initialize as None
        self.unlocked_file = None
        self.initUI()
        self.setAcceptDrops(True) # Enable drag n drop for files

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()
        config.style_main_layout(layout)
        win_size_pos.set_win_size(self)
        self.setWindowTitle(lang.t(config.XLSLOCK_NAME_TEMPLATE))  # Window name
        self.setWindowIcon(QtGui.QIcon(config.ICON_PATH))
        self.setLayout(layout)  # Set layout for widget
        config.apply_fusion_style()
        self.show()  # Display the window

        # Help label for users
        instruction_text = lang.t("xlslock_instructions", feedback=lang.t(config.FEEDBACK_TEXT_KEY))

        instruction_label = QtWidgets.QLabel(instruction_text)
        instruction_label.setWordWrap(True)  # More rows if text is too long

        # Adding logo
        logo_label = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap(config.LOGO)
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) # In the middle

        # Button to select a locked file
        self.select_locked_file_btn = QtWidgets.QPushButton(lang.t("select_file_to_unlock"), self)
        self.select_locked_file_btn.clicked.connect(self.select_locked_files)
        layout.addWidget(self.select_locked_file_btn)
        # Set font and color of the button
        config.style_button(self.select_locked_file_btn)

        # Label to display selected file path
        self.file_info_label = QtWidgets.QLabel(lang.t("no_file_to_unlock_label"))
        self.file_info_label.setWordWrap(True)  # More rows if text is too long

        # Button to unlock files - calls main function
        self.unlock_btn = QtWidgets.QPushButton(lang.t("unlock_file_btn"), self)
        self.unlock_btn.clicked.connect(lambda: xlslock_fn.unlock_files(self.locked_file))
        # Set font and color of the button
        config.style_button(self.unlock_btn)
        
        # Layout; Add both buttons in a horizontal layout for better placement
        layout.addWidget(instruction_label)
        layout.addWidget(logo_label)
        layout.addWidget(self.file_info_label)
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setSpacing(8)
        button_layout.addWidget(self.select_locked_file_btn)
        button_layout.addWidget(self.unlock_btn)
        layout.addLayout(button_layout)
        layout.addWidget(config.build_copyright_footer(self))

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent): # Obtaining files name, checking file type
        if event.mimeData().hasUrls:
            url = event.mimeData().urls()[0]
            file_name = url.toLocalFile()
            if self.is_excel_file(file_name):
                event.acceptProposedAction() # Drag and drop accept
            else:
                event.ignore()

    def dropEvent(self, event: QtGui.QDropEvent): # Process dragged file
        if event.mimeData().hasUrls():
            url = event.mimeData().urls()[0]
            file_name = url.toLocalFile()
            self.set_locked_file(file_name)
    
    def is_excel_file(self, file_name: str) -> bool: # Check if file type is Excel
        return file_name.lower().endswith(('.xls', '.xlsx', '.xlsm'))

    def select_locked_files(self): # Select a file to process
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, lang.t("select_file_to_unlock"), "", "Excel Files (*.xls *.xlsx *.xlsm)")
        if file_name:
            self.set_locked_file(file_name)
    
    def get_long_path_name(self, short_path: str) -> str:
        """ Convert short (8.3) path to full long path in Windows """
        buffer = ctypes.create_unicode_buffer(1024)
        ctypes.windll.kernel32.GetLongPathNameW(short_path, buffer, 1024)
        return buffer.value

    def set_locked_file(self, file_name: str):
        # Sets locked file if is Excel file and name is not longer than 256
        full_path = self.get_long_path_name(os.path.abspath(file_name)) # Full path of the file
        path_length = len(full_path)

        print(lang.t("file_path_length_info", path_length=path_length))
        print(full_path)

        if self.is_excel_file(file_name):
            if path_length > 255:
                extra_chars = path_length - 255
                long_file_name_text = lang.t("long_file_name_error", path_length=path_length, extra_chars=extra_chars)
                QtWidgets.QMessageBox.warning(self, lang.t("error_title"), long_file_name_text)
                return
            else:
                self.locked_file = file_name
                self.file_info_label.setText(lang.t("file_to_unlock_label", file_name=file_name))
        else:
            QtWidgets.QMessageBox.warning(self, lang.t("error_title"), lang.t("invalid_format"))

if __name__ == '__main__':
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("CodeBySophia.XLSlock")
    except Exception:
        pass
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(config.ICON_PATH))
    ex = xlslock()
    ex.setWindowIcon(QtGui.QIcon(config.ICON_PATH))
    ex.show()
    sys.exit(app.exec())
