

from sqlcipher3 import dbapi2 as sqlite

con = sqlite.connect("sample.db")
con.execute('pragma key="testing"')
cur = con.cursor()
cur.execute("CREATE TABLE movie(title, year, score)")
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
con.commit()

for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

