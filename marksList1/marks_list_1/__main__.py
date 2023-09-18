"""
This is a my clear code
"""


import sqlite3

from .modules import students as st
from .modules import marks as mk

OK = 0
ERROR = 1

con = sqlite3.connect("database.db")

cur = con.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER NOT NULL PRIMARY KEY,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        marks TEXT NOT NULL
)""")



while True:
    mk.clr_cnsl()
    print("1. Change existing marks")
    print("2. Add mark")
    print("3. Delete mark")
    print("4. Add student")
    print("5. Delete student")
    print("6. Show list of students")
    print("7. Exit")
    c = int(input())
    sts = cur.execute(""" SELECT * FROM students """)
    if c == st.CHANGE_EXISTS:
        if mk.change_existing_marks(cur, con, 0) == ERROR:
            continue
    elif c == st.ADD_NEW_MARK:
        if mk.add_new_mark(cur, con) == ERROR:
            continue
    elif c == st.DELETE_MARK:
        if mk.change_existing_marks(cur, con, 1) == ERROR:
            continue
    elif c == st.ADD_NEW_STUDENT:
        st.add_student(cur, con)
    elif c == st.DELETE_STUDENT:
        st.delete_student(cur, con)
    elif c == st.SHOW_DB:
        mk.clr_cnsl()
        mk.print_db(cur)
        input()
    elif c == st.EXIT_CYCLE:
        mk.clr_cnsl()
        break
    else:
        print("Incorrent Input")
        input()
        mk.clr_cnsl()

con.commit()
cur.close()
