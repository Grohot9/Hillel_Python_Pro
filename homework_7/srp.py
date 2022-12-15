class Student:
    def __init__(self, first_name, last_name, department):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department


class StudentService:
    def __init__(self, student: Student):
        self.student = student

    def change_department(self, new_department):
        self.student.department = new_department


class Teacher:
    def __init__(self, first_name, last_name, subject):
        self.first_name = first_name
        self.last_name = last_name
        self.subjects = [subject]


class TeacherService:
    def __init__(self, teacher: Teacher):
        self.teacher = teacher

    def add_subject(self, subject):
        self.teacher.subjects.append(subject)

    def remove_subject(self, subject):
        self.teacher.subjects.remove(subject)


class Group:
    def __init__(self, title, department, start_year):
        self.title = title
        self.department = department
        self.start_date = start_year
        self.members = dict()


class GroupService:
    def __init__(self, group: Group):
        self.group = group

    def change_title(self, new_title):
        self.group.title = new_title

    def end_year(self, duration_of_study=4):
        return self.group.start_date + duration_of_study

    def add(self, person: Student):
        if person.department != self.group.department:
            StudentService(person).change_department(self.group.department)
        self.group.members.update({len(self.group.members) + 1: (person.first_name, person.last_name)})
