def checkadj():
    for row2 in cur.execute("SELECT adjcode FROM adj WHERE adjcode = ?", (var4)):
        var5 = row2[0]
        print("checkadj-OrderIsValid", var5)

import sqlite3
con = sqlite3.connect("diplomacyGM.db")
cur = con.cursor()

cur.execute("SELECT sprov, eprov FROM orderscur")
records = cur.fetchall()
print("Total rows are:  ", len(records))
print("Printing each row")
for row in records:
    var1 = row[0]
    print(var1)
    var2 = row[1]
    print(var2)
    var3 = (var1 + var2)
    print(var3)
    var4 = (var3,)
    print(var4)
    checkadj()

cur.close()