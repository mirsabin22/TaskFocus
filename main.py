import sys
from PyQt5.QtWidgets import QApplication
from ui import ToDoTimerApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoTimerApp()
    window.show()
    sys.exit(app.exec())
