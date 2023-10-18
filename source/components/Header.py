# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from PIL import ImageTk, Image

from source._constants import *


class BackButton(tk.Button):
    """
    A custom back button widget for the NavigationBar.

    Attributes:
        master (tk.Widget): The parent widget where the back button will be placed.
        callback (callable): The callback function to be executed when the button is clicked.
    """

    def __init__(self, master: tk.Widget, callback: callable):
        """
        Initialize the BackButton widget.

        Args:
            master (tk.Widget): The parent widget where the back button will be placed.
            callback (callable): The callback function to be executed when the button is clicked.
        """
        super().__init__(master, width=50)
        self.callback = callback
        self.back_image = ImageTk.PhotoImage(
            Image.open(ARROW_IMAGE_PATH).resize((40, 40)).rotate(180))

        if callback:
            self.config(image=self.back_image, command=callback)
            self.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        else:
            self.grid_remove()

    def update_callback(self) -> None:
        """
        Update the callback function and show/hide the button accordingly.
        """
        if self.callback:
            self.config(image=self.back_image, command=self.callback)
            self.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        else:
            self.grid_remove()


class NavigationBar(tk.Frame):
    """
    A custom navigation bar widget for your tkinter application.

    Attributes:
        master (tk.Tk): The master window or frame where the navigation bar will be placed.
        title_label (tk.Label): The label widget for displaying the title.
        back_button (BackButton): The custom back button widget.
    """

    def __init__(self, master: tk.Tk, title: str):
        """
        Initialize the NavigationBar widget.

        Args:
            master (tk.Tk): The master window or frame where the navigation bar will be placed.
            title (str): The initial title to display in the navigation bar.
        """
        super().__init__(master)

        # Configure grid columns to expand equally
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Create a label for the title
        self.title_label = tk.Label(self, text=title, font=(
            FONT_NAME, TITLE_FONT_SIZE, "underline"), anchor="center")
        self.title_label.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        # Create a button for the callback button
        self.back_button = BackButton(self, None)

    def update_callback(self, callback: callable) -> None:
        """
        Update the callback function and show/hide the back button accordingly.

        Args:
            callback (callable): The callback function to associate with the back button.
        """
        self.back_button.callback = callback
        self.back_button.update_callback()

    def update_title(self, title: str) -> None:
        """
        Update the title displayed in the navigation bar.

        Args:
            title (str): The new title to be displayed.
        """
        self.title_label["text"] = title
