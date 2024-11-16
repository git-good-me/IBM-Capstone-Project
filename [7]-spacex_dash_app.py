# Import necessary libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load SpaceX data
spacex_df = pd.read_csv("spacex_launch_geo.csv")
launch_sites = spacex_df['Launch Site'].unique()

# Initialize Dash app
app = dash.Dash(__name__)

# App Layout
app.layout = html.Div([
    # Task 1: Dropdown for Launch Sites
    html.H1("SpaceX Launch Records Dashboard", style={'textAlign': 'center'}),
    
    html.Div([
        dcc.Dropdown(
            id='site-dropdown',
            options=[
                {'label': 'All Sites', 'value': 'ALL'}
            ] + [{'label': site, 'value': site} for site in launch_sites],
            value='ALL',
            placeholder="Select a Launch Site here",
            searchable=True
        ),
    ], style={'padding': '20px'}),
    
    # Task 2: Pie Chart for Success Rates
    html.Div(dcc.Graph(id='success-pie-chart')),
    
    # Task 3: Range Slider for Payload
    html.Div([
        html.P("Payload Range (Kg):"),
        dcc.RangeSlider(
            id='payload-slider',
            min=0, max=10000, step=1000,
            marks={i: f'{i} Kg' for i in range(0, 10001, 2000)},
            value=[0, 10000]
        ),
    ], style={'padding': '20px'}),
    
    # Task 4: Scatter Plot for Payload vs. Outcome
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# Task 2: Callback to Update Pie Chart
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def update_pie_chart(entered_site):
    """
    Updates the pie chart based on the selected launch site.
    If 'ALL' is selected, shows success distribution for all sites.
    If a specific site is selected, shows success vs. failure for that site.
    """
    if entered_site == 'ALL':
        # Create pie chart for all sites
        fig = px.pie(
            spacex_df,
            names='Launch Site',
            values='class',
            title='Total Success Launches by Site'
        )
    else:
        # Filter data for the selected site
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        fig = px.pie(
            filtered_df,
            names='class',
            title=f'Success vs. Failure for {entered_site}'
        )
    return fig

# Task 4: Callback to Update Scatter Plot
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def update_scatter_chart(entered_site, payload_range):
    """
    Updates the scatter plot based on the selected site and payload range.
    Shows payload mass vs. launch outcome for all sites or the selected site.
    Points are color-coded by Booster Version Category.
    """
    # Filter data based on payload range
    filtered_df = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= payload_range[0]) &
        (spacex_df['Payload Mass (kg)'] <= payload_range[1])
    ]
    
    if entered_site == 'ALL':
        # Scatter plot for all sites
        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title='Payload vs. Outcome for All Sites'
        )
    else:
        # Scatter plot for the selected site
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title=f'Payload vs. Outcome for {entered_site}'
        )
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
