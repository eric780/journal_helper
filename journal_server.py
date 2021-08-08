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

@app.route('/entry/random')
def getRandomEntry():
    sql = db_helper.connect()

    random_entry = db_helper.getRandomEntryFromDb(sql)

    sql.close()
    return jsonify(entry=random_entry)

@app.route('/entry/search/<query>')
def getSearchResults(query: str):
    sql = db_helper.connect()
    results = db_helper.getEntriesForQuery(sql, query)
    return jsonify(entries=results)