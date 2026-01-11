from student_system import generate_student_report

def test_report_contains_student_names():
    report = generate_student_report()
    assert "Amit" in report
    assert "Neha" in report


def test_report_contains_performance_status():
    report = generate_student_report()
    assert "Excellent" in report
    assert "Average" in report


def test_report_format():
    report = generate_student_report()
    assert report.startswith("---- Student Attendance & Performance Report ----")
