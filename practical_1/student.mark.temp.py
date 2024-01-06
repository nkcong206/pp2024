import csv

def check_id(id, list):
    for l in list:
        if l[0] == id:
            return True
    return False 

def input_students(num, students):
    n = int(input(f"number of students {num}, add number of new students: "))
    for i in range(n):
        id = input("Student ID: ")
        while check_id(id, students):
            print("This ID already exists. Enter a different ID.")
            id = input("Student ID: ")
        name = input("Student name: ")
        dob = input("Student date of birth: ")
        students.append((id, name, dob))
    save_students_to_csv(students)
    num += n    
    return num, students

def save_students_to_csv(students):
    with open('students.csv', 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Name', 'DoB']
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)        
        writer.writerows(students)

def input_students_from_csv():
    stu = []
    try:
        with open('students.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader, None)
            for row in reader:
                stu.append(row)
    except FileNotFoundError:
        pass
    n = len(stu)
    return n, stu

def input_courses(num, courses):
    n = int(input(f"Number of courses: {num}, add number of new courses: "))
    for i in range(n):
        id = input("Course ID: ")
        while check_id(id, courses):
            print("This ID already exists. Enter a different ID.")
            id = input("Course ID: ")
        name = input("Course name: ")
        courses.append((id, name))
    save_courses_to_csv(courses)
    num += n
    return num, courses

def save_courses_to_csv(courses):
    with open('courses.csv', 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Name']
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        writer.writerows(courses)

def input_courses_from_csv():
    courses = []
    try:
        with open('courses.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader, None)
            for row in reader:
                courses.append(row)
    except FileNotFoundError:
        pass
    n = len(courses)
    return n, courses

def input_marks(marks, courses, students):
    if not students or not courses:
        print("Students or courses list is empty. Exiting input_marks.")
        return marks
    
    print("List of courses:")
    for i, course in enumerate(courses):
        print(f"{i + 1}. {course[1]}")

    course_index = int(input("Select a course (enter index): ")) - 1
    selected_course = courses[course_index]

    if selected_course[0] in marks:
        print(f"Course '{selected_course[1]}' already exists in marks.")
        return marks 
    
    for student in students:
        mark = float(input(f"Enter marks for {student[1]} in {selected_course[1]}: "))
        if selected_course[0] in marks:
            marks[selected_course[0]].append((student[0], mark))
        else:
            marks[selected_course[0]] = [(student[0], mark)]

    save_marks_to_csv(marks)
    return marks
    
def input_marks_from_csv():
    marks = {}
    try:
        with open('marks.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader, None)
            for row in reader:
                course_id, student_id, mark = row
                mark = float(mark)
                if course_id in marks:
                    marks[course_id].append((student_id, mark))
                else:
                    marks[course_id] = [(student_id, mark)]
    except FileNotFoundError:
        pass
    return marks

def save_marks_to_csv(marks):
    with open('marks.csv', 'w', newline='') as csvfile:
        fieldnames = ['course_ID', 'student_ID', 'marks']
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)  
        for course_id, students in marks.items():
            for student_id, mark in students:
                writer.writerow([course_id, student_id, mark])
                

def list_courses(courses):
    print("List of courses:")
    for course in courses:
        print(f"- {course[1]}")

def list_students(students):
    print("List of students:")
    for student in students:
        print(f"- {student[1]}")

def show_student_marks(marks):
    print("List of courses:")
    for i, course_id in enumerate(marks.keys()):
        print(f"{i + 1}. Course ID: {course_id}")
    course_id = input("Course ID: ")
    print("Student marks for the course:")
    if course_id in marks:
        for student_mark in marks[course_id]:
            student_id = student_mark[0]
            mark = student_mark[1]
            print(f"Student ID: {student_id}, Mark: {mark}")
    else:
        print("No marks recorded for this course yet.")

def main():
    students_info = []
    courses_info = []
    marks_info = {}
    num_students = 0
    num_courses = 0
    
    num_students, students_info = input_students_from_csv()
    num_courses, courses_info = input_courses_from_csv()
    marks_info = input_marks_from_csv()
    
    print(students_info)
    print(courses_info)
    print(marks_info)
    while True:
        print("\n=== Student Mark Management ===")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks of a course")
        print("4. List courses")
        print("5. List students")
        print("6. Show student marks for a course")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            num_students, students_info = input_students(num_students,students_info)
        if choice == "2":
            num_courses, courses_info = input_courses(num_courses,courses_info)
        if choice == "3":
            marks_info = input_marks(marks_info,courses_info, students_info)
        elif choice == "4":
            list_courses(courses_info)
        elif choice == "5":
            list_students(students_info)
        elif choice == "6":
            show_student_marks(marks_info) 
        elif choice == "7":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Enter a valid option.")

if __name__ == "__main__":
    main()