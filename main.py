import mysql.connector

def connect_database():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="Your Password",
        database="college_management",
        use_pure=True
    )
    return connection


def add_student():
    connection = connect_database()
    cursor = connection.cursor()

    print("\n--- Add Student ---")

    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    course = input("Enter course: ")
    semester = int(input("Enter semester: "))
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    query = """
        INSERT INTO students
        (name, age, gender, course, semester, phone, email)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (name, age, gender, course, semester, phone, email)

    cursor.execute(query, values)
    connection.commit()

    print("\nStudent added successfully!")

    cursor.close()
    connection.close()

def view_students():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    print("\n--- All Students ---")

    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print("--------------------------------")
            print("Student ID:", student[0])
            print("Name:", student[1])
            print("Age:", student[2])
            print("Gender:", student[3])
            print("Course:", student[4])
            print("Semester:", student[5])
            print("Phone:", student[6])
            print("Email:", student[7])

    cursor.close()
    connection.close()

def search_student():
    connection = connect_database()
    cursor = connection.cursor()

    print("\n--- Search Student ---")

    student_id = int(input("Enter student ID: "))

    query = "SELECT * FROM students WHERE student_id = %s"

    cursor.execute(query, (student_id,))

    student = cursor.fetchone()

    if student:
        print("\nStudent Found!")
        print("--------------------------------")
        print("Student ID:", student[0])
        print("Name:", student[1])
        print("Age:", student[2])
        print("Gender:", student[3])
        print("Course:", student[4])
        print("Semester:", student[5])
        print("Phone:", student[6])
        print("Email:", student[7])
    else:
        print("\nStudent not found.")

    cursor.close()
    connection.close()

def update_student():
    connection = connect_database()
    cursor = connection.cursor()

    print("\n--- Update Student ---")

    student_id = int(input("Enter student ID: "))

    # Check student
    cursor.execute(
        "SELECT * FROM students WHERE student_id = %s",
        (student_id,)
    )

    student = cursor.fetchone()

    if not student:
        print("\nStudent not found.")
        cursor.close()
        connection.close()
        return

    print("\nStudent Found!")
    print("1. Name")
    print("2. Age")
    print("3. Gender")
    print("4. Course")
    print("5. Semester")
    print("6. Phone")
    print("7. Email")

    choice = int(input("\nWhat do you want to update? "))

    if choice == 1:
        new_value = input("Enter new name: ")
        query = "UPDATE students SET name = %s WHERE student_id = %s"

    elif choice == 2:
        new_value = int(input("Enter new age: "))
        query = "UPDATE students SET age = %s WHERE student_id = %s"

    elif choice == 3:
        new_value = input("Enter new gender: ")
        query = "UPDATE students SET gender = %s WHERE student_id = %s"

    elif choice == 4:
        new_value = input("Enter new course: ")
        query = "UPDATE students SET course = %s WHERE student_id = %s"

    elif choice == 5:
        new_value = int(input("Enter new semester: "))
        query = "UPDATE students SET semester = %s WHERE student_id = %s"

    elif choice == 6:
        new_value = input("Enter new phone: ")
        query = "UPDATE students SET phone = %s WHERE student_id = %s"

    elif choice == 7:
        new_value = input("Enter new email: ")
        query = "UPDATE students SET email = %s WHERE student_id = %s"

    else:
        print("\nInvalid choice.")
        cursor.close()
        connection.close()
        return

    cursor.execute(query, (new_value, student_id))
    connection.commit()

    print("\nStudent updated successfully!")

    cursor.close()
    connection.close()

def delete_student():
    connection = connect_database()
    cursor = connection.cursor()

    print("\n--- Delete Student ---")

    student_id = int(input("Enter student ID to delete: "))

    # Check if student exists
    cursor.execute(
        "SELECT * FROM students WHERE student_id = %s",
        (student_id,)
    )

    student = cursor.fetchone()

    if not student:
        print("\nStudent not found.")
        cursor.close()
        connection.close()
        return

    print("\nStudent Found:")
    print("Student ID:", student[0])
    print("Name:", student[1])
    print("Course:", student[4])
    print("Semester:", student[5])

    confirm = input("\nAre you sure you want to delete this student? (yes/no): ")

    if confirm.lower() == "yes":
        cursor.execute(
            "DELETE FROM students WHERE student_id = %s",
            (student_id,)
        )

        connection.commit()

        print("\nStudent deleted successfully!")

    else:
        print("\nDelete cancelled.")

    cursor.close()
    connection.close()


def add_teacher():
    connection = connect_database()
    cursor = connection.cursor()

    print("\n--- Add Teacher ---")

    name = input("Enter teacher name: ")
    gender = input("Enter gender: ")
    department = input("Enter department: ")
    subject = input("Enter subject: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    query = """
        INSERT INTO teachers
        (name, gender, department, subject, phone, email)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        name, gender, department,
        subject, phone, email
    )

    cursor.execute(query, values)
    connection.commit()

    print("\nTeacher added successfully!")

    cursor.close()
    connection.close()

