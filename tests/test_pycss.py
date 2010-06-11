import unittest

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
    'result':"""#navbar { width: 100%; height: 23px; }
#navbar ul { list-style-type: none; }
#navbar li { float: left; }
#navbar li a { font-weight: bold; }
""",}


class PyCSS(unittest.TestCase):

    def test_fixture_1_parsing(self):
        from pycss import PyCSS
        self.assertEquals(PyCSS.parse(FIXTURE_1['code']), FIXTURE_1['result'])

