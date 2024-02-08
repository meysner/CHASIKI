from PySide6.QtWidgets import QDialog, QLineEdit,QPushButton, QVBoxLayout,QHBoxLayout
from PySide6.QtGui import Qt
from PySide6.QtCore import QSize
import utils

class PopupDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowModality(Qt.WindowModality.WindowModal)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        self.text_field = QLineEdit(self)
        layout.addWidget(self.text_field)

        btn_layout = QHBoxLayout()
        layout.addLayout(btn_layout)

        confirm_button = QPushButton('Confirm', self)
        confirm_button.clicked.connect(self.accept)

        cancel_button = QPushButton('Cancel', self)
        cancel_button.clicked.connect(self.reject)

        utils.add_widgets_to_layout(btn_layout,[cancel_button,confirm_button])
