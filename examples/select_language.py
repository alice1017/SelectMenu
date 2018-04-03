#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals

from selectmenu import SelectMenu

menu = SelectMenu()
menu.add_choices(
    ["Python", "Ruby", "Javascript", "HTML", "CSS"])
result = menu.select("Choice languages")
print result
