"""Beach hero: large rounded photo with the name over a soft dark fade."""

from typing import Callable, Optional

import flet as ft

from gialos import theme
from gialos.data.beaches import Beach
from gialos.images import beach_image_src
from gialos.state import AppState


def build_hero(
    state: AppState,
    beach: Beach,
    height: int,
    badge: Optional[str] = None,
    on_click: Optional[Callable[[], None]] = None,
) -> ft.Container:
    layers: list[ft.Control] = [
        ft.Image(src=beach_image_src(beach.id), fit=ft.BoxFit.COVER),
        ft.Container(
            gradient=ft.LinearGradient(
                begin=ft.Alignment.TOP_CENTER,
                end=ft.Alignment.BOTTOM_CENTER,
                colors=["#000A2530", theme.PHOTO_FADE],
                stops=[0.45, 1.0],
            ),
        ),
        ft.Container(
            content=ft.Column(
                [
                    ft.Text(beach.name[state.language], style=theme.DISPLAY, color=theme.WHITE),
                    ft.Text(
                        f"{state.t('type_' + beach.beach_type)} · {state.t('setting_' + beach.setting)}",
                        size=theme.SIZE_BODY,
                        color=theme.WHITE_80,
                    ),
                ],
                spacing=theme.S1,
            ),
            left=theme.S4,
            right=theme.S4,
            bottom=theme.S4,
        ),
    ]
    if badge:
        layers.append(
            ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.AUTO_AWESOME, size=16, color=theme.ACCENT),
                        ft.Text(badge, style=theme.LABEL, color=theme.ACCENT),
                    ],
                    spacing=theme.S1,
                    tight=True,
                ),
                bgcolor=theme.WHITE,
                border_radius=16,
                padding=ft.Padding.symmetric(horizontal=12, vertical=theme.S2),
                left=theme.S3,
                top=theme.S3,
            )
        )
    return ft.Container(
        content=ft.Stack(layers, fit=ft.StackFit.EXPAND),
        height=height,
        border_radius=theme.RADIUS,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        on_click=(lambda _: on_click()) if on_click else None,
    )
