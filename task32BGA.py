class User:
    def __init__(self, email: str, password: str):
        self.email = email  
        self.password = password  

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        if "@" not in value:
            raise ValueError("Некорректный формат email (отсутствует '@')")
        self._email = value

    
    @property
    def password(self):
        raise AttributeError("Пароль недоступен для чтения!")

    @password.setter
    def password(self, value: str):
        self._password_hash = hash(value)

    def check_password(self, password: str) -> bool:
        return self._password_hash == hash(password)


# Пример использования:
user = User("test@example.com", "secret")
print(user.email)  # test@example.com

try:
    print(user.password)
except AttributeError as e:
    print(e) 

print(user.check_password("secret"))  
print(user.check_password("wrong"))   
