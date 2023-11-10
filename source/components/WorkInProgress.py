# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from PIL import ImageTk, Image

from utils.MyWidgets import MyFrame, TextLabel
from _constants import TRAFFIC_CONE_IMAGE_PATH


class WorkInProgress(MyFrame):
    """
    A class representing a work in progress frame.

    Args:
        master: The master frame.

    Attributes:
        traffic_cone_image: The image of a traffic cone.
        traffic_cone_label: The label for the traffic cone image.

    """

    def __init__(self, master: MyFrame):
        """
        Initialize the WorkInProgress frame.

        Args:
            master: The master frame.

        """
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        self.traffic_cone_image = ImageTk.PhotoImage(
            Image.open(TRAFFIC_CONE_IMAGE_PATH).resize((80, 80)))

        self.traffic_cone_label = TextLabel(
            self, image=self.traffic_cone_image)
        self.traffic_cone_label.grid(
            row=0, column=0, padx=10, pady=20, sticky=tk.NSEW)
