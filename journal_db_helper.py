from journal_utils import cleanEntryText
import sqlite3

JOURNAL_DB_FILENAME = "journal.db"
JOURNAL_TABLE_NAME = "journal"

SQL_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS {table_name} (
	date text PRIMARY KEY,
	entry text NOT NULL
);
""".format(table_name=JOURNAL_TABLE_NAME)

DEBUG = False

# creates and returns a sql connection. you must call close() on this when finished
def connect():
    sql = sqlite3.connect(JOURNAL_DB_FILENAME)
    # try to create table if doesn't exist
    sql.execute(SQL_CREATE_TABLE)
    sql.commit()
    return sql

# returns a query to get an entry
def sql_get_entry(date: str):
	return """
		SELECT * FROM {table_name} WHERE date=\"{date}\"
	""".format(table_name=JOURNAL_TABLE_NAME, date=date)

# returns a query to insert an entry
def sql_insert_entry(date, entry_text):
	return """
		INSERT INTO {table_name} (date, entry) VALUES(\"{date}\", \"{entry_text}\");
	""".format(table_name=JOURNAL_TABLE_NAME, date=date, entry_text=cleanEntryText(entry_text))

# inserts an entry into db
def insertEntryToDb(sql, date: str, entry: str):
    insert_query = sql_insert_entry(date, entry)
    if DEBUG:
        print('executing query:')
        print(repr(insert_query))
        print()
    sql.execute(insert_query)

# tries to get a date entry from db. returns either the entry as a tuple or None
def getEntryFromDb(sql, date: str):
    get_sql = sql_get_entry(date)
    cursor = sql.cursor()
    cursor.execute(get_sql)
    entries = cursor.fetchall()
    if len(entries) > 1:
        raise Exception("Broken invariant - got more than one entry for a date")

    if len(entries) == 0:
        return None
    else:
        return entries[0]

def clearAllSqlEntries():
	try:
		sql = sqlite3.connect(JOURNAL_DB_FILENAME)
		sql.execute("DELETE FROM {table_name}".format(table_name=JOURNAL_TABLE_NAME))
		sql.commit()
		print("all entries deleted from {table_name}".format(table_name=JOURNAL_TABLE_NAME))
		sql.close()
	except sqlite3.OperationalError:
		print("Error deleting table {table_name}".format(table_name=JOURNAL_TABLE_NAME))
		return
