

import sqlite3

import students as st
import marks as mk

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
    st.clrCnsl()
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
        if mk.changeExistingMarks(cur, con, 0) == ERROR:
            continue
    elif c == st.ADD_NEW_MARK:
        if mk.addNewMark(cur, con) == ERROR:
            continue
    elif c == st.DELETE_MARK:
        if mk.changeExistingMarks(cur, con, 1) == ERROR:
            continue
    elif c == st.ADD_NEW_STUDENT:
        st.addStudent(cur, con)
    elif c == st.DELETE_STUDENT:
        st.deleteStudent(cur, con)
    elif c == st.SHOW_DB:
        st.clrCnsl()
        mk.printDB(cur)
        input()
    elif c == st.EXIT_CYCLE:
        st.clrCnsl()
        break
    else:
        print("Incorrent Input")
        input()
        st.clrCnsl()

con.commit()
cur.close()