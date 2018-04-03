#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals

from prompt_toolkit.token import Token
from prompt_toolkit.styles import style_from_dict

from selectmenu import SelectMenu


class OriginalSelectMenu(SelectMenu):

    def _get_style(self):

        return style_from_dict(
            {
                Token.Selected: '#08e3ff',
                Token.Instruction: '#ff2408',
                Token.Answer: '#08e3ff bold',
                Token.Question: '#fff bold'
            }
        )


if __name__ == '__main__':

    menu = OriginalSelectMenu()
    menu.add_choices(
        ["Google Chrome", "FireFox", "Safari", "Internet Explorer"])
    result = menu.select("Choice your browser")
    print "You chosen '{}'".format(result)
