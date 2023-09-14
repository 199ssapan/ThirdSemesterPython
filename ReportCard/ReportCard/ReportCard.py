
import sqlite3
import os

ERROR = 1
OK = 0

CHANGE_EXISTS = 1
ADD_NEW_MARK = 2
DELETE_MARK = 3
ADD_NEW_STUDENT = 4
DELETE_STUDENT = 5
SHOW_DB = 6
ID = 0
NAME = 1
SURNAME = 2
MARKS = 3


con = sqlite3.connect("database.db")

cur = con.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER NOT NULL PRIMARY KEY,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        marks TEXT NOT NULL
)""")


def clrCnsl():
    os.system("cls")

def printDB(cur):
    clrCnsl()
    cur.execute(""" SELECT * FROM students """)
    students = cur.fetchall()
    print("%-s| %-7s| %-7s| %-7s" % ("id", "name", "surname", "marks"))
    for student in students:
        print("%-2d| %-7s| %-7s| %-7s" % (student[ID], student[NAME], student[SURNAME], student[MARKS]))
        print()

def changeExistingMarks(cur, con, delFlag):
    clrCnsl()
    cur.execute(""" SELECT * FROM students """)
    students = cur.fetchall()
    printDB(cur)
    option = "delete:     " if delFlag else "change:      "
    stId = int(input("Select the ID of the student whose grades you want to " + option))
    if stId > len(students):
        print("No such student")
        input()
        return ERROR
    clrCnsl()
    student = students[stId - 1]
    print("Number: ", end="")
    for i in range(len(student[MARKS])):
        print("%4s"  %  str(i + 1), end="")
    print()
    print("Mark  : ", end="")
    for i in range(len(student[MARKS])):
        print("%4s" % student[MARKS][i], end="")
    print()
    markNumber = int(input("Select the mark number you want to " + option))
    if markNumber > len(student[MARKS]):
        print("No such mark number")
        input()
        return ERROR
    if delFlag == 0:
        newMark = int(input("For what mark you want to change this?      "))
        if newMark < 2 or newMark > 5:
            print("Invalid mark range");
            input()
            return ERROR
        else: 
            result = student[3][:(markNumber - 1)] + str(newMark) + student[3][markNumber:]
    else:
        result = student[MARKS][:markNumber - 1] + student[MARKS][markNumber:]
    cur.execute(""" UPDATE students SET marks = ? WHERE student_id = ? """, (result, stId))
    con.commit()
    clrCnsl()
    return OK

def addNewMark(cur, con):
    clrCnsl()
    cur.execute(""" SELECT * FROM students """)
    students = cur.fetchall()
    printDB(cur)
    stId = int(input("Select the id of the student for whom you want to add a grade:    "))
    if stId > len(students):
        print("No such student")
        input()
        return ERROR
    clrCnsl()
    newMark = int(input("Enter a new mark:    "))
    if newMark < 2 or newMark > 5:
        print("Invalid mark range")
        input()
        return ERROR

    result = students[stId - 1][3] + str(newMark);
    cur.execute(""" UPDATE students SET marks = ? WHERE student_id = ? """, (result, stId))
    con.commit()
    clrCnsl()
    return OK


def checkMarkString(string):
    length = len(string)
    for i in range(length):
        if not(2 <= int(string[i]) <= 5):
            return 1
    return 0

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
    if marks.isdigit():
        if checkMarkString(marks):
            return ERROR
    else:
        return ERROR
    cur.execute(""" INSERT INTO students (name, surname, marks) VALUES (?, ?, ?) """, (name, surname, marks))
    con.commit()
    clrCnsl()
    return OK


def deleteStudent(cur, com):
    printDB(cur)
    students = cur.execute(""" SELECT * FROM students """)
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


while True:
    clrCnsl()
    print("1. Change existing marks")
    print("2. Add mark")
    print("3. Delete mark")
    print("4. Add student")
    print("5. Delete student")
    print("6. Show list of students")
    c = int(input())
    if c == CHANGE_EXISTS:
        if changeExistingMarks(cur, con, 0) == ERROR:
            continue
    elif c == ADD_NEW_MARK:
        if addNewMark(cur, con) == ERROR:
            continue
    elif c == DELETE_MARK:
        if changeExistingMarks(cur, con, 1) == ERROR:
            continue
    elif c == ADD_NEW_STUDENT:
        addStudent(cur, con)
    elif c == DELETE_STUDENT:
        deleteStudent(cur, con)
    elif c == SHOW_DB:
        clrCnsl()
        printDB(cur)
        input()
    else:
        print("Incorrent Input")
        input()
        clrCnsl()

con.commit()
cur.close()