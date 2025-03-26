from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QListWidget,
    QLineEdit, QLabel, QProgressBar, QMessageBox
)
from PyQt6.QtCore import QTimer
from database import Database
from tasks import TaskManager
from timer import PomodoroTimer

class ToDoTimerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        # Inisialisasi database dan manajemen tugas
        self.db = Database()
        self.task_manager = TaskManager(self.db, self.task_list)

        # Inisialisasi timer
        self.timer = PomodoroTimer(self)

        self.task_manager.load_tasks()

    def initUI(self):
        self.setWindowTitle("To-Do List dengan Pomodoro Timer")
        self.setGeometry(100, 100, 400, 500)

        layout = QVBoxLayout()

        # Input tugas
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Tambahkan tugas...")
        layout.addWidget(self.task_input)

        # Tombol tambah tugas
        self.add_task_btn = QPushButton("Tambah Tugas", self)
        self.add_task_btn.clicked.connect(self.add_task)
        layout.addWidget(self.add_task_btn)

        # List tugas
        self.task_list = QListWidget(self)
        layout.addWidget(self.task_list)

        # Tombol hapus tugas
        self.delete_task_btn = QPushButton("Hapus Tugas", self)
        self.delete_task_btn.clicked.connect(self.delete_task)
        layout.addWidget(self.delete_task_btn)

        # Timer dan progress bar
        self.timer_label = QLabel("25:00", self)
        layout.addWidget(self.timer_label)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        # Tombol start/pause timer
        self.timer_btn = QPushButton("Mulai Timer", self)
        self.timer_btn.clicked.connect(self.timer.start_timer)
        layout.addWidget(self.timer_btn)

        self.setLayout(layout)

    def add_task(self):
        self.task_manager.add_task(self.task_input.text())

    def delete_task(self):
        self.task_manager.delete_task()
