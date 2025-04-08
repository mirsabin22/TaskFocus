import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("tasks.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT
            )
        """)
        self.conn.commit()

    def fetch_tasks(self):
        self.cursor.execute("SELECT id, task FROM tasks")
        return self.cursor.fetchall()


    def add_task(self, task_text):
        self.cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task_text,))
        self.conn.commit()

    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()
    
    def update_task(self, task_id, new_text):
        self.cursor.execute("UPDATE tasks SET task = ? WHERE id = ?", (new_text, task_id))
        self.conn.commit()


    def close(self):
        self.conn.close()
