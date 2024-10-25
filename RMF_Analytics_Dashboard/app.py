import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.io as pio
import plotly.colors as pc
from rmf_dashboard import *

# Initialize the Dash App
app = dash.Dash(__name__)

# Define the app layout using Bootstrap components
app.layout = html.Div([
    html.H1("RFM Analysis Dashboard", className="text-center mb-4"),
    html.Div("Analyze customer segments based on RFM scores.", className="text-center mb-4"),
    
    # Dropdown for selecting the chart
    dcc.Dropdown(
        id='chart-type-dropdown',
        options=[
            {'label': 'RFM Value Segment Distribution', 'value': 'segment_distribution'},
            {'label': 'Distribution of RFM Values within Customer Segment', 'value': 'RFM_distribution'},
            {'label': 'Correlation Matrix of RFM Values within Champions Segment', 'value': 'correlation_matrix'},
            {'label': 'Comparison of RFM Segments', 'value': 'segment_comparison'},
            {'label': 'Comparison of RFM Segments based on Scores', 'value': 'segment_scores'},
        ],
        value='segment_distribution',  # Default selection
        className="mb-4",
    ),
    
    # Graph container
    dcc.Graph(id='rfm-chart', className="mb-4"),
])

# Define callback to update the selected chart
@app.callback(
    Output('rfm-chart', 'figure'),
    [Input('chart-type-dropdown', 'value')]
)
def update_chart(selected_chart_type):
    if selected_chart_type == 'segment_distribution':
        return fig_segment_dist
    elif selected_chart_type == 'RFM_distribution':
        return fig_treemap_segment_product
    elif selected_chart_type == 'correlation_matrix':
        return fig_corr_heatmap
    elif selected_chart_type == 'segment_comparison':
        return comparison_fig
    elif selected_chart_type == 'segment_scores':
        return fig
    
    # Return a default chart if no valid selection
    return fig_segment_dist

if __name__ == '__main__':
    app.run_server(port=8052)