#!/usr/bin/python3
"""
Containfile function
"""


def read_file(filename=""):
    """""reads a tex(UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
