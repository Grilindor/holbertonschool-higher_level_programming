#!/usr/bin/env python3
"""Serializing and Deserializing with XML"""


import xml.etree.ElementTree as ET


def serialize_to_xml(data, filename):
    """Deserialize an XML file into a Python dictionaryneed"""
    root = ET.Element('data')

    def dict_to_xml(element, data):
        for key, value in data.items():
            child = ET.SubElement(element, key)
            if isinstance(value, dict):
                dict_to_xml(child, value)
            else:
                child.text = str(value)

    dict_to_xml(root, data)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    def xml_to_dict(element):
        result = {}
        for child in element:
            if len(child):
                """Convert to int if possible"""
                result[child.tag] = xml_to_dict(child)
            else:
                result[child.tag] = child.text
        return result

    return xml_to_dict(root)
