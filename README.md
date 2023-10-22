# 📖 Apprends & Joue (Learn & Play) 🧑‍🏫

**Apprends & Joue** is a Tkinter-based educational game application designed to make learning mathematics and French spelling fun and engaging for primary school students. The application offers a variety of simple interactive games that promote learning while having a good time and learning to use a computer. 💻

## Table of Contents

- [📖 Apprends \& Joue (Learn \& Play) 🧑‍🏫](#-apprends--joue-learn--play-)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Release](#release)
  - [Features](#features)
  - [Project Structure](#project-structure)
  - [Getting Started](#getting-started)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

Education doesn't have to be dull, and that's the philosophy behind **Apprends & Joue**. This application seeks to provide students with a platform where they can enhance their math and French spelling skills while enjoying themselves. The games are designed to be interactive and educational, covering a range of difficulty levels to cater to different learning needs.

## Release

You can find the latest version of the executable in [Releases](https://github.com/cletqui/learn_play/releases).
The executable can be run with Windows. If necessary, the GitHub actions can be modified to deploy a MacOS compatible version too.

## Features

- Choose between two educational subjects: Mathematics and French.
- Multiple games for each subject.
- Adjustable difficulty levels to match the student's skill.
- Engaging interface with audio and visual elements.
- A simple and user-friendly interface designed for primary school students.
- A fun and interactive way to learn math and French spelling.

## Project Structure

The **Apprends & Joue** project is structured as follows:

- `app.spec` is the configuration file to create the executable with PyInstaller.
- `requirements.txt` is the configuration file for pip installation.
- **`source/`** contains the source code of the application:
  - `source/__main__.py`: the entry point for the application, where the MainApplication is created and called.
  - `source/_constants.py`: the constants of the application (image paths, colors, etc).
  - `source/MainApplication.py`: the core of the application, where the callback functions are defined.
  - **`source/assets/`** contains the assets (icon and images) for the application.
  - **`source/components/`** contains the main components of the application:
    - `source/components/MainCanvas.py`: the main canvas of the application, where you choose your subject.
    - `source/components/Header.py`: the header of the application.
    - `source/components/SubjectCanvas.py`: displays the available games for the selected subject.
    - `source/components/DifficultyCanvas.py`: allows you to choose the difficulty level for the games.
    - `source/components/GameCanvas.py`: the core of each game, where students practice their skills.
    - `source/components/WorkInProgress.py`: a blank page where the next games will be deployed.
  - **`source/utils/`** contains the utility assets (custom Tkinter widgets, custom functions):
    - `source/utils/MyWidgets.py`: the custom Tkinter widgets (font, colors, etc) for the application.

## Getting Started

To run the application locally, follow these steps:

1. Clone this repository to your local machine.
2. Make sure you have Python installed on your system.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run `source/__main__.py` using `python source/__main__.py` to start the application.
5. Select your subject, difficulty level, and start playing the games.

## Contributing

Contributions to this project are welcome. Whether you want to add more games, improve the user interface, or fix bugs, your help is appreciated. Please check the [CONTRIBUTING.md](CONTRIBUTING.md) file for more details on how to get involved.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and share it as per the license terms.

---

Let's make learning mathematics and French spelling an exciting adventure with **Apprends & Joue**!
