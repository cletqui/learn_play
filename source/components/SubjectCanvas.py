# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from PIL import ImageTk, Image
from typing import Callable

from utils.MyWidgets import MyFrame, TitleLabel, PrimaryButton
from _constants import GREATER_EQUAL_IMAGE_PATH, SOUND_IMAGE_PATH


class SubjectSectionCanvas(MyFrame):
    """
    A class representing a canvas for a subject section.

    Args:
        master: The master frame.
        column_number: The number of columns in the canvas.
        section: A dictionary representing the section.
        show_difficulty_callback: A callback function to show the difficulty.

    Attributes:
        column_number (int): The number of columns in the canvas.
        title (str): The title of the section.
        buttons (list): The list of buttons in the section.

    """

    def __init__(self, master: MyFrame, column_number: int, section: dict, show_difficulty_callback: Callable[[str], None]):
        """
        Initialize the SubjectSectionCanvas.

        Args:
            master: The master frame.
            column_number: The number of columns in the canvas.
            section: A dictionary representing the section.
            show_difficulty_callback: A callback function to show the difficulty.

        """
        super().__init__(master)

        self.column_number = column_number
        for i in range(self.column_number):
            self.grid_columnconfigure(i, weight=1)

        self.show_difficulty_callback = show_difficulty_callback

        self.title = section.get("title", "")
        self.buttons = section.get("buttons", [])


        self.title_label = TitleLabel(
            self, text=self.title)
        self.title_label.grid(row=0, column=0, columnspan=self.column_number,
                              padx=10, pady=10, sticky=tk.NSEW)
        
        row = 1
        column = 0

        for button in self.buttons:
            button_label = button.get("label", "")
            game_type = button.get("game_type", None)
            image_name = button.get("image", None)

            if button_label:
                button = PrimaryButton(
                    self, text=button_label, command=lambda g=game_type: self.show_difficulty_callback(game_type=g))

                if image_name:
                    if image_name == "sound":
                        image = SOUND_IMAGE_PATH
                    elif image_name == "greater-equal":
                        image = GREATER_EQUAL_IMAGE_PATH

                    if image:
                        button_image = ImageTk.PhotoImage(
                            Image.open(image).resize((20, 20)))
                        button.image = button_image
                        button.config(image=button_image, compound=tk.RIGHT)

                button.grid(row=row, column=column, padx=10,
                                 pady=10, sticky=tk.NSEW)

                column += 1
                if column >= self.column_number:
                    column = 0
                    row += 1
        
        


class SubjectCanvas(MyFrame):
    """
    A customizable canvas for subject-specific content.

    Attributes:
        master (tk.Widget): The parent widget where the canvas will be placed.
        sections (list[dict]): A list of dictionaries representing sections with buttons.
    """

    def __init__(self, master: MyFrame, sections: list[dict], show_difficulty_callback: Callable[[str], None]):
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
            self, column_number=2, section=section, show_difficulty_callback=self.show_difficulty_callback)
        self.section.grid(row=row_number, column=0,
                          padx=10, pady=10, sticky=tk.NSEW)


class MathsCanvas(SubjectCanvas):
    """
    A customizable canvas for mathematics content.

    Attributes:
        master (tk.Widget): The parent widget where the canvas will be placed.
        sound_number_callback (Callable): The callback for the "Son vers Nombre" button.
        sound_word_callback (Callable): The callback for the "Son vers Mot" button.
        count_callback (Callable): The callback for the "Compter" button.
    """

    def __init__(self, master: SubjectCanvas, show_difficulty_callback: Callable[[str], None]):
        self.sections = [
            {
                "title": "Écriture du nombre",
                "buttons": [
                    {"label": "Son vers Nombre",
                        "game_type": "sound-to-number", "image": "sound"},
                    {"label": "Son vers Mot",
                        "game_type": "sound-to-word", "image": "sound"}
                ]
            },
            {
                "title": "Comparaison",
                "buttons": [
                    {"label": "Comparer", "game_type": "compare",
                        "image": "greater-equal"},
                ]
            },
            {
                "title": "Dénombrement",
                "buttons": [
                    {"label": "Compter", "game_type": "count"},
                ]
            }
        ]

        super().__init__(master, self.sections, show_difficulty_callback)


class SpellingCanvas(SubjectCanvas):
    """
    A customizable canvas for spelling content.

    Attributes:
        master (tk.Widget): The parent widget where the canvas will be placed.
        simple_syllable_callback (Callable): The callback for the "Son Simple : Syllabe" button.
        simple_word_callback (Callable): The callback for the "Son Simple : Mot" button.
        complex_syllable_callback (Callable): The callback for the "Son Complexe : Syllabe" button.
        complex_word_callback (Callable): The callback for the "Son Complexe : Mot" button.
    """

    def __init__(self, master: SubjectCanvas, show_difficulty_callback: Callable[[str], None]):
        self.sections = [
            {
                "title": "Encodage",
                "buttons": [
                    {"label": "Son Simple : Syllabe",
                        "game_type": "simple-syllable", "image": "sound"},
                    {"label": "Son Simple : Mot",
                        "game_type": "simple-word", "image": "sound"},
                    {"label": "Son Complexe : Syllabe",
                        "game_type": "complex-syllable", "image": "sound"},
                    {"label": "Son Complexe : Mot",
                        "game_type": "complex-word", "image": "sound"}
                ]
            }
        ]

        super().__init__(master, self.sections, show_difficulty_callback)
