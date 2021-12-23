import json
import pathlib

path = pathlib.Path(__file__).parent.resolve()

def load_settings(_path):
    if _path != path:
        config = open(f"{_path}/settings/config.json")
    else:
        config = open(f"../settings/config.json")
        
    data = json.load(config)

    host = data.get('HOST')
    port = data.get('PORT')
    unicode = data.get('UNICODE')

    return host, port, unicode