PyCSS
=====


Example::

    mycss = {
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
    }

    PyCSS.parse(mycss)
    >>> #navbar { width: 100%; height: 23px; }
        #navbar ul { list-style-type: none; }
        #navbar li { float: left; }
        #navbar li a { font-weight: bold; }
