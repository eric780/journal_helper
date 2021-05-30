# journal_helper
Scripts for writing journal entries locally

Run journal_helper.py for instructions

## TODOs
- Support browsing entries by year and month and date
- Display entries on front end
- Add backend functionality to convert from SQl to txt (and tests)
- Front end functionality:
  - Browse entries by filters (eg. year, month, date)
  - Insert new entry (autodetect next missing date and whether you're all caught up)
  - Get random entry by filters (eg. year, month, date)


## Getting Started
Make sure you have pip3 for python 3 installed. 
To activate virtual environment, run `. venv/bin/activate`
Run `pip install -r requirements.txt` to install requirements.
`export FLASK_APP=journal_server.py` then `python3 -m flask run` to start the server

## Import
Imports txt entries into a sqlite db. Txt files should be formatting like the following:

2015-12-28

today i did something cool!

2015-12-29

yesterday was better than today.
