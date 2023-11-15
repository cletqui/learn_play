# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Application Entry Point
"""

# Import your tkinter window class
from main_application import MainApplication


def main():
    """
    Runs the main application.

    Returns:
        None

    Examples:
        >>> main()
    """

    app = MainApplication()
    app.mainloop()


if __name__ == "__main__":
    main()
