# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Work In Progress Canvas
"""

import tkinter as tk
from PIL import ImageTk, Image

from _constants import TRAFFIC_CONE_IMAGE_PATH, FONT_NAME, TEXT_FONT_SIZE
from utils.my_widgets import MyFrame, MyLabel


class WorkInProgress(MyFrame):
    """
    Represents a work in progress widget.

    The WorkInProgress class extends the MyFrame class and provides a widget to indicate that the feature or functionality is still in progress.
    It displays an image of a traffic cone to visually represent the work in progress state.
    """

    def __init__(self, master: MyFrame):
        """
        Initialize the WorkInProgress.

        Args:
            master: The master widget.
        """
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        self.traffic_cone_image = ImageTk.PhotoImage(
            Image.open(TRAFFIC_CONE_IMAGE_PATH).resize((80, 80))
        )

        self.traffic_cone_label = MyLabel(
            self, image=self.traffic_cone_image, font=(FONT_NAME, TEXT_FONT_SIZE))
        self.traffic_cone_label.grid(
            row=0, column=0, padx=10, pady=20, sticky=tk.NSEW)
