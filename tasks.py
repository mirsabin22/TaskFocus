from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidgetItem

class TaskManager:
    def __init__(self, db, task_list):
        self.db = db
        self.task_list = task_list

    def load_tasks(self):
        tasks = self.db.fetch_tasks()
        self.task_list.clear()
        for task_id, task_text in tasks:
            item = QListWidgetItem(task_text)
            item.setData(Qt.UserRole, task_id)  # Store task ID
            self.task_list.addItem(item)

    def add_task(self, task_text):
        if task_text:
            self.db.add_task(task_text)
            self.load_tasks()

    def delete_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            task_id = selected_item.data(Qt.UserRole)
            self.db.delete_task(task_id)
            self.load_tasks()
    
    def edit_task(self, new_text):
        selected_item = self.task_list.currentItem()
        if selected_item and new_text:
            task_id = selected_item.data(Qt.UserRole)
            self.db.update_task(task_id, new_text)
            self.load_tasks()

