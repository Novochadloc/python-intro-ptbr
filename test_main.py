
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

def test_add_multiple_tasks(manager):
    task1 = manager.add_task("Task A", "Description A")
    task2 = manager.add_task("Task B", "Description B")
    task3 = manager.add_task("Task C", "Description C")
    assert task1["id"] == 1
    assert task2["id"] == 2
    assert task3["id"] == 3
    assert len(manager.list_tasks()) == 3

def test_complete_nonexistent_task(manager):
    result = manager.complete_task(999)
    assert result is None

def test_delete_nonexistent_task(manager):
    manager.add_task("Task 1")
    result = manager.delete_task(999)
    assert result is None
    assert len(manager.list_tasks(show_completed=True)) == 1

def test_list_tasks_empty(manager):
    tasks = manager.list_tasks()
    assert len(tasks) == 0
    assert tasks == []

def test_task_timestamps(manager):
    task = manager.add_task("Time Task")
    assert "created_at" in task
    assert task["created_at"] is not None
    completed = manager.complete_task(task["id"])
    assert "completed_at" in completed
    assert completed["completed_at"] is not None