def view_teachers():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM teachers")

    teachers = cursor.fetchall()

    print("\n--- All Teachers ---")

    if len(teachers) == 0:
        print("No teachers found.")
    else:
        for teacher in teachers:
            print("--------------------------------")
            print("Teacher ID:", teacher[0])
            print("Name:", teacher[1])
            print("Gender:", teacher[2])
            print("Department:", teacher[3])
            print("Subject:", teacher[4])
            print("Phone:", teacher[5])
            print("Email:", teacher[6])

    cursor.close()
    connection.close()

def search_teacher():
    connection = connect_database()
    cursor = connection.cursor()

    print("\n--- Search Teacher ---")

    teacher_id = int(input("Enter teacher ID: "))

    cursor.execute(
        "SELECT * FROM teachers WHERE teacher_id = %s",
        (teacher_id,)
    )

    teacher = cursor.fetchone()

    if teacher:
        print("\nTeacher Found!")
        print("--------------------------------")
        print("Teacher ID:", teacher[0])
        print("Name:", teacher[1])
        print("Gender:", teacher[2])
        print("Department:", teacher[3])
        print("Subject:", teacher[4])
        print("Phone:", teacher[5])
        print("Email:", teacher[6])
    else:
        print("\nTeacher not found.")

    cursor.close()
    connection.close()

def update_teacher():
    connection = connect_database()
    cursor = connection.cursor()

    print("\n--- Update Teacher ---")

    teacher_id = int(input("Enter teacher ID: "))

    cursor.execute(
        "SELECT * FROM teachers WHERE teacher_id = %s",
        (teacher_id,)
    )

    teacher = cursor.fetchone()

    if not teacher:
        print("\nTeacher not found.")
        cursor.close()
        connection.close()
        return

    print("\nTeacher Found!")
    print("1. Name")
    print("2. Gender")
    print("3. Department")
    print("4. Subject")
    print("5. Phone")
    print("6. Email")

    choice = int(input("\nWhat do you want to update? "))

    if choice == 1:
        new_value = input("Enter new name: ")
        query = "UPDATE teachers SET name = %s WHERE teacher_id = %s"

    elif choice == 2:
        new_value = input("Enter new gender: ")
        query = "UPDATE teachers SET gender = %s WHERE teacher_id = %s"

    elif choice == 3:
        new_value = input("Enter new department: ")
        query = "UPDATE teachers SET department = %s WHERE teacher_id = %s"

    elif choice == 4:
        new_value = input("Enter new subject: ")
        query = "UPDATE teachers SET subject = %s WHERE teacher_id = %s"

    elif choice == 5:
        new_value = input("Enter new phone: ")
        query = "UPDATE teachers SET phone = %s WHERE teacher_id = %s"

    elif choice == 6:
        new_value = input("Enter new email: ")
        query = "UPDATE teachers SET email = %s WHERE teacher_id = %s"

    else:
        print("\nInvalid choice.")
        cursor.close()
        connection.close()
        return

    cursor.execute(query, (new_value, teacher_id))
    connection.commit()

    print("\nTeacher updated successfully!")

    cursor.close()
    connection.close()
    
    

def delete_teacher():
    connection = connect_database()
    cursor = connection.cursor()

    print("\n--- Delete Teacher ---")

    teacher_id = int(input("Enter teacher ID to delete: "))

    # Check if teacher exists
    cursor.execute(
        "SELECT * FROM teachers WHERE teacher_id = %s",
        (teacher_id,)
    )

    teacher = cursor.fetchone()

    if not teacher:
        print("\nTeacher not found.")
        cursor.close()
        connection.close()
        return

    print("\nTeacher Found:")
    print("Teacher ID:", teacher[0])
    print("Name:", teacher[1])
    print("Department:", teacher[3])
    print("Subject:", teacher[4])

    confirm = input(
        "\nAre you sure you want to delete this teacher? (yes/no): "
    )

    if confirm.lower() == "yes":
        cursor.execute(
            "DELETE FROM teachers WHERE teacher_id = %s",
            (teacher_id,)
        )

        connection.commit()

        print("\nTeacher deleted successfully!")

    else:
        print("\nDelete cancelled.")

    cursor.close()
    connection.close()

