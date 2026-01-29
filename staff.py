class Staff:
    def __init__(
        self, username: str, employee_id: str, role: str, password: str
    ) -> None:
        self._username = username.strip()
        self._employee_id = employee_id.strip()
        self._role = role.strip()
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

    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "employee_id": self.employee_id,
            "role": self.role,
            "password": self._password,
        }
