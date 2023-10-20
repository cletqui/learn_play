# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from PIL import ImageTk, Image

from source.utils.MyWidgets import MyFrame, TextLabel
from source._constants import TRAFFIC_CONE_IMAGE_PATH


class WorkInProgress(MyFrame):
    """
    A canvas for selecting a subject (Mathematics or Spelling).

    Attributes:
        mathematics_button (tk.Button): Button for selecting Mathematics.
        spelling_button (tk.Button): Button for selecting Spelling.
    """

    def __init__(self, master: MyFrame):
        """
        Initialize the MainCanvas.

        Args:
            master (tk.Widget): The parent widget where the canvas will be placed.
        """
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        self.traffic_cone_image = ImageTk.PhotoImage(
            Image.open(TRAFFIC_CONE_IMAGE_PATH).resize((80, 80)))

        self.traffic_cone_label = TextLabel(
            self, image=self.traffic_cone_image)
        self.traffic_cone_label.grid(
            row=0, column=0, padx=10, pady=20, sticky=tk.NSEW)
