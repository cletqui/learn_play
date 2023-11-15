# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main Canvas
"""

import tkinter as tk
from typing import Callable
from PIL import ImageTk, Image

from _constants import (
    LIGHT_SHADE_COLOR,
    PRIMARY_COLOR,
    WHITE_COLOR,
    MATHEMATICS_TITLE,
    SPELLING_TITLE,
    MATHEMATICS_IMAGE_PATH,
    SPELLING_IMAGE_PATH,
)
from utils.my_widgets import MyFrame, MyButton


class MainCanvas(MyFrame):
    """
    A canvas for the main interface.

    Args:
        master: The parent widget where the canvas will be placed.
        show_subject_canvas: A callback function that takes a string argument and does not return anything.

    Returns:
        None
    """

    def __init__(self, master: MyFrame, show_subject_canvas: Callable[[str], None]):
        """
        Initialize the MainCanvas.

        Args:
            master (tk.Widget): The parent widget where the canvas will be placed.
            show_subject_canvas (Callable): The callback for showing the subject.
        """

        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        self.config(bg=LIGHT_SHADE_COLOR)

        self.maths_image = ImageTk.PhotoImage(
            Image.open(MATHEMATICS_IMAGE_PATH).resize((80, 80))
        )

        self.maths_button = MyButton(
            self,
            bg=PRIMARY_COLOR,
            fg=WHITE_COLOR,
            height=150,
            width=300,
            text=MATHEMATICS_TITLE,
            image=self.maths_image,
            command=lambda: show_subject_canvas("mathematics"),
        )
        self.maths_button.grid(
            row=0, column=0, padx=10, pady=20, sticky=tk.NS)

        self.spelling_image = ImageTk.PhotoImage(
            Image.open(SPELLING_IMAGE_PATH).resize((80, 80))
        )

        self.spelling_button = MyButton(
            self,
            bg=PRIMARY_COLOR,
            fg=WHITE_COLOR,
            height=150,
            width=300,
            text=SPELLING_TITLE,
            image=self.spelling_image,
            command=lambda: show_subject_canvas("spelling"),
        )
        self.spelling_button.grid(
            row=1, column=0, padx=10, pady=20, sticky=tk.NS)
