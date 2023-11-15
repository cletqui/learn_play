# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Game Canvas
"""

import tkinter as tk
import random
import os
from typing import Callable, Tuple
from PIL import ImageTk, Image
from gtts import gTTS
import playsound
import pygame


from _constants import (
    FONT_NAME,
    TEXT_FONT_SIZE,
    TITLE_FONT_SIZE,
    RANDOM_NUMBER_SOUND_PATH,
    SOUND_IMAGE_PATH,
    MAGNIFYING_GLASS_IMAGE_PATH,
    CHECK_IMAGE_PATH,
    REFRESH_IMAGE_PATH,
    WARNING_IMAGE_PATH,
    PRIMARY_COLOR,
    MAIN_COLOR,
    LIGHT_SHADE_COLOR,
    WHITE_COLOR,
    QUESTION_MARK_IMAGE_PATH,
    EQUAL_IMAGE_PTH,
    GREATER_IMAGE_PTH,
    LOWER_IMAGE_PTH,
)
from utils.my_widgets import MyFrame, MyButton, MyLabel


class InputCanvas(MyFrame):
    """
    Represents a canvas for inputting numbers.

    The InputCanvas class extends the MyFrame class and provides a canvas for inputting numbers.
    It includes features such as listening to the number, checking the input, and displaying the result.
    """

    def __init__(
        self, master: MyFrame, difficulty: int, validate: Callable[[int, int], bool]
    ):
        """
        Initialize the InputCanvas.

        Args:
            master: The master widget.
            difficulty: The difficulty level of the game.
            validate: A callback function to validate the user input against the generated number.
        """

        super().__init__(master)
        # TODO factorize the default games into general classes

        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=1)

        self.difficulty = difficulty
        self.validate = validate

        self.number = None
        self.generate_random_number()

        self.sound_path = RANDOM_NUMBER_SOUND_PATH

        self.listen_image = ImageTk.PhotoImage(
            Image.open(SOUND_IMAGE_PATH).resize((70, 70))
        )
        self.magnifying_glass_image = ImageTk.PhotoImage(
            Image.open(MAGNIFYING_GLASS_IMAGE_PATH).resize((50, 50))
        )
        self.check_image = ImageTk.PhotoImage(
            Image.open(CHECK_IMAGE_PATH).resize((50, 50))
        )
        self.refresh_image = ImageTk.PhotoImage(
            Image.open(REFRESH_IMAGE_PATH).resize((50, 50))
        )
        self.warning_image = ImageTk.PhotoImage(
            Image.open(WARNING_IMAGE_PATH).resize((50, 50))
        )

        # Create a label with centered text
        self.listen_button = MyButton(
            self, text="Réécouter", image=self.listen_image, bg=PRIMARY_COLOR, fg=WHITE_COLOR
        )
        self.listen_button.grid(row=0, column=0, columnspan=2, pady=10)
        self.listen_button.config(command=self.listen_number)
        self.listen_button.bind("<space>", self.listen_number)

        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(
            self,
            textvariable=self.input_var,
            font=(FONT_NAME, TEXT_FONT_SIZE),
            highlightthickness=2,
        )
        self.input_entry.grid(row=1, column=0, padx=10,
                              pady=10, sticky=tk.NSEW)

        self.check_button = MyButton(
            self,
            width=120,
            text="   Vérifier",
            image=self.magnifying_glass_image,
            compound=tk.LEFT,
            command=self.check_number,
            bg=PRIMARY_COLOR,
            fg=WHITE_COLOR
        )
        self.check_button.grid(row=1, column=1, padx=10,
                               pady=10, sticky=tk.NSEW)
        self.input_entry.bind("<Return>", lambda _: self.check_number())
        self.input_entry.focus_set()

        self.result_label = MyLabel(
            self, text="", font=(FONT_NAME, TEXT_FONT_SIZE))
        self.result_label.grid(row=3, column=0, columnspan=2, pady=(10, 0))

        self.after(100, self.listen_number)

    def generate_random_number(self):
        """
        Generate a random number within the specified difficulty level.

        Returns:
            int: The generated random number.
        """

        self.number = random.choice(
            [i for i in range(self.difficulty + 1) if i != self.number])

    def listen_number(self):
        """
        Generate and play the text-to-speech audio for the random number.
        """

        # Generate a text-to-speech audio from the random number
        tts = gTTS(text=str(self.number), lang="fr", slow=True)
        # Save the audio as filename
        tts.save(self.sound_path)
        # Play the audio
        self.play()
        # Remove the audio when played (fixed a permission bug on Windows)
        os.remove(self.sound_path)

    def play(self):
        """
        Play the audio of the generated number using the available audio player libraries.
        """

        for play in [self.playsound, self.pygame]:
            try:
                print(f"Sound played with {self.playsound.__name__}.")
                return play()
            except Exception:
                print(Exception)
                continue
        return

    def playsound(self):
        """
        Play the audio file using the playsound library.

        This function plays the audio file specified by the sound path using the playsound library.
        It blocks the program execution until the audio finishes playing.
        """

        playsound.playsound(sound=self.sound_path, block=True)

    def pygame(self):
        """
        Play the audio file using the pygame library.

        This function initializes the pygame mixer, loads the audio file specified by the sound path,
        and plays the audio using the pygame mixer.
        """

        pygame.mixer.init()
        pygame.mixer.music.load(self.sound_path)
        pygame.mixer.music.play()

    def check_number(self):
        """
        Check the user input against the generated number and update the result accordingly.
        """

        user_input = self.input_var.get()

        if self.validate(user_input, self.number):
            self.update_canvas(result="okay")
            self.after(1500, self.reset_canvas)
            self.after(2000, self.listen_number)
        else:
            self.update_canvas(result="wrong")

    def get_result(self, result):
        """
        Get the color, message, and icon for the given result.

        Args:
            result: The result of the user input validation.

        Returns:
            Tuple[str, str, ImageTk.PhotoImage]: The color, message, and icon for the result.
        """

        if result == "okay":
            color = "green"
            message = " Bravo !"
            icon = self.check_image
        elif result == "wrong":
            color = "orange"
            message = "Presque, réécoute le nombre et retente ta chance."
            icon = self.refresh_image
        elif result == "bug":
            color = "red"
            message = "Attention à bien écrire en chiffres."
            icon = self.warning_image
        else:  # result == "reset"
            color = "black"
            message = ""
            icon = self.magnifying_glass_image

        return color, message, icon

    def update_canvas(self, result):
        """
        Update the result label and input entry based on the given result.

        Args:
            result: The result of the user input validation.
        """

        color, message, icon = self.get_result(result)

        self.input_entry.config(highlightcolor=color, fg=color)
        self.result_label.config(text=message, fg=color)
        self.check_button.config(highlightbackground=color, image=icon)
        self.check_button.after(
            1500, lambda: self.check_button.config(
                image=self.magnifying_glass_image)
        )

    def reset_canvas(self):
        """
        Reset the input entry and update the result label to its initial state.
        """

        self.update_canvas("reset")
        self.input_entry.delete(0, tk.END)
        self.generate_random_number()


class CompareCanvas(MyFrame):
    """
    Represents a canvas for comparing elements.

    The CompareCanvas class extends the tk.Widget class and provides a canvas for comparing elements.
    It can be used to visually compare and analyze different elements or objects.
    """

    def __init__(self, master: MyFrame, difficulty: int):
        """
        Initialize the CompareCanvas.

        Args:
            master: The master widget.
        """

        super().__init__(master)
        # TODO factorize the default games into general classes

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.difficulty = difficulty

        self.first_number = None
        self.second_number = None
        self.generate_random_numbers()

        self.first_number_label = MyLabel(
            self, text=self.first_number, font=(FONT_NAME, TITLE_FONT_SIZE))
        self.first_number_label.grid(row=0, column=0, padx=10,
                                     pady=100, sticky=tk.NSEW)

        self.unknown_label = MyLabel(
            self, text="...", font=(FONT_NAME, TITLE_FONT_SIZE))
        self.unknown_label.grid(row=0, column=1, padx=10,
                                pady=100, sticky=tk.NSEW)

        self.second_number_label = MyLabel(
            self, text=self.second_number, font=(FONT_NAME, TITLE_FONT_SIZE))
        self.second_number_label.grid(row=0, column=2, padx=10,
                                      pady=100, sticky=tk.NSEW)

        self.question_mark_image = ImageTk.PhotoImage(
            Image.open(QUESTION_MARK_IMAGE_PATH).resize((70, 70))
        )
        self.lower_image = ImageTk.PhotoImage(
            Image.open(LOWER_IMAGE_PTH).resize((70, 70))
        )
        self.equal_image = ImageTk.PhotoImage(
            Image.open(EQUAL_IMAGE_PTH).resize((70, 70))
        )
        self.greater_image = ImageTk.PhotoImage(
            Image.open(GREATER_IMAGE_PTH).resize((70, 70))
        )
        self.check_image = ImageTk.PhotoImage(
            Image.open(CHECK_IMAGE_PATH).resize((50, 50))
        )
        self.warning_image = ImageTk.PhotoImage(
            Image.open(WARNING_IMAGE_PATH).resize((50, 50))
        )

        self.lower_button = MyButton(
            self, text="est plus petit que", image=self.lower_image,
            bg=LIGHT_SHADE_COLOR, fg=MAIN_COLOR
        )
        self.lower_button.config(command=lambda: self.check_result("<"))
        self.lower_button.grid(row=1, column=0, padx=10, pady=10)
        self.equal_button = MyButton(
            self, text="est égal à", image=self.equal_image,
            bg=LIGHT_SHADE_COLOR, fg=MAIN_COLOR
        )
        self.equal_button.config(command=lambda: self.check_result("="))
        self.equal_button.grid(row=1, column=1, padx=10, pady=10)
        self.greater_button = MyButton(
            self, text="est plus grand que", image=self.greater_image,
            bg=LIGHT_SHADE_COLOR, fg=MAIN_COLOR
        )
        self.greater_button.config(command=lambda: self.check_result(">"))
        self.greater_button.grid(row=1, column=2, padx=10, pady=10)

        self.result_label = MyLabel(
            self, text="", font=(FONT_NAME, TEXT_FONT_SIZE))
        self.result_label.grid(row=2, column=0, columnspan=3)

    def generate_random_number(self):
        """
        Generate a random number within the specified difficulty level.

        Returns:
            int: The generated random number.
        """

        return random.randint(0, self.difficulty)

    def generate_random_numbers(self) -> None:
        """
        Generate two random numbers.

        Generates two random numbers and assigns them to the instance variables `first_number` and `second_number`.

        Args:
            self: The instance of the class.

        Returns:
            None
        """
        self.first_number = self.generate_random_number()
        self.second_number = self.generate_random_number()

    def update_canvas(self, tryout, button_compare):
        """
        Update the canvas based on the tryout result and button compare value.

        Updates the result label with the corresponding message based on the tryout result.
        Configures the button specified by the button_compare value with the appropriate color and icon.

        Args:
            tryout: The result of the tryout.
            button_compare: The comparison operator ("<", "=", or ">").

        Returns:
            None
        """

        (color, message, icon) = self.get_result(tryout)

        self.result_label.config(text=message)

        if button_compare == "<":
            button = self.lower_button
        elif button_compare == "=":
            button = self.equal_button
        else:
            button = self.greater_button

        button.config(highlightbackground=color, image=icon)

    def reset_canvas(self) -> None:
        """
        Reset the canvas to its initial state.

        Generates new random numbers, updates the number labels, resets the button images and highlights,
        and clears the result label.

        Args:
            self: The instance of the class.

        Returns:
            None
        """
        self.generate_random_numbers()
        self.first_number_label.config(text=self.first_number)
        self.second_number_label.config(text=self.second_number)
        self.lower_button.config(
            highlightbackground=PRIMARY_COLOR, image=self.lower_image)
        self.equal_button.config(
            highlightbackground=PRIMARY_COLOR, image=self.equal_image)
        self.greater_button.config(
            highlightbackground=PRIMARY_COLOR, image=self.greater_image)
        self.result_label.config(text="")

    def get_result(self, tryout: bool) -> Tuple[str, str, ImageTk.PhotoImage]:
        """
        Get the result information based on the tryout.

        Determines the color, message, and icon based on the tryout result.

        Args:
            tryout: The result of the tryout.

        Returns:
            Tuple[str, str, ImageTk.PhotoImage]: The color, message, and icon for the result.
        """
        if tryout:
            color = "green"
            message = " Bravo !"
            icon = self.check_image
        else:
            color = "orange"
            message = "Erreur."
            icon = self.warning_image

        return color, message, icon

    def check_result(self, button_compare: str) -> None:
        """
        Check the result of the comparison and update the canvas.

        Compares the numbers based on the given button_compare value ("<", "=", or ">").
        Updates the canvas based on the tryout result.
        If the tryout is True, it schedules a reset of the canvas after 1500 milliseconds.

        Args:
            button_compare: The comparison operator ("<", "=", or ">").

        Returns:
            None
        """
        if button_compare == "<":
            tryout = self.first_number < self.second_number
        elif button_compare == "=":
            tryout = self.first_number == self.second_number
        elif button_compare == ">":
            tryout = self.first_number > self.second_number
        else:
            tryout = False

        self.update_canvas(tryout, button_compare)

        if tryout:
            self.after(1500, self.reset_canvas)
