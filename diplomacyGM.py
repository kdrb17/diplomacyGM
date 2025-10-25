def check_adj():
    cur1.execute("SELECT adjcode FROM adjM WHERE adjcode = ?", (var4))
    records2 = cur1.fetchall()
    if len(records2) > 1:
        print("ERROR - more than 1 record")
    if len(records2) == 0:
        print("checkadj-OrderIsNOTValid", var4)
    if len(records2) == 1:
            print("checkadj-OrderIsValid", var4)

import sqlite3
con = sqlite3.connect("diplomacyGM.db")
cur = con.cursor()
cur1 = con.cursor()

cur.execute("SELECT sprov, eprov FROM orderscur")
records = cur.fetchall()
print("Total current orders are:  ", len(records))
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
    check_adj()

cur.close()