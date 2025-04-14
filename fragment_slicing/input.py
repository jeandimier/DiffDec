#!/usr/bin/env python

import json
import sys

from dacite import from_dict
from manager import Manager

from fragment_slicing.dtos import GeneralConfiguration

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        json_input = f.read().replace("\r", "").replace("\n", "")

    configuration = {}
    try:
        configuration = json.loads(json_input)
    except (ValueError, KeyError, TypeError):
        print("JSON format error")
    else:
        general_config = from_dict(data_class=GeneralConfiguration, data=configuration)
        manager = Manager(general_config)
        manager.run()
