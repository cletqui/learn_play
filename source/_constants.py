import os
dirname = os.path.dirname(__file__)

# Application window dimensions
WINDOW_WIDTH: int = 900
WINDOW_HEIGHT: int = 600

# File paths for images
# TODO deal with different path types (Linux, Windows)
FAVICON_PATH: str = os.path.join(dirname, "assets", "favicon.png") # "source/assets/favicon.png"
MATHEMATICS_IMAGE_PATH: str = os.path.join(dirname, "assets", "maths.png") # "source/assets/maths.png"
SPELLING_IMAGE_PATH: str = os.path.join(dirname, "assets", "spelling.png") # "source/assets/spelling.png"
ARROW_IMAGE_PATH: str = os.path.join(dirname, "assets", "arrow.png") # "source/assets/arrow.png"
SOUND_IMAGE_PATH: str = os.path.join(dirname, "assets", "sound.png") # "source/assets/sound.png"
MAGNIFYING_GLASS_IMAGE_PATH: str = os.path.join(dirname, "assets", "magnifying-glass.png") # "source/assets/magnifying-glass.png"
CHECK_IMAGE_PATH: str = os.path.join(dirname, "assets", "check.png") # "source/assets/check.png"
REFRESH_IMAGE_PATH: str = os.path.join(dirname, "assets", "refresh.png") # "source/assets/refresh.png"
WARNING_IMAGE_PATH: str = os.path.join(dirname, "assets", "warning.png") # "source/assets/warning.png"
TRAFFIC_CONE_IMAGE_PATH: str = os.path.join(dirname, "assets", "traffic-cone.png") # "source/assets/traffic-cone.png"

# Created file paths
RANDOM_NUMBER_SOUND_PATH = "random_number.mp3"

# Application titles
APP_TITLE: str = "Apprends & Joue"
SUBJECT_TITLE: str = "Choix de la matière"
MATHEMATICS_TITLE: str = "Mathématiques"
SPELLING_TITLE: str = "Français"
DIFFICULTY_TITLE: str = "Choix du niveau"
WORK_IN_PROGRESS_TITLE: str = "Travaux en cours..."

# Theme Colors (try http://colormind.io/bootstrap/)
LIGHT_SHADE_COLOR: str = "#F4F5F5"
LIGHT_ACCENT_COLOR: str = "#798178"
MAIN_COLOR: str = "#9794A9"
DARK_ACCENT_COLOR: str = "#A5455A"
DARK_SHADE_COLOR: str = "#4F545B"
PRIMARY_COLOR: str = "#9794a9"
INFO_COLOR: str = "#4f545b"
SUCCESS_COLOR: str = "#63a76b"
WARNING_COLOR: str = "#e09733"
DANGER_COLOR: str = "#f44336"
WHITE_COLOR: str = "#FFFFFF"

# Colors
BACKGROUND: str = LIGHT_SHADE_COLOR
HEADER_BACKGROUND: str = LIGHT_ACCENT_COLOR

# Font settings
FONT_NAME: str = "Roboto"
TITLE_FONT_SIZE: int = 24
TEXT_FONT_SIZE: int = 18
FONT_COLOR: str = DARK_SHADE_COLOR
