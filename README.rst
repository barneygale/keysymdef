keysymdef: X11 keysym data
==========================

This Python package contains the X11 and XF86 keysym definitions as lists of tuples::

    >>> from keysymdef import keysymdef, xf86keysym
    >>> print(keysymdef[1])
    ('BackSpace', 65288, None)
    >>> print(xf86keysym[1])
    ('MonBrightnessUp', 269025026, None)

The elements of each tuple are:

1. The mnemonic name (``str``)
2. The integer value (``int``)
3. The unicode code point, if any (``int`` or ``None``)

This data is hard-coded; consequently this package has no dependencies (on ``python-xlib`` or others).
