import sqlite3

t_connection = sqlite3.connect('../database/tamtime_database.db')

t_cursor = t_connection.cursor()

#TODO : Some inserts
t_cursor.execute('INSERT INTO tram (tram_id, tram_occupation) VALUES (1, 56)')
t_cursor.execute('INSERT INTO tram (tram_id, tram_occupation) VALUES (2, 99)')
t_cursor.execute('INSERT INTO tram (tram_id, tram_occupation) VALUES (3, 2)')
t_cursor.execute('INSERT INTO tram (tram_id, tram_occupation) VALUES (4, 41)')

t_connection.commit()

t_connection.close();
