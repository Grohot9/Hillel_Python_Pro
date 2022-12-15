class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sleep(self, hours=8):
        return f"{self.first_name} slept {hours} hours."


class Student(Person):
    def __init__(self, first_name, last_name, department):
        super().__init__(first_name=first_name, last_name=last_name)
        self.department = department

    def sleep(self, hours=4):
        return f"Student {self.first_name} slept {hours} hours."


class Teacher(Person):
    def __init__(self, first_name, last_name, main_subject):
        super().__init__(first_name=first_name, last_name=last_name)
        self.subjects = [main_subject]

    def sleep(self, hours=8):
        return f"{self.subjects[0]} teacher {self.first_name} slept {hours} hours."


class Group:
    def __init__(self, title, department, start_year):
        self.title = title
        self.department = department
        self.start_date = start_year
