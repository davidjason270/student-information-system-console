import os

student_records = []
database = "records.txt"

def delete():
    index = int(input("Enter the student number of the student to delete"))
    student_records.pop(index-1)
    saveTasks()
    viewTask()

def loadTasks():
    with open(database, "r") as db:
        lines = db.readlines()
        for line in lines:
            student_records.append(line.strip())

def saveTasks():
    with open(database, "w") as db:
        for item in student_records:
            db.write(f"{item}\n")

def addTask():
    os.system("cls")
    print("\n\tAdd New Student\n")
    # ask the user to add an item
    listItem = input("Enter a Fullname:\n");
    student_records.append(listItem)
    saveTasks()

def viewTask():
    os.system("cls")
    print("\n\tView Tasks\n")
    if len(student_records) == 0:
        print("Empty Student Records")
    else:
        for i, item in enumerate(student_records, 1):
            print(f"{i}. {item}")
    os.system("pause")
    os.system("cls")

def menu():
    loadTasks()
    while True:
        print("----------------------------\n\tStudent Records System\n----------------------------")
        print("  1. View All Students Records")
        print("  2. Add Student")
        print("  3. Delete Student")
        print("  4. Exit")
        print("-------------------------\n")
        choice = int(input("Please select an Option :"))

        if choice == 1:
            viewTask()
        elif choice == 2:
            addTask()
        elif choice == 3:
           delete()
        elif choice == 4:
            print("Good bye")
            break
        else:
            print("Invalid Choice")

#call menu function
menu()