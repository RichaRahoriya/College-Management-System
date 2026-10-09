import mysql.connector

print("Starting...")

# Connect to MySQL
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Your Password",
    connection_timeout=5,
    use_pure=True
)

print("CONNECTED!")

# Create cursor
cursor = connection.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS college_management")

print("Database created successfully!")

# Select database
cursor.execute("USE college_management")

# Create students table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT,
        gender VARCHAR(20),
        course VARCHAR(50),
        semester INT,
        phone VARCHAR(15),
        email VARCHAR(100)
    )
""")

print("Students table created successfully!")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS teachers (
        teacher_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        gender VARCHAR(20),
        department VARCHAR(100),
        subject VARCHAR(100),
        phone VARCHAR(15),
        email VARCHAR(100)
    )
""")

print("Teachers table created successfully!")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        course_id INT AUTO_INCREMENT PRIMARY KEY,
        course_name VARCHAR(100) NOT NULL,
        department VARCHAR(100),
        semester INT,
        subject VARCHAR(100),
        teacher_id INT,
        FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
    )
""")

print("Courses table created successfully!")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS marks (
        marks_id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT,
        course_id INT,
        marks INT,
        FOREIGN KEY (student_id) REFERENCES students(student_id),
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
    )
""")

print("Marks table created successfully!")

# Close connection
cursor.close()
connection.close()

print("DONE!")