# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from PIL import ImageTk, Image
import random
import os
from gtts import gTTS
import playsound


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Apprentissage")
        self.geometry("800x600")
        self.resizable(0, 0)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=11)

        # Create a nav bar to display title
        self.nav_bar = NavigationBar(self, "Apprentissage")
        self.nav_bar.grid(row=0, column=0, sticky=tk.NSEW)

        # Create a main frame to hold content
        self.main_frame = tk.Frame(self)

        # Initialize with
        self.show_main_canvas()

    def show_main_canvas(self):
        # Clear the main frame
        self.main_frame.destroy()

        # Create the new main frame from main canvas
        self.main_frame = MainCanvas(
            self, spelling_callback=self.show_spelling_canvas, maths_callback=self.show_maths_canvas)
        self.main_frame.grid(row=1, column=0, sticky=tk.NSEW)

        # Update the title for the navigation bar
        self.nav_bar.update_title("Choix de la matière")
        # Update the callback for the navigation bar
        self.nav_bar.update_callback(None)

    def show_spelling_canvas(self):
        # Clear the main frame
        self.main_frame.destroy()

        # Create the new main frame from main canvas
        self.main_frame = SpellingCanvas(
            self, sound_number_callback=self.show_difficulty_canvas, sound_letter_callback=self.show_difficulty_canvas)
        self.main_frame.grid(row=1, column=0, sticky=tk.NSEW)

        # Update the title for the navigation bar
        self.nav_bar.update_title("Français")
        # Update the callback for the navigation bar
        self.nav_bar.update_callback(self.show_main_canvas)

    def show_maths_canvas(self):
        # Clear the main frame
        self.main_frame.destroy()

        # Create the new main frame from main canvas
        self.main_frame = MathsCanvas(
            self, sound_number_callback=self.show_difficulty_canvas, sound_letter_callback=self.show_difficulty_canvas)
        self.main_frame.grid(row=1, column=0, sticky=tk.NSEW)

        # Update the title for the navigation bar
        self.nav_bar.update_title("Mathématiques")
        # Update the callback for the navigation bar
        self.nav_bar.update_callback(self.show_main_canvas)

    def show_difficulty_canvas(self):
        # Clear the main frame
        self.main_frame.destroy()

        # Create the new main frame from difficulty canvas
        self.main_frame = DifficultyCanvas(
            self, difficulty_callback=self.show_typing_canvas)
        self.main_frame.grid(row=1, column=0, sticky=tk.NSEW)

        # Update the title for the navigation bar
        self.nav_bar.update_title("Choix du niveau")
        # Update the callback for the navigation bar
        self.nav_bar.update_callback(self.show_main_canvas)

    def show_typing_canvas(self, difficulty):
        # Clear the main frame
        self.main_frame.destroy()

        # Create the new main frame from difficulty canvas
        self.main_frame = TypingCanvas(self, difficulty)
        self.main_frame.grid(row=1, column=0, sticky=tk.NSEW)

        # Update the title for the navigation bar
        self.nav_bar.update_title(
            f"Écoute et écris en chiffres (entre 0 et {difficulty})")
        # Update the callback for the navigation bar
        self.nav_bar.update_callback(self.show_difficulty_canvas)


class NavigationBar(tk.Frame):
    def __init__(self, master, title):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.back_image = ImageTk.PhotoImage(
            Image.open("./images/arrow.png").resize((40, 40)).rotate(180))

        # Store the callback function
        self.callback = None
        # Create a button for the callback button
        self.back_button = tk.Button(self, width=50, image=self.back_image)

        # Create a label for the title
        self.title_label = tk.Label(self, text=title, font=(
            "Roboto", 24), anchor="center")
        self.title_label.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

    def update_callback(self, callback):
        # Update the callback state
        self.callback = callback

        if callback:
            # Assign the callback to the callback button
            self.back_button.config(command=callback)
            if self.back_button.grid_info() == {}:
                # Add it to the grid if it has been removed
                self.back_button.grid(
                    row=0, column=0, padx=10, pady=10, sticky=tk.W)
        else:
            # Remove the callback button and no callback function is defined
            self.back_button.grid_remove()

    def update_title(self, title):
        self.title_label["text"] = title


class MainCanvas(tk.Frame):
    def __init__(self, master, spelling_callback, maths_callback):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        self.maths_image = ImageTk.PhotoImage(
            Image.open("./images/maths.png").resize((80, 80)))
        self.spelling_image = ImageTk.PhotoImage(
            Image.open("./images/spelling.png").resize((80, 80)))

        self.sound_letter_button = tk.Button(
            self, height=150, width=300, text="Mathématiques", font=("Roboto", 24), image=self.maths_image, compound=tk.TOP, command=maths_callback)
        self.sound_letter_button.grid(
            row=0, column=0, padx=10, pady=20, sticky=tk.NS)

        self.sound_number_button = tk.Button(
            self, height=150, width=300, text="Français", font=("Roboto", 24), image=self.spelling_image, compound=tk.TOP, command=spelling_callback)
        self.sound_number_button.grid(
            row=1, column=0, padx=10, pady=20, sticky=tk.NS)


