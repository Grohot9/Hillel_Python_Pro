class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Graded:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = list()


class GradeSetter:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def set_grade(graded: Graded, grade):
        graded.grades.append(grade)


class Student(Person, Graded):
    def __init__(self, first_name, last_name, department):
        super().__init__(first_name=first_name, last_name=last_name)
        self.department = department


class Teacher(Person, GradeSetter):
    def __init__(self, first_name, last_name, main_subject):
        super().__init__(first_name=first_name, last_name=last_name)
        self.subjects = [main_subject]

    def set_grade(self, graded: Graded, grade, subject=None):
        if subject is None:
            subject = self.subjects[0]
        print(f"{graded.first_name} {graded.last_name} gets {grade} in {subject}!")


class Group:
    def __init__(self, title, department, start_year):
        self.title = title
        self.department = department
        self.start_date = start_year
