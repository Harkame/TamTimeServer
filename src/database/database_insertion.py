import sqlite3

t_connection = sqlite3.connect("./database/tamtime_database.db")
from datetime import date, datetime
t_cursor = t_connection.cursor()

#TODO : Some inserts
t_cursor.execute("INSERT INTO tram (tram_id, tram_occupation) VALUES (1, 56)")
t_cursor.execute("INSERT INTO tram (tram_id, tram_occupation) VALUES (2, 99)")
t_cursor.execute("INSERT INTO tram (tram_id, tram_occupation) VALUES (3, 2)")
t_cursor.execute("INSERT INTO tram (tram_id, tram_occupation) VALUES (4, 41)")

t_cursor.execute("INSERT INTO report (report_id, report_stop, report_type, report_message, report_date, report_confirm) VALUES (1, 1, 1, 'Controleur', '26/02/20018', 1)")
t_cursor.execute("INSERT INTO report (report_id, report_stop, report_type, report_message, report_date, report_confirm) VALUES (2, 1, 1, 'Controleur', '15/03/20018', 1)")
t_cursor.execute("INSERT INTO report (report_id, report_stop, report_type, report_message, report_date, report_confirm) VALUES (3, 1, 1, 'Controleur', '12/01/20018', 1)")
t_cursor.execute("INSERT INTO report (report_id, report_stop, report_type, report_message, report_date, report_confirm) VALUES (4, 1, 1, 'Controleur', '02/02/20018', 1)")
t_connection.commit()

t_connection.close();
