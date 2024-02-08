from PySide6.QtWidgets import QDialog, QLineEdit,QPushButton, QVBoxLayout,QLabel,QHBoxLayout
from PySide6.QtGui import Qt
import utils

class ConfirmationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Name')
        self.setWindowModality(Qt.WindowModality.WindowModal)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        label = QLabel("Are you sure you want to delete?")
        layout.addWidget(label)

        btn_layout = QHBoxLayout()
        layout.addLayout(btn_layout)

        confirm_button = QPushButton('Delete', self)
        confirm_button.clicked.connect(self.accept)

        cancel_button = QPushButton('Cancel', self)
        cancel_button.clicked.connect(self.reject)

        utils.add_widgets_to_layout(btn_layout,[cancel_button,confirm_button])