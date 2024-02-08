from PySide6.QtWidgets import QApplication
from progress_bar_window import ProgressBarWindow
import configManager as CAMA

if __name__ == "__main__":
    app = QApplication([])
    configManager = CAMA.ConfigManager()
    window = ProgressBarWindow(configManager)
    window.setGeometry(100, 100, 400, 20)
    window.setMinimumSize(10,10)
    window.show()
    app.exec()