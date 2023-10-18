# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from PIL import ImageTk, Image

from source.components.Header import NavigationBar
from source.components.SubjectCanvas import MathsCanvas, SpellingCanvas
from source.components.DifficultyCanvas import DifficultyCanvas
from source.components.TypingCanvas import TypingCanvas
from source._constants import *


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
        self.resizable(0, 0)
        self.iconphoto(False, tk.PhotoImage(file=FAVICON_PATH))

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=11)

        # Create a nav bar to display title
        self.nav_bar = NavigationBar(self, APP_TITLE)
        self.nav_bar.grid(row=0, column=0, sticky=tk.NSEW)

        # Create a main frame to hold content
        self.main_frame = tk.Frame(self)

        # Initialize with
        self.show_main_canvas()

    def show_main_canvas(self) -> None:
        """
        Show the main canvas with subject selection.

        Clears the main frame and shows the main canvas.
        """
        self.clear_main_frame()

        # Create the new main frame from main canvas
        self.main_frame = MainCanvas(
            self,  mathematics_callback=self.show_mathematics_canvas, spelling_callback=self.show_spelling_canvas)
        self.main_frame.grid(row=1, column=0, sticky=tk.NSEW)

        # Update the title for the navigation bar
        self.nav_bar.update_title(SUBJECT_TITLE)
        # Update the callback for the navigation bar
        self.nav_bar.update_callback(None)

    def show_mathematics_canvas(self) -> None:
        """
        Show the mathematics canvas.

        Clears the main frame and shows the mathematics canvas.
        """
        self.clear_main_frame()

        # Create the new main frame from main canvas
        self.main_frame = MathsCanvas(
            self, sound_number_callback=self.show_difficulty_canvas, sound_word_callback=self.show_difficulty_canvas, count_callback=self.show_difficulty_canvas)
        self.main_frame.grid(row=1, column=0, sticky=tk.NSEW)

        # Update the title for the navigation bar
        self.nav_bar.update_title(MATHEMATICS_TITLE)
        # Update the callback for the navigation bar
        self.nav_bar.update_callback(self.show_main_canvas)

    def show_spelling_canvas(self) -> None:
        """
        Show the spelling canvas.

        Clears the main frame and shows the spelling canvas.
        """
        self.clear_main_frame()

        # Create the new main frame from main canvas
        self.main_frame = SpellingCanvas(
            self, simple_syllable_callback=self.show_difficulty_canvas, simple_word_callback=self.show_difficulty_canvas, complex_syllable_callback=self.show_difficulty_canvas, complex_word_callback=self.show_difficulty_canvas)
        self.main_frame.grid(row=1, column=0, sticky=tk.NSEW)

        # Update the title for the navigation bar
        self.nav_bar.update_title(SPELLING_TITLE)
        # Update the callback for the navigation bar
        self.nav_bar.update_callback(self.show_main_canvas)

    def show_difficulty_canvas(self) -> None:
        """
        Show the difficulty canvas.

        Clears the main frame and shows the difficulty canvas.
        """
        self.clear_main_frame()

        # Create the new main frame from difficulty canvas
        self.main_frame = DifficultyCanvas(
            self, difficulty_callback=self.show_typing_canvas)
        self.main_frame.grid(row=1, column=0, sticky=tk.NSEW)

        # Update the title for the navigation bar
        self.nav_bar.update_title(DIFFICULTY_TITLE)
        # Update the callback for the navigation bar
        self.nav_bar.update_callback(self.show_main_canvas)

    def show_typing_canvas(self, difficulty: int) -> None:
        """
        Show the typing canvas with a specific difficulty level.

        Clears the main frame and shows the typing canvas with the specified difficulty level.

        Args:
            difficulty (int): The selected difficulty level.
        """
        self.clear_main_frame()

        # Create the new main frame from difficulty canvas
        self.main_frame = TypingCanvas(self, difficulty)
        self.main_frame.grid(row=1, column=0, sticky=tk.NSEW)

        # Update the title for the navigation bar
        self.nav_bar.update_title(
            f"Écoute et écris en chiffres (entre 0 et {difficulty})")
        # Update the callback for the navigation bar
        self.nav_bar.update_callback(self.show_difficulty_canvas)

    def clear_main_frame(self) -> None:
        """Clear the main frame by destroying its content."""
        self.main_frame.destroy()


class MainCanvas(tk.Frame):
    """
    A canvas for selecting a subject (Mathematics or Spelling).

    Attributes:
        mathematics_button (tk.Button): Button for selecting Mathematics.
        spelling_button (tk.Button): Button for selecting Spelling.
    """

    def __init__(self, master: tk.Widget, mathematics_callback: callable, spelling_callback: callable):
        """
        Initialize the MainCanvas.

        Args:
            master (tk.Widget): The parent widget where the canvas will be placed.
            mathematics_callback (callable): The callback for selecting Mathematics.
            spelling_callback (callable): The callback for selecting Spelling.
        """
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        self.maths_image = ImageTk.PhotoImage(
            Image.open(MATHEMATICS_IMAGE_PATH).resize((80, 80)))
        self.spelling_image = ImageTk.PhotoImage(
            Image.open(SPELLING_IMAGE_PATH).resize((80, 80)))

        self.sound_letter_button = tk.Button(
            self, height=150, width=300, text=MATHEMATICS_TITLE, font=(FONT_NAME, TITLE_FONT_SIZE), image=self.maths_image, compound=tk.TOP, command=mathematics_callback)
        self.sound_letter_button.grid(
            row=0, column=0, padx=10, pady=20, sticky=tk.NS)

        self.sound_number_button = tk.Button(
            self, height=150, width=300, text=SPELLING_TITLE, font=(FONT_NAME, TITLE_FONT_SIZE), image=self.spelling_image, compound=tk.TOP, command=spelling_callback)
        self.sound_number_button.grid(
            row=1, column=0, padx=10, pady=20, sticky=tk.NS)
