import json
import sqlite3
import datetime
from flask import Flask, request

from models.tram import Tram
from models.stop import Stop
from models.report import Report
from models.mark import Mark
from models.mark_average import MarkAverage

app = Flask(__name__)

database = sqlite3.connect("./database/tamtime_database.db")
cursor = database.cursor()
print("[Database connection OK]");

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

#http://localhost:5000/marks_average
@app.route("/marks_average", methods=['GET'])
def get_marks_average():
    cursor.execute("SELECT stop_id, AVG(mark) AS average_mark FROM mark GROUP BY stop_id")

    marks = list()

    for mark in cursor.fetchall():
        marks.append(MarkAverage(mark[0], mark[1])) #Parsing of tuple to object

    return json.dumps([ob.__dict__ for ob in marks])

#http://localhost:5000/mark?stop_id=9&mark=1987&android_id="gekrgkr"
#http://localhost:5000/mark?stop_id=4&mark=1&android_id="gekrgkr"
@app.route("/mark", methods=['POST'])
def post_mark():
    if request.args.get("stop_id", None) is None or request.args.get("mark", None) is None or request.args.get("android_id", None) is None:
        return "Wrong parameters", 400

    mark = int(request.args.get("mark", None))

    if mark < 0 or mark > Mark.MARK_LIMIT:
        return "Not valid mark", 400

    stop_id = int(request.args.get("stop_id", None))

    ip_adress = request.args.get("android_id", "")

    cursor.execute("INSERT OR REPLACE INTO mark (stop_id, mark, android_id) VALUES (?, ?, ?)",
        (stop_id, mark, ip_adress))

    database.commit()

    return "Mark added", 200

@app.teardown_request
def clean_old_reports(response):
    cursor.execute("DELETE FROM report WHERE report.date < date('now','-6 hours')")
    database.commit()
