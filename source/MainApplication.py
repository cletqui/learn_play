# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

from components.Header import NavigationBar
from components.MainCanvas import MainCanvas
from components.SubjectCanvas import MathsCanvas, SpellingCanvas
from components.DifficultyCanvas import DifficultyCanvas
from components.GameCanvas import TypingNumbersCanvas, TypingWordsCanvas, CompareCanvas
from components.WorkInProgress import WorkInProgress
from utils.MyWidgets import MyFrame
from _constants import APP_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, FAVICON_PATH, SUBJECT_TITLE, MATHEMATICS_TITLE, SPELLING_TITLE, DIFFICULTY_TITLE, WORK_IN_PROGRESS_TITLE


class MainApplication(tk.Tk):
    """
    Main application class for your tkinter application.

    Attributes:
        nav_bar (NavigationBar): The navigation bar widget.
        main_frame (tk.Frame): The main content frame.
    """

    def __init__(self):
        """
        Initialize the MainApplication.

        Initializes the main application window, sets up the navigation bar, and initializes the main content frame.
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
        self.add_canvas(MyFrame(self))

        # Initialize with
        self.show_main_canvas()

    def show_main_canvas(self) -> None:
        """
        Show the main canvas with subject selection.

        Clears the main frame and shows the main canvas.
        """
        self.clear_main_frame()

        # Create the new main frame from main canvas
        self.add_canvas(MainCanvas(
            self, show_subject_canvas=self.show_subject_canvas))

        # Update the title for the navigation bar
        self.nav_bar.update_title(SUBJECT_TITLE)
        # Update the callback for the navigation bar
        self.nav_bar.update_callback(None)

    def show_subject_canvas(self, subject: str = None) -> None:
        """
        Show the subject canvas.

        Args:
            subject (str): "mathematics" or "spelling".
        """
        self.clear_main_frame()

        # If subject is specified, use subject to show the corresponding canvas, otherwise use self.subject
        if subject:
            print(f"Subject \"{subject}\" selected.")
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
            print(f"Subject \"{subject}\" not yet supported...")
            canvas = WorkInProgress(self)
            header_title = WORK_IN_PROGRESS_TITLE

        # Create the new main frame from main canvas
        self.add_canvas(canvas)

        # Update the title for the navigation bar
        self.nav_bar.update_title(header_title)
        # Update the callback for the navigation bar
        self.nav_bar.update_callback(self.show_main_canvas)

    def show_difficulty_canvas(self, game_type: str = None) -> None:
        """
        Show the difficulty canvas.

        Clears the main frame and shows the difficulty canvas.
        """
        self.clear_main_frame()

        if game_type:
            print(f"Subject \"{game_type}\" selected.")
            self.game_type = game_type

        if game_type in {"sound-to-number", "sound-to-word", "compare"}:
            canvas = DifficultyCanvas(
                self, game_type=self.game_type, show_game_canvas=self.show_game_canvas)
            header_title = DIFFICULTY_TITLE
        else:
            print(f"Game type \"{game_type}\" not yet supported...")
            canvas = WorkInProgress(self)
            header_title = WORK_IN_PROGRESS_TITLE

        # Create the new main frame from difficulty canvas
        self.add_canvas(canvas)

        # Update the title for the navigation bar
        self.nav_bar.update_title(header_title)
        # Update the callback for the navigation bar
        self.nav_bar.update_callback(self.show_subject_canvas)

    def show_game_canvas(self, game_type: str = None, difficulty: int = None) -> None:
        """
        Show the typing canvas with a specific difficulty level.

        Clears the main frame and shows the typing canvas with the specified difficulty level.

        Args:
            difficulty (int): The selected difficulty level.
        """
        self.clear_main_frame()

        if difficulty:
            self.difficulty = difficulty

        if game_type:
            self.game_type = game_type

        print(f"Game type \"{game_type}\" in difficulty \"{difficulty}\" is selected.")

        # Select the new main frame
        if game_type == "compare":
            canvas == CompareCanvas(self, self.difficulty)
            header_title = "Compare les nombres"
        elif game_type == "sound-to-number":
            canvas = TypingNumbersCanvas(self, self.difficulty)
            header_title = "Écoute et écris en chiffres"
        elif game_type == "sound-to-word":
            canvas = TypingWordsCanvas(self, self.difficulty)
            header_title = "Écoute et écris en mots"
        else:
            canvas = WorkInProgress(self)
            header_title = WORK_IN_PROGRESS_TITLE

        # Create the new main frame from difficulty canvas
        self.add_canvas(canvas)

        # Update the title for the navigation bar
        self.nav_bar.update_title(header_title)
        # Update the callback for the navigation bar
        self.nav_bar.update_callback(
            lambda g=game_type: self.show_difficulty_canvas(game_type=g))

    def add_canvas(self, Canvas: tk.Widget) -> None:
        """
        Add Canvas to main frame

        Args:
            Canvas (tk.Widget): The Canvas to add to the main frame
        """
        self.main_frame = Canvas
        self.main_frame.grid(row=1, column=0, sticky=tk.NSEW)

    def clear_main_frame(self) -> None:
        """Clear the main frame by destroying its content.
        """
        self.main_frame.destroy()
