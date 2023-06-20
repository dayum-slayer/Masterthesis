import mysql.connector

db = mysql.connector.connect(
host = "localhost",
user = "root",
passwd= "13l00d0R4ng3!",
database = "demo"
)

# Cursor erstellen
cursor = db.cursor()

# Beispielabfrage ausführen
cursor.execute("SELECT * FROM gdr0001_2021")

# Ergebnisse abrufen
results = cursor.fetchone()

#speichern der Daten in Variablen
'''V_n = results[1]
p_ein = results[2]
p_aus = results[3]
t_ein = results[4]
t_aus = results[5]'''
V_n, p_ein, p_aus, t_ein, t_aus = results[1], results[2], results[3], results[4], results[5]
print(str(V_n), str(p_ein), str(t_aus))


# Verbindung schließen
db.close()