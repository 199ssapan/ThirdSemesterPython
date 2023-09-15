import os
import marks as mk
import sqlite3

ERROR = 1
OK = 0

CHANGE_EXISTS = 1
ADD_NEW_MARK = 2
DELETE_MARK = 3
ADD_NEW_STUDENT = 4
DELETE_STUDENT = 5
SHOW_DB = 6
EXIT_CYCLE = 7

def clrCnsl():
    os.system("cls")



def addStudent(cur, con):
    clrCnsl()
    name = input("Enter student's name:     ")
    if name == "":
        print("Name must be not empty string")
        input()
        return ERROR
    surname = input("Enter student's surname:     ")
    if surname == "":
        print("Surname must be not empty string")
        input()
        return ERROR
    marks = input("Enter student's marks(if he has no marks just push 'Enter')      ")
    if marks.isdigit() or marks == "":
        if mk.checkMarkString(marks):
            print("Marks must be integer numbers")
            return ERROR
    else:
        return ERROR
    cur.execute(""" INSERT INTO students (name, surname, marks) VALUES (?, ?, ?) """, (name, surname, marks))
    con.commit()
    clrCnsl()
    return OK


def deleteStudent(cur, con):
    if mk.checkEmptyDB(cur):
        print("No students")
        return ERROR
    students = cur.execute(""" SELECT * FROM students """)
    mk.printDB(cur)
    cur.execute(""" SELECT * FROM students """)
    students = cur.fetchall()
    stId = int(input("Select the id of the student you want to delete:    "))
    if stId > len(students):
        print("Invalid id")
        input()
        return ERROR
    cur.execute(""" DELETE FROM students WHERE student_id = ? """, (stId,))
    cur.execute(""" UPDATE students SET student_id = student_id - 1 WHERE student_id > ? """, (stId,))
    con.commit()
    clrCnsl()
    return OK