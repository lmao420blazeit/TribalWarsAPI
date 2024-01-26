from .prefect_config.flows import fetch_from_api

if __name__ == "__main__":
    tribalwars_server_list = ["tribalwars.com.pt",
                              "die-staemme.de",
                              "tribalwars.com.br"]
    fetch_from_api(tribalwars_server_list) #.visualize()