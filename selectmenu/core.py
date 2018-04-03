#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals

from prompt_toolkit.token import Token
from prompt_toolkit.styles import style_from_dict
from prompt_toolkit.filters import IsDone
from prompt_toolkit.shortcuts import create_eventloop
from prompt_toolkit.interface import CommandLineInterface
from prompt_toolkit.application import Application
from prompt_toolkit.layout.controls import TokenListControl
from prompt_toolkit.layout.dimension import LayoutDimension as LD
from prompt_toolkit.layout.containers import (
    ConditionalContainer, ScrollOffsets, HSplit, Window)

from selectmenu.keybinding import set_key_binding
from selectmenu.control import SelectControl


class SelectMenu(object):

    def add_choices(self, choice_list):

        if not isinstance(choice_list, list):
            raise ValueError("The choices is not list.")

        self.choices = choice_list
        self.controller = SelectControl(self.choices)

    def select(self, message=None):

        self.prompt_msg = message

        layout = self._get_layout()
        style = self._get_style()
        registry = set_key_binding(self.controller)

        application = Application(
            layout=layout,
            style=style,
            key_bindings_registry=registry
        )

        eventloop = create_eventloop()

        try:
            cli = CommandLineInterface(
                application=application,
                eventloop=eventloop
            )
            cli.run()

        finally:
            eventloop.close()
            return self.controller.selected

    def _get_layout(self):

        token_list_window = Window(
            height=LD.exact(1),
            content=TokenListControl(self._get_prompt_tokens)
        )

        conditional_window = ConditionalContainer(
            Window(
                self.controller,
                width=LD.exact(43),
                height=LD.exact(len(self.choices)),
                scroll_offsets=ScrollOffsets(top=1, bottom=1)
            ),
            filter=~IsDone()
        )

        if self.prompt_msg:

            return HSplit([
                    token_list_window,
                    conditional_window
            ])

        else:

            return HSplit([
                conditional_window
            ])

    def _get_style(self):

        return style_from_dict(
            {
                Token.Selected: '#FF9D00',
                Token.Instruction: '',
                Token.Answer: '#FF9D00 bold',
                Token.Question: 'bold'
            }
        )

    def _get_prompt_tokens(self, cli):

        if self.prompt_msg:

            return [
                (Token.Question, self.prompt_msg),
                (Token.Instruction, ' (Use arrow keys)')
            ]

        else:

            return []
