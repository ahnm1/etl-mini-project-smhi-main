# Import modules
import os
import psycopg2
import pandas as pd
# from pprint import pprint


class DBWorker:
    def __init__(self):
        pass


    # Define functions
    def cur_dir(self):
        """
        Returns the directory of the Python file

        Returns
        -------
        cur_dir_path : str
            Directory path to the current file.

        """
        cur_dir_path = os.path.dirname(os.path.realpath('__file__'))
        parent_dir   = os.path.abspath(os.path.join(cur_dir_path, os.pardir))
        parent_parent_dir   = os.path.abspath(os.path.join(parent_dir, os.pardir))
        print(parent_parent_dir)
        return parent_parent_dir





    def read_json_to_df(self, clean_data_path):
        """
        Reads a JSON file and returns the data in a Pandas DataFrame 

        Parameters
        ----------
        clean_data_path : str
            Path to the cleaned data

        Returns
        -------
        df : pandas.DataFrame
            Pandas DataFrame with the weather data.

        """
        df = pd.read_json(clean_data_path, dtype = {'date': str, 
                                                    'hour': int, 
                                                    'temp': int, 
                                                    'hPa': float, 
                                                    'percipitetion': float})
                        
        return df





    def create_conn(self):
        """
        Creates connection to the PostgreSQL database

        Returns
        -------
        conn : 
            Connection to the database.

        """
        conn = psycopg2.connect(
            host="192.168.1.46",
            port="5432",
            database="mini_etl_project",
            user="postgres",
            password="rweq-4231")
        # print('CONNECT')
        return conn





    def data_to_list(self, dataframe):
        """
        Transforms the Pandas DataFrame to tuples

        Parameters
        ----------
        dataframe : pandas.DataFrame
            DataFrame to transform.

        Returns
        -------
        list_of_data : list
            List of tuples, one for each row in the DataFrame.

        """
        list_of_data = []
        
        for i in range(len(dataframe)):
            list_of_data.append(tuple(dataframe.iloc[i]))
        # print(list_of_data)
        
        return list_of_data





    def add_new_line(self, data_tuple, conn):
        """
        Add new line to the PostgreSQL database

        Parameters
        ----------
        data_tuple : tuple
            Tuple with elements from a row in a DataFrame.
        conn : 
            Connection to the PosgreSQL server.

        Returns
        -------
        None.

        """
        # print('ADD LINE: START')
        cur = conn.cursor()
        cur.execute(f"INSERT INTO weather_data (date, time, temperature, air_pressure, precipitation) VALUES {data_tuple};") #, data_tuple[1], data_tuple[2], data_tuple[3] ,data_tuple[4]
        cur.execute("COMMIT;")
        cur.close()
        # print('ADD LINE: END')





    def add_data_to_db(self, dataframe, conn):
        """
        Adds data to PosgreSQL database

        Parameters
        ----------
        dataframe : pandas.DataFrame
            DataFrame with the data.
        conn : 
            Connection to the PostgreSQL.

        Returns
        -------
        None.

        """
        data_tuple = self.data_to_list(dataframe)
        # print('ADD DB: START')
        for i in range(0, 24):
            self.add_new_line(data_tuple[i], conn)
        # print('ADD DB: END')





# Calling the main functions
if __name__ == '__main__':
    cur_dir_path = DBWorker().cur_dir()
    clean_data_path = cur_dir_path + '/data_harmonized.json' #'/data/testing/cleansed/data.json'
    conn = DBWorker.create_conn()
    dataframe = DBWorker.read_json_to_df(clean_data_path)
    DBWorker.add_data_to_db(dataframe, conn)