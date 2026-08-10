# Attendance Tracker
# TechStart Solutions Internal Tool

student_list = ["Alice", "Bob", "Carol", "David"]
attendance = {}

# Main program
for student in student_list:
    response = input("Is " + student + " present? (yes/no): ")
    attendance[mark_name] = response  

# Display attendance record
print("\n--- Attendance Record ---")
for student in student_list:
    if student in attendance:
        print(student + ": " + attendance[student])
    else:
        print(student + ": Not marked")
