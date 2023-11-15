# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main Application
"""

import tkinter as tk
import num2words

from _constants import (
    APP_TITLE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    FAVICON_PATH,
    SUBJECT_TITLE,
    MATHEMATICS_TITLE,
    SPELLING_TITLE,
    DIFFICULTY_TITLE,
    WORK_IN_PROGRESS_TITLE,
)
from components.header import NavigationBar
from components.main_canvas import MainCanvas
from components.subject_canvas import MathsCanvas, SpellingCanvas
from components.work_in_progress import WorkInProgress
from components.difficulty_canvas import DifficultyCanvas
from components.game_canvas import InputCanvas, CompareCanvas
from utils.my_widgets import MyFrame


class MainApplication(tk.Tk):
    """
    Represents the main application.

    The MainApplication class extends the tk.Tk class and provides the main functionality of the application.
    It initializes the main application window, sets up the navigation bar, and manages the main content frame.
    """

    def __init__(self):
        """
        Initialize the MainApplication.

        Initializes the main application window, sets up the navigation bar, and initializes the main content frame.

        Returns:
            None
        """

        super().__init__()

        self.title(APP_TITLE)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        # Make the window not resizable (to avoid dealing with resizing designs)
        self.resizable(False, False)
        self.iconphoto(False, tk.PhotoImage(file=FAVICON_PATH))

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)  # Header row
        self.grid_rowconfigure(1, weight=1)  # Main row

        # Create a nav bar to display title
        self.nav_bar = NavigationBar(self, APP_TITLE)
        self.nav_bar.grid(row=0, column=0, sticky=tk.NSEW)

        # Create a main frame to hold content
        self.main_frame = MyFrame(self)
        self.main_frame.grid(row=1, column=0, sticky=tk.NSEW)

        # Initialise the global variables
        self.subject = ""
        self.game_type = ""
        self.difficulty = ""

        # Initialize with
        self.show_main_canvas()

    def replace_canvas(self, canvas: tk.Frame, title: str, callback: callable) -> None:
        """
        Replace the main canvas.

        Args:
            canvas: The new canvas to replace the current main canvas.
            title: The new title for the navigation bar.
            callback: The new callback function for the navigation bar.

        Returns:
            None
        """

        self.main_frame.destroy()
        self.main_frame = canvas
        self.main_frame.grid(row=1, column=0, sticky=tk.NSEW)
        self.nav_bar.update_nav_bar(title, callback)

    def show_main_canvas(self) -> None:
        """
        Show the main canvas with subject selection.

        Clears the main frame and shows the main canvas.

        Returns:
            None
        """

        self.replace_canvas(MainCanvas(
            self, show_subject_canvas=self.show_subject_canvas), SUBJECT_TITLE, None)

    def show_subject_canvas(self, subject: str = None) -> None:
        """
        Show the subject canvas.

        Args:
            subject: The subject to show. Can be "mathematics" or "spelling".

        Returns:
            None
        """

        if subject:
            print(f'Subject "{subject}" selected.')
            self.subject = subject

        if self.subject == "mathematics":
            canvas = MathsCanvas(
                self, show_difficulty_callback=self.show_difficulty_canvas)
            header_title = MATHEMATICS_TITLE
        elif self.subject == "spelling":
            canvas = SpellingCanvas(
                self, show_difficulty_callback=self.show_difficulty_canvas)
            header_title = SPELLING_TITLE
        else:
            print(f'Subject "{subject}" not yet supported...')
            canvas = WorkInProgress(self)
            header_title = WORK_IN_PROGRESS_TITLE

        self.replace_canvas(canvas, header_title, self.show_main_canvas)

    def show_difficulty_canvas(self, game_type: str = None) -> None:
        """
        Show the difficulty canvas.

        Args:
            game_type: The game type to show. Can be "sound-to-number", "sound-to-word", or "compare".

        Returns:
            None
        """
        if game_type:
            print(f'Subject "{game_type}" selected.')
            self.game_type = game_type

        if game_type in {"sound-to-number", "sound-to-word", "compare"}:
            canvas = DifficultyCanvas(
                self, game_type=self.game_type, show_game_canvas=self.show_game_canvas)
            header_title = DIFFICULTY_TITLE
        else:
            print(f'Game type "{game_type}" not yet supported...')
            canvas = WorkInProgress(self)
            header_title = WORK_IN_PROGRESS_TITLE

        self.replace_canvas(canvas, header_title,
                            lambda: self.show_subject_canvas(self.subject))

    def show_game_canvas(self, game_type: str = None, difficulty: int = None) -> None:
        """
        Show the game canvas with a specific difficulty level.

        Clears the main frame and shows the game canvas with the specified difficulty level.

        Args:
            game_type: The game type to show. Can be "compare", "sound-to-number", or "sound-to-word".
            difficulty: The selected difficulty level.

        Returns:
            None
        """

        if difficulty:
            self.difficulty = difficulty
        if game_type:
            self.game_type = game_type

        print(
            f'Game type "{game_type}" in difficulty "{difficulty}" is selected.')

        if game_type == "sound-to-number":
            canvas = InputCanvas(self, self.difficulty,
                                 lambda input, number: int(input) == number)
            header_title = "Écoute et écris en chiffres"
        elif game_type == "sound-to-word":
            canvas = InputCanvas(self, self.difficulty, lambda input,
                                 number: input == num2words.num2words(number, lang="fr"))
            header_title = "Écoute et écris en mots"
        elif game_type == "compare":
            canvas = CompareCanvas(self, self.difficulty)
            header_title = "Compare les nombres"
        else:
            canvas = WorkInProgress(self)
            header_title = WORK_IN_PROGRESS_TITLE

        self.replace_canvas(canvas, header_title,
                            lambda: self.show_difficulty_canvas(game_type))
