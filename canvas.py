# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from PIL import ImageTk, Image
import random
from gtts import gTTS
import playsound


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Les Nombres")
        self.geometry("800x600")
        self.resizable(0, 0)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=11)

        # Create a nav bar to display title
        self.nav_bar = NavigationBar(self, "Les Nombres")
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
            self, sound_number_callback=self.show_difficulty_canvas, sound_letter_callback=self.show_difficulty_canvas)
        self.main_frame.grid(row=1, column=0, sticky=tk.NSEW)

        # Update the title for the navigation bar
        self.nav_bar.update_title("Les Nombres")
        # Update the callback for the navigation bar
        self.nav_bar.update_callback(None)

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

        # Store the callback function
        self.callback = None
        # Create a button for the callback button
        self.back_button = tk.Button(self, text="←", font=(
            "Roboto", 14))

        # Create a label for the title
        self.title_label = tk.Label(self, text=title, font=(
            "Roboto", 18), anchor="center")
        self.title_label.grid(row=0, column=0, columnspan=4, pady=(10, 0))

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
    def __init__(self, master, sound_number_callback, sound_letter_callback):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.sound_number_button = tk.Button(
            self, text="son vers nombre", font=("Roboto", 14))
        self.sound_number_button.grid(
            row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)
        self.sound_number_button.config(
            command=sound_number_callback)

        self.sound_letter_button = tk.Button(
            self, text="son vers mot", font=("Roboto", 14))
        self.sound_letter_button.grid(
            row=0, column=1, padx=10, pady=10, sticky=tk.NSEW)
        self.sound_letter_button.config(
            command=sound_letter_callback)

        self.other_button = tk.Button(
            self, text="autre", font=("Roboto", 14))
        self.other_button.grid(
            row=0, column=2, padx=10, pady=10, sticky=tk.NSEW)


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

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)

        self.difficulty = difficulty
        self.random_number = None
        self.generate_random_number()

        self.listen_image = ImageTk.PhotoImage(
            Image.open("./images/volume.png").resize((30, 30)))

        # Create a label with centered text
        self.listen_button = tk.Button(self, text="Réécouter", image=self.listen_image, font=(
            "Roboto", 14), anchor="center")
        self.listen_button.grid(row=0, column=0, columnspan=2, pady=(10, 0))
        self.listen_button.config(command=self.listen_number)
        self.listen_button.bind

        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(
            self, textvariable=self.input_var, font=("Roboto", 14), highlightthickness=2)
        self.input_entry.grid(row=1, column=0, padx=10,
                              pady=10, sticky=tk.NSEW)

        self.check_button = tk.Button(self, text="Vérifier", font=(
            "Roboto", 14), command=self.check_number)
        self.check_button.grid(row=1, column=1, padx=10,
                               pady=10, sticky=tk.NSEW)
        self.input_entry.bind("<Return>", lambda event: self.check_number())
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
        filename = "random_number.mp3"
        tts.save(filename)
        # Play the audio
        playsound.playsound(filename)

    def check_number(self):
        user_input = self.input_var.get()

        if user_input.isnumeric() and int(user_input) == self.random_number:
            self.print_result("green", "Bravo !")
            self.after(1500, self.reset)
            self.generate_random_number()
            self.after(2000, self.listen_number)
        else:
            self.print_result("red", "Incorrecte, réessaie.")

    def print_result(self, highlightcolor, message):
        self.input_entry.config(
            highlightcolor=highlightcolor, fg=highlightcolor)
        self.result_label.config(text=message, fg=highlightcolor)

    def reset(self):
        self.print_result("black", "")
        self.input_entry.delete(0, tk.END)


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
