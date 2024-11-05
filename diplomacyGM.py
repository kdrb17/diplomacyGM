import sqlite3
con = sqlite3.connect("diplomacyGM.db")
cur = con.cursor()
for row in cur.execute("SELECT provcode, provname FROM provinces ORDER BY provcode"):
    print(row)
