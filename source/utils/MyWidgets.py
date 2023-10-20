# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

from source._constants import FONT_NAME, TITLE_FONT_SIZE, TEXT_FONT_SIZE, LIGHT_SHADE_COLOR, MAIN_COLOR, DARK_SHADE_COLOR, PRIMARY_COLOR, INFO_COLOR, WHITE_COLOR


class MyFrame(tk.Frame):
    def __init__(self, master, bg=LIGHT_SHADE_COLOR, *args, **kwargs):
        super().__init__(master, bg=bg, *args, **kwargs)


class MyButton(tk.Button):
    def __init__(self, master, font=(FONT_NAME, TEXT_FONT_SIZE), highlightbackground=DARK_SHADE_COLOR, compound=tk.TOP, *args, **kwargs):
        super().__init__(master, font=font, compound=compound,
                         highlightbackground=highlightbackground, *args, **kwargs)


class PrimaryButton(MyButton):
    def __init__(self, master, bg=PRIMARY_COLOR, fg=WHITE_COLOR, *args, **kwargs):
        super().__init__(master, bg=bg, fg=fg, * args, **kwargs)


class InfoButton(MyButton):
    def __init__(self, master, bg=INFO_COLOR, fg=WHITE_COLOR, *args, **kwargs):
        super().__init__(master, bg=bg, fg=fg, * args, **kwargs)

# TODO define the other buttons


class MyLabel(tk.Label):
    def __init__(self, master, font=(FONT_NAME), anchor="center", bg=LIGHT_SHADE_COLOR, fg=DARK_SHADE_COLOR, *args, **kwargs):
        super().__init__(master, font=font, anchor=anchor,
                         bg=bg, fg=fg, *args, **kwargs)


class HeaderLabel(MyLabel):
    def __init__(self, master, font=(FONT_NAME, TITLE_FONT_SIZE, "bold"), bg=MAIN_COLOR, fg=WHITE_COLOR, * args, **kwargs):
        super().__init__(master, font=font, bg=bg, fg=fg, *args, **kwargs)


class TitleLabel(MyLabel):
    def __init__(self, master, font=(FONT_NAME, TITLE_FONT_SIZE), * args, **kwargs):
        super().__init__(master, font=font, *args, **kwargs)


class TextLabel(MyLabel):
    def __init__(self, master, font=(FONT_NAME, TEXT_FONT_SIZE), * args, **kwargs):
        super().__init__(master, font=font, *args, **kwargs)
