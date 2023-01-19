# Import modules
import os
import pandas as pd


# Definition of functions
def get_parent_dir():
    """
    Returns the parent dictionary of the Python file

    Returns
    -------
    parent_dir : str
        Path to the parent directory of the file.

    """
    cur_dir_path = os.path.dirname(os.path.realpath('__file__'))
    parent_dir   = os.path.abspath(os.path.join(cur_dir_path, os.pardir))

    return parent_dir





def read_json_to_df (raw_data_file):
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





def harmonize_data(df):
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





def save_harmonized_df(dataframe, parent_dir):
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
    dataframe.to_json(parent_dir + '/data/testing/cleansed/data.json', orient = 'records')





# Calling the functions
if __name__ == '__main__':
    parent_dir = get_parent_dir()
    raw_data_file = parent_dir + '/data/testing/raw/data.json'
    df = read_json_to_df (raw_data_file)
    dataframe = harmonize_data(df)
    save_harmonized_df(dataframe, parent_dir)