class SimpleUser:

    logins = []

    def __init__(self, login: str, password: str, name: str, surname: str, permission: int = 1):
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname
        self.permission = permission
        if login not in SimpleUser.logins:
            SimpleUser.logins.append(self.login)
        else:
            print(f"*************** This login -> < {self.login} > is allready in use ***************")


class User(SimpleUser):

    def print_user(self):
        print(f"Name -> {self.name}, Login -> {self.login} Perm -> {self.permission}")


class Admin(SimpleUser):
    def __init__(self, login: str, password: str, name: str, surname: str):
        super().__init__(
            login=login,
            password=password,
            name=name,
            surname=surname,
            permission=2
        )

    def print_user(self):
        print(f"Name -> {self.name}, Login -> {self.login} Perm -> {self.permission}")

user_admin = Admin("xXx3evsxXx", "password1", "Misha", "Lyvak")
user1 = User("login2", "password2", "Masha", "Grusiuk", 1)
user2 = User("xXx3evsxXx", "password3", "Oleg", "Krolik", 1)


user_admin.print_user()
user1.print_user()
user2.print_user()

def print_logins() -> None:
    return ", ".join([log for log in SimpleUser.logins])

def printerr():
    print(f"Used logins are -> {print_logins()}")

printerr()