import os
import psycopg2
import pandas as pd
from pprint import pprint


def cur_dir():
    cur_dir_path = os.path.dirname(os.path.realpath('__file__'))
#parent_dir   = os.path.abspath(os.path.join(cur_dir_path, os.pardir))

clean_data = cur_dir_path + '/data/testing/cleansed/data.json'
# print(clean_data)

df = pd.read_json(clean_data, dtype = {'date': str, 'hour': int, 'temp': int, 'hPa': float, 'percipitetion': float})
# print(df)

print(df)
# df = df.reset_index()
# for index, row in df.iterrows():
#     print(row)

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="mini_etl_project",
    user="postgres",
    password="rweq-4231")

#def read_weatherdata():
#    cur = conn.cursor()
#    cur.execute("SELECT * FROM weather_data;")
#    rows = cur.fetchall()
#    cur.close()
#    return rows

def data_to_list(dataframe):
    list_of_data = []
    for i in range(len(dataframe)):
        list_of_data.append(tuple(dataframe.iloc[i]))
    print(list_of_data)
    
    return list_of_data

def add_new_line(data_tuple):
    print(data_tuple)

    cur = conn.cursor()
    cur.execute(f"INSERT INTO weather_data (date, time, temperature, air_pressure, precipitation) VALUES {data_tuple};") #, data_tuple[1], data_tuple[2], data_tuple[3] ,data_tuple[4]
    cur.execute("COMMIT;")
    cur.close()


def add_data_to_db(dataframe):
    data_tuple = data_to_list(dataframe)

    #for item in data_tuple:
    #    add_new_line(item)
    
    for i in range(0, 24):
        add_new_line(data_tuple[i])

add_data_to_db(df)