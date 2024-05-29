#!/usr/bin/env python3
""" """


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """ """
    root = ET.Element("data")
    for key, value in dictionary["data"].items():
        filename = ET.SubElement(root, key)
        filename.text = value
    tree = ET.ElementTree(root)
    tree.write("data.xml")

def deserialize_from_xml(filename):
    tree  = ET.parse('data.xml')
    root = tree.getroot()
