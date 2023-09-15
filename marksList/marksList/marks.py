import students as st
import sqlite3

ID = 0
NAME = 1
SURNAME = 2
MARKS = 3

OK = 0
ERROR = 1

def checkEmptyDB(cur):
    cur.execute(""" SELECT * FROM students """)
    sts = cur.fetchall()
    if len(sts) == 0:
        return 1
    return 0


def printDB(cur):
    st.clrCnsl()
    cur.execute(""" SELECT * FROM students """)
    sts = cur.fetchall()
    if len(sts) == 0:
        print("No students")
        return OK
    print("%-s| %-7s| %-7s| %-7s" % ("id", "name", "surname", "marks"))
    for student in sts:
        print("%-2d| %-7s| %-7s| %-7s" % (student[ID], student[NAME], student[SURNAME], student[MARKS]))
        print()

def changeExistingMarks(cur, con, delFlag):
    if checkEmptyDB(cur):
        print("No students")
        return ERROR
    st.clrCnsl()
    cur.execute(""" SELECT * FROM students """)
    sts = cur.fetchall()
    printDB(cur)
    option = "delete:     " if delFlag else "change:      "
    stId = int(input("Select the ID of the student whose grades you want to " + option))
    if stId > len(sts):
        print("No such student")
        input()
        return ERROR
    st.clrCnsl()
    student = sts[stId - 1]
    print("Number: ", end="")
    for i in range(len(student[MARKS])):
        print("%4s"  %  str(i + 1), end="")
    print()
    print("Mark  : ", end="")
    for i in range(len(student[MARKS])):
        print("%4s" % student[MARKS][i], end="")
    print()
    if student[3] == "":
        print("This student has no marks")
        return ERROR
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
            return st.ERROR
        else: 
            result = student[3][:(markNumber - 1)] + str(newMark) + student[3][markNumber:]
    else:
        result = student[MARKS][:markNumber - 1] + student[MARKS][markNumber:]
    cur.execute(""" UPDATE students SET marks = ? WHERE student_id = ? """, (result, stId))
    con.commit()
    st.clrCnsl()
    return OK

def addNewMark(cur, con):
    if checkEmptyDB(cur):
        print("No students")
        return ERROR
    st.clrCnsl()
    cur.execute(""" SELECT * FROM students """)
    students = cur.fetchall()
    printDB(cur)
    stId = int(input("Select the id of the student for whom you want to add a grade:    "))
    if stId > len(students):
        print("No such student")
        input()
        return ERROR
    st.clrCnsl()
    newMark = int(input("Enter a new mark:    "))
    if newMark < 2 or newMark > 5:
        print("Invalid mark range")
        input()
        return ERROR

    result = students[stId - 1][3] + str(newMark);
    cur.execute(""" UPDATE students SET marks = ? WHERE student_id = ? """, (result, stId))
    con.commit()
    st.clrCnsl()
    return OK


def checkMarkString(string):
    length = len(string)
    for i in range(length):
        if not(2 <= int(string[i]) <= 5):
            return ERROR
    return OK