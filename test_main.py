import pytest
from main import talk, take_command, execute_command

def test_talk():
    """Test if talk() runs without errors."""
    try:
        talk("Hello, testing talk function!")
    except Exception as e:
        pytest.fail(f"talk() raised an error: {e}")

def test_take_command(monkeypatch):
    """Mock take_command() to simulate user input."""
    monkeypatch.setattr('builtins.input', lambda: "Alexa, play some music")
    command = take_command()
    assert isinstance(command, str), "Command should be a string"

def test_execute_command(monkeypatch):
    """Mock execute_command() to avoid side effects."""
    monkeypatch.setattr('main.take_command', lambda: "play despacito")
    try:
        execute_command()
    except Exception as e:
        pytest.fail(f"execute_command() raised an error: {e}")
