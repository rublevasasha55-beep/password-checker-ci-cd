"""
Тесты для проверки пароля
"""

from password_checker import is_password_strong

def test_empty_password():
    """Пустой пароль должен быть слабым."""
    assert is_password_strong("") == False

def test_short_password():
    """Короткий пароль (менее 8 символов) должен быть слабым."""
    assert is_password_strong("123") == False
    assert is_password_strong("pass") == False

def test_password_without_digits():
    """Пароль без цифр должен быть слабым."""
    assert is_password_strong("password") == False
    assert is_password_strong("Password") == False

def test_password_without_letters():
    """Пароль без букв должен быть слабым."""
    assert is_password_strong("12345678") == False

def test_strong_password():
    """Корректный сильный пароль."""
    assert is_password_strong("Pass1234") == True
    assert is_password_strong("StrongPass123") == True
    assert is_password_strong("MyP@ssw0rd") == True

def test_fixed_broken():
    """Исправленный тест (задание 5.4)."""
    # Пароль "12345" - короткий и без букв, должен быть СЛАБЫМ
    # Теперь утверждение правильное!
    assert is_password_strong("12345") == False
