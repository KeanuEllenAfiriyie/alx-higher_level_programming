#!/usr/bin/python3
"""
Contai function "wrtie_file"
"""


def write_file(filename="", text=""):
    """returns the number of char to "filename" from "text" """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
