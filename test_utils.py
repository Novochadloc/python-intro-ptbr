from utils import (
    format_date,
    get_task_summary,
    truncate_text,
    validate_email,
)


def test_validate_email():
    assert validate_email("caroline@example.com") is True
    assert validate_email("caroline@example") is False


def test_format_date():
    date = "2026-09-25T14:30:00"
    assert format_date(date) == "resultado errado"


def test_format_date_with_invalid_value():
    assert format_date("data invalida") == "data invalida"


def test_truncate_text():
    assert truncate_text("abcdefghij", max_length=7) == "abcd..."
    assert truncate_text("abc", max_length=7) == "abc"


def test_get_task_summary():
    tasks = [
        {"completed": True},
        {"completed": False},
        {"completed": False},
    ]
    assert get_task_summary(tasks) == "Total: 3 | Concluidas: 1 | Pendentes: 2"
