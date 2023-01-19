# Import modules
import os
# from pprint import pprint
import requests

class SourceToRaw:
    def __init__(self):
        raw_file = os.getcwd() + '/data/testing/raw/data.json'
        # print(self.get_parent_dir())
        # parent_dir = self.get_parent_dir()
        
        data = self.request_to_dict(16, 58)
        self.dict_to_json_file(data, raw_file) # parent_dir + "/data/testing/raw/data.json")


    # Define functions
    def get_parent_dir(self):
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





    def request_to_dict(self, lon, lat):
        """
        Requests API from SMHI and returns a Python dict 

        Parameters
        ----------
        lat : int/float
            Latitude value for a location
        lon : int/float
            Longitude value for a location

        Returns
        -------
        dict
            The requested data as a Python dictonary
        """
        # url     = 'https://opendata-download-metobs.smhi.se'
        # url_get = '/api/version/1.0/parameter/1/station-set/all/period/latest-hour/data.json'
        
        
        # r = requests.get(url + url_get)
        url_get = f'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{lon}/lat/{lat}/data.json'
        r = requests.get(url_get)
        
        return r.text#json()





    def dict_to_json_file(self, data_dict, filepath):
        """
        Saves a Python dict as a JSON-file at a specific file path

        Parameters
        ----------
        data_dict : dict
            Weather data as a Python dictonary
        filepath : str
            file path as a string 

        Returns
        -------
        None.

        """
        with open(filepath, 'w') as outfile:
            outfile.writelines(str(data_dict))




def main():
    # parent_dir = get_parent_dir()
    # data = request_to_dict(16, 58)
    # dict_to_json_file(data, parent_dir + "/data/testing/raw/data.json")
    pass


# Calling the functions
if __name__ == '__main__':
    main()