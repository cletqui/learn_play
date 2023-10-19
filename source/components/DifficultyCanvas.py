# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from typing import Callable

from source._constants import FONT_NAME, TEXT_FONT_SIZE


class DifficultyCanvas(tk.Frame):
    def __init__(self, master: tk.Widget, game_type: str, show_game_canvas: Callable[[str, int], None]):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.difficulties = [10, 20, 50, 100, 1000, 10000, 100000, 1000000]

        row = 0
        column = 0

        for difficulty in self.difficulties:
            difficulty_button = tk.Button(
                self, text=f"0 - {difficulty}", font=(FONT_NAME, TEXT_FONT_SIZE))
            difficulty_button.grid(
                row=row, column=column, padx=10, pady=10, sticky=tk.NSEW)
            difficulty_button.config(
                command=lambda d=difficulty, g=game_type: show_game_canvas(game_type=g, difficulty=d))

            column += 1
            if column >= 3:
                column = 0
                row += 1
