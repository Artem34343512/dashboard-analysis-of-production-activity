from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/Artem34343512/dashboard-analysis-of-production-activity/main/productionactivity.csv')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='Гистограмма производственной активности'),

    dcc.Graph(figure=px.histogram(df, x='Номер цеха', y='Количество(шт)'))
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)