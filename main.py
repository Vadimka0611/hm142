class Student:
    def __init__(self, first_name, last_name, record_book):
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Record book: {self.record_book}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self):
        return hash(str(self))

class GroupOverflowError(Exception):

    def __init__(self, message="Cannot add more than 10 students"):
        self.message = message
        super().__init__(self.message)

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupOverflowError(f"Cannot add student {student.first_name} {student.last_name}, group already has 10 students")
        self.group.add(student)

    def delete_student(self, last_name):
        student_delete = self.find_student(last_name)
        if student_delete:
            self.group.remove(student_delete)
        else:
            print(f"Student '{last_name}' not found")

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join([str(student) for student in self.group])
        return f"Group {self.number}:\n{all_students}"

if __name__ == "__main__":

    st1 = Student('Steve', 'Jobs', 'AN142')
    st2 = Student('Liza', 'Taylor', 'AN145')

    gr = Group('PD1')
    gr.add_student(st1)
    gr.add_student(st2)

    print(gr)

    assert gr.find_student('Jobs') == st1
    assert gr.find_student('Jobs2') is None

    gr.delete_student('Taylor')
    print(gr)

    try:
        for i in range(9):
            gr.add_student(Student(f"First{i}", f"Last{i}", f"AN{i+146}"))
        gr.add_student(Student("New", "Student", "AN156"))
    except GroupOverflowError as e:
        print(e)
