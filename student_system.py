# Student Attendance & Performance Management System
# Main branch version with simple function returning formatted output

def generate_student_report():
    students = {
        1: {
            "name": "Amit",
            "age": 20,
            "department": "Computer Science",
            "attendance": 2,
            "marks": [70, 80, 75]
        },
        2: {
            "name": "Neha",
            "age": 21,
            "department": "Mechanical",
            "attendance": 1,
            "marks": [55, 60, 50]
        }
    }

    report = "---- Student Attendance & Performance Report ----\n\n"

    for student_id in students:
        student = students[student_id]

        average = sum(student["marks"]) / len(student["marks"])

        if average >= 75:
            status = "Excellent"
        elif average >= 50:
            status = "Average"
        else:
            status = "Needs Improvement"

        report += f"Student ID: {student_id}\n"
        report += f"Name: {student['name']}\n"
        report += f"Age: {student['age']}\n"
        report += f"Department: {student['department']}\n"
        report += f"Attendance: {student['attendance']}\n"
        report += f"Average Marks: {average}\n"
        report += f"Performance Status: {status}\n"
        report += "----------------------------------\n"

    return report


# Normal execution
if __name__ == "__main__":
    output = generate_student_report()
    print(output)
