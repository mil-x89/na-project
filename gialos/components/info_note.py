"""Info box that explains a planned system (recommender / prediction)."""

import flet as ft

from gialos import theme


def build_info_note(icon: ft.IconData, title: str, body: str) -> ft.Container:
    return ft.Container(
        content=ft.Row(
            [
                ft.Container(
                    content=ft.Icon(icon, color=theme.ACCENT, size=20),
                    width=40,
                    height=40,
                    alignment=ft.Alignment.CENTER,
                    shape=ft.BoxShape.CIRCLE,
                    bgcolor=theme.ACCENT_12,
                ),
                ft.Column(
                    [
                        ft.Text(title, style=theme.BODY_STRONG),
                        ft.Text(body, style=theme.CAPTION),
                    ],
                    spacing=theme.S1,
                    expand=True,
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.START,
            spacing=theme.S3,
        ),
        bgcolor=theme.ACCENT_5,
        border=ft.Border.all(1, theme.ACCENT_12),
        border_radius=theme.RADIUS,
        padding=theme.CARD_PADDING,
    )
