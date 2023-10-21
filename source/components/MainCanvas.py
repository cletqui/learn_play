# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from PIL import ImageTk, Image
from typing import Callable

from utils.MyWidgets import MyFrame, PrimaryButton
from _constants import LIGHT_SHADE_COLOR, MATHEMATICS_TITLE, SPELLING_TITLE, MATHEMATICS_IMAGE_PATH, SPELLING_IMAGE_PATH


class MainCanvas(MyFrame):
    """
    A canvas for selecting a subject (Mathematics or Spelling).

    Attributes:
        mathematics_button (tk.Button): Button for selecting Mathematics.
        spelling_button (tk.Button): Button for selecting Spelling.
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
            Image.open(MATHEMATICS_IMAGE_PATH).resize((80, 80)))
        self.spelling_image = ImageTk.PhotoImage(
            Image.open(SPELLING_IMAGE_PATH).resize((80, 80)))

        self.sound_letter_button = PrimaryButton(
            self, height=150, width=300, text=MATHEMATICS_TITLE, image=self.maths_image, command=lambda: show_subject_canvas("mathematics"))
        self.sound_letter_button.grid(
            row=0, column=0, padx=10, pady=20, sticky=tk.NS)

        self.sound_number_button = PrimaryButton(
            self, height=150, width=300, text=SPELLING_TITLE, image=self.spelling_image, command=lambda: show_subject_canvas("spelling"))
        self.sound_number_button.grid(
            row=1, column=0, padx=10, pady=20, sticky=tk.NS)
