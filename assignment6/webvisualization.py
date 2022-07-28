from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates

from typing import Optional
import pandas as pd
import datetime

import webvisualization_plots

# create app variable (FastAPI instance)
app = FastAPI()
templates = Jinja2Templates(directory="templates")


# mount one or more static directories,
# e.g. your auto-generated Sphinx documentation with html files
app.mount(
    # the URL where these files will be available
    "/static",
    StaticFiles(
        # the directory the files are in
        directory="static/",
        html=True,
    ),
    # an internal name for FastAPI
    name="static",
)


@app.get("/")
def plot_reported_cases_per_million_html(request: Request):
    """
    Root route for the web application.
    Handle requests that go to the path "/".
    """

    return templates.TemplateResponse(
        "plot_reported_cases_per_million.html",
        {
            "request": request,
            "countries": get_countries(),
            "start_date": str(datetime.date(2020, 1, 1)),
            "end_date": str(datetime.date.today()),
            "interval": "Daily",
        },
    )


@app.get("/plot_reported_cases_per_million.json")
def plot_reported_cases_per_million_json(countries: Optional[str] = None,
    start: Optional[str] = None, end: Optional[str] = None, interval: Optional[str] = None):
    """Return json chart from altair"""

    if countries:
        countries = countries.split(",")
    chart = webvisualization_plots.plot_reported_cases_per_million(countries=countries, start=start, end=end, interval=interval)
    return chart.to_dict()


def get_countries():
    """Return unique country names"""

    path = "data/owid-covid-data.csv"
    df = pd.read_csv(path, usecols=["location"])
    return df.location.drop_duplicates()



def main():
    """Called when run as a script. Launches the web app. """
    import uvicorn
    import pydoc, os

    # Export documentation to help file
    pydoc.writedoc("webvisualization.py")

    uvicorn.run(app)



if __name__ == "__main__":
    main()