from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd


df= pd.read_csv('https://raw.githubusercontent.com/Artem34343512/dashboard-analysis-of-production-activity/main/productionactivity.csv')

grouped_df = df.groupby(['Дата', 'Вид работ']).sum()


df_long = grouped_df.reset_index().melt(id_vars=['Дата'], value_vars=grouped_df.columns[1:], var_name='Вид работ', value_name='Количество_шт')


fig = px.scatter(df_long, x='Дата', y='Количество_шт', color='Вид работ')


fig.show()




app = Dash(__name__)
if __name__ == '__main__':
   app.run(debug=True)


