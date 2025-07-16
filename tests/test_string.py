# tests/test_string.py

def test_upper():
    assert "hello".upper() == "HELLO"

def test_startswith():
    assert "hello".startswith("h")
