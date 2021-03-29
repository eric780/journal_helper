import datetime
import re
import sys
from io import open
from journal_utils import *

# prints out any lines that are formatted incorrectly
def getDateFormatted(year, file):
  date = datetime.date.today().replace(year=year).strftime('%Y-%m-%d')
  printing = False
  for line in file:
    if date in line:
      printing = True
      print(line.rstrip('\n'))
      continue
    elif isDateFormatted(line):
      printing = False
      continue
    elif printing:
      print(line.rstrip('\n'))

def getFixedLineEndingsFilename(year):
  return str(year) + "_fixed_line_endings.txt"

# writes to a new file with line endings converted to unix-style \n rather than windows style \r\n
def fixLineEndings(year, filename):
  output_name = getFixedLineEndingsFilename(year)
  with open(filename, 'r') as infile, open(output_name, 'w+', newline="\n") as outfile:
    outfile.writelines(infile)

def main():
  # Print out incorrect dates
  print("Incorrectly formatted dates: ")
  year = int(sys.argv[1])
  filename = str(year) + '.txt'
  with open(filename, 'r') as file:
    getDateFormatted(year, file) 

  print("Fixing line endings, output will be found in " + getFixedLineEndingsFilename(year))
  fixLineEndings(year, filename)


if __name__ == "__main__":
  main()
