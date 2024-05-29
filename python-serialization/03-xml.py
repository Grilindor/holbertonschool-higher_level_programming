#!/usr/bin/env python3
"""Serializing and Deserializing with XML"""


import xml.etree.ElementTree as ET


def serialize_to_xml(data, filename):
    """Serialize a Python dictionary into an XML file"""
    root = ET.Element('data')

    def dict_to_xml(element, data):
        for key, value in data.items():
            if isinstance(value, dict):
                child = ET.SubElement(element, key)
                dict_to_xml(child, value)
            else:
                child = ET.SubElement(element, key)
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
            if len(child) == 0:
                try:
                    """Convert to int if possible"""
                    result[child.tag] = int(child.text)
                except ValueError:
                    """Return as string if conversion fails"""
                    result[child.tag] = child.text
            else:
                result[child.tag] = xml_to_dict(child)
        return result

    return xml_to_dict(root)
