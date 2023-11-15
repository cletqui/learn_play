# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
My Widgets
"""

import tkinter as tk

from _constants import (
    FONT_NAME,
    TEXT_FONT_SIZE,
    LIGHT_SHADE_COLOR,
    DARK_SHADE_COLOR,
)


class MyFrame(tk.Frame):
    """
    Represents a custom frame widget.

    The MyFrame class extends the tk.Frame class and provides a custom frame widget with a specified background color.
    """

    def __init__(self, master, *args, bg=LIGHT_SHADE_COLOR,  **kwargs):
        """
        Initialize the MyFrame.

        Args:
            master: The master widget.
            bg: The background color of the frame.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """

        super().__init__(master, *args, bg=bg, **kwargs)


class MyButton(tk.Button):
    """
    Initialize the MyFrame.

    Args:
        master: The master widget.
        bg: The background color of the frame.
        *args: Additional positional arguments.
        **kwargs: Additional keyword arguments.
    """

    def __init__(
        self,
        master,
        *args,
        font=(FONT_NAME, TEXT_FONT_SIZE),
        highlightbackground=DARK_SHADE_COLOR,
        compound=tk.TOP,
        bg=LIGHT_SHADE_COLOR,
        fg=DARK_SHADE_COLOR,
        **kwargs
    ):
        """
        Initialize the MyButton.

        Args:
            master: The master widget.
            font: The font of the button.
            highlightbackground: The highlight background color of the button.
            compound: The compound style of the button.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """

        super().__init__(
            master,
            *args,
            font=font,
            compound=compound,
            highlightbackground=highlightbackground,
            bg=bg,
            fg=fg,
            **kwargs
        )


class MyLabel(tk.Label):
    """
    Represents a custom label widget.

    The MyLabel class extends the tk.Label class and provides a custom label widget with a specified font, anchor, background color, and foreground color.
    """

    def __init__(
        self,
        master,
        *args,
        font=(FONT_NAME, TEXT_FONT_SIZE),
        anchor="center",
        bg=LIGHT_SHADE_COLOR,
        fg=DARK_SHADE_COLOR,
        **kwargs
    ):
        """
        Initialize the MyLabel.

        Args:
            master: The master widget.
            font: The font of the label.
            anchor: The anchor position of the label.
            bg: The background color of the label.
            fg: The foreground color of the label.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """

        super().__init__(
            master, *args, font=font, anchor=anchor, bg=bg, fg=fg, **kwargs
        )
