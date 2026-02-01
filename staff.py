from abc import ABC


class Staff(ABC):
    VALID_ROLES = {"worker", "manager"}
    ROLE: str = ""

    def __init__(self, username: str, employee_id: str, password: str) -> None:
        role = self.ROLE.strip().lower()
        if role not in self.VALID_ROLES:
            raise ValueError("Invalid staff role")
        self._username = username.strip()
        self._employee_id = employee_id.strip()
        self._role = role
        self._password = password.strip()

    @property
    def username(self) -> str:
        return self._username

    @property
    def employee_id(self) -> str:
        return self._employee_id

    @property
    def role(self) -> str:
        return self._role

    def check_password(self, password: str) -> bool:
        return self._password == password

    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "employee_id": self.employee_id,
            "role": self.role,
            "password": self._password,
        }


class Worker(Staff):
    ROLE = "worker"


class Manager(Staff):
    ROLE = "manager"
