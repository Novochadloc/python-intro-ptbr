import re
from datetime import datetime

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
            return f"{days} dias atras"
    except:
        return "data invalida"

def truncate_text(text, max_length=50):
    if len(text) > max_length:
        return text[:max_length-3] + "..."
    return text

def get_task_summary(tasks):
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    pending = total - completed
    return f"Total: {total} | Concluidas: {completed} | Pendentes: {pending}"
