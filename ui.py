from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QListWidget,
    QLineEdit, QLabel, QProgressBar, QMessageBox
)
from PyQt5.QtCore import QTimer
from database import Database
from tasks import TaskManager
from timer import PomodoroTimer


class ToDoTimerApp(QWidget):
    def __init__(self):
        super().__init__()

        # Inisialisasi database
        self.db = Database()

        # Buat Timer sebelum UI agar tidak terjadi AttributeError
        self.timer = PomodoroTimer(self)

        # Inisialisasi UI
        self.initUI()

        # Buat TaskManager setelah UI dibuat
        self.task_manager = TaskManager(self.db, self.task_list)

        # Load tasks setelah UI selesai dibuat
        self.task_manager.load_tasks()

    def initUI(self):
        self.setWindowTitle("To-Do List dengan Pomodoro Timer")
        self.resize(500, 700)
        self.setMinimumSize(400, 600)

 

        layout = QVBoxLayout()
        layout.setSpacing(10)

        button_style = """
            QPushButton {
                padding: 8px;
                font-size: 13px;
                background-color: #f9c74f;
                border: none;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #f9844a;
                color: white;
            }
        """

        input_style = """
            QLineEdit {
                padding: 6px;
                font-size: 13px;
            }
        """

        # Input tugas
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Tambahkan tugas...")
        self.task_input.setStyleSheet(input_style)
        layout.addWidget(self.task_input)

        # Tombol tambah tugas
        self.add_task_btn = QPushButton("Tambah Tugas", self)
        self.add_task_btn.setStyleSheet(button_style)
        self.add_task_btn.clicked.connect(self.add_task)
        layout.addWidget(self.add_task_btn)

        # Tombol edit tugas
        self.edit_task_btn = QPushButton("Edit Tugas", self)
        self.edit_task_btn.setStyleSheet(button_style)
        self.edit_task_btn.clicked.connect(self.edit_task)
        layout.addWidget(self.edit_task_btn)

        # List tugas
        self.task_list = QListWidget(self)
        layout.addWidget(self.task_list)
        self.task_list.itemDoubleClicked.connect(self.load_task_to_input)

        # Tombol hapus tugas
        self.delete_task_btn = QPushButton("Hapus Tugas", self)
        self.delete_task_btn.setStyleSheet(button_style)
        self.delete_task_btn.clicked.connect(self.delete_task)
        layout.addWidget(self.delete_task_btn)

        # Timer
        self.timer_label = QLabel("25:00", self)
        self.timer_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(self.timer_label)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        # Tombol timer
        self.timer_btn = QPushButton("Mulai Timer", self)
        self.timer_btn.setStyleSheet(button_style)
        self.timer_btn.clicked.connect(self.timer.handle_timer_click)
        layout.addWidget(self.timer_btn)

        self.reset_btn = QPushButton("Reset Timer", self)
        self.reset_btn.setStyleSheet(button_style)
        self.reset_btn.clicked.connect(self.timer.reset_timer)
        layout.addWidget(self.reset_btn)

        self.setLayout(layout)

        # Menyesuaikan dan mengunci ukuran window
        # self.adjustSize()
        # self.setFixedSize(self.size())

    def add_task(self):
        self.task_manager.add_task(self.task_input.text())
        self.task_input.clear()

    def delete_task(self):
        self.task_manager.delete_task()

    def edit_task(self):
        new_text = self.task_input.text()
        self.task_manager.edit_task(new_text)
        self.task_input.clear()

    def load_task_to_input(self, item):
        self.task_input.setText(item.text())