class SpellingCanvas(tk.Frame):
    def __init__(self, master, sound_number_callback, sound_letter_callback):
        super().__init__(master)

        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure(2, weight=1)

        # self.sound_number_button = tk.Button(
        #     self, text="son vers nombre", font=("Roboto", 14))
        # self.sound_number_button.grid(
        #     row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)
        # self.sound_number_button.config(
        #     command=sound_number_callback)

        # self.sound_letter_button = tk.Button(
        #     self, text="son vers mot", font=("Roboto", 14))
        # self.sound_letter_button.grid(
        #     row=0, column=1, padx=10, pady=10, sticky=tk.NSEW)
        # self.sound_letter_button.config(
        #     command=sound_letter_callback)

        # self.other_button = tk.Button(
        #     self, text="autre", font=("Roboto", 14))
        # self.other_button.grid(
        #     row=0, column=2, padx=10, pady=10, sticky=tk.NSEW)


class MathsCanvas(tk.Frame):
    def __init__(self, master, sound_number_callback, sound_letter_callback):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.label = tk.Label(self, text="Test", font=("Roboto", 18))
        self.label.grid(row=0, column=0, columnspan=3,
                        padx=10, pady=10, sticky=tk.NSEW)

        self.sound_number_button = tk.Button(
            self, text="son vers nombre", font=("Roboto", 14))
        self.sound_number_button.grid(
            row=1, column=0, padx=10, pady=10, sticky=tk.NSEW)
        self.sound_number_button.config(
            command=sound_number_callback)

        self.sound_letter_button = tk.Button(
            self, text="son vers mot", font=("Roboto", 14))
        self.sound_letter_button.grid(
            row=1, column=1, padx=10, pady=10, sticky=tk.NSEW)
        self.sound_letter_button.config(
            command=sound_letter_callback)

        self.other_button = tk.Button(
            self, text="autre", font=("Roboto", 14))
        self.other_button.grid(
            row=1, column=2, padx=10, pady=10, sticky=tk.NSEW)

        self.label2 = tk.Label(self, text="Test2", font=("Roboto", 18))
        self.label2.grid(row=2, column=0, columnspan=3,
                         padx=10, pady=10, sticky=tk.NSEW)


class DifficultyCanvas(tk.Frame):
    def __init__(self, master, difficulty_callback):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.difficulties = [10, 20, 50, 100, 1000, 10000, 100000, 1000000]

        row = 0
        column = 0

        for difficulty in self.difficulties:
            difficulty_button = tk.Button(
                self, text=f"0 - {difficulty}", font=("Roboto", 14))
            difficulty_button.grid(
                row=row, column=column, padx=10, pady=10, sticky=tk.NSEW)
            difficulty_button.config(
                command=lambda d=difficulty: difficulty_callback(d))

            column += 1
            if column >= 3:
                column = 0
                row += 1


class TypingCanvas(tk.Frame):
    def __init__(self, master, difficulty):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=1)

        self.difficulty = difficulty
        self.random_number = None
        self.generate_random_number()
        self.sound_filename = "random_number.mp3"

        self.listen_image = ImageTk.PhotoImage(
            Image.open("./images/sound.png").resize((70, 70)))
        self.magnifying_glass_image = ImageTk.PhotoImage(
            Image.open("./images/magnifying-glass.png").resize((50, 50)))
        self.check_image = ImageTk.PhotoImage(
            Image.open("./images/check.png").resize((50, 50)))
        self.refresh_image = ImageTk.PhotoImage(
            Image.open("./images/refresh.png").resize((50, 50)))
        self.warning_image = ImageTk.PhotoImage(
            Image.open("./images/warning.png").resize((50, 50)))

        # Create a label with centered text
        self.listen_button = tk.Button(self, text="Réécouter", image=self.listen_image, font=(
            "Roboto", 18), anchor="center")
        self.listen_button.grid(row=0, column=0, columnspan=2, pady=10)
        self.listen_button.config(command=self.listen_number)
        self.listen_button.bind

        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(
            self, textvariable=self.input_var, font=("Roboto", 18), highlightthickness=2)
        self.input_entry.grid(row=1, column=0, padx=10,
                              pady=10, sticky=tk.NSEW)

        self.check_button = tk.Button(self, width=120, text="   Vérifier", font=(
            "Roboto", 14), image=self.magnifying_glass_image, compound=tk.LEFT, command=self.check_number)
        self.check_button.grid(row=1, column=1, padx=10,
                               pady=10, sticky=tk.NSEW)
        self.input_entry.bind("<Return>", lambda _: self.check_number())
        self.input_entry.focus_set()

        self.result_label = tk.Label(self, text="", font=("Roboto", 14))
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
        tts = gTTS(text=str(self.random_number), lang='fr', slow=True)
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
        self.check_button.config(highlightcolor=color, image=icon)
        self.check_button.after(1500, lambda: self.check_button.config(
            image=self.magnifying_glass_image))

    def reset(self):
        self.update_result("reset")
        self.input_entry.delete(0, tk.END)


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
