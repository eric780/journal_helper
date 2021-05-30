from flask import Flask, render_template, jsonify
import journal_db_helper as db_helper

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entry/list/<int:year>')
def getEntriesForYear(year: int):
    sql = db_helper.connect()

    # list of tuples
    entries = db_helper.getEntriesForYear(sql, year)

    sql.close()
    return jsonify(entries=entries)
