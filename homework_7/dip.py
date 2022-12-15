import json
import sys


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    def __init__(self, first_name, last_name, department):
        super().__init__(first_name=first_name, last_name=last_name)
        self.department = department


class StudentService:
    def __init__(self, student: Student):
        self.student = student

    def change_department(self, new_department):
        self.student.department = new_department


class Teacher(Person):
    def __init__(self, first_name, last_name, main_subject):
        super().__init__(first_name=first_name, last_name=last_name)
        self.subjects = [main_subject]


class Group:
    def __init__(self, title: str, department: str, start_year: int):
        self.title = title
        self.department = department
        self.start_date = start_year
        self.members = dict()


class GroupService:
    def __init__(self, group: Group):
        self.group = group

    def add(self, person: Student):
        if person.department != self.group.department:
            StudentService(person).change_department(self.group.department)
        self.group.members.update({len(self.group.members) + 1: [person.first_name, person.last_name]})


class TxtPrinter:
    @staticmethod
    def write(message):
        with open("log.txt", "a+", encoding="UTF-8") as txt_log:
            txt_log.write(f"{message}\n")


class TerminalPrinter:
    @staticmethod
    def write(message):
        sys.stderr.write(f"{message}\n")


class JSONPrinter:
    @staticmethod
    def write(message):
        with open("log.json", "w") as json_log:
            json_log.write(json.dumps(message))


class GroupLogger:
    def __init__(self, group: Group):
        self.group = group

    def log_all(self, notifier):
        notifier().write(self.group.members)

    def log_one(self, member_id, notifier):
        notifier().write(f"{member_id}: {self.group.members.get(member_id, {})}")
