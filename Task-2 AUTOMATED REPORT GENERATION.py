import numpy as np
students= [
    {"Name": "John", "Math": 85, "Science": 90, "English": 78},
    {"Name": "Reshma", "Math": 92, "Science": 88, "English": 95},
    {"Name": "Michael", "Math": 78, "Science": 85, "English": 90},
    {"Name": "Madhavi", "Math": 79, "Science": 83, "English": 87},
    
]

def generate_report(students):
    report = ""
    for student in students:
        report += f"Student Name: {student['Name']}\n"
        report += f"Math: {student['Math']}\n"
        report += f"Science: {student['Science']}\n"
        report += f"English: {student['English']}\n"
        report += f"Average: {(student['Math'] + student['Science'] + student['English']) / 3:.2f}\n\n"
    return report

report = generate_report(students)

# Save report to file
with open("student_report.txt", "w") as f:
    f.write(report)

print("Report generated successfully!")
print(report)
