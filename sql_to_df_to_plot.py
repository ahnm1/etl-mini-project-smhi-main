import os
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="mini_etl_project",
    user="postgres",
    password="tAggA67!")#byt lösenord

def postgresql_to_dataframe(conn, select_query, column_names):
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1
    tupples = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(tupples, columns=column_names)
    return df

#test DF för att se så att det funkar
column_name = ["date", "time", "temperature", "air_pressure", "precipitation"]
df = postgresql_to_dataframe(conn, "SELECT date, time, temperature, air_pressure, precipitation FROM Weather_data;", column_name)
df.head(10)
print (df)

#test plot för att se så att det funkar
column_name = ["date", "time", "temperature", "air_pressure", "precipitation"]
df = postgresql_to_dataframe(conn, "SELECT date, time, temperature, air_pressure, precipitation FROM Weather_data;", column_name)
fig = px.bar(df, x="date", y="temperature", title='Temperature over time')
fig.show()