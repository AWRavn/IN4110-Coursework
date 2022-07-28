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

## Usage
. Example usage from the root directory:
```bash
python3 webvisualization_plots.py
python3 webvisualization.py
```

The dataset needs to be manually downloaded into the `.\data\` directory in the root. The file was too large to upload.

## Not Implemented
- Pandas preprocessing likely required to clean up leading entries in rolling mean graph.
- Cumulatve means currently sums up all checked values. Correct values are shown if selecting only one country.
	This again should likely be adjusted by Pandas preprocessing.
- Documentation Help page is not fully implemented, due to isses with the package.
- Bonus task currently plots temperature values for each month in each year in scatterplot. Preprocessing to plot mean 
	yearly temperature is needed.

Additionally documentation and parts of the code still require some cleanup.
