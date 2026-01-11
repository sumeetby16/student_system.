# Student Attendance & Performance Management System
# Simple base version for main branch

class Student:
    def __init__(self, student_id, name, age, department):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.department = department
        self.attendance = 0
        self.marks = []

    def mark_attendance(self):
        self.attendance += 1

    def add_mark(self, mark):
        self.marks.append(mark)

    def get_average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    def get_performance_status(self):
        avg = self.get_average()
        if avg >= 75:
            return "Excellent"
        elif avg >= 50:
            return "Average"
        else:
            return "Needs Improvement"


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, department):
        self.students[student_id] = Student(student_id, name, age, department)

    def mark_attendance(self, student_id):
        if student_id in self.students:
            self.students[student_id].mark_attendance()
        else:
            print("Student not found")

    def add_marks(self, student_id, mark):
        if student_id in self.students:
            self.students[student_id].add_mark(mark)
        else:
            print("Student not found")

    def display_student_details(self, student_id):
        if student_id not in self.students:
            print("Student not found")
            return

        student = self.students[student_id]
        print("\n--- Student Report ---")
        print("ID:", student.student_id)
        print("Name:", student.name)
        print("Age:", student.age)
        print("Department:", student.department)
        print("Attendance:", student.attendance)
        print("Average Marks:", student.get_average())
        print("Performance Status:", student.get_performance_status())


# Program execution
if __name__ == "__main__":
    system = StudentManagementSystem()

    # Adding students
    system.add_student(1, "Amit", 20, "Computer Science")
    system.add_student(2, "Neha", 21, "Mechanical")

    # Mark attendance
    system.mark_attendance(1)
    system.mark_attendance(1)
    system.mark_attendance(2)

    # Add marks
    system.add_marks(1, 70)
    system.add_marks(1, 80)
    system.add_marks(1, 75)

    system.add_marks(2, 55)
    system.add_marks(2, 60)
    system.add_marks(2, 50)

    # Display reports
    system.display_student_details(1)
    system.display_student_details(2)
