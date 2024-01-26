import requests
import xmltodict
from urllib.parse import unquote
from datetime import datetime
import itertools
import re
import pandas as pd
from .world import World
import pycountry

class ServerBaseClass:
    """Server Base Class used for managing server information."""

    def __init__(self):
        """Constructor for ServerBaseClass."""
        pass
        
    def get_active_servers(self, server: str = "tribalwars.com.pt") -> dict:
        """
        Get a dictionary of active servers based on the provided base server.

        :param server: The base URL domain for the region (default is "tribalwars.com.pt").
        :type server: str

        :return: A dictionary mapping server tag to server base URL.
        :rtype: dict
        {'pts1': 'https://pts1.tribalwars.com.pt', 'ptc1': 'https://ptc1.tribalwars.com.pt', 
        'ptc2': 'https://ptc2.tribalwars.com.pt', 'ptp5': 'https://ptp5.tribalwars.com.pt', 
        'pt88': 'https://pt88.tribalwars.com.pt', 'pt90': 'https://pt90.tribalwars.com.pt', 
        'pt91': 'https://pt91.tribalwars.com.pt', 'pt92': 'https://pt92.tribalwars.com.pt'}
        """
        base_server = server
        server_list = f"http://{base_server}/backend/get_servers.php"
        re_text = re.findall(r'(\".+?\")', requests.get(server_list).text)
        re_text = [x.strip('"') for x in re_text]
        pairs = itertools.zip_longest(*[iter(re_text)] * 2, fillvalue=None)
        dct = {key: value for key, value in pairs}
        return(dct)
    
    def get_servers_table(self, server: str = "tribalwars.com.pt") -> dict:
        servers_list = self.get_active_servers(server=server)
        server_df = pd.DataFrame(list(servers_list.items()), columns=['Server Code', 'URL'])
        server_df["Region"] = server_df["Server Code"].apply(lambda x: re.findall(r'^([a-zA-Z]{2})', x)[0].upper())
        server_df["Name"] = server_df["Region"].apply(lambda x: pycountry.countries.get(alpha_2=x).name)
        return(server_df)
    
class Server(ServerBaseClass):
    """Child class of ServerBaseClass for additional server-related functionality."""
    
    def __init__(self, server):
        """
        Constructor for the Server class.

        :param server: The base URL domain for the region.
        :type server: str
        """
        self.server = server

    def generate_worlds(self):
        """
        Generate a list of World objects based on active servers.

        :return: A list of World objects.
        :rtype: list
        """
        server_dict = self.get_active_servers(self.server)
        worlds_list = []
        for gameworld, server in server_dict.items():
            worlds_list.append(World(gameworld, server))
        return(worlds_list)
    

if __name__ == "__main__":
    ServerBaseClass().get_region_table()
