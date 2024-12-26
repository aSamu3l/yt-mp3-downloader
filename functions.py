import os
from CTkMessagebox import CTkMessagebox as CTkM
from customtkinter import filedialog as fd

def select_destination_folder() -> str:
    """
    Prompts the user to select the destination folder using a file dialog.

    Returns:
        str: The path to the selected destination folder.
    """
    path = fd.askdirectory(title="Select destination folder")
    if not os.path.exists(path):
        CTkM(title = "Error", message = "The path does not exist", icon = "cancel")
        return ""
    return path