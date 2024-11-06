import sqlite3
con = sqlite3.connect("diplomacyGM.db")
cur = con.cursor()
for row in cur.execute("SELECT sprov, eprov FROM orderscur"):
    var1 = row[0]
    print(var1)
    var2 = row[1]
    print(var2)
