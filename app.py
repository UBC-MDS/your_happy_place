from errno import EEXIST
from dash import Dash, html, dcc, Input, Output, State
import altair as alt
import dash
from vega_datasets import data
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv('data/processed/us_counties_processed.csv')

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.title = "Your Happy Place: Counties Comparison by Climate and Demographics"

df = df[["state",
        "county", 
        "county_state",
        "year", 
        "month", 
        "mean_temp", 
        "min_temp", 
        "max_temp", 
        "rain", 
        "snow", 
        "precipitation", 
        "percent_unemployed_CDC",
        "population_density_per_sqmi",
        "percent_age_17_and_younger",
        "percent_age_65_and_older",
        ]]
states = df.state.unique()
county_opt_dict = {}
for state in states:
    state_df = df[df['state']==state]
    counties = state_df.county.unique()
    county_opt_dict[state]=counties

df = df.groupby(["state","county","county_state","month"], as_index=False).agg({"mean_temp":"mean", 
                                                                                "min_temp":"mean", 
                                                                                "max_temp":"mean", 
                                                                                "precipitation":"mean",
                                                                                "rain":"mean",
                                                                                "snow":"mean",
                                                                                "percent_unemployed_CDC":"mean",
                                                                                "population_density_per_sqmi":"mean",
                                                                                "percent_age_17_and_younger":"mean",
                                                                                "percent_age_65_and_older":"mean" })

df["day"] = 1
df["year"] = 2020
df["date"] = pd.to_datetime(df[['month', 'day', 'year']])
nestedOptions = county_opt_dict[states[0]]

global selected_counties 
selected_counties = ['Yolo, California', 'Houston, Texas', 'Middlesex, Massachusetts']

app.layout = dbc.Container(
    [
        dbc.Row([html.H1('Your Happy Place')],
            style={'margin-top':'20px',
                   'color':'#90a0ab'}),
        html.Hr([]),
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(
                id='state-widget',
                value='Alabama',  # REQUIRED to show the plot on the first page load
                options=[
                    {'label': state, 'value': state} for state in states],
                style={'margin-bottom': '5px',
                        'max-width': '250px'}),
                dcc.Dropdown(
                    id='county-widget',
                    value='Autauga',
                    style={'margin-bottom': '5px',
                        'max-width': '250px'}),
                    
                dbc.Button('Add County', 
                    className="me-1", 
                    id='add-county', 
                    n_clicks=0,
                    style={'width': '100%',
                        'max-width': '250px'}
                )
            ], md=4),

            dbc.Col([
                html.Div(id='selected_counties'),
                dbc.Button('Reset', 
                    className="me-1", 
                    id='reset', 
                    n_clicks=0,
                    style={'width': '100%',
                        'max-width': '250px'}
                )], md=4),
            ], style={'margin-top':'20px'}),
            
        html.Hr([]),

        dbc.Row([html.Div([
            html.Iframe(
            id='scatter',
            style={'border-width': '0', 'width': '100%', 'height': '2000px'}),
            ],style={}),
        ])
        
    ]
)

#state selector
@app.callback(
    [Output('county-widget', 'options'),
    Output('county-widget', 'value'),],
    [Input('state-widget', 'value')]
)
def update_county_dropdown(state):
    if not(state):
        county=''
        return {}, None
    return [{'label': county, 'value': county} for county in county_opt_dict[state]], None


#Button clicker
# TODO: add remove Input below
# make sure remove buttons have neccesary ids / props
@app.callback(
    Output('selected_counties', 'children'),
    [Input("add-county", "n_clicks"),
    Input("reset", "n_clicks")],[
    State('state-widget', 'value'),
    State('county-widget', 'value')])
def set_display_children(add_county, reset, state, county):
    ctx = dash.callback_context
    trig = ctx.triggered[0]['prop_id']

    if (trig == 'reset.n_clicks'):
        return "Please select some countries of interest! :)"
    else:
        if (state and county):
            county_state = county + ", " + state
            if county_state not in selected_counties:
                selected_counties.append(county_state)
        return html.Ul([html.Li([x]) for x in selected_counties])

# plot
@app.callback(
    Output('scatter', 'srcDoc'),
    [Input("add-county", "n_clicks"),
    Input("reset", "n_clicks"),
    ],[
    State('state-widget', 'value'),
    State('county-widget', 'value')])
