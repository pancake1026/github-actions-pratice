# test_sample.py

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 3 - 1 == 2

def test_fail_case():
    assert 2 * 2 == 4  # 這一行會故意讓 CI 失敗（測試紅燈情境）
