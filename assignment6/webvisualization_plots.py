#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

import altair as alt
import pandas as pd


def get_data_from_csv(columns=None, countries=None, start=None, end=None):
    """Creates pandas dataframe from .csv file.

    Data will be filtered based on data column name, list of countries to be plotted and
    time frame chosen.

    Args:
        columns (list(string)): a list of data columns you want to include
        countries ((list(string), optional): List of countries you want to include.
            If none is passed, dataframe should be filtered for the 6 countries with the highest
            number of cases per million at the last current date available in the timeframe chosen.
        start (string, optional): The first date to include in the returned dataframe.
            If specified, records earlier than this will be excluded.
            Default: include earliest date
            Example format: "2021-10-10"
        end (string, optional): The latest date to include in the returned data frame.
            If specified, records later than this will be excluded.
            Example format: "2021-10-10"
            
    Returns:
        cases_df (dataframe): returns dataframe for the timeframe, columns, and countries chosen
    """

    # specify path, columns and read the csv file
    path = "data/owid-covid-data.csv"
    if columns == None:
        columns=[]
    df = pd.read_csv(
        path,
        sep=",",
        usecols=["location"] + ["date"] + ["new_cases_per_million"] + columns,
        parse_dates=["date"],
        date_parser=lambda col: pd.to_datetime(col, format="%Y-%m-%d"),
    )

    # if no countries specified pick 6 with the highest case count at end_date
    if countries is None:

        # set end date, if none specified pick latest date available
        if end is None:
            end_date = df.date.iloc[-1]
        else:
            end_date = datetime.strptime(end, "%Y-%m-%d")

        # find highest case counts on the last included day
        df_latest_dates = df[df.date.isin([end_date])]
        countries = df_latest_dates.nlargest(6, columns=["new_cases_per_million"])["location"].values

    # now filter to include only the selected countries
    cases_df = df[df.location.isin(countries)]

    # apply date filters
    if start is not None:
        start_date = datetime.strptime(start, "%Y-%m-%d")
        cases_df = cases_df.loc[cases_df["date"] >= start_date]

    if end is not None:
        end_date = datetime.strptime(end, "%Y-%m-%d")
        if start_date is not None and start_date >= end_date:
            raise ValueError("The start date must be earlier than the end date.")
        cases_df = cases_df.loc[cases_df["date"] <= end_date]

    return cases_df


def plot_reported_cases_per_million(countries=None, start=None, end=None, interval=None):
    """Plots data of reported covid-19 cases per million using altair.
    Calls the function get_data_from_csv to receive a dataframe used for plotting.

    Args:
        countries ((list(string), optional): List of countries you want to filter.
            If none is passed, dataframe will be filtered for the 6 countries with the highest
            number of cases per million at the last current date available in the timeframe chosen.
        start (string, optional): a string of the start date of the table, none
            of the dates will be older then this on
        end (string, optional): a string of the en date of the table, none of
            the dates will be newer then this one
        interval (string, optional): a string of the chosen plot interval. Implemented options:
            'daily', 'rollingmean' and 'cumulative'

    Returns:
        altair Chart of number of reported covid-19 cases over time.
    """

    # create dataframe
    cases_df = get_data_from_csv(countries=countries, start=start, end=end)

    # Note: when you want to plot all countries simultaneously while enabling checkboxes, you might need to disable altairs max row limit by commenting in the following line
    alt.data_transformers.disable_max_rows()


    if interval==None or interval=='daily':
        chart = (
            alt.Chart(cases_df, title="Daily New Confirmed COVID-19 Cases per Million People")
            .mark_line()
            .encode(
                x=alt.X(
                    "date:T",
                    axis=alt.Axis(
                        format="%b, %Y", title="Date", titleFontSize=14, tickCount=20
                    ),
                ),
                y=alt.Y(
                    "new_cases_per_million",
                    axis=alt.Axis(
                        title="Number of Reported Cases per Million",
                        titleFontSize=14,
                        tickCount=10,
                    ),
                ),
                color=alt.Color("location:N", legend=alt.Legend(title="Country")),
                tooltip=[alt.Tooltip("date:T", title="Date"), 
                    alt.Tooltip("new_cases_per_million", title="New Cases")],
            )
            .interactive()
        )
    elif interval=="rollingmean":
        chart = (
            alt.Chart(cases_df, title="Rolling Mean of Confirmed COVID-19 Cases per Million People")
            .mark_line()
            .transform_window(
                rolling_mean="mean(new_cases_per_million)",
                frame = [-6, 0],
            ).encode(
                x=alt.X(
                    "date:T",
                    axis=alt.Axis(
                        format="%b, %Y", title="Date", titleFontSize=14, tickCount=20
                    ),
                ),
                y=alt.Y(
                    "rolling_mean:Q",
                    axis=alt.Axis(
                        title="Rolling Mean of Reported Cases per Million",
                        titleFontSize=14,
                        tickCount=10,
                    ),
                ),
                
                color=alt.Color("location:N", legend=alt.Legend(title="Country")),
                tooltip=[alt.Tooltip("date:T", title="Date"), 
                    alt.Tooltip("rolling_mean:Q", title="Rolling Mean")],
            )
            .interactive()
        )
    elif interval=="cumulative":
        chart = (
            alt.Chart(cases_df, title="Cumulative Count of Confirmed COVID-19 Cases per Million People")
            .mark_line()
            .transform_window(
                sort=[{"field": "date"}],
                cumulative_count="sum(new_cases_per_million)",
                frame=[None, 0],
            ).encode(
                x=alt.X(
                    "date:T",
                    axis=alt.Axis(
                        format="%b, %Y", title="Date", titleFontSize=14, tickCount=20
                    ),
                ),
                y=alt.Y(
                    "cumulative_count:Q",
                    axis=alt.Axis(
                        title="Cumulative Count of Reported Cases per Million",
                        titleFontSize=14,
                        tickCount=10,
                    ),
                ),
                
                color=alt.Color("location:N", legend=alt.Legend(title="Country")),
                tooltip=[alt.Tooltip("date:T", title="Date"), 
                    alt.Tooltip("cumulative_count:Q", title="Cumulative Count")],
            )
            .interactive()
        )
    else:
        print("Undefined input")

    return chart


def main():
    """Function called when run as a script

    Creates a chart and display it or save it to a file
    """

    chart = plot_reported_cases_per_million(countries=["Norway"], interval='daily', start="2020-01-06", end="2021-12-01")
    # chart.show requires altair_viewer
    # or you could save to a file instead
    chart.show()


if __name__ == "__main__":
    main()