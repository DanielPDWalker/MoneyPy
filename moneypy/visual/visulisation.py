import utils as utils


def plot_line_chart(df_list, colors=None):
    if colors == None:
        colors = cl.scales['10']['div']
        
    data = []
    date_range_tuple = utils.min_max_date(df_list)
    max_range_tuple = utils.max_date_range(date_range_tuple)
    date_range_tuple = utils.min_max_date_format(df_list)
    
    for index, df in enumerate(df_list):
        line_chart = go.Scatter(
            x = df['Date'],
            y = df['Amount'],
            hoverinfo='y+x',
            name = df.name + " (" + str(date_range_tuple[index][0]) + " - " + str(date_range_tuple[index][1]) + ")",
            line = dict(
                width = 2,
                dash = 'dot'))
        
        data.append(line_chart)
        
    layout=dict(
        title = '{} to {} Line Chart'.format(str(max_range_tuple[0]), str(max_range_tuple[1])),
        hoverdistance = 1,
        xaxis=dict(
            tickformat='%b %d',
            tickmode="auto",
            tickangle=-45,
            ticks='outside',
            ticklen=4,
            tickwidth=2,
            title = 'Date'),
        yaxis = dict(title = 'Amount'))
    
    fig = dict(data=data, layout=layout)
    iplot(fig)


def plot_grouped_bar_chart(df_list, colors=None):
    if colors == None:
        colors = cl.scales['10']['div']
        
    data = []
    date_range_tuple = utils.min_max_date(df_list)
    max_range_tuple = utils.max_date_range(date_range_tuple, 1)
    
    for df in df_list:
        bar_chart = go.Bar(
            x=df['Date'],
            y=df['Amount'],
            name = df.name,
            opacity=0.75)
    
        data.append(bar_chart)
    data = data
    layout = go.Layout(
        barmode='group',
        title = '{} to {}   Income & Outgoings Comparison'.format(max_range_tuple[0],max_range_tuple[1]),
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
    if colors == None:
        colors = cl.scales['10']['div']
        
    data = []
    date_range_tuple = utils.min_max_date(df_list)
    max_range_tuple = utils.max_date_range(date_range_tuple)

    for df in df_list:
        pie_chart = go.Pie(labels = df['Description'], values = df['Amount'], 
                   hoverinfo='label+percent', 
                   textinfo='value', 
                   textfont=dict(size=18), marker=dict(colors=colors, line=dict(color="#000000", width=1)))
        data.append(pie_chart)
        
    data = data
    layout = go.Layout(
        title = '{} Pie Chart'.format(df.name))
    
    fig = go.Figure(data=[pie_chart], layout=layout)
    iplot(fig)     
