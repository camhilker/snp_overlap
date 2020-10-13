import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

plot = pd.read_csv('plotly_data.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    dcc.Graph(id='graph-with-radio'),
    dcc.RadioItems(id='overlap_set',
        options=[
            {'label': 'Original 256', 'value': 'o256'},
            {'label': 'Microhaplotype', 'value': 'mh'},
            {'label': 'Kidd 55', 'value': 'k55'},
            {'label': 'FrogKB', 'value': 'frog'},
            {'label': 'Global Diversity Array', 'value': 'gda'}
        ]
    ),
])


@app.callback(
    Output('graph-with-radio', 'figure'),
    [Input('overlap_set', 'value')])
def update_figure(snp_set):
    fig = px.scatter(plot, x="count", y="ave_imp_value", size="std_imp_value", color=snp_set, color_discrete_map={True:'orange', False:'aquamarine'},
                 hover_name="snp", width=1200, height=800, 
                 labels={'ave_imp_value':'Average RF Importance Value', 
                 'count':'Number of Times in Top Features', 
                 'sig_snp_set':'Appears in SNP Set', 
                 'std_imp_value':'Variance of Importance Value',
                 'o256':'Overlaps With Original 256 SNPs',
                 'mh':'Overlaps With Original Microhap SNPs',
                 'k55':'Overlaps With Original Kidd 55 SNPs',
                 'frog':'Overlaps With FrogKB SNPs',
                 'gda':'Overlaps with GDA SNPs'})

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
