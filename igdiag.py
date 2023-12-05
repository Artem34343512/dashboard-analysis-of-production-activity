from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv('https://raw.githubusercontent.com/Artem34343512/dashboard-analysis-of-production-activity/main/productionactivity.csv')

app = Dash(__name__)
grouped_df = df.groupby('Вид работ').sum()


labels = grouped_df.index
sizes = grouped_df['Количество(шт)']
colors = ['#ff9999','#66b3ff','#99ff99']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')


plt.title('Количество работ по видам')


plt.show()
if __name__ == '__main__':
    app.run(debug=True)
