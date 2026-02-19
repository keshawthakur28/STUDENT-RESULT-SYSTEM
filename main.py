import sqlite3

# ------------------ Database Setup ------------------

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    roll_no TEXT,
    subject1 INTEGER,
    subject2 INTEGER,
    subject3 INTEGER,
    percentage REAL,
    grade TEXT
)
""")

conn.commit()
conn.close()

print("Database and Table Created Successfully")

# ------------------ Calculate Percentage ------------------

def calculate_percentage(m1, m2, m3):
    percentage = (m1 + m2 + m3) / 3
    return percentage

# ------------------ Calculate Grade ------------------

def calculate_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"

# ------------------ Add Student ------------------

def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    m1 = int(input("Enter Subject 1 Marks: "))
    m2 = int(input("Enter Subject 2 Marks: "))
    m3 = int(input("Enter Subject 3 Marks: "))

    percentage = calculate_percentage(m1, m2, m3)
    grade = calculate_grade(percentage)

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students(name, roll_no, subject1, subject2, subject3, percentage, grade)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, roll, m1, m2, m3, percentage, grade))

    conn.commit()
    conn.close()

    print("Student Added Successfully!")

# ------------------ Show Students ------------------

def show_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    if len(records) == 0:
        print("No Students Found!")
    else:
        print("\n--- Student Records ---")
        for row in records:
            print("ID:", row[0])
            print("Name:", row[1])
            print("Roll No:", row[2])
            print("Subject1:", row[3])
            print("Subject2:", row[4])
            print("Subject3:", row[5])
            print("Percentage:", round(row[6], 2))
            print("Grade:", row[7])
            print("------------------------")

    conn.close()

# ------------------ Main Menu ------------------

while True:
    print("\n--- Student Result Management System ---")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice! Please try again.")
