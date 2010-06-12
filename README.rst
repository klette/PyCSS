PyCSS
=====

Experimental python dict to css converter.

Not as fancy as Sass and those things, but still kinda useful :-)

You get variables and functions for free, and you can define values as lambdas
if you want (but not keys just yet.)


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


PyCSS color library
-------------------

``pycss.colors`` has some predefined colors for you. As of now we have the tango color scheme in place.

Tango Color Scheme
^^^^^^^^^^^^^^^^^^

.. image:: PyCSS/raw/master/doc/tango_colors.png


Example::
   >>> from pycss.colors import *
   >>>print tango_alumunium[0]
   #EEEEEC

The index goes from lighest to darkes version of the color.

