import sqlite3

t_connection = sqlite3.connect("./database/tamtime_database.db")
from datetime import date, datetime
t_cursor = t_connection.cursor()

t_cursor.execute("INSERT INTO tram (occupation) VALUES (56)")
t_cursor.execute("INSERT INTO tram (occupation) VALUES (99)")
t_cursor.execute("INSERT INTO tram (occupation) VALUES (2)")
t_cursor.execute("INSERT INTO tram (occupation) VALUES (41)")

t_cursor.execute("INSERT INTO report (stop_id, type, message) VALUES (1, 1, 'Controleur')")
t_cursor.execute("INSERT INTO report (stop_id, type, message) VALUES (1, 1, 'Controleur')")
t_cursor.execute("INSERT INTO report (stop_id, type, message) VALUES (1, 1, 'Controleur')")
t_cursor.execute("INSERT INTO report (stop_id, type, message) VALUES (1, 1, 'Controleur')")

t_cursor.execute("INSERT INTO report_confirm (report_id, ip_adress) VALUES (1,'190.1.1.1')")
t_cursor.execute("INSERT INTO report_confirm (report_id, ip_adress) VALUES (1,'190.1.11.1')")
t_cursor.execute("INSERT INTO report_confirm (report_id, ip_adress) VALUES (2,'190.17.1.1')")

t_cursor.execute("INSERT INTO mark (stop_id, mark, ip_adress) VALUES (1, 3,'190.1.1.1')")
t_cursor.execute("INSERT INTO mark (stop_id, mark, ip_adress) VALUES (1, 1,'190.98.12.1')")
t_cursor.execute("INSERT INTO mark (stop_id, mark, ip_adress) VALUES (2, 4,'190.14.1.1')")

t_connection.commit()

t_connection.close();
