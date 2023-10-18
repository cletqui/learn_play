# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from PIL import ImageTk, Image
import random
import os
from gtts import gTTS
import playsound

from source._constants import *


class TypingCanvas(tk.Frame):
    def __init__(self, master, difficulty):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=1)

        self.difficulty = difficulty
        self.random_number = None
        self.generate_random_number()
        self.sound_filename = RANDOM_NUMBER_SOUND_PATH

        self.listen_image = ImageTk.PhotoImage(
            Image.open(SOUND_IMAGE_PATH).resize((70, 70)))
        self.magnifying_glass_image = ImageTk.PhotoImage(
            Image.open(MAGNIFYING_GLASS_IMAGE_PATH).resize((50, 50)))
        self.check_image = ImageTk.PhotoImage(
            Image.open(CHECK_IMAGE_PATH).resize((50, 50)))
        self.refresh_image = ImageTk.PhotoImage(
            Image.open(REFRESH_IMAGE_PATH).resize((50, 50)))
        self.warning_image = ImageTk.PhotoImage(
            Image.open(WARNING_IMAGE_PATH).resize((50, 50)))

        # Create a label with centered text
        self.listen_button = tk.Button(self, text="Réécouter", font=(
            FONT_NAME, TEXT_FONT_SIZE), image=self.listen_image, compound=tk.TOP)
        self.listen_button.grid(row=0, column=0, columnspan=2, pady=10)
        self.listen_button.config(command=self.listen_number)
        self.listen_button.bind

        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(
            self, textvariable=self.input_var, font=(FONT_NAME, TEXT_FONT_SIZE), highlightthickness=2)
        self.input_entry.grid(row=1, column=0, padx=10,
                              pady=10, sticky=tk.NSEW)

        self.check_button = tk.Button(self, width=120, text="   Vérifier", font=(
            FONT_NAME, TEXT_FONT_SIZE), image=self.magnifying_glass_image, compound=tk.LEFT, command=self.check_number)
        self.check_button.grid(row=1, column=1, padx=10,
                               pady=10, sticky=tk.NSEW)
        self.input_entry.bind("<Return>", lambda _: self.check_number())
        self.input_entry.focus_set()

        self.result_label = tk.Label(
            self, text="", font=(FONT_NAME, TEXT_FONT_SIZE))
        self.result_label.grid(row=3, column=0,
                               columnspan=2, pady=(10, 0))

        self.after(100, self.listen_number)

    def generate_random_number(self):
        random_number = random.randint(0, self.difficulty)
        if self.random_number:
            while self.random_number == random_number:
                random_number = random.randint(0, self.difficulty)
        self.random_number = random_number
        return random_number

    def listen_number(self):
        # Generate a text-to-speech audio from the random number
        tts = gTTS(text=str(self.random_number), lang="fr", slow=True)
        # Save the audio as filename
        tts.save(self.sound_filename)
        # Play the audio
        playsound.playsound(sound=self.sound_filename, block=True)
        # Remove the audio when played (fixed a permission bug on Windows)
        os.remove(self.sound_filename)

    def check_number(self):
        user_input = self.input_var.get()

        if user_input.isnumeric():
            if int(user_input) == self.random_number:
                self.update_result(result="okay")
                self.after(1500, self.reset)
                self.generate_random_number()
                self.after(2000, self.listen_number)
            else:
                self.update_result(result="wrong")
        else:
            self.update_result(result="bug")

    def update_result(self, result):
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
        elif result == "reset":
            color = "black"
            message = ""
            icon = self.magnifying_glass_image

        self.input_entry.config(
            highlightcolor=color, fg=color)
        self.result_label.config(text=message, fg=color)
        self.check_button.config(highlightbackground=color, image=icon)
        self.check_button.after(1500, lambda: self.check_button.config(
            image=self.magnifying_glass_image))

    def reset(self):
        self.update_result("reset")
        self.input_entry.delete(0, tk.END)


class TypingNumbersCanvas(tk.Frame):
    def __init__(self, master, difficulty):
        super().__init__(master)
