import unittest
from pycss import PyCSS
from fixtures import *


class TestParsing(unittest.TestCase):
    def setUp(self):
        self.pycss = PyCSS()

    def test_fixture_1_parsing(self):
        result = self.pycss.parse(FIXTURE_PLAIN['code'])
        for expected in FIXTURE_PLAIN['result']:
            self.assertTrue(expected in result)

    def test_fixture_2_parsing_callable_values(self):
        result = self.pycss.parse(FIXTURE_LAMBDA['code'])
        for expected in FIXTURE_LAMBDA['result']:
            self.assertTrue(expected in result)
    
    def test_fixture_3_colors(self):
        result = self.pycss.parse(FIXTURE_COLORS['code'])
        print result
        for expected in FIXTURE_COLORS['result']:
            self.assertTrue(expected in result)

