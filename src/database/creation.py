import sqlite3

database = sqlite3.connect("./database/tamtime_database.db")
from datetime import date, datetime
cursor = database.cursor()

cursor.execute('PRAGMA foreign_keys = 1')
cursor.execute('DROP TABLE IF EXISTS tram')
cursor.execute('DROP TABLE IF EXISTS report')
cursor.execute('DROP TABLE  IF EXISTS report_confirm')
cursor.execute("CREATE TABLE tram (id INTEGER PRIMARY KEY AUTOINCREMENT, occupation INT)")
cursor.execute("CREATE TABLE report (id INTEGER PRIMARY KEY AUTOINCREMENT, stop_id INT, type INT, message TEXT DEFAULT \"\", date DATETIME DEFAULT (datetime('now')))")
cursor.execute("CREATE TABLE report_confirm (report_id INTEGER REFERENCES report(id) ON DELETE CASCADE, ip_adress TEXT, PRIMARY KEY(report_id, ip_adress))")
database.commit()

database.close();
