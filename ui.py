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
        self.timer = PomodoroTimer(self)  # Tambahkan ini lebih awal

        # Inisialisasi UI
        self.initUI()

        # Buat TaskManager setelah UI dibuat
        self.task_manager = TaskManager(self.db, self.task_list)

        # Load tasks setelah UI selesai dibuat
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

        # Tombol edit tugas
        self.edit_task_btn = QPushButton("Edit Tugas", self)
        self.edit_task_btn.clicked.connect(self.edit_task)
        layout.addWidget(self.edit_task_btn)

        # List tugas
        self.task_list = QListWidget(self)
        layout.addWidget(self.task_list)

        self.task_list.itemDoubleClicked.connect(self.load_task_to_input)

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
        self.timer_btn.clicked.connect(self.timer.handle_timer_click)  # ← change here
        layout.addWidget(self.timer_btn)

        self.reset_btn = QPushButton("Reset Timer", self)
        self.reset_btn.clicked.connect(self.timer.reset_timer)
        layout.addWidget(self.reset_btn)


        self.setLayout(layout)

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


