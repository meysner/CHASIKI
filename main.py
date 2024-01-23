from PySide6.QtWidgets import QApplication
from progress_bar_window import ProgressBarWindow

if __name__ == "__main__":
    app = QApplication([])
    start_hour = 5
    end_hour = 22
    window = ProgressBarWindow(start_hour, end_hour)
    window.setGeometry(100, 100, 400, 60)
    window.show()
    app.exec()