# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import your tkinter window class
from MainApplication import MainApplication


def main():
    """
    The entry point of the application.

    Runs the main application loop.

    """
    app = MainApplication()
    app.mainloop()


if __name__ == "__main__":
    main()
