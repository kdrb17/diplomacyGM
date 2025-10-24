def check_adj():
    cur2.execute("SELECT adjcode FROM adjM WHERE adjcode = ?", (var4)")
    
    

import sqlite3
con = sqlite3.connect("diplomacyGM.db")
cur1 = con.cursor()

cur1.execute("SELECT sprov, eprov FROM orderscur")
records = cur1.fetchall()
print("Total rows are:  ", len(records))
print("Printing each row")
for row in records:
    var1 = row[0]
    print(var1)
    var2 = row[1]
    print(var2)
    var3 = (var1 + var2)
    print(var3)
    var4 = (var3, )
    check_adj()

cur1.close()