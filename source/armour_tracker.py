import json
import os
from collections import defaultdict
from collections.abc import Iterable, Sequence
from dataclasses import dataclass, field
from tkinter import (
    Button,
    Checkbutton,
    Frame,
    IntVar,
    Label,
    StringVar,
    Tk,
    messagebox,
)

from source.botw_armour_data import BOTW_ARMOUR_DATA
from source.constants import (
    ARMOUR_WIDTH,
    DATA_FOLDER,
    FONT,
    PADX,
    STAR,
    STORING_SEPARATOR,
    TOTALS_WIDTH,
)
from source.game import Game
from source.helpers import create_scrollable_frame, format_ingredients
from source.totk_armour_data import TOTK_ARMOUR_DATA


@dataclass(slots=True)
class ArmourTracker:
    root: Tk
    username: str
    game: Game = field(init=False, default=Game.BOTW)
    checkbox_vars: dict[tuple[str, int], IntVar] = field(
        init=False, default_factory=dict
    )
    collected_vars: dict[str, IntVar] = field(init=False, default_factory=dict)
    total_labels: dict[str, Checkbutton | Label] = field(
        init=False, default_factory=dict
    )
    toggle_button: Button = field(init=False)
    armour_frame: Frame = field(init=False)
    totals_frame: Frame = field(init=False)
    game_var: StringVar = field(init=False)

    @property
    def save_path(self) -> str:
        return os.path.join(
            f"{DATA_FOLDER}_{self.game}", f"{self.username}.json"
        )

    def __post_init__(self) -> None:
        if not self.username.isidentifier():
            raise ValueError(f"Invalid username: {self.username}.")

        self.root.title(f"Zelda {self.game.upper()} Armour Tracker")

        self.game_var = StringVar(value=self.game.value)
        self.toggle_button = Button(
            self.root,
            text=(
                "Switch to "
                f"{Game.TOTK.upper() if self.game is Game.BOTW else Game.BOTW.upper()}"
            ),
            command=self.toggle_game,
            font=FONT,
        )
        self.toggle_button.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

        self.load()

        self.root.attributes("-fullscreen", True)

    def toggle_game(self) -> None:
        # Switch game
        self.game = Game.TOTK if self.game is Game.BOTW else Game.BOTW
        self.game_var.set(self.game.value)
        self.toggle_button.config(
            text=f"Switch to {'TOTK' if self.game is Game.BOTW else 'BOTW'}"
        )
        # Destroy old frames and rebuild
        self.armour_frame.destroy()
        self.totals_frame.destroy()
        self.checkbox_vars.clear()
        self.collected_vars.clear()
        self.total_labels.clear()

        self.load()

    def load(self) -> None:
        self.armour_frame = create_scrollable_frame(self.root, ARMOUR_WIDTH, 0)
        self.totals_frame = create_scrollable_frame(self.root, TOTALS_WIDTH, 2)

        self.build_headers()
        self.build_rows()
        self.update_totals()

        if os.path.exists(self.save_path):
            self.load_state()

    def build_headers(self) -> None:
        Label(self.armour_frame, text="Armour Piece", font=FONT).grid(
            row=0, column=0, sticky="w", padx=5, pady=5
        )

        for i in range(1, 5):
            Label(self.armour_frame, text=STAR * i, font=FONT).grid(
                row=0, column=i, padx=5
            )

        Label(self.totals_frame, text="Item", font=FONT).grid(
            row=0, column=0, sticky="w", padx=PADX
        )
        Label(self.totals_frame, text="Qty", font=FONT).grid(
            row=0, column=1, sticky="w", padx=PADX
        )
        Label(self.totals_frame, text="✓", font=FONT).grid(
            row=0, column=2, sticky="w", padx=PADX
        )

    def build_rows(self) -> None:
        armour_data = (
            BOTW_ARMOUR_DATA if self.game is Game.BOTW else TOTK_ARMOUR_DATA
        )
        sorted_armour = sorted(
            armour_data.items(), key=lambda x: x[1]["index"]
        )

        for row_index, (armour_name, armour_info) in enumerate(
            sorted_armour, 1
        ):
            upgrades = armour_info["upgrades"]
            Label(self.armour_frame, text=armour_name).grid(
                row=row_index, column=0, sticky="w", padx=5
            )

            if not upgrades:
                Label(self.armour_frame, text="\n").grid(
                    row=row_index, column=1, sticky="w", padx=5
                )
                continue

            self.build_row(row_index, armour_name, upgrades)

    def build_row(
        self,
        row_index: int,
        armour_name: str,
        upgrades: Sequence[Iterable[tuple[str, int]]],
    ) -> None:
        for level in range(4):
            var = IntVar()
            item_text = format_ingredients(sorted(upgrades[level]))
            checkbutton = Checkbutton(
                self.armour_frame,
                text=item_text,
                variable=var,
                command=lambda n=armour_name, l=level: self.validate_checkbox(  # type: ignore
                    n, l
                ),
                anchor="w",
                justify="left",
            )
            checkbutton.grid(
                row=row_index, column=level + 1, sticky="w", padx=PADX
            )
            self.checkbox_vars[(armour_name, level)] = var

    def update_totals(self) -> None:
        totals: defaultdict[str, int] = defaultdict(int)
        armour_data = (
            BOTW_ARMOUR_DATA if self.game is Game.BOTW else TOTK_ARMOUR_DATA
        )

        for armour_name, armour_info in armour_data.items():
            upgrades = armour_info["upgrades"]

            for level, ingredients in enumerate(upgrades):
                if self.checkbox_vars[(armour_name, level)].get() != 0:
                    continue

                for item, qty in ingredients:
                    totals[item] += qty

        for label in self.total_labels.values():
            label.destroy()

        self.total_labels.clear()

        for row_offset, (item, qty) in enumerate(sorted(totals.items()), 1):
            if self.collected_vars.get(item, IntVar()).get():
                continue

            item_label = Label(self.totals_frame, text=item)
            qty_label = Label(self.totals_frame, text=str(qty))

            item_label.grid(row=row_offset, column=0, sticky="w", padx=PADX)
            qty_label.grid(row=row_offset, column=1, sticky="w", padx=PADX)

            if not (var := self.collected_vars.get(item)):
                var = IntVar()
                self.collected_vars[item] = var

            cb = Checkbutton(
                self.totals_frame,
                variable=var,
                command=lambda: (self.update_totals(), self.save_state()),  # type: ignore
            )
            cb.grid(row=row_offset, column=2)

            self.total_labels[item] = item_label
            self.total_labels[f"{item}_qty"] = qty_label
            self.total_labels[f"{item}_cb"] = cb

    def validate_checkbox(self, armour_name: str, level: int) -> None:
        var = self.checkbox_vars[(armour_name, level)]

        if var.get() == 1 and level > 0:
            prev_var = self.checkbox_vars[(armour_name, level - 1)]

            if prev_var.get() == 0:
                var.set(0)
                messagebox.showerror(
                    "Upgrade Error",
                    f"You must check off {STAR * level} before checking "
                    f"{STAR * (level + 1)} for {armour_name!r}.",
                )
                return

        self.update_totals()
        self.save_state()

    def save_state(self) -> None:
        state = {
            "checkboxes": {
                f"{armour}{STORING_SEPARATOR}{level}": value.get()
                for (armour, level), value in self.checkbox_vars.items()
            },
            "collected": {
                key: value.get() for key, value in self.collected_vars.items()
            },
        }

        with open(self.save_path, "w", encoding="utf-8") as file:
            json.dump(state, file, indent=2)

    def load_state(self) -> None:
        try:  # pylint: disable=too-many-try-statements
            with open(self.save_path, encoding="utf-8") as file:
                state: dict[str, dict[str, int]] = json.load(file)
        except FileNotFoundError:
            return

        for key, value in state.get("checkboxes", {}).items():
            name, level = key.split(STORING_SEPARATOR)
            self.checkbox_vars[(name, int(level))].set(value)

        for item, value in state.get("collected", {}).items():
            self.collected_vars[item].set(value)

        self.update_totals()
