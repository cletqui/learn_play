# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

from source._constants import *


class SubjectCanvas(tk.Frame):
    """
    A customizable canvas for subject-specific content.

    Attributes:
        master (tk.Widget): The parent widget where the canvas will be placed.
        sections (list[dict]): A list of dictionaries representing sections with buttons.
    """

    def __init__(self, master: tk.Widget, sections: list[dict]):
        """
        Initialize the SubjectCanvas.

        Args:
            master (tk.Widget): The parent widget where the canvas will be placed.
            sections (list[dict]): A list of dictionaries representing sections with buttons.
        """
        super().__init__(master)

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

        title_label = tk.Label(
            self, text=title, font=(FONT_NAME, TITLE_FONT_SIZE))
        title_label.grid(row=row, column=0, columnspan=self.column_number,
                         padx=10, pady=10, sticky=tk.NSEW)
        row += 1

        for button in buttons:
            button_label = button.get("label", "")
            button_callback = button.get("callback", None)

            if button_label:
                button = tk.Button(self, text=button_label, font=(
                    FONT_NAME, TEXT_FONT_SIZE), command=button_callback)
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
        sound_number_callback (callable): The callback for the "Son vers Nombre" button.
        sound_word_callback (callable): The callback for the "Son vers Mot" button.
        count_callback (callable): The callback for the "Compter" button.
    """

    def __init__(self, master: tk.Widget, sound_number_callback: callable, sound_word_callback: callable, count_callback: callable):
        self.sections = [
            {
                "title": "Écriture du nombre",
                "buttons": [
                    {"label": "Son vers Nombre", "callback": sound_number_callback},
                    {"label": "Son vers Mot", "callback": sound_word_callback}
                ]
            },
            {
                "title": "Dénombrement",
                "buttons": [
                    {"label": "Compter", "callback": count_callback},
                ]
            }
        ]

        super().__init__(master, self.sections)


class SpellingCanvas(SubjectCanvas):
    """
    A customizable canvas for spelling content.

    Attributes:
        master (tk.Widget): The parent widget where the canvas will be placed.
        simple_syllable_callback (callable): The callback for the "Son Simple : Syllabe" button.
        simple_word_callback (callable): The callback for the "Son Simple : Mot" button.
        complex_syllable_callback (callable): The callback for the "Son Complexe : Syllabe" button.
        complex_word_callback (callable): The callback for the "Son Complexe : Mot" button.
    """

    def __init__(self, master: tk.Widget, simple_syllable_callback: callable, simple_word_callback: callable, complex_syllable_callback: callable, complex_word_callback: callable):
        self.sections = [
            {
                "title": "Encodage",
                "buttons": [
                    {"label": "Son Simple : Syllabe",
                        "callback": simple_syllable_callback},
                    {"label": "Son Simple : Mot",
                        "callback": simple_word_callback},
                    {"label": "Son Complexe : Syllabe",
                        "callback": complex_syllable_callback},
                    {"label": "Son Complexe : Mot",
                        "callback": complex_word_callback}
                ]
            }
        ]

        super().__init__(master, self.sections)
