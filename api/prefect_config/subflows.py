import sys
sys.path.append("..")
from api.twapi.baseserver import Server
# python -m api 


from prefect import task, flow
import os
import json
from datetime import datetime
from api.pandera.schemas import *

date = str(datetime.datetime.now().strftime("%Y-%m-%d"))

@flow(name="Get player data")
def fetch_player_data(worlds):
    """
    Function returns the player data for a specific world.

    :param worlds: List of objects of class World
    :type parameter1: List[World]

    :return: Uploads data into a json
    :rtype: None
    """
    for obj in worlds:
        #data = json.loads(data)
        if not os.path.exists("data"):
            os.makedirs("data")

        if not os.path.exists("data/player-data"):
            os.makedirs("data/player-data")

        if not os.path.exists("data/player-data/{}".format(date)):
            os.makedirs("data/player-data/{}".format(date))

        json_path = 'data/player-data/{}/{}.json'.format(date, getattr(obj, "gameworld"))
        if not os.path.exists(json_path):
            data = obj.get_player()
            data = json.dumps(data)
            data = json.loads(data)
            data = player_data_schema.validate(pd.DataFrame(data).T, lazy = True)
            data.to_json(json_path, orient='records', lines=True)

    return

@flow(name="Get ally data")
def fetch_ally_data(worlds):
    """
    Function returns the ally data for a specific world.

    :param worlds: List of objects of class World
    :type parameter1: List[World]

    :return: Uploads data into a json
    :rtype: None
    """
    for obj in worlds:
        #data = json.loads(data)
        if not os.path.exists("data"):
            os.makedirs("data")

        if not os.path.exists("data/ally-data"):
            os.makedirs("data/ally-data")

        if not os.path.exists("data/ally-data/{}".format(date)):
            os.makedirs("data/ally-data/{}".format(date))

        json_path = 'data/ally-data/{}/{}.json'.format(date, getattr(obj, "gameworld"))
        if not os.path.exists(json_path):
            data = json.dumps(obj.get_ally())
            data = json.loads(data)
            data = ally_data_schema.validate(pd.DataFrame(data).T, lazy = True)
            data.to_json(json_path, orient='records', lines=True)

    return

@flow(name="Get ODD data")
def fetch_defense_data(worlds):
    """
    Function returns the defense data for a specific world.

    :param worlds: List of objects of class World
    :type parameter1: List[World]

    :return: Uploads data into a json
    :rtype: None
    """
    for obj in worlds:
        #data = json.loads(data)
        if not os.path.exists("data"):
            os.makedirs("data")

        if not os.path.exists("data/defense-data"):
            os.makedirs("data/defense-data")

        if not os.path.exists("data/defense-data/{}".format(date)):
            os.makedirs("data/defense-data/{}".format(date))

        json_path = 'data/defense-data/{}/{}.json'.format(date, getattr(obj, "gameworld"))
        if not os.path.exists(json_path):
            data = json.dumps(obj.get_odd())
            data = json.loads(data)
            data = defense_data_schema.validate(pd.DataFrame(data).T, lazy = True)
            data.to_json(json_path, orient='records', lines=True)

    return

@flow(name="Get ODA data",  log_prints=True)
def fetch_attack_data(worlds):
    """
    Function returns the attack data for a specific world.

    :param worlds: List of objects of class World
    :type parameter1: List[World]

    :return: Uploads data into a json
    :rtype: None
    """
    for obj in worlds:
        #data = json.loads(data)
        if not os.path.exists("data"):
            os.makedirs("data")

        if not os.path.exists("data/attack-data"):
            os.makedirs("data/attack-data")

        if not os.path.exists("data/attack-data/{}".format(date)):
            os.makedirs("data/attack-data/{}".format(date))

        json_path = 'data/attack-data/{}/{}.json'.format(date, getattr(obj, "gameworld"))
        if not os.path.exists(json_path):
            data = json.dumps(obj.get_oda())
            data = json.loads(data)
            data = attack_data_schema.validate(pd.DataFrame(data).T, lazy = True)
            data.to_json(json_path, orient='records', lines=True)

    return

@flow(name="Get village data")
def fetch_village_data(worlds):
    """
    Function returns the village data for a specific world.

    :param worlds: List of objects of class World
    :type parameter1: List[World]

    :return: Uploads data into a json
    :rtype: None
    """
    for obj in worlds:
        #data = json.loads(data)
        if not os.path.exists("data"):
            os.makedirs("data")

        if not os.path.exists("data/village-data"):
            os.makedirs("data/village-data")

        if not os.path.exists("data/village-data/{}".format(date)):
            os.makedirs("data/village-data/{}".format(date))

        json_path = 'data/village-data/{}/{}.json'.format(date, getattr(obj, "gameworld"))
        if not os.path.exists(json_path):
            data = json.dumps(obj.get_village())
            data = json.loads(data)
            data = village_data_schema.validate(pd.DataFrame(data).T, lazy = True)
            data.to_json(json_path, orient='records', lines=True)

    return