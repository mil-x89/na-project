"""gialos: beach recommender mockup for Thassos.

Run from the project folder:
    flet run main.py
"""

from pathlib import Path

import flet as ft

from gialos.app import GialosApp

# Absolute path, so images load no matter which folder the app is started from.
ASSETS_DIR = Path(__file__).resolve().parent / "assets"


def main(page: ft.Page) -> None:
    GialosApp(page)


if __name__ == "__main__":
    ft.run(main, assets_dir=str(ASSETS_DIR))
