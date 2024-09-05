import json

def load_level_data() -> dict:
    with open("Assets/map/level_maps.json",'r') as json_map_data:
        data = json.load(json_map_data)
    return data




if __name__ == "__main__":
    print("Hello, World!")