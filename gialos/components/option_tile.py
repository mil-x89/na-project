"""Tappable answer tile for the onboarding questions."""

from typing import Callable

import flet as ft

from gialos import theme


def build_option_tile(
    icon: ft.IconData,
    title: str,
    subtitle: str,
    selected: bool,
    on_click: Callable[[], None],
) -> ft.Container:
    return ft.Container(
        content=ft.Row(
            [
                ft.Container(
                    content=ft.Icon(icon, size=22, color=theme.WHITE if selected else theme.ACCENT),
                    width=48,
                    height=48,
                    alignment=ft.Alignment.CENTER,
                    border_radius=14,
                    bgcolor=theme.ACCENT if selected else theme.ACCENT_5,
                ),
                ft.Column(
                    [
                        ft.Text(title, style=theme.BODY_STRONG),
                        ft.Text(subtitle, style=theme.CAPTION),
                    ],
                    spacing=2,
                    expand=True,
                ),
                ft.Icon(
                    ft.Icons.CHECK_CIRCLE if selected else ft.Icons.RADIO_BUTTON_UNCHECKED,
                    color=theme.ACCENT if selected else theme.LINE,
                    size=24,
                ),
            ],
            spacing=theme.S3,
        ),
        bgcolor=theme.ACCENT_5 if selected else theme.SURFACE,
        border=ft.Border.all(1.5, theme.ACCENT if selected else theme.LINE),
        border_radius=theme.RADIUS_SMALL + 4,
        padding=theme.S3,
        shadow=None if selected else ft.BoxShadow(blur_radius=12, color=theme.SHADOW, offset=ft.Offset(0, 2)),
        ink=True,
        on_click=lambda _: on_click(),
    )
