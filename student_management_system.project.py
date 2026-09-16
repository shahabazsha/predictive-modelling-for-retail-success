import os

students = []


# -------------------------
# Add Student
# -------------------------
def add_student():
    name = input("Enter name: ")

    try:
        age = int(input("Enter age: "))
        marks = int(input("Enter marks: "))
    except ValueError:
        print("Please enter numbers for age and marks.")
        return

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)

    if marks >= 50:
        print("Pass")
    else:
        print("Fail")

    print("Student added successfully!")


# -------------------------
# View Students
# -------------------------
def view_students():
    if len(students) == 0:
        print("No students found.")
        return

    print("\n--- All Students ---")

    for student in students:
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Marks:", student["marks"])
        print("----------------")


# -------------------------
# Search Student
# -------------------------
def search_student():
    search_name = input("Enter student name to search: ")

    for student in students:
        if student["name"] == search_name:
            print("\nStudent found!")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


# -------------------------
# Update Student
# -------------------------
def update_student():
    update_name = input("Enter student name to update: ")

    for student in students:
        if student["name"] == update_name:

            print("Student found.")

            new_name = input("Enter new name: ")

            try:
                new_age = int(input("Enter new age: "))
                new_marks = int(input("Enter new marks: "))
            except ValueError:
                print("Please enter numbers for age and marks.")
                return

            student["name"] = new_name
            student["age"] = new_age
            student["marks"] = new_marks

            print("Student updated successfully!")
            return

    print("Student not found.")


# -------------------------
# Delete Student
# -------------------------
def delete_student():
    delete_name = input("Enter student name to delete: ")

    for student in students:
        if student["name"] == delete_name:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# -------------------------
# Save Students to File
# -------------------------
def save_students():
    file = open("student.txt", "w")

    for student in students:
        file.write(student["name"] + "\n")
        file.write(str(student["age"]) + "\n")
        file.write(str(student["marks"]) + "\n")

    file.close()

    print("Students saved to student.txt")


# -------------------------
# Read Students from File
# -------------------------
def read_file():
    file = open("student.txt", "r")

    content = file.read()

    print("\n--- File Content ---")
    print(content)

    file.close()


# -------------------------
# Main Program
# -------------------------
while True:

    print("\n==========================")
    print(" Student Management System")
    print("==========================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save Students")
    print("7. Read File")
    print("8. Show Current Folder")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        save_students()

    elif choice == "7":
        read_file()

    elif choice == "8":
        print(os.getcwd())

    elif choice == "9":
        print("Program closed.")
        break

    else:
        print("Invalid choice. Please try again.")   
