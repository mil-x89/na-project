"""Primary and secondary buttons (full width, thumb-zone sized)."""

from typing import Callable, Optional

import flet as ft

from gialos import theme


def primary_button(text: str, on_click: Callable[[], None], icon: Optional[ft.IconData] = None) -> ft.FilledButton:
    return ft.FilledButton(
        content=text,
        icon=icon,
        height=theme.BUTTON_HEIGHT,
        expand=True,
        style=ft.ButtonStyle(
            bgcolor=theme.ACCENT,
            color=theme.WHITE,
            elevation=0,
            shape=ft.RoundedRectangleBorder(radius=theme.BUTTON_HEIGHT / 2),
            text_style=ft.TextStyle(size=theme.SIZE_BODY, weight=theme.BOLD),
        ),
        on_click=lambda _: on_click(),
    )


def secondary_button(text: str, on_click: Callable[[], None], icon: Optional[ft.IconData] = None) -> ft.TextButton:
    return ft.TextButton(
        content=text,
        icon=icon,
        height=44,
        style=ft.ButtonStyle(
            color=theme.ACCENT,
            shape=ft.RoundedRectangleBorder(radius=22),
            text_style=ft.TextStyle(size=theme.SIZE_SMALL, weight=theme.BOLD),
        ),
        on_click=lambda _: on_click(),
    )


def bottom_bar(*controls: ft.Control) -> ft.Container:
    """Sticky action area at the bottom of a screen (thumb zone)."""
    return ft.Container(
        content=ft.Column(list(controls), spacing=theme.S1, horizontal_alignment=ft.CrossAxisAlignment.STRETCH),
        padding=ft.Padding.only(left=theme.S4, right=theme.S4, top=theme.S3, bottom=theme.S4),
        bgcolor=theme.BACKGROUND,
        border=ft.Border.only(top=ft.BorderSide(1, theme.LINE)),
    )
