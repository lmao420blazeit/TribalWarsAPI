import sys
sys.path.append("..")

# python -m api 

from .subflows import *
from .tasks import fetch_server_data

@flow(name="Get data for all endpoints and dump it into json.")
def fetch_from_api(tribalwars_server_list) -> None:
    """
    Starts the subflows. Main flow.
    
    Fetches data for all endpoints from multiple Tribal Wars servers
    and dumps it into JSON files.
    Creates a object dict for each {server (str): World (object)}

    Flow isnt able to leverage ConcurrentTaskRunner() because different
    tasks share the same objects.

    :return: None
    :rtype: None
    """

    obj_list = []
    for server in tribalwars_server_list:
        # create a list of objects per server
        obj_list.extend(Server(server).generate_worlds())

    fetch_server_data(tribalwars_server_list)
    fetch_player_data(obj_list)
    fetch_ally_data(obj_list)
    fetch_defense_data(obj_list)
    fetch_attack_data(obj_list)
    fetch_village_data(obj_list)

    return

if __name__ == "__main__":
    tribalwars_server_list = ["tribalwars.com.pt",
                              "die-staemme.de",
                              "tribalwars.com.br"]
    fetch_from_api(tribalwars_server_list)
