from tkinter import Tk

from source.prompt_login import prompt_login


def main() -> None:
    root = Tk()
    prompt_login(root)
    root.mainloop()


if __name__ == "__main__":
    main()
