from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMessageBox

class PomodoroTimer:
    def __init__(self, ui):
        self.ui = ui
        self.timer = QTimer(ui)
        self.timer.timeout.connect(self.update_timer)
        self.timer_running = False
        self.seconds_left = 1500  # 25 menit

    def start_timer(self):
        """Mulai atau hentikan timer"""
        if self.timer_running:
            self.timer.stop()
            self.ui.timer_btn.setText("Mulai Timer")
            self.timer_running = False
        else:
            self.timer.start(1000)  # Update tiap 1 detik
            self.ui.timer_btn.setText("Pause Timer")
            self.timer_running = True

    def update_timer(self):
        """Update countdown timer"""
        if self.seconds_left > 0:
            self.seconds_left -= 1
            minutes = self.seconds_left // 60
            seconds = self.seconds_left % 60
            self.ui.timer_label.setText(f"{minutes:02}:{seconds:02}")

            # Update progress bar
            elapsed = 1500 - self.seconds_left
            self.ui.progress_bar.setValue(int((elapsed / 1500) * 100))
        else:
            self.timer.stop()
            QMessageBox.information(self.ui, "Waktu Habis!", "Istirahat sejenak!")
            self.seconds_left = 300  # Istirahat 5 menit
            self.ui.timer_btn.setText("Mulai Timer")
            self.timer_running = False
