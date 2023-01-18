import os
import pandas as pd
from pprint import pprint

# from datetime import datetime

cur_dir_path = os.path.dirname(os.path.realpath('__file__'))
parent_dir   = os.path.abspath(os.path.join(cur_dir_path, os.pardir))

raw_data_file = parent_dir + '/data/testing/raw/data.json'

with open(raw_data_file, 'r') as in_file:
    raw_data  = in_file.readline()
    dict_data = eval(raw_data)

    # pprint(dict_data['timeSeries'][0]['parameters'])
    # print(type(dict_data['timeSeries'][0]['parameters']))
    

    # print(type(dict_data['station']))
    df = pd.DataFrame(dict_data['timeSeries'])
    print(df)




#### Lite kod:

column_names = list(dict_data['timeSeries'][0]['parameters'][0].keys())
column_names.insert(0, 'validTime')

dataframe = pd.DataFrame(columns = column_names) # tomt dataframe med rätt kolumnnamn för ett kunna lägga till saker i
print(dataframe.head(22))
dfc = df.explode('parameters')

print(dfc.head(22))

# date          - for each:
# temp          - 'name': 't',    'unit': 'Cel'
# hPa           - 'name': 'msl',  'unit': 'hPa'
# percipitation - 'name': 'pmax', 'unit': 'kg/m2/h'

# for i in range(len(dfc)):
#     # print(df.loc[i]['validTime'])
#     for j in range(len(dfc.loc[i]['parameters'])):
#         print(dfc.loc[i]['parameters'])
#         print(type(dfc.loc[i]['parameters']))


#         # for k in df.loc[i]['parameters']:
#         #     print(k)
#         #     if k['name'] == 't':
#         #         print(k[''])
            
#         print('\n\n')