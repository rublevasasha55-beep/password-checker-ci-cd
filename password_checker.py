"""
Простая проверка сложности пароля
"""

def is_password_strong(password):
    """Проверяет, достаточно ли сложный пароль."""
    if not password:
        return False
    
    # Длина не менее 8 символов
    if len(password) < 8:
        return False
    
    # Содержит хотя бы одну цифру
    if not any(char.isdigit() for char in password):
        return False
    
    # Содержит хотя бы одну букву
    if not any(char.isalpha() for char in password):
        return False
    
    return True

def main():
    """Пример использования функции."""
    test_passwords = ["", "123", "password", "pass123", "StrongPass123"]
    for pwd in test_passwords:
        result = is_password_strong(pwd)
        print(f"Пароль '{pwd}': {'✅ Сильный' if result else '❌ Слабый'}")
