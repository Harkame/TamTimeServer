import json
import sqlite3

from flask import Flask, request

app = Flask(__name__)

t_connection = sqlite3.connect("./database/tamtime_database.db")
t_cursor = t_connection.cursor()
print("[Database connection OK]");

#TODO : Move this class in tram.py
class Tram(object):
    def __init__(self, p_id, p_occupation):
        self.id = p_id
        self.occupation = p_occupation

class Report(object):
    def __init__(self, p_id, p_stop, p_type, p_message, p_date, p_confirm):
        self.id = p_id
        self.stop = p_stop
        self.type = p_type
        self.message = p_message
        self.date = p_date
        self.confirm = p_confirm

#http://localhost:5000/get_trams
@app.route("/trams", methods=['GET'])
def get_trams():
    t_cursor.execute("SELECT * FROM tram")

    t_trams = list()

    for t_tram in t_cursor.fetchall():
        t_trams.append(Tram(t_tram[0], t_tram[1])) #Parsing of tuple to object

    return json.dumps([ob.__dict__ for ob in t_trams])

#http://localhost:5000/reports
@app.route("/reports", methods=['GET'])
def get_reports():
    t_cursor.execute("SELECT * FROM report")

    t_reports = list()

    for t_report in t_cursor.fetchall():
        t_reports.append(Report(t_report[0], t_report[1], t_report[2], t_report[3], t_report[4], t_report[5])) #Parsing of tuple to object

    return json.dumps([ob.__dict__ for ob in t_reports])

#http://localhost:5000/report?report_id=42&report_stop=1&report_type=1&report_message="controleur"&report_date="26/04/2018"&report_confirm=1
@app.route("/report", methods=['POST'])
def post_report():
    t_report = Report(int(request.args.get("report_id", None)), int(request.args.get("report_stop", None)), int(request.args.get("report_type", None)), request.args.get("report_message", None), request.args.get("report_date", None), int(request.args.get("report_confirm", None)))

    t_cursor.execute("INSERT INTO report (report_id, report_stop, report_type, report_message, report_date, report_confirm) VALUES (?, ?, ?, ?, ?, ?)", (t_report.id, t_report.stop,  t_report.type, t_report.message, t_report.date, t_report.confirm))
    t_connection.commit()
    return "ok";
