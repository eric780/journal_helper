import argparse
import journal_db_helper as db_helper
import journal_utils as utils
import re
import sqlite3
import sys

def _importYearToSql(sql, year: str):
	date_buffer = None
	entry_buffer = ""
	# open file read-only
	for line in open(year + ".txt", 'r', encoding="utf-8-sig"): # using utf-8-sig to prevent issues like https://stackoverflow.com/questions/17912307/u-ufeff-in-python-string
		if utils.isDateFormatted(line):
			# new date reached, dump previous values into sql
			if entry_buffer:
				db_helper.insertEntryToDb(sql, date_buffer, entry_buffer)
			# clear buffers and prepare for next entry
			date_buffer = utils.cleanEntryDate(line) 
			entry_buffer = ""
		else:
			entry_buffer += line
	# if we reach the EOF make sure to dump the buffer
	if entry_buffer:
		db_helper.insertEntryToDb(sql, date_buffer, entry_buffer)

	# commit once we finish a whole file
	sql.commit()
	print("all entries for " + year + " inserted")

def importTextToSql(years):
	print("Clearing previously imported entries...")
	db_helper.clearAllSqlEntries()
	sql = db_helper.connect()
	print("database opened")

	for year in years:
		_importYearToSql(sql, str(year))

	sql.close()

def main():
	if len(sys.argv) < 2:
		printOptions()
		return

	arg1 = sys.argv[1]

	if arg1 == "import":
		print("importing all text files into sqlite (erases previous data")
		first_year = 2013
		recent_year = 2021
		years = list(range(first_year, recent_year+1))
		importTextToSql(years)
	elif arg1 == "input":
		if len(sys.argv) < 3:
			print("For import, please pass a date in the format yyyy-mm-dd")
			return

		input_date = sys.argv[2]
		if not utils.isDateFormatted(input_date):
			print("Please pass a date in the format yyyy-mm-dd")
			return

		sql = db_helper.connect()
		entry = db_helper.getEntryFromDb(sql, input_date)
		if entry:
			print("Date already exists!:", entry[1])
		elif not utils.isDateStringReal(input_date):
			print("Date is not a valid date")
		else:
			handleNewEntry(input_date)

	# TODO support viewing too

	else:
		print("unrecognized argument.")

def handleNewEntry(date: str):
	# TODO
	print("new entry! coming soon :')")

def printOptions():
	print("Options:")
	print("import - Import all text files into sqlite (erases previous data)")

if __name__ == "__main__":
 	main()