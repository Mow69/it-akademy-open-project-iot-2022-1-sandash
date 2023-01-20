import sqlite3

connexion = sqlite3.connect("bdd.db")
cursor = connexion.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS rfids(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    distant_id INTEGER,
    rfid INTEGER,
    present INTEGER,
    validate INTEGER
)''')

connexion.commit()
connexion.close()

