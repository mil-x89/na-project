"""Screen 1: onboarding. Welcome, then one question per page, then "finding your beach"."""

from typing import TYPE_CHECKING

import flet as ft

from gialos import theme
from gialos.components import icons
from gialos.components.buttons import bottom_bar, primary_button
from gialos.components.option_tile import build_option_tile
from gialos.images import beach_image_src

if TYPE_CHECKING:
    from gialos.app import GialosApp

# (preference field, option values). Text keys: "q_<field>", "opt_<field>_<value>",
# "desc_<field>_<value>".
QUESTIONS = (
    ("day", ("today", "tomorrow", "day_after")),
    ("surface", ("sand", "pebbles", "any")),
    ("vibe", ("quiet", "organized", "any")),
    ("wind_tolerance", ("low", "medium", "high")),
)

WELCOME_BEACH = "golden_beach"   # image on the welcome screen


def _welcome(app: "GialosApp") -> ft.Control:
    state = app.state
    points = [
        (ft.Icons.WATER_DROP, "welcome_point_1"),
        (ft.Icons.AIR, "welcome_point_2"),
        (ft.Icons.AUTO_AWESOME, "welcome_point_3"),
    ]
    art = ft.Container(
        content=ft.Image(src=beach_image_src(WELCOME_BEACH), fit=ft.BoxFit.COVER),
        height=200,
        border_radius=theme.RADIUS,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        shadow=theme.soft_shadow(),
    )
    body = ft.ListView(
        [
            art,
            ft.Container(height=theme.S2),
            ft.Text(state.t("welcome_eyebrow"), style=theme.LABEL, color=theme.ACCENT),
            ft.Text(state.t("welcome_title"), style=theme.DISPLAY),
            ft.Text(state.t("welcome_body"), style=theme.BODY),
            ft.Container(height=theme.S2),
            *[
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Icon(icon, size=18, color=theme.ACCENT),
                            width=36,
                            height=36,
                            alignment=ft.Alignment.CENTER,
                            shape=ft.BoxShape.CIRCLE,
                            bgcolor=theme.ACCENT_12,
                        ),
                        ft.Text(state.t(key), style=theme.BODY, color=theme.INK, expand=True),
                    ],
                    spacing=12,
                )
                for icon, key in points
            ],
        ],
        spacing=theme.S3,
        padding=ft.Padding.only(left=theme.S4, right=theme.S4, top=theme.S2, bottom=theme.S4),
        expand=True,
    )
    return ft.Column(
        [body, bottom_bar(ft.Row([primary_button(state.t("get_started"), app.onboarding_next, ft.Icons.ARROW_FORWARD)]))],
        spacing=0,
        expand=True,
    )


def _question(app: "GialosApp", number: int) -> ft.Control:
    state = app.state
    field, options = QUESTIONS[number - 1]
    is_last = number == len(QUESTIONS)

    def choose(value: str):
        setattr(state.preferences, field, value)
        app.render()

    header = ft.Row(
        [
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK_IOS_NEW,
                icon_color=theme.INK,
                icon_size=18,
                tooltip=state.t("back"),
                on_click=lambda _: app.onboarding_back(),
            ),
            ft.Container(
                content=ft.ProgressBar(
                    value=number / len(QUESTIONS),
                    color=theme.ACCENT,
                    bgcolor=theme.LINE,
                    bar_height=6,
                    border_radius=3,
                ),
                expand=True,
            ),
            ft.Text(f"{number}/{len(QUESTIONS)}", style=theme.LABEL),
        ],
        spacing=12,
    )
    tiles = [
        build_option_tile(
            icons.OPTIONS[(field, value)],
            state.t(f"opt_{field}_{value}"),
            state.t(f"desc_{field}_{value}"),
            getattr(state.preferences, field) == value,
            lambda v=value: choose(v),
        )
        for value in options
    ]
    body = ft.ListView(
        [
            header,
            ft.Container(height=theme.S2),
            ft.Text(state.t("step_counter", n=number, total=len(QUESTIONS)), style=theme.LABEL, color=theme.ACCENT),
            ft.Text(state.t("q_" + field), style=theme.DISPLAY),
            ft.Container(height=theme.S2),
            *tiles,
            ft.Container(height=theme.S2),
            ft.Row(
                [
                    ft.Icon(ft.Icons.AUTO_AWESOME, size=16, color=theme.INK_60),
                    ft.Text(state.t("recommender_hint"), style=theme.CAPTION, expand=True),
                ],
                spacing=theme.S2,
            ),
        ],
        key=f"question-{field}",
        spacing=12,
        padding=ft.Padding.only(left=theme.S3, right=theme.S4, top=0, bottom=theme.S4),
        expand=True,
    )
    cta = primary_button(
        state.t("find_my_beach" if is_last else "next"),
        app.onboarding_next,
        ft.Icons.AUTO_AWESOME if is_last else ft.Icons.ARROW_FORWARD,
    )
    return ft.Column([body, bottom_bar(ft.Row([cta]))], spacing=0, expand=True)


def _matching(app: "GialosApp") -> ft.Control:
    state = app.state
    return ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.ProgressRing(width=56, height=56, stroke_width=5, color=theme.ACCENT),
                    width=112,
                    height=112,
                    alignment=ft.Alignment.CENTER,
                    shape=ft.BoxShape.CIRCLE,
                    bgcolor=theme.ACCENT_5,
                ),
                ft.Container(height=theme.S2),
                ft.Text(state.t("matching_title"), style=theme.TITLE, text_align=ft.TextAlign.CENTER),
                ft.Text(state.t("matching_body"), style=theme.BODY, text_align=ft.TextAlign.CENTER),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=theme.S2,
        ),
        alignment=ft.Alignment.CENTER,
        padding=theme.S6,
        expand=True,
    )


def build(app: "GialosApp") -> ft.Control:
    if app.state.matching:
        return _matching(app)
    if app.state.onboarding_step == 0:
        return _welcome(app)
    return _question(app, app.state.onboarding_step)
