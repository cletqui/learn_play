# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Header
"""

import tkinter as tk
from typing import Callable
from PIL import ImageTk, Image

from _constants import (
    MAIN_COLOR,
    WHITE_COLOR,
    DARK_SHADE_COLOR,
    ARROW_IMAGE_PATH,
    FONT_NAME,
    TITLE_FONT_SIZE,
    INFO_COLOR
)
from utils.my_widgets import MyButton, MyLabel


class BackButton(MyButton):
    """
    Represents a back button widget.

    The BackButton class extends the InfoButton class and provides a back button widget with a specified callback function.
    It displays an arrow image and allows the user to navigate back to a previous screen or perform a specific action when clicked.
    """

    def __init__(self, master: MyButton, callback: Callable):
        """
        Initialize the BackButton.

        Args:
            master: The master widget.
            callback: The callback function to be executed when the button is clicked.
        """

        super().__init__(master, bg=INFO_COLOR, fg=WHITE_COLOR, width=50)

        self.callback = callback
        self.back_image = ImageTk.PhotoImage(
            Image.open(ARROW_IMAGE_PATH).resize((40, 40)).rotate(180)
        )
        # TODO change image colors and rotate the arrow image

        self.update_callback()

    def update_callback(self) -> None:
        """
        Update the callback function of the BackButton.

        If a callback is defined, the button is shown and configured with the updated callback.
        If no callback is defined, the button is removed from the grid.
        """

        if self.callback:
            self.config(image=self.back_image, command=self.callback)
            self.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        else:
            self.grid_remove()


class NavigationBar(tk.Frame):
    """
    Represents a navigation bar widget.

    The NavigationBar class extends the tk.Frame class and provides a navigation bar widget with a title label and a back button.
    It allows updating the callback function of the back button and the title text.
    """

    def __init__(self, master: tk.Frame, title: str):
        """
        Initialize the NavigationBar.

        Args:
            master: The master widget.
            title: The title of the navigation bar.
        """

        super().__init__(master)

        # Configure grid columns to expand equally
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.config(
            bg=MAIN_COLOR, highlightbackground=DARK_SHADE_COLOR, highlightthickness=3
        )

        # Create a label for the title
        self.title_label = MyLabel(self, text=title, font=(
            FONT_NAME, TITLE_FONT_SIZE, "bold"), bg=MAIN_COLOR, fg=WHITE_COLOR)
        self.title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

        # Create a button for the callback button
        self.back_button = BackButton(self, None)

    def update_nav_bar(self, title: str, callback: Callable) -> None:
        """
        Update the navigation bar.

        Args:
            title: The new title for the navigation bar.
            callback: The new callback function for the navigation bar.

        Returns:
            None
        """
        self.title_label["text"] = title
        self.back_button.callback = callback
        self.back_button.update_callback()
