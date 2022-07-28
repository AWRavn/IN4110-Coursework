## Prerequisites


**Installing Python**

Make sure you have Python3 installed on your machine. This program is confirmed to work on version 3.8.10.

You may check your Python version by running:
```bash
python3 --version
```

**Installing dependencies**

Install all dependencies that are required for the project by running:
```bash
pip install -r requirements.txt
```

## Testing the Code

Tests are made using pytest framework.

To run the tests call the following command in `./code/` directory:
```bash
pytest
```

## Code Structure
```
README.md
requirements.txt
code/
|- requesting_urls.py
|- filter_urls.py
|- time_planner.py
|- fetch_player_statistics.py
|- tests.py
requesting_urls/
|- (...)
filter_urls/
|- (...)
datetime_filter/
|- (...)
```

## Usage
The programs in this directory involce parsing html files. Each of them outputs results nicely to a relevant report file. Example usage from the ./code directory:
```bash
python3 requesting_urls.py
python3 filter_urls.py
python3 time_planner.py
```
## Not Implemented
- Regex for finding Dates
- Challenge - Wiki Race with URLs

Additionally documentation and parts of the code still require some cleanup.
