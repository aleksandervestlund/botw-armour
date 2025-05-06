import os
from tkinter import Button, Entry, Label, StringVar, Tk, Toplevel

from source.armour_tracker import ArmourTracker
from source.constants import DATA_FOLDER


def prompt_login(root: Tk) -> None:
    def on_login() -> None:
        if not (username := username_var.get().strip().lower()):
            return

        login_window.destroy()
        save_path = os.path.join(DATA_FOLDER, f"{username}.json")
        armour_tracker = ArmourTracker(root, username)

        if os.path.exists(save_path):
            armour_tracker.load_state()

    login_window = Toplevel(root)
    login_window.title("Login")
    login_window.grab_set()

    username_var = StringVar()
    Label(login_window, text="Enter username:").pack(pady=5)
    Entry(login_window, textvariable=username_var).pack(pady=5)
    Button(login_window, text="Login", command=on_login).pack(pady=10)
