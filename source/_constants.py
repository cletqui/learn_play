"""
Project Constants
"""

import os

dirname = os.path.dirname(__file__)


def image_path(image_name: str, image_dir: str = dirname) -> str:
    """
    Returns the path of an image file given its name and the directory name.

    Args:
        image_name (str): The name of the image file.
        image_dir (str, optional): The directory name. Defaults to dirname.

    Returns:
        str: The path of the image file.

    Examples:
        >>> image_path("logo.png")
        '/path/to/assets/logo.png'
    """

    return os.path.join(image_dir, "assets", image_name)


# Application window dimensions
WINDOW_WIDTH: int = 900
WINDOW_HEIGHT: int = 600

# File paths for images
FAVICON_PATH: str = image_path("favicon.png")
MATHEMATICS_IMAGE_PATH: str = image_path("maths.png")
SPELLING_IMAGE_PATH: str = image_path("spelling.png")
ARROW_IMAGE_PATH: str = image_path("arrow.png")
SOUND_IMAGE_PATH: str = image_path("sound.png")
GREATER_EQUAL_IMAGE_PATH: str = image_path("greater-equal.png")
MAGNIFYING_GLASS_IMAGE_PATH: str = image_path("magnifying-glass.png")
CHECK_IMAGE_PATH: str = image_path("check.png")
REFRESH_IMAGE_PATH: str = image_path("refresh.png")
WARNING_IMAGE_PATH: str = image_path("warning.png")
TRAFFIC_CONE_IMAGE_PATH: str = image_path("traffic-cone.png")
QUESTION_MARK_IMAGE_PATH: str = image_path("question-mark.png")
EQUAL_IMAGE_PTH: str = image_path("equal.png")
GREATER_IMAGE_PTH: str = image_path("greater.png")
LOWER_IMAGE_PTH: str = image_path("lower.png")

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
