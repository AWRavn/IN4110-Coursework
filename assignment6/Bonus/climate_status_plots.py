import pandas as pd
import altair as alt

import climate_status_data_prep


def plot_mean_temperature():
    """
    Plots data of climate status using altair. Calls the function climate_status_data_prep to 
    receive a dataframe used for plotting.

    Return:
        chart (alt.Chart):           Chart of number of reported covid-19 cases over time
    """

	# create dataframe
    temp_df = climate_status_data_prep.read_csv()

    alt.data_transformers.disable_max_rows()

    chart = (
        alt.Chart(temp_df, title="Climate Status")
        .mark_line()
        .encode(
            x=alt.X(
                "Date:T",
                axis=alt.Axis(
                    format="%b, %Y", title="Date", titleFontSize=14, tickCount=20
                ),
            ),
            y=alt.Y(
                "Mean Temperature",
                axis=alt.Axis(
                    title="Temperature [Celsius]",
                    titleFontSize=14,
                    tickCount=10,
                ),
            ),
            tooltip=[alt.Tooltip("Date:T", title="Date"), 
                alt.Tooltip("Mean Temperature", title="Temperature")],
        )
        .interactive()
	)   

    return chart


def main():
    """
    Function called when run as a script. Creates a chart and displays it.
    """

	chart = plot_mean_temperature()
	chart.show()


if __name__ == "__main__":
	main()