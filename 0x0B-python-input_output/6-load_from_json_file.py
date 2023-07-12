#!/usr/bin/python3
"""
Contains the "load_froon_file" function
"""

import json


def load_from_json_file(filename):
    """creates an Objecom a "JSON file" """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
