
import pytest
import json
import os
from pathlib import Path
from main import TaskManager

@pytest.fixture
def manager():
    test_file = "test_tasks.json"
    if Path(test_file).exists():
        os.remove(test_file)
    mgr = TaskManager(test_file)
    yield mgr
    if Path(test_file).exists():
        os.remove(test_file)

def test_add_task(manager):
    task = manager.add_task("Study", "Python")
    assert task["title"] == "Study"
    assert task["description"] == "Python"
    assert task["completed"] == False
    assert task["id"] == 1

def test_list_tasks(manager):
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    tasks = manager.list_tasks()
    assert len(tasks) == 2

def test_complete_task(manager):
    task = manager.add_task("Do something")
    completed = manager.complete_task(task["id"])
    assert completed["completed"] == True
    assert completed["completed_at"] is not None

def test_delete_task(manager):
    task1 = manager.add_task("Task 1")
    task2 = manager.add_task("Task 2")
    manager.delete_task(task1["id"])
    tasks = manager.list_tasks(show_completed=True)
    assert len(tasks) == 1
    assert tasks[0]["id"] == task2["id"]

def test_get_stats(manager):
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    manager.add_task("Task 3")
    manager.complete_task(1)
    stats = manager.get_stats()
    assert stats["total"] == 3
    assert stats["completed"] == 1
    assert stats["pending"] == 2
