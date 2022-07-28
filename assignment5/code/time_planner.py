from bs4 import BeautifulSoup
from requesting_urls import *
import re
import os


def extract_events(url):
	"""
	Extracts date, venue and discipline for competitions.

    Args:
        url (string):           Website url to extract events from.

    Returns:
        events (list[tuple]):	List of tuples where each row represents an event, and each 
        						tuple contains [date, venue, discipline].

	"""

	# Get the html
	html = get_html(url)

	# Make soup
	soup = BeautifulSoup(html, 'html.parser')

	# Get table and extract rows
	header = soup.find(id='Calendar')
	table = header.find_all_next('table')[0]
	table_rows = table.find_all('tr')

	# Initialize variables
	events = []
	found_event = None
	found_venue = None
	found_discipline = None
	full_row_length = 9
	short_row_length = full_row_length - 2
	disciplines = {
		'DH':	'Downhill',
		'SL':	'Slalom',
		'GS':	'Giant Slalom',
		'SG':	'Super Giant Slalom',
		'AC':	'Alpine Combined',
		'PG':	'Parallel Giant Slalom',
	}

	for row in table_rows:

		# Get all cells
		cells = row.find_all('td')

		# Ignore too short rows
		if len(cells) not in {full_row_length, short_row_length}:
			continue

		# Get event
		event = cells[1].text.strip()
		if int(event) in range(1, 100):
			found_event = event
		else:
			found_event = None

		# Get date, venue and discipline id
		if len(cells)==full_row_length:
			found_date = cells[2].text.strip()
			venue = cells[3]
			found_venue = venue.text.strip()
			discipline = cells[4]
		else:
			found_date = cells[1].text.strip()
			venue = cells[2]
			found_venue = venue.text.strip()
			discipline = cells[3]

		# Get discipline
		discipline_pattern = re.compile(r'DH|SL|GS|SG|AC|PG')
		discipline_key = re.search(discipline_pattern, discipline.text.strip()).group(0)
		if discipline_key in disciplines:
			found_discipline = disciplines.get(discipline_key)
		else:
			found_discipline = None

		# If all parts are found add to events
		if found_event and found_venue and found_discipline:
			events.append((found_date, found_venue, found_discipline))

	return events


def create_betting_slip(events, output):
	"""
	Saves a markdown format betting slip to the location '../datetime_filter/<output>.md'.

	Args:
		events (list[tuple]):	List of tuples where each row represents an event, and each 
        						tuple contains [date, venue, discipline].
        output (string):        Name of the output file. 

	"""

	# Create directory if needed
	os.makedirs('../datetime_filter', exist_ok=True)

	with open(f'../datetime_filter/{output}.md', 'w') as out_file:
		out_file.write(f'# BETTING SLIP ({output})\n\nName:\n\n')
		out_file.write('Date | Venue | Discipline | Who wins?\n')
		out_file.write(' --- | --- | --- | --- \n')
		for e in events:
			date, venue, discipline = e
			out_file.write(f'{date} | {venue} | {discipline} | \n')


def main():
	"""
	Create output files for test webpages.
	"""

	url='https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup'

	events = extract_events(url)
	
	create_betting_slip(events, 'betting_slip_empty')


if __name__ == '__main__':
	main()
