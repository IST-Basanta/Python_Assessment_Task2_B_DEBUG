# This program uses two data structures: student_list as a  list, and attendance as
# a dictionary with each student's name as the key and "yes" or "no" as the value.
# Logic: The program asks whether each student is present or absent and saves
# the response in the attendance dictionary.
# Logic: Finally, the attendance is displayed.

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
