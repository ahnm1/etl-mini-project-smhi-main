# Import modules
import requests


# Class
class SourceToRaw:
    def __init__(self):
        data = self.request_to_dict(16, 58)
        self.dict_to_json_file(data, 'data_raw.json')



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

        url_get = f'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{lon}/lat/{lat}/data.json'
        r = requests.get(url_get)
        
        return r.text





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