import unittest
from pycss import PyCSS

FIXTURE_1 = {
    'code': {
        '#navbar': {
            'width': '100%',
            'height': '23px',

            'ul': {
                'list-style-type': 'none',
            },
            'li': {
                'float': 'left',
                'a': {
                    'font-weight': 'bold'
                },
            },
        }
    },
    'result': [
    '#navbar { width: 100%; height: 23px; }',
    '#navbar ul { list-style-type: none; }',
    '#navbar li { float: left; }',
    '#navbar li a { font-weight: bold; }',
    ]
}

FIXTURE_2 = {
    'code': {
        '#foobar': {
            'width': lambda: '100%',
        },
        '#navbar': {
            'width': '100%',
            'height': '23px',

            'ul': {
                'list-style-type': 'none',
            },
            'li': {
                'float': 'left',
                'a': {
                    'font-weight': lambda: 'normal',
                },
            },
        }
    },
    'result': [
    '#foobar { width: 100%; }',
    '#navbar { width: 100%; height: 23px; }',
    '#navbar ul { list-style-type: none; }',
    '#navbar li { float: left; }',
    '#navbar li a { font-weight: normal; }',
    ]}


class TestParsing(unittest.TestCase):
    def setUp(self):
        self.pycss = PyCSS()

    def test_fixture_1_parsing(self):
        result = self.pycss.parse(FIXTURE_1['code'])
        for expected in FIXTURE_1['result']:
            self.assertTrue(expected in result)

    def test_fixture_2_parsing_callable_values(self):
        result = self.pycss.parse(FIXTURE_2['code'])
        for expected in FIXTURE_2['result']:
            self.assertTrue(expected in result)

