#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals

from prompt_toolkit.token import Token
from prompt_toolkit.layout.controls import TokenListControl


class SelectControl(TokenListControl):
    selected_option_index = 0
    answered = False

    def __init__(self, choices, **kwargs):
        self.choices = choices
        super(SelectControl, self).__init__(
            self._get_choice_tokens, **kwargs)

    @property
    def choice_count(self):
        return len(self.choices)

    def _get_choice_tokens(self, cli):
        tokens = []

        def append(index, label):
            selected = (index == self.selected_option_index)

            def select_item(cli, mouse_event):
                # bind option with this index to mouse event
                self.selected_option_index = index
                self.answered = True
                cli.set_return_value(None)

            tokens.append(
                (Token.Selected if selected else Token,
                 ' > ' if selected else '   ')
            )

            if selected:
                tokens.append((Token.SetCursorPosition, ''))

            tokens.append(
                (Token.Selected if selected else Token,
                 '%-24s' % label, select_item)
            )
            tokens.append((Token, '\n'))

        # prepare the select choices
        for i, choice in enumerate(self.choices):
            append(i, choice)

        tokens.pop()  # Remove last newline.
        return tokens

    @property
    def selected(self):
        return self.choices[self.selected_option_index]
