# SelectMenu

[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)

## :page_facing_up: Overview

**SelectMenu** is the input form to **choose from menu** by arrow keys.

SelectMenu powered by [**python-prompt-toolkit**](https://github.com/jonathanslenders/python-prompt-toolkit).

## :pencil2: Usage

```python
>>> from selectmenu import SelectMenu
>>> menu = SelectMenu()
>>> menu.add_choices(
...    ["Python", "Ruby", "Javascript", "HTML", "CSS"])
>>> result = menu.select("What language do you like?")
What language do you like? (Use arrow keys)
 > Python
   Ruby
   Javascript
   HTML
   CSS
>>> print result
Python
```

## :inbox_tray: Installation

```
$ git clone git@github.com:alice1017/SelectMenu.git
$ cd SelectMenu
$ python setup.py build install
```

TODO: I will upload pypi registry.

## :eyes: Contribution

1. Forks on [Github](https://github.com/alice1017/SelectMenu)
2. Find a bug? Send a pull request to get it merged and published.
