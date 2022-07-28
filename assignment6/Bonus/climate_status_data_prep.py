import requests
from bs4 import BeautifulSoup
import os
import pandas as pd


def get_csv(url, output_filename=None):
	"""
	Downloads specified csv content to ./data/ directory.

	Args:
		url (string): 				The url containing the csv file
		output_filename (string): 	Name of the output file
	Return:
		None
	"""

	# Create directory if needed
	os.makedirs('./data/', exist_ok=True)

	r = requests.get(url, allow_redirects=True)
	with open(f"data/{output_filename}.csv", "wb") as f:
		f.write(r.content)


def get_html(url, output_filename=None):
	"""
	Writes specified html content to a new file or overwrites the existing file.

	Args:
		url (string): 				The url containing the the html page
		output_filename (string): 	Optional. Name of the output file
	Return:
		html (string):				The html content.
	"""

	# Create directory if needed
	os.makedirs('./data/', exist_ok=True)

	r = requests.get(url)

	if output_filename != None:
		with open(f"data/{output_filename}.txt", 'wb') as f:
			f.write(b"url: {r.url}\n")
			f.write(r.content)

	return r.text


def get_temperature_means():
	"""
	Returns dictionary of monthly mean surface temperatures.
	Data manually gotten from: https://www.ncdc.noaa.gov/monitoring-references/faq/anomalies.php#mean

	Return:
		means (dict(float)):		Dictionary containing monthly means	
	"""

	means = {
		1: 12.0,
		2: 12.1, 
		3: 12.7, 
		4: 13.7, 
		5: 14.8, 
		6: 15.5, 
		7: 15.8, 
		8: 15.6, 
		9: 15.0, 
		10: 14.0, 
		11: 12.9, 
		12: 12.2
	}

	return means


def read_csv():
	"""
	Process the data and output the result as pandas dataframe.

	Returns:
		df(pd.dataFrame):		Formatted Pandas dataframe containing climate data
	"""

	df = pd.read_csv(
		"./data/anomaly_data.csv",
		sep=",",
		header=4,
		engine="python",
		parse_dates=["Year"],
		date_parser=lambda col: pd.to_datetime(col, format="%Y%m"),
		)
	
	df=df.rename(columns = {'Year':'Date', 'Value': 'Anomaly Value'})
	df["Mean Value"] = pd.DatetimeIndex(df["Date"]).month.map(get_temperature_means())
	df["Mean Temperature"] = df["Anomaly Value"] + df["Mean Value"]

	return df


def main():
    """
    Function called when run as a script. Displays formatted dataframe.
    """

	print(read_csv())


if __name__ == "__main__":
	main()