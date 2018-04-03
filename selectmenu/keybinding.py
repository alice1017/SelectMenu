#!/usr/bin/env python
# coding: utf-8

from prompt_toolkit.keys import Keys
from prompt_toolkit.key_binding.manager import KeyBindingManager


def set_key_binding(cntrllr):

    manager = KeyBindingManager.for_prompt()
    registry = manager.registry

    @registry.add_binding(Keys.ControlQ, eager=True)
    @registry.add_binding(Keys.ControlC, eager=True)
    def _(event):

        event.cli.set_return_value(None)

    @registry.add_binding(Keys.Down, eager=True)
    @registry.add_binding(Keys.ControlN, eager=True)
    def move_cursor_down(event):

        cntrllr.selected_option_index = (
            (cntrllr.selected_option_index + 1) % cntrllr.choice_count)

    @registry.add_binding(Keys.Up, eager=True)
    @registry.add_binding(Keys.ControlP, eager=True)
    def move_cursor_up(event):

        cntrllr.selected_option_index = (
            (cntrllr.selected_option_index - 1) % cntrllr.choice_count)

    @registry.add_binding(Keys.Enter, eager=True)
    def set_answer(event):
        cntrllr.answered = True
        event.cli.set_return_value(None)

    return registry
