# -*- coding: utf-8 -*-
"""
Parse 實價登錄
"""
import logging
import pprint
from xml.etree import ElementTree
from datetime_utils import roc_date_to_datetime
__INT_FIELDS = [
    u"建物現況格局-廳", u"建物現況格局-房", u"建物現況格局-衛", u"總價元",
    u"單價元平方公尺", u"車位總價元"]
__FLOAT_FIELDS = [
    u"土地移轉總面積平方公尺",
    u"建物移轉總面積平方公尺",
    u"車位移轉總面積平方公尺"]
__ROC_DATE_FIELDS = [u"交易年月日", u"建築完成年月"]


def _convert_type(doc):
    for tag_name in __ROC_DATE_FIELDS:
        if tag_name in doc and doc[tag_name]:
            doc[tag_name] = roc_date_to_datetime(doc[tag_name])
    for tag_name in __INT_FIELDS:
        if tag_name in doc and doc[tag_name]:
            doc[tag_name] = int(doc[tag_name])
    for tag_name in __FLOAT_FIELDS:
        if tag_name in doc and doc[tag_name]:
            doc[tag_name] = float(doc[tag_name])
    return doc


class BaseXMLParser(object):
    """
    Parse housing opendata xml.
    """
    def __init__(self, xml_path):
        """
        Args:
        xml_path -- The full path of FalV.xml. If not specified, use default
                    one.
        """
        self.xml_path = xml_path

    def parse(self):
        tree = ElementTree.parse(self.xml_path)
        e_lvr_land = tree.getroot()

        for transaction_element in e_lvr_land:
            doc = {_.tag: _.text for _ in transaction_element}
            try:
                doc = _convert_type(doc)
            except TypeError:
                pprint.pprint(doc)
                raise
