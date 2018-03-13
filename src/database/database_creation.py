import sqlite3

t_connection = sqlite3.connect("./database/tamtime_database.db")
from datetime import date, datetime
t_cursor = t_connection.cursor()

t_cursor.execute("CREATE TABLE tram (tram_id INT PRIMARY KEY NOT NULL, tram_occupation INT)")
t_cursor.execute("CREATE TABLE report (report_id INT PRIMARY KEY NOT NULL, report_stop INT, report_type INT, report_message TEXT, report_date DATE, report_confirm INT)")

t_connection.commit()

t_connection.close();
