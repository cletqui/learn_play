import tkinter as tk
import random
from gtts import gTTS
import os


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Les Nombres")
        self.geometry("800x600")
        self.resizable(0, 0)

        # Create a main frame to hold content
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.show_main_canvas()

    def show_main_canvas(self):
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        main_canvas = MainCanvas(self.main_frame)
        main_canvas.pack(fill="both", expand=True)
        main_canvas.bind_button_callback(self.show_difficulty_canvas)

    def show_difficulty_canvas(self):
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        difficulty_canvas = DifficultyCanvas(self.main_frame)
        difficulty_canvas.pack(fill="both", expand=True)
        difficulty_canvas.bind_button_callback(self.show_main_canvas)

    def show_typing_canvas(self, sound_type, difficulty):
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        typing_canvas = TypingCanvas(self.main_frame, sound_type, difficulty)
        typing_canvas.pack(fill="both", expand=True)
        typing_canvas.bind_button_callback(self.show_difficulty_canvas)


class MainCanvas(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Create a label with centered text
        label = tk.Label(self, text="Les nombres", font=(
            "Courier New", 18), anchor="center")
        label.grid(row=0, column=0, columnspan=3, pady=(10, 0), sticky=tk.N)

        self.sound_number_button = tk.Button(
            self, text="son vers nombre", font=("Courier New", 14))
        self.sound_number_button.grid(
            row=1, column=0, padx=10, pady=10, sticky=tk.EW)

        self.sound_letter_button = tk.Button(
            self, text="son vers mot", font=("Courier New", 14))
        self.sound_letter_button.grid(
            row=1, column=1, padx=10, pady=10, sticky=tk.EW)

        self.other_button = tk.Button(
            self, text="autre", font=("Courier New", 14))
        self.other_button.grid(
            row=1, column=2, padx=10, pady=10, sticky=tk.EW)

    def bind_button_callback(self, callback):
        self.sound_number_button.config(command=callback)
        self.sound_letter_button.config(command=callback)


class DifficultyCanvas(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=3)
        self.grid_columnconfigure(3, weight=3)

        # Create a label with centered text
        label = tk.Label(self, text="Choix du niveau",
                         font=("Courier New", 18), anchor="center")
        label.grid(row=0, column=0, columnspan=4, pady=(10, 0))

        self.back_button = tk.Button(self, text="←", font=("Courier New", 14))
        self.back_button.grid(row=0, column=0, padx=10,
                              pady=10, sticky=tk.NSEW)

        self.difficulty_1_button = tk.Button(
            self, text="0 - 10", font=("Courier New", 14))
        self.difficulty_1_button.grid(
            row=1, column=1, padx=10, pady=10, sticky=tk.NSEW)

        self.difficulty_2_button = tk.Button(
            self, text="0 - 50", font=("Courier New", 14))
        self.difficulty_2_button.grid(
            row=1, column=2, padx=10, pady=10, sticky=tk.NSEW)

        self.difficulty_3_button = tk.Button(
            self, text="0 - 100", font=("Courier New", 14))
        self.difficulty_3_button.grid(
            row=1, column=3, padx=10, pady=10, sticky=tk.NSEW)

        self.difficulty_4_button = tk.Button(
            self, text="0 - 1000", font=("Courier New", 14))
        self.difficulty_4_button.grid(
            row=2, column=1, padx=10, pady=10, sticky=tk.NSEW)

        self.difficulty_5_button = tk.Button(
            self, text="0 - 10000", font=("Courier New", 14))
        self.difficulty_5_button.grid(
            row=2, column=2, padx=10, pady=10, sticky=tk.NSEW)

        self.difficulty_6_button = tk.Button(
            self, text="0 - 100000", font=("Courier New", 14))
        self.difficulty_6_button.grid(
            row=2, column=3, padx=10, pady=10, sticky=tk.NSEW)

    def bind_button_callback(self, callback):
        self.back_button.config(command=callback)


class TypingCanvas(tk.Frame):
    def __init__(self, master, sound_type, difficulty):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=3)
        self.grid_columnconfigure(3, weight=3)

        # tts = gTTS(text="This is the pc speaking", lang='en')

        # tts.save("pcvoice.mp3")
        # # to start the file from python
        # os.system("start pcvoice.mp3")

        # Create a label with centered text
        label = tk.Label(self, text=sound_type, font=(
            "Courier New", 18), anchor="center")
        label.grid(row=0, column=0, columnspan=4, pady=(10, 0))

        self.back_button = tk.Button(self, text="←", font=("Courier New", 14))
        self.back_button.grid(row=0, column=0, padx=10,
                              pady=10, sticky=tk.NSEW)

        random_number = random.randint(0, difficulty)
        self.random_number_label = tk.Label(
            self, text=f"Random Number: {random_number}", font=("Courier New", 14))
        self.random_number_label.grid(
            row=1, column=0, columnspan=4, pady=(10, 0))

        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(
            self, textvariable=self.input_var, font=("Courier New", 14))
        self.input_entry.grid(row=2, column=1, padx=10,
                              pady=10, sticky=tk.NSEW)

        check_button = tk.Button(self, text="Check", font=(
            "Courier New", 14), command=self.check_number)
        check_button.grid(row=2, column=2, padx=10, pady=10, sticky=tk.NSEW)

        self.result_label = tk.Label(self, text="", font=("Courier New", 14))
        self.result_label.grid(row=3, column=0, columnspan=4, pady=(10, 0))

    def bind_button_callback(self, callback):
        self.back_button.config(command=callback)

    def check_number(self):
        user_input = self.input_var.get()
        random_number = int(self.random_number_label.cget(
            "text").split(":")[1].strip())

        if user_input.isnumeric() and int(user_input) == random_number:
            result = "Correct!"
        else:
            result = "Incorrect. Try again."

        self.result_label.config(text=result)


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
