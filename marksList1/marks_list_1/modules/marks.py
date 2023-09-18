"""
Module that contains functions to work with student's marks
"""

import os

ID = 0
NAME = 1
SURNAME = 2
MARKS = 3

OK = 0
ERROR = 1

def clr_cnsl():
    """ Short func to clear the screen """
    os.system("cls")

def check_empty_db(cur):
    """ Checking is database empty """
    cur.execute(""" SELECT * FROM students """)
    sts = cur.fetchall()
    if len(sts) == 0:
        return 1
    return 0


def print_db(cur):
    """ Prints data base """
    clr_cnsl()
    cur.execute(""" SELECT * FROM students """)
    sts = cur.fetchall()
    if len(sts) == 0:
        print("No students")
        return OK
    print(f"{'id':<2}| {'name':<7}| {'surname':<7}| {'marks':<7}")
    for student in sts:
        print(f"{student[ID]:2}| {student[NAME]:7}| {student[SURNAME]:7}| {student[MARKS]:7}")
        print()
    return OK

def change_existing_marks(cur, con, del_flag):
    """ Change or delete marks, depends on del_flag """
    if check_empty_db(cur):
        print("No students")
        return ERROR
    clr_cnsl()
    cur.execute(""" SELECT * FROM students """)
    sts = cur.fetchall()
    print_db(cur)
    option = "delete:     " if del_flag else "change:      "
    st_id = int(input("Select the ID of the student whose grades you want to " + option))
    if st_id > len(sts):
        print("No such student")
        input()
        return ERROR
    clr_cnsl()
    student = sts[st_id - 1]
    print("Number: ", end="")
    for i in range(len(student[MARKS])):
        print(f"{str(i + 1)} : 4", end="")
    print()
    print("Mark  : ", end="")
    for i in range (len(student[MARKS])):
        print(f"{student[MARKS][i] : 4}", end="")
    print()
    if student[3] == "":
        print("This student has no marks")
        return ERROR
    mark_number = int(input("Select the mark number you want to " + option))
    if mark_number > len(student[MARKS]):
        print("No such mark number")
        input()
        return ERROR
    if del_flag == 0:
        new_mark = int(input("For what mark you want to change this?      "))
        if new_mark < 2 or new_mark > 5:
            print("Invalid mark range")
            input()
            return ERROR
        result = student[3][:(mark_number - 1)] + str(new_mark) + student[3][mark_number:]
    else:
        result = student[MARKS][:mark_number - 1] + student[MARKS][mark_number:]
    cur.execute(""" UPDATE students SET marks = ? WHERE student_id = ? """, (result, st_id))
    con.commit()
    clr_cnsl()
    return OK

def add_new_mark(cur, con):
    """ Add new mark for a student """
    if check_empty_db(cur):
        print("No students")
        return ERROR
    clr_cnsl()
    cur.execute(""" SELECT * FROM students """)
    students = cur.fetchall()
    print_db(cur)
    st_id = int(input("Select the id of the student for whom you want to add a grade:    "))
    if st_id > len(students):
        print("No such student")
        input()
        return ERROR
    clr_cnsl()
    new_mark = int(input("Enter a new mark:    "))
    if new_mark < 2 or new_mark > 5:
        print("Invalid mark range")
        input()
        return ERROR

    result = students[st_id - 1][3] + str(new_mark)
    cur.execute(""" UPDATE students SET marks = ? WHERE student_id = ? """, (result, st_id))
    con.commit()
    clr_cnsl()
    return OK


def check_mark_string(string):
    """ Checking mark string for invalid chars """
    length = len(string)
    for i in range(length):
        if not 2 <= int(string[i]) <= 5:
            return ERROR
    return OK
