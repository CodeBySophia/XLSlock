from PySide6 import QtWidgets, QtGui, QtCore
import os
import sys

def resource_path(relative_path: str) -> str:
    """Return absolute path to a bundled resource (dev and PyInstaller onefile)."""
    base_path = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
    return os.path.join(base_path, relative_path)

CREATOR = "CodeBySophia - codebysophia@gmail.com"
LOGO = resource_path("company_logo.png")
ICON_PATH = resource_path("icon.ico")
# templates for translated text (keys in lang.py)
XLSLOCK_NAME_TEMPLATE = "xlslock_name"

FEEDBACK_TEXT_KEY = "feedback_text_public"
COPYRIGHT_TEXT = "\u00A9 2026 CodeBySophia All rights reserved"

# Window style
def apply_fusion_style():
    # Set Fusion style
    QtWidgets.QApplication.setStyle("Fusion")

    # Change color palette to light theme
    palette = QtGui.QPalette()
    # Window background and text colors
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(255, 255, 255))  # White window background
    palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(0, 0, 0))    # Black text color
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(245, 245, 245))    # Light gray text field background
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(255, 255, 255))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(255, 255, 220)) # Tooltip background
    palette.setColor(QtGui.QPalette.ToolTipText, QtGui.QColor(0, 0, 0))      # Tooltip text
    palette.setColor(QtGui.QPalette.Text, QtGui.QColor(0, 0, 0))            # Text color
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(240, 240, 240))    # Button background
    palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(0, 0, 0))      # Button text color
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(0, 120, 215))   # Highlight color (blue)
    palette.setColor(QtGui.QPalette.HighlightedText, QtGui.QColor(255, 255, 255)) # Highlighted text

    QtWidgets.QApplication.setPalette(palette)

    icon = QtGui.QIcon(ICON_PATH)
    QtWidgets.QApplication.setWindowIcon(icon)
    app = QtWidgets.QApplication.instance()
    if app is not None:
        app.setStyleSheet(APP_WINDOW_STYLE)

QLINE_STYLE = """
QLineEdit {
    color: black;
    background-color: #f5f5f5;
}
QLineEdit::placeholder {
    color: #7a7a7a;
}
"""

QTEXT_STYLE = """
QTextEdit {
    color: #1f1f1f;
    background-color: #f5f5f5;
    border: 1px solid #cfcfcf;
    border-radius: 8px;
    padding: 6px 8px;
}
QTextEdit:focus {
    border: 1px solid #ff7f00;
    background-color: #ffffff;
}
QTextEdit::placeholder {
    color: #7a7a7a;
}
"""

# Button styles
# In-app buttons
FN_BUTTON_STYLE = """
QPushButton {
    background-color: #ff0000;
    color: #ffffff;
    font-weight: 700;
    font-size: 13px;
    border: 1px solid #c10000;
    border-radius: 10px;
    padding: 8px 12px;
}
QPushButton:hover {
    background-color: #45a049;
    border-color: #357b39;
}
QPushButton:pressed {
    background-color: #ffa500;
    border-color: #cc8400;
}
QPushButton:disabled {
    background-color: #d0d0d0;
    border-color: #c2c2c2;
    color: #707070;
}
"""

# Button to run other apps
APP_BUTTON_STYLE = FN_BUTTON_STYLE

APP_WINDOW_STYLE = """
QWidget {
    font-size: 12px;
}
QTextEdit, QTableWidget, QListWidget {
    border: 1px solid #d8d8d8;
    border-radius: 8px;
    background: #ffffff;
}
QHeaderView::section {
    background: #f1f1f1;
    border: 1px solid #d6d6d6;
    padding: 5px;
    font-weight: 600;
}
"""

def style_main_layout(layout: QtWidgets.QLayout) -> None:
    if layout is None:
        return
    layout.setContentsMargins(14, 12, 14, 12)
    layout.setSpacing(10)

def style_button(button: QtWidgets.QPushButton, *, launcher: bool = False, compact: bool = False) -> QtWidgets.QPushButton:
    if button is None:
        return button
    button.setStyleSheet(APP_BUTTON_STYLE if launcher else FN_BUTTON_STYLE)
    button.setMinimumHeight(30 if compact else 42)
    button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
    return button

def build_copyright_footer(parent=None) -> QtWidgets.QLabel:
    footer = QtWidgets.QLabel(COPYRIGHT_TEXT, parent)
    footer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    footer.setStyleSheet("color: gray; font-size: 10px;")
    return footer
