# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Subject Canvas
"""

import tkinter as tk
from typing import Callable
from PIL import ImageTk, Image

from _constants import (
    GREATER_EQUAL_IMAGE_PATH,
    SOUND_IMAGE_PATH,
    FONT_NAME,
    TITLE_FONT_SIZE,
    PRIMARY_COLOR,
    WHITE_COLOR,
)
from utils.my_widgets import MyFrame, MyLabel, MyButton


class SubjectSectionCanvas(MyFrame):
    """
    Represents a canvas for displaying a section of subjects.

    The SubjectSectionCanvas class extends the MyFrame class and provides a canvas for displaying a section of subjects.
    It displays a title label and buttons for each subject, allowing the user to select a subject and trigger a callback function.
    """

    def __init__(
        self,
        master: MyFrame,
        column_number: int,
        section: dict,
        show_difficulty_callback: Callable[[str], None],
    ):
        """
        Initialize the SubjectSectionCanvas.

        Args:
            master: The master widget.
            column_number: The number of columns to display the buttons.
            section: A dictionary containing the section details, including the title and buttons.
            show_difficulty_callback: A callback function to show the difficulty canvas for the selected subject.
        """

        super().__init__(master)

        self.column_number = column_number
        for i in range(self.column_number):
            self.grid_columnconfigure(i, weight=1)

        self.show_difficulty_callback = show_difficulty_callback

        self.title = section.get("title", "")
        self.buttons = section.get("buttons", [])

        self.create_title_label()

        row = 1
        column = 0

        for button in self.buttons:
            button_label = button.get("label", "")
            game_type = button.get("game_type", None)
            image_name = button.get("image", None)

            if button_label:
                button = MyButton(
                    self,
                    text=f"{button_label} ",
                    command=lambda g=game_type: self.show_difficulty_callback(
                        game_type=g
                    ),
                    bg=PRIMARY_COLOR,
                    fg=WHITE_COLOR
                )

                if image_name:
                    if image_name == "sound":
                        image = SOUND_IMAGE_PATH
                    elif image_name == "greater-equal":
                        image = GREATER_EQUAL_IMAGE_PATH

                    if image:
                        button_image = ImageTk.PhotoImage(
                            Image.open(image).resize((20, 20))
                        )
                        button.image = button_image
                        button.config(image=button_image, compound=tk.RIGHT)

                button.grid(row=row, column=column, padx=10,
                            pady=10, sticky=tk.NSEW)

                column += 1
                if column >= self.column_number:
                    column = 0
                    row += 1

    def create_title_label(self) -> None:
        """
        Creates a title label widget and adds it to the canvas.

        Args:
            self: The instance of the SubjectSectionCanvas.

        Returns:
            None
        """
        self.title_label = MyLabel(
            self, text=self.title, font=(FONT_NAME, TITLE_FONT_SIZE))
        self.title_label.grid(
            row=0, column=0, columnspan=self.column_number, padx=10, pady=10, sticky=tk.NSEW)


class SubjectCanvas(MyFrame):
    """
    A customizable canvas for subject-specific content.

    Attributes:
        master (tk.Widget): The parent widget where the canvas will be placed.
        sections (list[dict]): A list of dictionaries representing sections with buttons.
    """

    def __init__(
        self,
        master: MyFrame,
        sections: list[dict],
        show_difficulty_callback: Callable[[str], None],
    ):
        """
        Initialize the SubjectCanvas.

        Args:
            master (tk.Widget): The parent widget where the canvas will be placed.
            sections (list[dict]): A list of dictionaries representing sections with buttons.
        """

        super().__init__(master)
        # TODO add images to understand the subjects

        self.grid_columnconfigure(0, weight=1)

        self.show_difficulty_callback = show_difficulty_callback

        for row_number, section in enumerate(sections):
            self.add_section(row_number, section)

    def add_section(self, row_number: int, section: dict) -> None:
        """
        Add a section with buttons to the canvas.

        Args:
            section (dict): A dictionary representing a section with buttons.
            row (int): The current row in the grid.

        Returns:
            int: The updated row number after adding the section.
        """

        self.section = SubjectSectionCanvas(
            self,
            column_number=2,
            section=section,
            show_difficulty_callback=self.show_difficulty_callback,
        )
        self.section.grid(row=row_number, column=0,
                          padx=10, pady=10, sticky=tk.NSEW)


class MathsCanvas(SubjectCanvas):
    """
    A canvas for math exercises.

    Args:
        master: The master SubjectCanvas object.
        show_difficulty_callback: A callback function that takes a string argument and does not return anything.

    Returns:
        None
    """

    def __init__(
        self, master: SubjectCanvas, show_difficulty_callback: Callable[[str], None]
    ):
        """
        Initializes a SubjectCanvas object.

        Args:
            master: The master SubjectCanvas object.
            show_difficulty_callback: A callback function that takes a string argument and does not return anything.

        Returns:
            None
        """

        self.sections = [
            {
                "title": "Écriture du nombre",
                "buttons": [
                    {
                        "label": "Son vers Nombre",
                        "game_type": "sound-to-number",
                        "image": "sound",
                    },
                    {
                        "label": "Son vers Mot",
                        "game_type": "sound-to-word",
                        "image": "sound",
                    },
                ],
            },
            {
                "title": "Comparaison",
                "buttons": [
                    {
                        "label": "Comparer",
                        "game_type": "compare",
                        "image": "greater-equal",
                    },
                ],
            },
            {
                "title": "Dénombrement",
                "buttons": [
                    {"label": "Compter", "game_type": "count"},
                ],
            },
        ]

        super().__init__(master, self.sections, show_difficulty_callback)


class SpellingCanvas(SubjectCanvas):
    """
    A canvas for spelling exercises.

    Args:
        master: The master SubjectCanvas object.
        show_difficulty_callback: A callback function that takes a string argument and does not return anything.

    Returns:
        None
    """

    def __init__(
        self, master: SubjectCanvas, show_difficulty_callback: Callable[[str], None]
    ):
        """
        Initializes a SpellingCanvas object.

        Args:
            master: The master SubjectCanvas object.
            show_difficulty_callback: A callback function that takes a string argument and does not return anything.

        Returns:
            None
        """
        self.sections = [
            {
                "title": "Encodage",
                "buttons": [
                    {
                        "label": "Son Simple : Syllabe",
                        "game_type": "simple-syllable",
                        "image": "sound",
                    },
                    {
                        "label": "Son Simple : Mot",
                        "game_type": "simple-word",
                        "image": "sound",
                    },
                    {
                        "label": "Son Complexe : Syllabe",
                        "game_type": "complex-syllable",
                        "image": "sound",
                    },
                    {
                        "label": "Son Complexe : Mot",
                        "game_type": "complex-word",
                        "image": "sound",
                    },
                ],
            }
        ]

        super().__init__(master, self.sections, show_difficulty_callback)
