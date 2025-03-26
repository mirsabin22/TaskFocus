class TaskManager:
    def __init__(self, db, task_list):
        self.db = db
        self.task_list = task_list

    def load_tasks(self):
        tasks = self.db.fetch_tasks()
        self.task_list.clear()
        for task in tasks:
            self.task_list.addItem(task[0])

    def add_task(self, task_text):
        if task_text:
            self.db.add_task(task_text)
            self.load_tasks()

    def delete_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            self.db.delete_task(selected_item.text())
            self.load_tasks()
