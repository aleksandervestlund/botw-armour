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

    Label(login_window, text="Enter username:").pack(pady=5)

    username_var = StringVar()
    entry = Entry(login_window, textvariable=username_var)
    entry.pack(pady=5)
    entry.focus_set()

    Button(login_window, text="Login", command=on_login).pack(pady=10)
    login_window.bind("<Return>", lambda _: on_login())
