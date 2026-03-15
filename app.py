import json
import os

database = "students.json"
student_records = []

def loadStudentRecords():
    global student_records
    if os.path.exists(database):
        with open(database, "r") as db:
            student_records = json.load(db)
    else:
        student_records = []


def saveStudentRecords():
    with open(database, "w") as db:
        json.dump(student_records, db, indent=4)


def calculateGrade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

def gradePoint(grade):
    table = {
        "A":4,
        "B":3,
        "C":2,
        "D":1,
        "F":0
    }
    return table.get(grade,0)


def calculateGPA(subjects):

    total_points = 0
    total_subjects = len(subjects)

    for subject in subjects:
        grade = subject["grade"]
        total_points += gradePoint(grade)

    if total_subjects == 0:
        return 0

    gpa = total_points / total_subjects
    return round(gpa,2)


def addStudent():

    os.system("cls")

    print("\nAdd Student\n")

    name = input("Enter student name: ")
    subjects = []

    total_subjects = int(input("How many subjects?: "))

    # enter subject marks
    for i in range(total_subjects):

        print(f"\nSubject {i+1}")

        subject_name = input("Subject name: ")
        mark = int(input("Marks: "))

        grade = calculateGrade(mark)

        subjects.append({
            "subject":subject_name,
            "marks":mark,
            "grade":grade
        })

    gpa = calculateGPA(subjects)

    student = {
        "name":name,
        "subjects":subjects,
        "gpa":gpa
    }

    student_records.append(student)

    saveStudentRecords()

    print("\nStudent added successfully")
    os.system("pause")
    os.system("cls")

def viewStudents():
    os.system("cls")
    print("\nStudent Records\n")
    if len(student_records) == 0:
        print("No student records found")
    else:
        for i, student in enumerate(student_records,1):
            print(f"\n{i}. {student['name']}")
            print("Subjects:")
            for sub in student["subjects"]:
                print(f"   {sub['subject']} - {sub['marks']} - {sub['grade']}")
            print("GPA:", student["gpa"])
    os.system("pause")
    os.system("cls")

# ---------------------------------------------
# Delete student
# ---------------------------------------------
def deleteStudent():

    viewStudents()

    index = int(input("\nEnter student number to delete: "))

    if index <= len(student_records):

        student_records.pop(index-1)
        saveStudentRecords()

        print("Student deleted")

    else:
        print("Invalid student number")

    os.system("pause")
    os.system("cls")

# ---------------------------------------------
# Generate report
# ---------------------------------------------
def generateReport():

    os.system("cls")

    print("\nStudent GPA Report\n")

    if len(student_records) == 0:
        print("No records")

    else:

        for student in student_records:
            print(f"{student['name']}  |  GPA: {student['gpa']}")

    os.system("pause")
    os.system("cls")

# ---------------------------------------------
# Main menu
# ---------------------------------------------
def menu():

    loadStudentRecords()

    while True:

        print("-----------------------------")
        print(" Student Management System")
        print("-----------------------------")

        print("1. View Students")
        print("2. Add Student")
        print("3. Delete Student")
        print("4. Generate GPA Report")
        print("5. Exit")

        print("-----------------------------")

        choice = input("Select option: ")

        if choice == "1":
            viewStudents()

        elif choice == "2":
            addStudent()

        elif choice == "3":
            deleteStudent()

        elif choice == "4":
            generateReport()

        elif choice == "5":
            print("Goodbye")
            break

        else:
            print("Invalid option")
            os.system("pause")
            os.system("cls")

# ---------------------------------------------
# Start program
# ---------------------------------------------
menu()