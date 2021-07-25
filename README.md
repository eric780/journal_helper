# journal_helper
Scripts for writing journal entries locally

Run journal_helper.py for instructions

## PRIMARY USER JOURNEYS
- View random entry
  - Browse nearby entries
- Browse specific entries
  - Filter by keywords
Housekeeping
  - View missing/short entries
  - Check for duplicate entries
- Analysis/Fun
  - Generate word clouds
  - Training bag of words

## NOT GOOD FOR
- Adding new entries (just write directly to text files)

## TODOs
- Clean up frontend UI
- Browse nearby entries when showing an entry
- Add functionality to sanity check entries (eg. scan for duplicates, already in journal_helper)


## Getting Started
Make sure you have pip3 for python 3 installed. 
To activate virtual environment, run `. venv/bin/activate`
Run `pip install -r requirements.txt` to install requirements.
To start the server with autoreload enabled:
`FLASK_APP=journal_server.py FLASK_ENV=development python3 -m flask run`

## Import
Imports txt entries into a sqlite db. Txt files should be formatting like the following:

2015-12-28

today i did something cool!

2015-12-29

yesterday was better than today.
