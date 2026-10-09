College Student Management System

📌 Project Overview

The College Student Management System is a console-based application developed using Python and MySQL. It helps manage college students, teachers, courses, and marks through a simple menu-driven interface.

The system performs basic CRUD (Create, Read, Update, Delete) operations and stores records in a MySQL database.

🚀 Features

👨‍🎓 Student Management

- Add new student records
- View all students
- Search students
- Update student details
- Delete student records

👩‍🏫 Teacher Management

- Add teacher records
- View all teachers
- Search teachers
- Update teacher details
- Delete teacher records

📚 Course Management

- Add new courses
- View course details with teacher names
- Search courses
- Update course information
- Delete courses

📝 Marks Management

- Add marks for students
- View marks with student and course details
- Search marks records
- Update marks
- Delete marks records

🛠️ Technologies Used

- Programming Language: Python
- Database: MySQL
- Database Connector: mysql-connector-python
- IDE: Visual Studio Code

⚙️ Requirements

- Python 3
- MySQL Server
- MySQL Workbench (optional)
- "mysql-connector-python" package

🔧 Installation and Setup

1. Download or clone this repository.

2. Install the required Python package:
   
   pip install mysql-connector-python

3. Make sure your MySQL Server is running.

4. Open "database.py" and "main.py", configure your MySQL connection credentials by replacing "Your Password" with your own MySQL password.

5. Run the database setup file once to create the database and tables:
   
   python database.py

6. Open "main.py" and configure your MySQL connection credentials.

7. Start the application:
   
   python main.py

🗄️ Database Structure

The system uses four main tables:

- "students" — stores student information
- "teachers" — stores teacher information
- "courses" — stores course details and teacher references
- "marks" — stores student marks for courses

Foreign keys connect courses with teachers and marks with students and courses.

🎯 Objective

The objective of this project is to practice Python programming, database connectivity, SQL queries, and CRUD operations by developing a basic college management application.
