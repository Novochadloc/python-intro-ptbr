import json
from datetime import datetime
from pathlib import Path

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        if Path(self.filename).exists():
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def _save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, title, description=""):
        task = {"id": len(self.tasks) + 1, "title": title, "description": description, "completed": False, "created_at": datetime.now().isoformat(), "completed_at": None}
        self.tasks.append(task)
        self._save_tasks()
        return task

    def list_tasks(self, show_completed=False):
        return self.tasks if show_completed else [t for t in self.tasks if not t["completed"]]

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                task["completed_at"] = datetime.now().isoformat()
                self._save_tasks()
                return task
        return None

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        self._save_tasks()

    def get_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def get_stats(self):
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t["completed"]])
        pending = total - completed
        return {"total": total, "completed": completed, "pending": pending, "completion_rate": (completed / total * 100) if total > 0 else 0}

if __name__ == "__main__":
    print("Task Manager Ready")

git add main.py
git commit -m "Melhorias no gerenciador de tarefas"
git push origin feature/testes-adicionais

