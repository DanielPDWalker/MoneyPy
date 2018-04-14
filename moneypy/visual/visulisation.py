"""visulisation.py module - Contains the plotting functions.

It uses the utility functions from utils.py,
to get dates for use in titles and legends of the plots.
"""
import plotly.graph_objs as go
import colorlover as cl
import utils as utils

from plotly.offline import iplot


def plot_line_chart(df_list, colors=None):
    """Plot a line chart using all the dataframes in a list passed to it.

    (Works with as many dataframes as you want*. *Within reason)
    Can be passed custom colors, but has a default.
    """
    colors = colors or cl.scales['10']['div']
    data = []

    date_range_tuple = utils.min_max_date(df_list)
    max_range_tuple = utils.max_date_range(date_range_tuple)
    dates_as_string_tuple = utils.format_date_to_string(max_range_tuple)
    date_range_tuple = utils.min_max_date_format(df_list)

    for index, df in enumerate(df_list):
        line_chart = go.Scatter(
            x=df['Date'],
            y=df['Amount'],
            hoverinfo='y+x',
            name=df.name + " ({} - {})".format(
                str(date_range_tuple[index][0]),
                str(date_range_tuple[index][1])),
            line=dict(
                width=2,
                dash='dot'))

        data.append(line_chart)

    layout = dict(
        title='{} to {} Line Chart'.format(
            dates_as_string_tuple[0],
            dates_as_string_tuple[1]),
        hoverdistance=1,
        xaxis=dict(
            tickformat='%b %d',
            tickmode="auto",
            tickangle=-45,
            ticks='outside',
            ticklen=4,
            tickwidth=2,
            title='Date'),
        yaxis=dict(title='Amount'))

    fig = dict(data=data, layout=layout)
    iplot(fig)


def plot_grouped_bar_chart(df_list, colors=None):
    """Plot a grouped bar char using all the dataframes in a list passed to it.

    (Works best with 2 dataframes).
    Can be passed custom colors, but has a default.
    """
    colors = colors or cl.scales['10']['div']

    data = []
    date_range_tuple = utils.min_max_date(df_list)
    max_range_tuple = utils.max_date_range(date_range_tuple)
    dates_as_string_tuple = utils.format_date_to_string(max_range_tuple,
                                                        "yymm")

    for df in df_list:
        bar_chart = go.Bar(
            x=df['Date'],
            y=df['Amount'],
            name=df.name,
            opacity=0.75)

        data.append(bar_chart)
    data = data
    layout = go.Layout(
        barmode='group',
        title='{} to {} Income & Outgoings Comparison'.format(
            dates_as_string_tuple[0], dates_as_string_tuple[1]),
        xaxis=dict(
            tickformat='%B',
            autotick=True,
            tickangle=-45,
            ticks='outside',
            ticklen=6,
            tickwidth=2,))

    fig = go.Figure(data=data, layout=layout)
    iplot(fig)


def plot_pie_chart(df_list, colors=None):
    """Plot a pie chart using all the dataframes in a list passed to it.

    (Works best with 1 dataframe).
    Can be passed custom colors, but has a default.
    """
    colors = colors or cl.scales['10']['div']

    data = []

    for df in df_list:
        pie_chart = go.Pie(
            labels=df['Description'],
            values=df['Amount'],
            hoverinfo='label+percent',
            textinfo='value',
            textfont=dict(size=18),
            marker=dict(colors=colors, line=dict(color="#000000", width=1)))
        data.append(pie_chart)

    data = data
    layout = go.Layout(
        title='{} Pie Chart'.format(df.name))

    fig = go.Figure(data=[pie_chart], layout=layout)
    iplot(fig)
