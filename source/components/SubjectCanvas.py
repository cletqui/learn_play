# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from typing import Callable

from utils.MyWidgets import MyFrame, TitleLabel, PrimaryButton


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

        self.show_difficulty_callback = show_difficulty_callback

        self.column_number = 2
        for i in range(self.column_number):
            self.grid_columnconfigure(i, weight=1)

        self.row_number = 0
        for section in sections:
            self.row_number += self.add_section(section, self.row_number)

    def add_section(self, section: dict, row: int) -> int:
        """
        Add a section with buttons to the canvas.

        Args:
            section (dict): A dictionary representing a section with buttons.
            row (int): The current row in the grid.

        Returns:
            int: The updated row number after adding the section.
        """
        title = section.get("title", "")
        buttons = section.get("buttons", [])
        column = 0

        title_label = TitleLabel(
            self, text=title)
        title_label.grid(row=row, column=0, columnspan=self.column_number,
                         padx=10, pady=10, sticky=tk.NSEW)
        row += 1

        for button in buttons:
            button_label = button.get("label", "")
            game_type = button.get("game_type", None)

            if button_label:
                button = PrimaryButton(
                    self, text=button_label, command=lambda g=game_type: self.show_difficulty_callback(game_type=g))
                button.grid(row=row, column=column,
                            padx=10, pady=10, sticky=tk.NSEW)
                column += 1
                if column >= self.column_number:
                    column = 0
                    row += 1
        row += 1

        return row


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
                    {"label": "Son vers Nombre", "game_type": "sound-to-number"},
                    {"label": "Son vers Mot", "game_type": "sound-to-word"}
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
                        "game_type": "simple-syllable"},
                    {"label": "Son Simple : Mot",
                        "game_type": "simple-word"},
                    {"label": "Son Complexe : Syllabe",
                        "game_type": "complex-syllable"},
                    {"label": "Son Complexe : Mot",
                        "game_type": "complex-word"}
                ]
            }
        ]

        super().__init__(master, self.sections, show_difficulty_callback)
