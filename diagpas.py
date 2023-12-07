from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

df= pd.read_csv('https://raw.githubusercontent.com/Artem34343512/dashboard-analysis-of-production-activity/main/productionactivity.csv')

grouped_df = df.groupby(['Дата',]).sum()

df_long = grouped_df.reset_index().melt(id_vars=['Дата'], value_vars=grouped_df.columns[1:],  value_name='Количество_шт')

fig = px.scatter(df_long, x='Дата', y='Количество_шт')

app = Dash(__name__)

app.layout = html.Div([
 dcc.Graph(figure=fig)
])

if __name__ == '__main__':
 app.run_server(debug=True)