#!/usr/bin/python3
"""
Coains the "from_json_string" function
"""

import json


def from_json_string(my_str):
    """ret object represented by a JSON string"""
    return json.loads(my_str)
