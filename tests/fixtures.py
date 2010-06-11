from pycss import colors

FIXTURE_PLAIN = {
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

FIXTURE_LAMBDA = {
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

FIXTURE_COLORS = {
    'code': {
        '#foobar': {
            'color': colors.tango_red1,
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
    '#foobar { color: #123456; width: 100%; }',
    '#navbar { width: 100%; height: 23px; }',
    '#navbar ul { list-style-type: none; }',
    '#navbar li { float: left; }',
    '#navbar li a { font-weight: normal; }',
    ]}
