import unittest
import os
from base_xml_parser import BaseXMLParser


class BaseXMLParserTest(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.dirname(os.path.abspath(__file__))

    def test_a(self):
        xml = os.path.join(self.test_dir, "o_lvr_land_a.xml")
        parser = BaseXMLParser(xml)
        parser.parse()


if __name__ == "__main__":
    unittest.main()
