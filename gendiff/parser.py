import json
import yaml
from yaml.loader import SafeLoader


def parse(data_in, data_type):
    if data_type == 'json':
        data_in = json.loads(data_in)
    elif data_type in 'yaml' or data_type in 'yml':
        data_in = yaml.load(data_in, Loader=SafeLoader)
    return data_in
