from json2xml import json2xml
import json


def read_from_json(payload):
    """
        The function reads all the required fields from json then converts to xml.
        """
    payload = json.dumps(payload)
    p = json.loads(payload)
    data = json2xml.Json2xml(p, wrapper="Gepg", pretty=True, attr_type=False).to_xml()
    return data


def read_from_reconciliation_json(payload):
    """
    The function reads all the required fields from json then converts to xml.
    """
    payload = json.dumps(payload)
    p = json.loads(payload)
    data = json2xml.Json2xml(p, wrapper="gepgReconSubReq").to_xml()
    return data


def parser_response_json(payload, wrapper=None):
    """
        The function reads all the required fields from json then converts to xml.
        """
    payload = json.dumps(payload)
    p = json.loads(payload)
    data = json2xml.Json2xml(p, wrapper=wrapper, pretty=True, attr_type=False).to_xml()
    return data