def plot_altair(add_county, reset, state, county):
    ctx = dash.callback_context
    trig = ctx.triggered[0]['prop_id']

    if (trig == 'reset.n_clicks'):
        global selected_counties 
        selected_counties = []
        df_filtered = df[df['county_state'].isin(selected_counties)]
        print('here')
        #df_filtered = df[df['county'=="nonexistant_to_return_empty_df"]]
    else:
        if (state and county):
            #print(selected_counties)
            df_filtered = df[df['county_state'].isin(selected_counties)]

    click = alt.selection_multi(fields=['county_state'], bind='legend')

    chart_unemp = alt.Chart(df_filtered).mark_bar().encode(
        color = alt.Color('county_state',
            legend=alt.Legend(
            orient='top',
            columns=4,
            title="", 
            labelFontSize=18, 
            labelLimit=0 )
        ),
        opacity=alt.condition(click, alt.value(1), alt.value(0.05)),
        x=alt.X('county_state', title=""),
        y=alt.Y('percent_unemployed_CDC', title="Unemployed (%)")).properties(
            title="Percent Unemployed CDC").add_selection(click)

    chart_den = alt.Chart(df_filtered).mark_bar().encode(
        color = alt.Color('county_state'),
        opacity=alt.condition(click, alt.value(1), alt.value(0.05)),
        x=alt.X('county_state', title=""),
        y=alt.Y('population_density_per_sqmi', title="Population Density (per sqrm)")).properties(
            title="Population Density").add_selection(click)

    chart_18 = alt.Chart(df_filtered).mark_bar().encode(
        color = alt.Color('county_state'),
        opacity=alt.condition(click, alt.value(1), alt.value(0.05)),
        x=alt.X('county_state', title=""),
        y=alt.Y('percent_age_17_and_younger', title="Residents under 18 yo (%)")).properties(
            title="Percent Population 18 and younger").add_selection(click)

    chart_65 = alt.Chart(df_filtered).mark_bar().encode(
        color = alt.Color('county_state'),
        opacity=alt.condition(click, alt.value(1), alt.value(0.05)),
        x=alt.X('county_state', title=""),
        y=alt.Y('percent_age_65_and_older', title="Residents over 65 yo (%)")).properties(
            title="Percent Population 65 and over").add_selection(click)

    chart_t = alt.Chart(df_filtered).mark_line().encode(
        color = alt.Color('county_state' ),
        opacity=alt.condition(click, alt.value(1), alt.value(0.2)),
        x=alt.X('month(date):T', title="Month"),
        y=alt.Y('mean_temp', title="Mean Temperature (F°)")).properties(
            title="Mean Monthly Temperature")

    chart_rain = alt.Chart(df_filtered).mark_line().encode(
        color = alt.Color('county_state'),
        opacity=alt.condition(click, alt.value(1), alt.value(0.2)),
        x=alt.X('month(date):T', title="Month"),
        y=alt.Y('rain', title="Mean Rainfall (in)")).properties(
            title="Mean Monthly Rainfall")

    chart_snow = alt.Chart(df_filtered).mark_line().encode(
        color = alt.Color('county_state' ),
        opacity=alt.condition(click, alt.value(1), alt.value(0.2)),
        x=alt.X('month(date):T', title="Month"),
        y=alt.Y('snow', title="Mean Snowfall (in)")).properties(
            title="Mean Monthly Snowfall")

    chart_t_min = alt.Chart(df_filtered).mark_line().encode(
        color = alt.Color('county_state' ),
        opacity=alt.condition(click, alt.value(1), alt.value(0.2)),
        x=alt.X('month(date):T', title="Month"),
        y=alt.Y('min_temp', title="Min Temperature (F°)")).properties(
            title="Minn Monthly Temperature")

    chart_t_max = alt.Chart(df_filtered).mark_line().encode(
        color = alt.Color('county_state' ),
        opacity=alt.condition(click, alt.value(1), alt.value(0.2)),
        x=alt.X('month(date):T', title="Month"),
        y=alt.Y('max_temp', title="Max Temperature (F°)")).properties(
            title="Max Monthly Temperature")

    chart_per = alt.Chart(df_filtered).mark_line().encode(
        color = alt.Color('county_state' ),
        opacity=alt.condition(click, alt.value(1), alt.value(0.2)),
        x=alt.X('month(date):T', title="Month"),
        y=alt.Y('precipitation', title="Mean Precipitation (in)")).properties(
            title="Mean Monthly Precipitation")

    chart_combo = (chart_unemp & chart_den & chart_18 & chart_65)| ( chart_t & chart_t_min & chart_t_max) | (chart_per & chart_rain & chart_snow) 

    return chart_combo.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)