from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates

from typing import Optional
import pandas as pd
import datetime

import climate_status_plots

# create app variable (FastAPI instance)
app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def plot_climate_data_html(request: Request):
    """
    Root route for the web application.
    Handle requests that go to the path "/".
    """

    return templates.TemplateResponse(
        "plot_climate_data.html",
        {
            "request": request,
        },
    )


@app.get("/plot_climate_data.json")
def plot_climate_data_json():
    """Return json chart from altair"""

    chart = climate_status_plots.plot_mean_temperature()
    return chart.to_dict()


def main():
    """Called when run as a script. Launches the web app. """
    import uvicorn

    uvicorn.run(app)


if __name__ == "__main__":
    main()