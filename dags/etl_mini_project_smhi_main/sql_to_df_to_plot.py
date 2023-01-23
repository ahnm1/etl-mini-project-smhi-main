# Import modules
import os
import psycopg2
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from etl_mini_project_smhi_main.conn import DBWorker




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
def get_df():
    column_name = ["date", "time", "temperature", "air_pressure", "precipitation"]
    db_worker = DBWorker()
    conn = db_worker.create_conn()
    df = postgresql_to_dataframe(conn, "SELECT date, time, temperature, air_pressure, precipitation FROM Weather_data;", column_name)
    df.head(10)
    print (df)
    return df.tail(24)

#test plot för att se så att det funkar
def plot_df():
    column_name = ["date", "time", "temperature", "air_pressure", "precipitation"]
    db_worker = DBWorker()
    conn = db_worker.create_conn()
    df = postgresql_to_dataframe(conn, "SELECT date, time, temperature, air_pressure, precipitation FROM Weather_data;", column_name)
    # fig = px.bar(df, x="date", y="temperature", title='Temperature over time')
    # fig.show()

    #matplotlib test
    plt.plot(df["time"], df["temperature"])
    plt.show()
    plt.savefig(f'Temperature_plot_{df["date"][0]}.jpg')
    #fig.savefig('matplotlib_subplots.jpg')