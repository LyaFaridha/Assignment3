from dash import Dash, html, dcc, Input, Output
import plotly.express as px

app = Dash(__name__)
server = app.server

app.title = "MCM7003 Data Visualization Interactive Demo" 

fig1 = px.line(x=["a","b","c","d","e"], y=[1,3,2,2,3], title="Sample figure")	

df = px.data.iris()
fig2 = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="A Plotly Express Figure")

app.layout = html.Div(
    [html.H1("Data Visualization"),
    dcc.RadioItems(id='my-radio', options=['Figure 1', 'Figure 2'], value='Figure 1', inline=True),
    dcc.Graph(id='graph-output', figure ={})]
)


@app.callback(
    Output(component_id='graph-output', component_property='figure'),
    Input(component_id='my-radio', component_property='value')
)

def update_my_graph(val_chosen):
    if (val_chosen == 'Figure 1'):
        return fig1	
    else: 
        return fig2


if __name__ == '__main__':
    app.run_server(debug=True)
country_counts = df['Country of Origin'].value_counts()
fig = px.bar(country_counts, x=country_counts.index, y=country_counts.values)

fig.update_layout(
    xaxis_title = 'Country of Origin',
    yaxis_title = 'Count',
    title={'text' : 'Distribution of Country of Origins', 'x' : 0.5}
)
fig.show()

import plotly.express as px

df = px.data.gapminder()
country_counts = df['country'].value_counts()
fig_country_counts = px.bar(country_counts, x=country_counts.index, y=country_counts.values)

fig_country_counts.update_layout(
    xaxis_title='Country of Origin',
    yaxis_title='Count',
    title={'text': 'Distribution of Country of Origins', 'x': 0.5}
)

from dash import Dash, html, dcc, Input, Output
import plotly.express as px

app = Dash(__name__)
server = app.server

app.title = "MCM7003 Data Visualization Interactive Demo" 

fig1 = px.line(x=["a","b","c","d","e"], y=[1,3,2,2,3], title="Sample figure")

df = px.data.iris()
fig2 = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="A Plotly Express Figure")

# Define the new figure
df_gapminder = px.data.gapminder()
country_counts = df_gapminder['country'].value_counts()
fig_country_counts = px.bar(country_counts, x=country_counts.index, y=country_counts.values)

fig_country_counts.update_layout(
    xaxis_title='Country of Origin',
    yaxis_title='Count',
    title={'text': 'Distribution of Country of Origins', 'x': 0.5}
)

app.layout = html.Div(
    [html.H1("Data Visualization"),
     dcc.RadioItems(id='my-radio', options=['Figure 1', 'Figure 2', 'Country Counts'], value='Figure 1', inline=True),
     dcc.Graph(id='graph-output', figure={})]
)


@app.callback(
    Output(component_id='graph-output', component_property='figure'),
    Input(component_id='my-radio', component_property='value')
)
def update_my_graph(val_chosen):
    if val_chosen == 'Figure 1':
        return fig1
    elif val_chosen == 'Figure 2':
        return fig2
    elif val_chosen == 'Country Counts':
        return fig_country_counts


if __name__ == '__main__':
    app.run_server(debug=True)
