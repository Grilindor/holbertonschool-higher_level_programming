#!/usr/bin/env python3
"""function that convert format CSV in to format JSON with serialisation"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """serialisation, Handle exceptions"""
    try:
        with open(csv_filename, 'r') as csvf:
            csvReader = csv.DictReader(csvf)
            data = list(csvReader)

        json_filename = 'data.json'
        with open(json_filename, 'w') as jsonf:
            jsonf.write(json.dumps(data, indent=4))
        return True
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
