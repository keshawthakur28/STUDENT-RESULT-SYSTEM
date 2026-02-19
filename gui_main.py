import tkinter as tk
from tkinter import messagebox
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

# ------------------ Functions ------------------

def calculate_percentage(m1, m2, m3):
    return (m1 + m2 + m3) / 3

def calculate_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"

def add_student():
    try:
        name = name_entry.get()
        roll = roll_entry.get()
        m1 = int(sub1_entry.get())
        m2 = int(sub2_entry.get())
        m3 = int(sub3_entry.get())

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

        messagebox.showinfo("Success", "Student Added Successfully!")

        clear_fields()

    except:
        messagebox.showerror("Error", "Please enter valid data")

def show_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    output_text.delete("1.0", tk.END)

    for row in records:
        output_text.insert(tk.END, f"ID: {row[0]}\n")
        output_text.insert(tk.END, f"Name: {row[1]}\n")
        output_text.insert(tk.END, f"Roll: {row[2]}\n")
        output_text.insert(tk.END, f"Marks: {row[3]}, {row[4]}, {row[5]}\n")
        output_text.insert(tk.END, f"Percentage: {round(row[6],2)}\n")
        output_text.insert(tk.END, f"Grade: {row[7]}\n")
        output_text.insert(tk.END, "----------------------\n")

    conn.close()

def clear_fields():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    sub1_entry.delete(0, tk.END)
    sub2_entry.delete(0, tk.END)
    sub3_entry.delete(0, tk.END)

# ------------------ GUI Design ------------------

root = tk.Tk()
root.title("Student Result Management System")
root.geometry("500x600")

tk.Label(root, text="Student Result Management System", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Student Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Roll Number").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Label(root, text="Subject 1 Marks").pack()
sub1_entry = tk.Entry(root)
sub1_entry.pack()

tk.Label(root, text="Subject 2 Marks").pack()
sub2_entry = tk.Entry(root)
sub2_entry.pack()

tk.Label(root, text="Subject 3 Marks").pack()
sub3_entry = tk.Entry(root)
sub3_entry.pack()

tk.Button(root, text="Add Student", command=add_student, bg="green", fg="white").pack(pady=10)
tk.Button(root, text="Show Students", command=show_students, bg="blue", fg="white").pack(pady=5)

output_text = tk.Text(root, height=15)
output_text.pack(pady=10)

root.mainloop()