def add_course():
    connection = connect_database()
    cursor = connection.cursor()

    print("\n--- Add Course ---")

    course_name = input("Enter course name: ")
    department = input("Enter department: ")
    semester = int(input("Enter semester: "))
    subject = input("Enter subject: ")
    teacher_id = int(input("Enter teacher ID: "))

    # Check whether teacher exists
    cursor.execute(
        "SELECT * FROM teachers WHERE teacher_id = %s",
        (teacher_id,)
    )

    teacher = cursor.fetchone()

    if not teacher:
        print("\nTeacher not found. Please enter a valid teacher ID.")
        cursor.close()
        connection.close()
        return

    query = """
        INSERT INTO courses
        (course_name, department, semester, subject, teacher_id)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        course_name,
        department,
        semester,
        subject,
        teacher_id
    )

    cursor.execute(query, values)
    connection.commit()

    print("\nCourse added successfully!")

    cursor.close()
    connection.close()

def view_courses():
    connection = connect_database()
    cursor = connection.cursor()

    query = """
        SELECT
            courses.course_id,
            courses.course_name,
            courses.department,
            courses.semester,
            courses.subject,
            teachers.name
        FROM courses
        JOIN teachers
        ON courses.teacher_id = teachers.teacher_id
    """

    cursor.execute(query)

    courses = cursor.fetchall()

    print("\n--- All Courses ---")

    if len(courses) == 0:
        print("No courses found.")
    else:
        for course in courses:
            print("--------------------------------")
            print("Course ID:", course[0])
            print("Course Name:", course[1])
            print("Department:", course[2])
            print("Semester:", course[3])
            print("Subject:", course[4])
            print("Teacher:", course[5])

    cursor.close()
    connection.close()

def search_course():
    connection = connect_database()
    cursor = connection.cursor()

    print("\n--- Search Course ---")

    course_id = int(input("Enter course ID: "))

    query = """
        SELECT
            courses.course_id,
            courses.course_name,
            courses.department,
            courses.semester,
            courses.subject,
            teachers.name
        FROM courses
        JOIN teachers
        ON courses.teacher_id = teachers.teacher_id
        WHERE courses.course_id = %s
    """

    cursor.execute(query, (course_id,))

    course = cursor.fetchone()

    if course:
        print("\nCourse Found!")
        print("--------------------------------")
        print("Course ID:", course[0])
        print("Course Name:", course[1])
        print("Department:", course[2])
        print("Semester:", course[3])
        print("Subject:", course[4])
        print("Teacher:", course[5])
    else:
        print("\nCourse not found.")

    cursor.close()
    connection.close()

def update_course():
    connection = connect_database()
    cursor = connection.cursor()

    print("\n--- Update Course ---")

    course_id = int(input("Enter course ID: "))

    cursor.execute(
        "SELECT * FROM courses WHERE course_id = %s",
        (course_id,)
    )

    course = cursor.fetchone()

    if not course:
        print("\nCourse not found.")
        cursor.close()
        connection.close()
        return

    print("\nWhat do you want to update?")
    print("1. Course Name")
    print("2. Department")
    print("3. Semester")
    print("4. Subject")
    print("5. Teacher")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_value = input("Enter new course name: ")
        query = "UPDATE courses SET course_name = %s WHERE course_id = %s"

    elif choice == "2":
        new_value = input("Enter new department: ")
        query = "UPDATE courses SET department = %s WHERE course_id = %s"

    elif choice == "3":
        new_value = int(input("Enter new semester: "))
        query = "UPDATE courses SET semester = %s WHERE course_id = %s"

    elif choice == "4":
        new_value = input("Enter new subject: ")
        query = "UPDATE courses SET subject = %s WHERE course_id = %s"

    elif choice == "5":
        new_value = int(input("Enter new teacher ID: "))

        cursor.execute(
            "SELECT * FROM teachers WHERE teacher_id = %s",
            (new_value,)
        )

        teacher = cursor.fetchone()

        if not teacher:
            print("\nTeacher not found.")
            cursor.close()
            connection.close()
            return

        query = "UPDATE courses SET teacher_id = %s WHERE course_id = %s"

    else:
        print("\nInvalid choice.")
        cursor.close()
        connection.close()
        return

    cursor.execute(query, (new_value, course_id))
    connection.commit()

    print("\nCourse updated successfully!")

    cursor.close()
    connection.close()

def delete_course():
    connection = connect_database()
    cursor = connection.cursor()

    print("\n--- Delete Course ---")

    course_id = int(input("Enter course ID: "))

    cursor.execute(
        "SELECT * FROM courses WHERE course_id = %s",
        (course_id,)
    )

    course = cursor.fetchone()

    if not course:
        print("\nCourse not found.")
        cursor.close()
        connection.close()
        return

    print("\nCourse Found!")
    print("Course ID:", course[0])
    print("Course Name:", course[1])
    print("Department:", course[2])
    print("Semester:", course[3])
    print("Subject:", course[4])

    confirm = input("\nAre you sure you want to delete this course? (yes/no): ")

    if confirm.lower() == "yes":
        cursor.execute(
            "DELETE FROM courses WHERE course_id = %s",
            (course_id,)
        )

        connection.commit()
        print("\nCourse deleted successfully!")

    else:
        print("\nCourse was not deleted.")

    cursor.close()
    connection.close()

def add_marks():
    connection = connect_database()
    cursor = connection.cursor()

    print("\n--- Add Marks ---")

    student_id = int(input("Enter student ID: "))
    course_id = int(input("Enter course ID: "))
    marks = int(input("Enter marks: "))

    # Check student
    cursor.execute(
        "SELECT * FROM students WHERE student_id = %s",
        (student_id,)
    )

    student = cursor.fetchone()

    if not student:
        print("\nStudent not found.")
        cursor.close()
        connection.close()
        return

    # Check course
    cursor.execute(
        "SELECT * FROM courses WHERE course_id = %s",
        (course_id,)
    )

    course = cursor.fetchone()

    if not course:
        print("\nCourse not found.")
        cursor.close()
        connection.close()
        return

    # Check marks
    if marks < 0 or marks > 100:
        print("\nMarks must be between 0 and 100.")
        cursor.close()
        connection.close()
        return

    query = """
        INSERT INTO marks
        (student_id, course_id, marks)
        VALUES (%s, %s, %s)
    """

    values = (student_id, course_id, marks)

    cursor.execute(query, values)
    connection.commit()

    print("\nMarks added successfully!")

    cursor.close()
    connection.close()

def view_marks():
    connection = connect_database()
    cursor = connection.cursor()

    query = """
        SELECT
            marks.marks_id,
            students.name,
            courses.course_name,
            courses.subject,
            marks.marks
        FROM marks
        JOIN students
            ON marks.student_id = students.student_id
        JOIN courses
            ON marks.course_id = courses.course_id
    """

    cursor.execute(query)

    results = cursor.fetchall()

    print("\n--- All Marks ---")

    if len(results) == 0:
        print("No marks found.")
    else:
        for result in results:
            print("--------------------------------")
            print("Marks ID:", result[0])
            print("Student:", result[1])
            print("Course:", result[2])
            print("Subject:", result[3])
            print("Marks:", result[4])

    cursor.close()
    connection.close()

def search_marks():
    connection = connect_database()
    cursor = connection.cursor()

    print("\n--- Search Marks ---")

    student_id = int(input("Enter student ID: "))

    query = """
        SELECT
            students.name,
            courses.course_name,
            courses.subject,
            marks.marks
        FROM marks
        JOIN students
            ON marks.student_id = students.student_id
        JOIN courses
            ON marks.course_id = courses.course_id
        WHERE marks.student_id = %s
    """

    cursor.execute(query, (student_id,))

    results = cursor.fetchall()

    if len(results) == 0:
        print("\nNo marks found for this student.")
    else:
        print("\n--- Student Marks ---")

        for result in results:
            print("--------------------------------")
            print("Student:", result[0])
            print("Course:", result[1])
            print("Subject:", result[2])
            print("Marks:", result[3])

    cursor.close()
    connection.close()

def update_marks():
    connection = connect_database()
    cursor = connection.cursor()

    print("\n--- Update Marks ---")

    marks_id = int(input("Enter marks ID: "))

    cursor.execute(
        "SELECT * FROM marks WHERE marks_id = %s",
        (marks_id,)
    )

    record = cursor.fetchone()

    if not record:
        print("\nMarks record not found.")
        cursor.close()
        connection.close()
        return

    print("\nCurrent Marks:", record[3])

    new_marks = int(input("Enter new marks: "))

    if new_marks < 0 or new_marks > 100:
        print("\nMarks must be between 0 and 100.")
        cursor.close()
        connection.close()
        return

    cursor.execute(
        "UPDATE marks SET marks = %s WHERE marks_id = %s",
        (new_marks, marks_id)
    )

    connection.commit()

    print("\nMarks updated successfully!")

    cursor.close()
    connection.close()

def delete_marks():
    connection = connect_database()
    cursor = connection.cursor()

    print("\n--- Delete Marks ---")

    marks_id = int(input("Enter marks ID: "))

    cursor.execute(
        "SELECT * FROM marks WHERE marks_id = %s",
        (marks_id,)
    )

    record = cursor.fetchone()

    if not record:
        print("\nMarks record not found.")
        cursor.close()
        connection.close()
        return

    print("\nMarks Record Found!")
    print("Marks ID:", record[0])
    print("Student ID:", record[1])
    print("Course ID:", record[2])
    print("Marks:", record[3])

    confirm = input(
        "\nAre you sure you want to delete these marks? (yes/no): "
    )

    if confirm.lower() == "yes":
        cursor.execute(
            "DELETE FROM marks WHERE marks_id = %s",
            (marks_id,)
        )

        connection.commit()
        print("\nMarks deleted successfully!")

    else:
        print("\nMarks were not deleted.")

    cursor.close()
    connection.close()

#main function
while True:
    print("\n================================")
    print("     COLLEGE MANAGEMENT SYSTEM")
    print("================================")

    print("1. Student Management")
    print("2. Teacher Management")
    print("3. Course Management")
    print("4. Marks Management")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\n--- Student Management ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back")

        student_choice = input("\nEnter your choice: ")

        if student_choice == "1":
            add_student()

        elif student_choice == "2":
            view_students()

        elif student_choice == "3":
            search_student()

        elif student_choice == "4":
            update_student()

        elif student_choice == "5":
            delete_student()

        elif student_choice == "6":
            print("\nGoing back...")

        else:
            print("\nInvalid choice!")

    elif choice == "2":
        print("\n--- Teacher Management ---")
        print("1. Add Teacher")
        print("2. View Teachers")
        print("3. Search Teacher")
        print("4. Update Teacher")
        print("5. Delete Teacher")
        print("6. Back")

        teacher_choice = input("\nEnter your choice: ")

        if teacher_choice == "1":
            add_teacher()

        elif teacher_choice == "2":
            view_teachers()

        elif teacher_choice == "3":
            search_teacher()

        elif teacher_choice == "4":
            update_teacher()

        elif teacher_choice == "5":
            delete_teacher()

        elif teacher_choice == "6":
            print("\nGoing back...")

        else:
            print("\nInvalid choice!")

    elif choice == "3":
        print("\n--- Course Management ---")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Search Course")
        print("4. Update Course")
        print("5. Delete Course")
        print("6. Back")

        course_choice = input("\nEnter your choice: ")

        if course_choice == "1":
            add_course()

        elif course_choice == "2":
            view_courses()

        elif course_choice == "3":
            search_course()

        elif course_choice == "4":
            update_course()

        elif course_choice == "5":
            delete_course()

        elif course_choice == "6":
            print("\nGoing back...")

        else:
            print("\nInvalid choice!")

    elif choice == "4":
        print("\n--- Marks Management ---")
        print("1. Add Marks")
        print("2. View Marks")
        print("3. Search Marks")
        print("4. Update Marks")
        print("5. Delete Marks")
        print("6. Back")

        marks_choice = input("\nEnter your choice: ")

        if marks_choice == "1":
            add_marks()

        elif marks_choice == "2":
            view_marks()

        elif marks_choice == "3":
            search_marks()

        elif marks_choice == "4":
            update_marks()

        elif marks_choice == "5":
            delete_marks()

        elif marks_choice == "6":
            print("\nGoing back...")

        else:
            print("\nInvalid choice!")

    elif choice == "5":
        print("\nThank you for using College Management System!")
        break

    else:
        print("\nInvalid choice!")


