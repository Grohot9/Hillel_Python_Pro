class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    def __init__(self, first_name, last_name, department):
        super().__init__(first_name=first_name, last_name=last_name)
        self.department = department


class Teacher(Person):
    def __init__(self, first_name, last_name, main_subject):
        super().__init__(first_name=first_name, last_name=last_name)
        self.subjects = [main_subject]


class Group:
    def __init__(self, title, department, start_year):
        self.title = title
        self.department = department
        self.start_date = start_year
