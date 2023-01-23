# Import modules
import pandas as pd


# Class
class RawToHarmonized:
    def __init__(self):
        df            = self.read_json_to_df ('data_raw.json')
        dataframe     = self.harmonize_data(df)
        self.save_harmonized_df(dataframe, 'data_harmonized.json')




    def read_json_to_df (self, raw_data_file):
        """
        Reads a JSON file and transforms it to a Pandas DataFrame

        Parameters
        ----------
        raw_data_file : str
            Path to the JSON file with the data.

        Returns
        -------
        df : pandas.DataFrame
            Pandas DataFrame from the JSON file data.

        """
        with open(raw_data_file, 'r') as in_file:
            raw_data  = in_file.readline()
            dict_data = eval(raw_data)

        df = pd.DataFrame(dict_data['timeSeries'])

        return df





    def harmonize_data(self, df):
        """
        Pandas DataFrame with date, hour, temperature, air pressure and percipitation
        from the SMHI data transformed into a pandas DataFrame

        Parameters
        ----------
        df : pandas.DataFrame
            Pandas DataFrame with two columns: 'validTime' (datetime value) and 
            'parameters' (a list with a dict with data).

        Returns
        -------
        dataframe : pandas.DataFrame
            Pandas DataFrame with columns date, hour, temperature, air pressure and percipitation.

        """
        extracted_data = {'date': [], 'hour': [], 'temp': [], 'hPa': [], 'percipitation': []}
        for i in range(len(df)):
            date_time = df.loc[i]['validTime'].split('T')
            date = date_time[0]
            time_split = date_time[1].split(':')
            time = time_split[0]

            extracted_data['date'].append(date)
            extracted_data['hour'].append(time)


            for j in range(len(df.loc[i]['parameters'])):

                if df.loc[i]['parameters'][j]['name'] == 't':
                    extracted_data['temp'].append(df.loc[i]['parameters'][j]['values'][0])

                elif df.loc[i]['parameters'][j]['name'] == 'msl':
                    extracted_data['hPa'].append(df.loc[i]['parameters'][j]['values'][0])

                elif df.loc[i]['parameters'][j]['name'] == 'pmax':
                    extracted_data['percipitation'].append(df.loc[i]['parameters'][j]['values'][0])

                else:
                    continue

        dataframe = pd.DataFrame(extracted_data)

        return dataframe





    def save_harmonized_df(self, dataframe, target_dir):
        """
        Saves Pandas DataFrame as a JSON file

        Parameters
        ----------
        dataframe : pandas.DataFrame
            Cleanded DataFrame data.
        parent_dir : str
            Path tho parent directory to the current file.

        Returns
        -------
        None.

        """
        dataframe.to_json(target_dir, orient = 'records')