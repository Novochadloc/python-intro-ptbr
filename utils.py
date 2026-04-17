import re
from datetime import datetime, timedelta

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def format_date(date_string):
    try:
        dt = datetime.fromisoformat(date_string)
        return dt.strftime("%d/%m/%Y %H:%M")
    except:
        return date_string

def get_days_ago(date_string):
    try:
        dt = datetime.fromisoformat(date_string)
        diff = datetime.now() - dt
        days = diff.days
        if days == 0:
            return "hoje"
        elif days == 1:
            return "ontem"
        else:
            return f"{days} dias atrás"
    except:
        return "data inválida"

def truncate_text(text, max_length=50):
    if len(text) > max_length:
        return text[:max_length-3] + "..."
    return text

def calculate_priority(task):
    if task.get("priority") == "high":
        return 1
    elif task.get("priority") == "medium":
        return 2
    else:
        return 3

def sort_tasks_by_priority(tasks):
    return sorted(tasks, key=calculate_priority)

def filter_tasks_by_keyword(tasks, keyword):
    keyword = keyword.lower()
    return [
        t for t in tasks 
        if keyword in t["title"].lower() or keyword in t.get("description", "").lower()
    ]

def get_overdue_tasks(tasks):
    overdue = []
    for task in tasks:
        if not task["completed"] and task.get("due_date"):
            due = datetime.fromisoformat(task["due_date"])
            if due < datetime.now():
                overdue.append(task)
    return overdue

def export_to_csv(tasks, filename="tasks_export.csv"):
    import csv
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "description", "completed", "created_at"])
        writer.writeheader()
        writer.writerows(tasks)

def import_from_csv(filename):
    import csv
    tasks = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["completed"] = row["completed"].lower() == "true"
            tasks.append(row)
    return tasks

def get_task_summary(tasks):
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    pending = total - completed
    
    return f"Total: {total} | Concluídas: {completed} | Pendentes: {pending}"
