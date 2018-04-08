import json
import sqlite3
import datetime
from flask import Flask, request

app = Flask(__name__)

database = sqlite3.connect("./database/tamtime_database.db")
cursor = database.cursor()
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

class Stop(object):
    def __init__(self, p_id, p_property):
        self.id = p_id
        self.property = p_stop

class Mark(object):
    def __init__(self, p_stop_id, p_mark, p_ip_adress):
        self.stop_id = p_stop_id
        self.mark = p_mark
        self.ip_adress = p_ip_adress

#http://localhost:5000/get_trams
@app.route("/trams", methods=['GET'])
def get_trams():
    cursor.execute("SELECT * FROM tram")

    trams = list()

    for tram in cursor.fetchall():
        trams.append(Tram(tram[0], tram[1])) #Parsing of tuple to object

    return json.dumps([ob.__dict__ for ob in trams])

#http://localhost:5000/reports
@app.route("/reports", methods=['GET'])
def get_reports():
    cursor.execute("SELECT *, (SELECT COUNT(*) FROM report_confirm WHERE report_confirm.report_id = report.id) AS confirm FROM report")

    t_reports = list()

    for t_report in cursor.fetchall():
        t_reports.append(Report(t_report[0], t_report[1], t_report[2], t_report[3], t_report[4], t_report[5])) #Parsing of tuple to object

    return json.dumps([ob.__dict__ for ob in t_reports])

#http://localhost:5000/report?stop=1&type=1&message="controleur"
@app.route("/report", methods=['POST'])
def post_report():
    if request.args.get("stop", None) is None or request.args.get("type", None) is None:
        return "", 400

    stop_id = int(request.args.get("stop", None))
    report_type = int(request.args.get("type", None))
    message = request.args.get("message", "")

    cursor.execute("INSERT INTO report (stop_id, type, message) VALUES (?, ?, ?)",
        (stop_id, report_type, message))
    database.commit()
    return "", 200

#http://localhost:5000/confirm?id=2O
@app.route("/confirm", methods=['POST'])
def confirm_report():
    if request.args.get("id", None) is None:
        return "", 400

    report_id = int(request.args.get("id", None))
    ip_adress = request.remote_addr

    try:
        cursor.execute("INSERT INTO report_confirm (report_id, ip_adress) VALUES (?, ?)",
            (report_id, ip_adress))
    except sqlite3.IntegrityError:
        return "", 403

    database.commit()
    return "",200

@app.route("/marks", methods=['GET'])
def get_marks():
    cursor.execute("SELECT * FROM mark")

    marks = list()

    for mark in cursor.fetchall():
        marks.append(Mark(mark[0], mark[1]), mark[2]) #Parsing of tuple to object

    return json.dumps([ob.__dict__ for ob in marks])

@app.route("/mark", methods=['POST'])
def post_mark():
    if request.args.get("stop_id", None) is None or request.args.get("mark", None) is None or request.args.get("ip_adress", None) is None:
        return "", 400

    stop_id = int(request.args.get("stop_id", None))
    mark = int(request.args.get("mark", None))
    ip_adress = request.args.get("ip_adress", "")

    cursor.execute("INSERT INTO mark (stop_id, mark, ip_adress) VALUES (?, ?, ?)",
        (stop_id, mark, ip_adress))
    database.commit()
    return "", 200

@app.teardown_request
def clean_old_reports(response):
    cursor.execute("DELETE FROM report WHERE report.date < date('now','-6 hours')")
    database.commit()
