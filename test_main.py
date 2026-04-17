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
    task = manager.add_task("Estudar", "Python")
    assert task["title"] == "Estudar"
    assert task["description"] == "Python"
    assert task["completed"] == False
    assert task["id"] == 1


def test_list_tasks(manager):
    manager.add_task("Tarefa 1")
    manager.add_task("Tarefa 2")
    tasks = manager.list_tasks()
    assert len(tasks) == 2


def test_complete_task(manager):
    task = manager.add_task("Fazer algo")
    completed = manager.complete_task(task["id"])
    assert completed["completed"] == True
    assert completed["completed_at"] is not None


def test_delete_task(manager):
    task1 = manager.add_task("Tarefa 1")
    task2 = manager.add_task("Tarefa 2")
    manager.delete_task(task1["id"])
    tasks = manager.list_tasks(show_completed=True)
    assert len(tasks) == 1
    assert tasks[0]["id"] == task2["id"]


def test_get_task(manager):
    task = manager.add_task("Buscar isso")
    found = manager.get_task(task["id"])
    assert found["title"] == "Buscar isso"


def test_update_task(manager):
    task = manager.add_task("Original")
    updated = manager.update_task(task["id"], title="Atualizado")
    assert updated["title"] == "Atualizado"


def test_get_stats(manager):
    manager.add_task("Tarefa 1")
    manager.add_task("Tarefa 2")
    manager.add_task("Tarefa 3")
    manager.complete_task(1)
    
    stats = manager.get_stats()
    assert stats["total"] == 3
    assert stats["completed"] == 1
    assert stats["pending"] == 2
    assert stats["completion_rate"] == pytest.approx(33.33, 0.1)


def test_list_tasks_filter(manager):
    manager.add_task("Tarefa 1")
    manager.add_task("Tarefa 2")
    manager.complete_task(1)
    
    pending = manager.list_tasks(show_completed=False)
    all_tasks = manager.list_tasks(show_completed=True)
    
    assert len(pending) == 1
    assert len(all_tasks) == 2


def test_persistence(manager):
    manager.add_task("Persistir")
    
    new_manager = TaskManager("test_tasks.json")
    tasks = new_manager.list_tasks(show_completed=True)
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Persistir"
