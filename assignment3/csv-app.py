from typing import Optional
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
    def read_all(self):
        pass

    @abstractmethod
    def do_read(self, id):
        pass

    @abstractmethod
    def do_update(self, id, user: User):
        pass

    @abstractmethod
    def do_delete(self, id):
        pass


class MyCSVRepo(BaseUserRepository):

    def __init__(self, filename: str, fieldnames: list):

        self.repo = list[User] 
        self.filename = filename
        self.fieldnames = fieldnames

        with open(filename, mode="r", newline="") as file:
            csv_reader = csv.DictReader(file)
            self.repo = [User(**row) for row in csv_reader]

    def do_create(self, user: User):
        self.repo.append(user)
        self.do_save_file()

    def read_all(self):
        return self.repo

    def do_read(self, id):
        return self.repo[str(id)]

    def do_update(self, id, user: User):
        self.repo[str(id)] = user
        self.do_save_file()

    def do_delete(self, id):
        for user in self.repo:
            if int(user.id) == int(id):
                self.repo.remove(user)
                break

        self.do_save_file()

    def do_save_file(self):
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for user in self.repo:
                writer.writerow(asdict(user))


class MyMemoryRepo(BaseUserRepository):

    def __init__(self, id_field: str):

        self.repo = list[User]

    def do_create(self, user: User):
        self.repo.append(user)

    def read_all(self):
        return self.repo

    def do_read(self, id):
        return self.repo[id]

    def do_update(self, id, user: User):
        self.repo[id] = user

    def do_delete(self, id):
        for user in self.repo:
            if int(user.id) == int(id):
                self.repo.remove(user)
                break
        


# Defining main function
def main():
    print("generic repository example")
    csv_repo = MyCSVRepo("users.csv", "id", ["id", "username", "isadmin"])

    print(csv_repo.read_all())

    csv_repo.do_create(User(1, "fakeuser1", False))

# Using the special variable
# __name__
if __name__ == "__main__":
    main()