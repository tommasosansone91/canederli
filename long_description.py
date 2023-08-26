
LONG_DESCRIPTION = \
"""
This package contains the function 'canederlist' 

i.e. 

Comma 
And 
NEwline 
Delimited 
Elements 
Reformatted as 
LIst of 
STrings 

which allows to reformat a multiline string containing words separated by commas into a list of strings.

This is useful when we have hardcoded a list of variables and we want to quickly get a list of their names as strings.


usage
-----

The list of variables (i.e. not the variable containing the list, the hardcoded list of variables) must be copied and pasted as argument of canederlist(), enclosed in triple quotes (\"\"\").

The function canederlist will remove 
 - multiple spaces (double or more, but not single spaces)
 - newline characters
 - triple points ...
 - (if selected in the input) round () and square [] parentheses
 - (if selected in the input) single spaces
and split the remaining elements separated by commas into a list of strings.


example
-------

```
from canederli import canederlist
columns = [ names, 
            descriptions, 
            x_coordinates, 
            y_coordinates ]

columns_labels = canederlist(\"\"\"
 names, 
            descriptions, 
            x_coordinates, 
            y_coordinates 
\"\"\")

print(columns_labels)
['names', 'descriptions', 'x_coordinates', 'y_coordinates']

```

example removing parentheses
----------------------------

```

from canederli import canederlist
columns = [ names, 
            descriptions, 
            x_coordinates, 
            y_coordinates ]

columns_labels = canederlist(\"\"\"
 names, 
            descriptions, 
            x_coordinates, 
            y_coordinates ]
\"\"\",1)  # <--- this is the same as setting optional parameter rm_parentheses=True

print(columns_labels)
['names', 'descriptions', 'x_coordinates', 'y_coordinates']

```

"""