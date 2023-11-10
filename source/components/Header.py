# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from PIL import ImageTk, Image
from typing import Callable

from utils.MyWidgets import InfoButton, HeaderLabel
from _constants import MAIN_COLOR, DARK_SHADE_COLOR, ARROW_IMAGE_PATH


class BackButton(InfoButton):
    """
    A class representing a back button.

    Args:
        master: The master button.
        callback: A callback function to be called when the button is clicked.

    Attributes:
        callback (Callable): The callback function for the button.
        back_image: The image for the back button.

    """

    def __init__(self, master: InfoButton, callback: Callable):
        """
        A class representing a back button.

        Args:
            master: The master button.
            callback: A callback function to be called when the button is clicked.

        Attributes:
            callback (Callable): The callback function for the button.
            back_image: The image for the back button.

        """
        super().__init__(master, width=50)
        self.callback = callback
        self.back_image = ImageTk.PhotoImage(
            Image.open(ARROW_IMAGE_PATH).resize((40, 40)).rotate(180))
        # TODO change image colors and rotate the arrow image

        # If a callback is defined show the button, otherwise remove it from the grid
        if callback:
            self.config(image=self.back_image, command=callback)
            self.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        else:
            self.grid_remove()

    def update_callback(self) -> None:
        """
        Update the callback function and show/hide the button accordingly.

        Returns:
            None

        """
        if self.callback:
            self.config(image=self.back_image, command=self.callback)
            self.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        else:
            self.grid_remove()


class NavigationBar(tk.Frame):
    """
    A class representing a navigation bar.

    Args:
        master: The master frame.
        title: The title of the navigation bar.

    Attributes:
        title_label: The label for the title.
        back_button: The button for the callback.

    """
    def __init__(self, master: tk.Frame, title: str):
        """
        Initialize the NavigationBar.

        Args:
            master: The master frame.
            title: The title of the navigation bar.

        """
        super().__init__(master)

        # Configure grid columns to expand equally
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.config(bg=MAIN_COLOR,
                    highlightbackground=DARK_SHADE_COLOR, highlightthickness=3)

        # Create a label for the title
        self.title_label = HeaderLabel(self, text=title)
        self.title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

        # Create a button for the callback button
        self.back_button = BackButton(self, None)

    def update_callback(self, callback: Callable) -> None:
        """
        Update the callback function for the back button.

        Args:
            callback: A callback function to be called when the back button is clicked.

        Returns:
            None

        """
        self.back_button.callback = callback
        self.back_button.update_callback()

    def update_title(self, title: str) -> None:
        """
        Update the title of the navigation bar.

        Args:
            title: The new title.

        Returns:
            None

        """
        self.title_label["text"] = title
