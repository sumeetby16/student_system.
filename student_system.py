# Student Attendance & Performance Management System
# Base version for main branch

class Student:
    def __init__(self, student_id, name, department):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.attendance = 0
        self.marks = []

    def mark_attendance(self):
        self.attendance += 1

    def add_marks(self, mark):
        self.marks.append(mark)

    def average_marks(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, department):
        self.students[student_id] = Student(student_id, name, department)

    def mark_attendance(self, student_id):
        if student_id in self.students:
            self.students[student_id].mark_attendance()

    def add_marks(self, student_id, mark):
        if student_id in self.students:
            self.students[student_id].add_marks(mark)

    def display_student(self, student_id):
        if student_id not in self.students:
            print("Student not found")
            return

        student = self.students[student_id]
        print("Student ID:", student.student_id)
        print("Name:", student.name)
        print("Department:", student.department)
        print("Attendance:", student.attendance)
        print("Average Marks:", student.average_marks())


# Simple execution
if __name__ == "__main__":
    system = StudentManagementSystem()

    system.add_student(1, "Amit", "Computer Science")
    system.add_student(2, "Neha", "Mechanical")

    system.mark_attendance(1)
    system.mark_attendance(1)

    system.add_marks(1, 70)
    system.add_marks(1, 80)

    system.display_student(1)
