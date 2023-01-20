import sqlite3

connexion = sqlite3.connect("../bdd.db")
cursor = connexion.cursor()

cursor.execute("SELECT * FROM rfids")
for result in cursor:
    print(result)

connexion.close()
