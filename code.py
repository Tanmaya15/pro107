import pandas as pd
import csv
import plotly.express as px

df=pd.read_csv("data107.csv")

print(df.groupby("level")["attempt"].mean())

fig = px.scatter(df, x="student_id", y="level",
	          size="attempt",color="attempt",
                   size_max=20)
fig.show()