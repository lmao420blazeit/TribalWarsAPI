import sys
sys.path.append("..")
from api.twapi.baseserver import ServerBaseClass
from prefect import task
import os
from datetime import datetime
import json
import pandas as pd

date = str(datetime.now().strftime("%Y-%m-%d"))

@task(name = "Fetch server data")
def fetch_server_data(server):
    data_list = []
    for _server in server:
        data = ServerBaseClass().get_servers_table(server=_server)
        data_list.append(data)

    data_list = pd.concat(data_list).to_json(orient = "records")

    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists("data/server-data"):
        os.makedirs("data/server-data")
        
    json_path = 'data/server-data/server_data.json'.format(date)
    # overwrite
    with open(json_path, 'w') as f:
        json.dump(data_list, f)  