import sqlite3
conn = sqlite3.connect("./faili/my.db")

def kverijs(vaicajums):
    cur = conn.cursor()
    cur.execute(vaicajums)
    conn.commit()

tabulas_dzesana = "DROP TABLE skoleni"

tabulas_izveide = """
CREATE TABLE IF NOT EXISTS skoleni(
    id_skolenam INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT
    uzvards TEXT
    vecums INTEGER
)

"""
datu_pievienosana = """
INSERT INTO SKOLENI ()
"""

kverijs(tabulas_izveide)

