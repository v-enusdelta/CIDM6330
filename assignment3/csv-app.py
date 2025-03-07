from typing import Optional, List
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict, field, InitVar
import csv

@dataclass
class User:
    id: int
    username: str
    isadmin: bool


class BaseUserRepository(ABC):
    @abstractmethod
    def do_create(self, user: User):
        pass

    @abstractmethod
    def read_all(self) -> List[User]:
        pass

    @abstractmethod
    def do_read(self, id: int) -> Optional[User]:
        pass

    @abstractmethod
    def do_update(self, id: int, user: User):
        pass

    @abstractmethod
    def do_delete(self, id: int):
        pass


class MyCSVRepo(BaseUserRepository):

    def __init__(self, filename: str, id_field: str, fieldnames: list):
        self.repo: List[User] = []
        self.filename = filename
        self.fieldnames = fieldnames

        with open(filename, mode="r", newline="") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                product = User(id=int(row['id']), username=row['username'], isadmin=bool(row['isadmin']))
                self.repo.append(product)

    def do_create(self, user: User):
        self.repo.append(user)
        self.do_save_file()

    def read_all(self) -> List[User]:
        return self.repo

    def do_read(self, id: int) -> Optional[User]:
        for user in self.repo:
            if user.id == id:
                return user
        return None

    def do_update(self, id: int, user: User):
        for i, u in enumerate(self.repo):
            if u.id == id:
                self.repo[i] = user
                self.do_save_file()
                return

    def do_delete(self, id: int):
        self.repo = [user for user in self.repo if user.id != id]
        self.do_save_file()

    def do_save_file(self):
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for user in self.repo:
                writer.writerow(asdict(user))


class MyMemoryRepo(BaseUserRepository):

    def __init__(self, id_field: str):
        self.repo: List[User] = []

    def do_create(self, user: User):
        self.repo.append(user)

    def read_all(self) -> List[User]:
        return self.repo

    def do_read(self, id: int) -> Optional[User]:
        for user in self.repo:
            if user.id == id:
                return user
        return None

    def do_update(self, id: int, user: User):
        for i, u in enumerate(self.repo):
            if u.id == id:
                self.repo[i] = user
                return

    def do_delete(self, id: int):
        self.repo = [user for user in self.repo if user.id != id]


# Defining main function
def main():
    print("generic repository example")
    csv_repo = MyCSVRepo("users.csv", "id", ["id", "username", "isadmin"])
    csv_repo.do_create(User(1,"fakeuser1",True))
    csv_repo.do_create(User(2,"fakeuser2",False))
    csv_repo.do_create(User(3,"fakeuser3",True))

    print(csv_repo.read_all())


# Using the special variable
# __name__
if __name__ == "__main__":
    main()