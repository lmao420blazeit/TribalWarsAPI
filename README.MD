# TribalWarsAPI

Standalone application to fetch daily data from tribalwars public API and dump it into JSON. Uses prefect as a workflow orchestration tool and pandera as data validation tool.

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

*Fetch_from_api* is the main flow. The argument which must be passed is the url list for each region. It generates a list of World type objects for each server in the region. For each server, it sequentially fetches the data for each dimension: player_data, ally_data, defense_data, attack_data, village_data.


```python

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
```

!(assets/overview_api.png)

### Example flow run

Flows run in SequentialTaskRunner() mode in local infraestructure. ConcurrentTaskRunner is not supported since subflows share the same class objects.

![Example Image](assets/main_flow.png)
