import json
import sqlite3

from flask import Flask

app = Flask(__name__)

t_connection = sqlite3.connect('../database/tamtime_database.db')
t_cursor = t_connection.cursor()
print("[Database connection OK]");

#TODO : Move this class in tram.py
class Tram(object):
    def __init__(self, p_id, p_occupation):
        self.tram_id = p_id
        self.tram_occupation = p_occupation

@app.route('/trams')
def trams():
    t_cursor.execute('SELECT * FROM tram')

    t_trams = list()

    for t_tram in t_cursor.fetchall():
        t_trams.append(Tram(t_tram[0], t_tram[1])) #Parsing of tuple to object

    return json.dumps([ob.__dict__ for ob in t_trams])
