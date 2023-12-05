from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

data= pd.read_csv('https://raw.githubusercontent.com/Artem34343512/dashboard-analysis-of-production-activity/main/productionactivity.csv')

app = Dash(__name__)
fig = px.line(data, x='Дата', y='Количество(шт)', color='Вид работ', facet_col='Номер цеха',
              title='График')
fig.show()
if __name__ == '__main__':
    app.run(debug=True)
