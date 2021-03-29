from datetime import datetime
import re
import unittest

def getFilenameFromYear(year):
	return year + ".txt"

# takes a line of text and checks if its a date. only accept yyyy-mm-dd and then some newlines
def isDateFormatted(line):
  pattern = re.compile("20[0-9][0-9]-[0-9][0-9]-[0-9][0-9][\r]*[\n]*$")
  return pattern.search(line) != None

def isDateStringReal(date: str):
	(year, month, day) = splitDateValues(date)
	return isDateReal(year, month, day)

def isDateReal(year: int, month: int, day: int): 
	try:
		datetime(year, month, day)
		return True
	except ValueError:
		return False

# takes a line of text and returns a triplet of year, month, day
def splitDateValues(line):
	if not isDateFormatted(line):
		return None

	split = line.split('-')
	return int(split[0]), int(split[1]), int(split[2])

# cleans a date for insertion, eg. removing new lines
def cleanEntryDate(entry_date):
	# some preconditions
	if not isDateFormatted(entry_date):
		raise ValueError("Not properly formatted date", entry_date)

	(year, month, day) = splitDateValues(entry_date)
	if not isDateReal(year, month, day):
		raise ValueError("Not an actual date", entry_date)

	replaces = { "\n": "" }
	return replaceText(replaces, entry_date)

# prepares entry text for db insertion, eg. replacing double quote literals
def cleanEntryText(entry_text):
	replaces = {
		"\"": "''", # replace double quote with two single quotes
		"\r\n": "\n" # replace windows-style carriage returns
	}
	return replaceText(replaces, entry_text)

# takes a dict of replacements, returns text with those replacements run
def replaceText(replaces, text):
	# https://stackoverflow.com/questions/6116978/how-to-replace-multiple-substrings-of-a-string
	replaces = dict((re.escape(k), v) for k,v in replaces.items())
	pattern = re.compile("|".join(replaces.keys()))
	return pattern.sub(lambda m: replaces[re.escape(m.group(0))], text)

class JournalUtilsTests(unittest.TestCase):
	def test_cleanEntryText(self):
		self.assertEqual(cleanEntryText("\r"), "\r")
		self.assertEqual(cleanEntryText("\r\n"), "\n")
		self.assertEqual(cleanEntryText("what a nice test suite "), "what a nice test suite ")
		self.assertEqual(cleanEntryText("and then he said \"what???\""), "and then he said ''what???''")

	def test_isDateLine(self):
		self.assertTrue(isDateFormatted("2020-11-30"))
		self.assertTrue(isDateFormatted("2020-56-38"))
		self.assertTrue(isDateFormatted("2020-11-30\r"))
		self.assertTrue(isDateFormatted("2020-11-30\n"))

		self.assertFalse(isDateFormatted("2020-11-30\rfff"))
		self.assertFalse(isDateFormatted("2020-11-30f")) # fail if extra text after
		self.assertFalse(isDateFormatted("1990-30-30")) # only recognize year 2000 or later
		self.assertFalse(isDateFormatted("2020-FF-JJ"))
		self.assertFalse(isDateFormatted("20201130"))
		self.assertFalse(isDateFormatted("11-30-2020"))

	def test_isRealDate(self):
		self.assertTrue(isDateReal(2020, 2, 29))
		self.assertTrue(isDateReal(1998, 12, 30))
		self.assertTrue(isDateReal(2250, 6, 12))
		self.assertFalse(isDateReal(2020, 2, 30))
		self.assertFalse(isDateReal(2020, 6, 52))

if __name__ == "__main__":
	unittest.main()