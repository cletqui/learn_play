# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Difficulty Canvas
"""

import tkinter as tk
from typing import Callable

from utils.my_widgets import MyFrame, MyButton
from _constants import PRIMARY_COLOR, WHITE_COLOR


class DifficultyCanvas(MyFrame):
    """
    Represents a canvas for selecting difficulty levels.

    The DifficultyCanvas class extends the MyFrame class and provides a canvas for selecting difficulty levels.
    It displays buttons for different difficulty levels and allows the user to choose a difficulty level for a specific game type.
    """

    def __init__(
        self,
        master: MyFrame,
        game_type: str,
        show_game_canvas: Callable[[str, int], None],
    ):
        """
        Initialize the DifficultyCanvas.

        Args:
            master: The master widget.
            game_type: The type of the game.
            show_game_canvas: A callback function to show the game canvas with the selected game type and difficulty level.
        """

        super().__init__(master)
        # TODO implement other types of level/difficulty canvas

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.difficulties = [10, 20, 50, 100, 1000, 10000, 100000, 1000000]

        row = 0
        column = 0

        for index, difficulty in enumerate(self.difficulties):
            row, column = divmod(index, 3)
            difficulty_button = MyButton(
                self, text=f"0 - {difficulty}", bg=PRIMARY_COLOR, fg=WHITE_COLOR)
            difficulty_button.grid(
                row=row, column=column, padx=10, pady=10, sticky=tk.NSEW
            )
            difficulty_button.config(
                command=lambda d=difficulty: show_game_canvas(
                    game_type=game_type, difficulty=d
                )
            )
