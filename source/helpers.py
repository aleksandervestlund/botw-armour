from collections.abc import Iterable
from dataclasses import dataclass
from tkinter import Canvas, Frame, Scrollbar, Tk
from typing import TypedDict


HEIGHT = 0.945


@dataclass(slots=True)
class IndexGenerator:
    _current_idx: int = 0

    def get_next_index(self) -> int:
        idx = self._current_idx
        self._current_idx += 1
        return idx


class ArmourPiece(TypedDict):
    index: int
    upgrades: list[list[tuple[str, int]]]


def format_ingredients(ingredients: Iterable[tuple[str, int]]) -> str:
    return "\n".join(f"{qty} {item}" for item, qty in ingredients)


def create_scrollable_frame(root: Tk, width: float, pos: int) -> Frame:
    canvas = Canvas(
        root,
        width=root.winfo_screenwidth() * width,
        height=root.winfo_screenheight() * HEIGHT,
    )
    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    frame = Frame(canvas)
    frame.bind(
        "<Configure>",
        lambda _: canvas.configure(scrollregion=canvas.bbox("all")),
    )
    canvas.create_window((0, 0), window=frame, anchor="nw")
    canvas.grid(row=0, column=pos, sticky="nw", padx=10, pady=5)
    scrollbar.grid(row=0, column=pos + 1, sticky="ns")
    return frame
