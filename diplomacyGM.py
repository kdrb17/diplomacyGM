import sqlite3
con = sqlite3.connect("diplomacyGM.db")
cur = con.cursor()
for row in cur.execute("SELECT sprov, eprov FROM orderscur"):
    var1 = row[0]
    print(var1)
    var2 = row[1]
    print(var2)
var3 = (var1 + var2)
print(var3)
var4 = (var3,)
for row in cur.execute("SELECT adjcode FROM adj WHERE adjcode = ?", (var4)):
    var5 = row[0]
    print(var5)