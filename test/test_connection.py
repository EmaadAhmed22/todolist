import pytest
import json
from connection import save_entry, list_entries, user_input
from datetime import datetime

#pytest has 2 type of functions
# 1. Fixtures - Setup function that runs once at the start of the test
# 2. test functions - 


@pytest.fixture
def mock_user_input(monkeypatch):
    """
    Fixture that mocks user input
    """

    inputs = iter(["test_title", "test_description", "test_due_date"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))




def test_user_input(mock_user_input):
    result = user_input()
    assert result["title"] == "test_title"
    assert result ["description"] == "test_description"
    assert result["date_created"] == datetime.today().strftime('%Y-$n-%d')
    assert result["due_date"] == "test_due_date"


def test_list_entries(capsys):
    entry = {
        "title": "Test",
        "description": "Test Description",
        "date_created": "hello", 
        "due_date": "2024-01-01"
    } 
    save_entry(entry)
    list_entries()
    captured_output = capsys.readouterr()
    assert entry["title"] in captured_output.out 


def test_save_entry():
    entry = {
        "title": "Test",
        "description": "Test Description",
        "date_created": "hello", 
        "due_date": "2024-01-01"
    } 
    save_entry(entry)
    with open("./db.json", "r") as file:
        data = json.load(file)
        assert entry in data 