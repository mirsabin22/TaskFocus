from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox, QSystemTrayIcon, QApplication
from PyQt5.QtGui import QIcon

class PomodoroTimer:
    def __init__(self, ui):
        self.ui = ui
        self.timer = QTimer(ui)
        self.timer.timeout.connect(self.update_timer)
        self.timer_running = False
        self.seconds_left = 1500  # 25 minutes
        self.in_break = False

        #tray icon
        self.tray_icon = QSystemTrayIcon(self.ui.style().standardIcon(QApplication.style().SP_ComputerIcon), self.ui)
        if not self.tray_icon.isSystemTrayAvailable():
            QMessageBox.warning(self.ui, "Peringatan", "System tray tidak tersedia.")
        else:
            self.tray_icon.setVisible(True)

    def handle_timer_click(self):
        current_task = self.ui.task_list.currentItem()
        if not current_task:
            QMessageBox.warning(self.ui, "Peringatan", "Pilih tugas terlebih dahulu!")
            return

        if self.timer_running:
            self.pause_timer()
        else:
            self.start_timer()

    def start_timer(self):
        self.timer.start(1000)
        self.timer_running = True
        self.ui.timer_btn.setText("Pause Timer")

    def pause_timer(self):
        self.timer.stop()
        self.timer_running = False
        self.ui.timer_btn.setText("Lanjutkan Timer")

    def reset_timer(self):
        self.timer.stop()
        self.timer_running = False
        self.seconds_left = 1500
        self.ui.timer_label.setText("25:00")
        self.ui.progress_bar.setValue(0)
        self.ui.timer_btn.setText("Mulai Timer")

    def update_timer(self):
        if self.seconds_left > 0:
            self.seconds_left -= 1
            minutes = self.seconds_left // 60
            seconds = self.seconds_left % 60
            self.ui.timer_label.setText(f"{minutes:02}:{seconds:02}")

            elapsed = 1500 - self.seconds_left
            self.ui.progress_bar.setValue(int((elapsed / 1500) * 100))
        else:
            self.timer.stop()
            self.timer_running = False
            self.ui.timer_btn.setText("Mulai Timer")
            self.seconds_left = 300  # 5 minutes break

            # Show system tray notification
            if self.tray_icon.isVisible():
                self.tray_icon.showMessage("Waktu Habis!", "Istirahat sejenak!", QSystemTrayIcon.Information, 5000)
            else:
                QMessageBox.information(self.ui, "Waktu Habis!", "Istirahat sejenak!")
