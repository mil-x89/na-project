"""Screen 2: the single recommended beach (the result of the onboarding questions)."""

from typing import TYPE_CHECKING

import flet as ft

from gialos import theme
from gialos.components import icons
from gialos.components.buttons import bottom_bar, primary_button, secondary_button
from gialos.components.hero import build_hero
from gialos.components.info_note import build_info_note
from gialos.components.stats import conditions_grid
from gialos.data.beaches import get_beach
from gialos.data.forecasts import get_forecast

if TYPE_CHECKING:
    from gialos.app import GialosApp

REVEAL_ANIMATION = ft.Animation(600, ft.AnimationCurve.EASE_OUT_BACK)


def _reason_chip(icon: ft.IconData, text: str) -> ft.Container:
    return ft.Container(
        content=ft.Row(
            [ft.Icon(icon, size=16, color=theme.ACCENT), ft.Text(text, style=theme.BODY_STRONG, size=theme.SIZE_SMALL)],
            spacing=6,
            tight=True,
        ),
        bgcolor=theme.ACCENT_5,
        border=ft.Border.all(1, theme.ACCENT_12),
        border_radius=16,
        padding=ft.Padding.symmetric(horizontal=12, vertical=theme.S2),
    )


def build(app: "GialosApp") -> ft.Control:
    state = app.state
    rec = app.recommendation()
    beach = get_beach(rec.beach_id)
    day_index = state.preferences.day_index
    day = get_forecast(beach.id)[day_index]
    day_word = state.t("day_lower_" + state.preferences.day)

    hero = ft.Container(
        content=build_hero(state, beach, theme.HERO_HEIGHT, badge=state.t("top_match"),
                           on_click=lambda: app.open_beach(beach.id)),
        border_radius=theme.RADIUS,
        shadow=ft.BoxShadow(blur_radius=40, spread_radius=-8, color=theme.GLOW, offset=ft.Offset(0, 16)),
        scale=0.85 if state.reveal_pending else 1,
        animate_scale=REVEAL_ANIMATION,
        # Scale only, no opacity fade-in: kept simple as a precaution after blank
        # frames during off-screen testing (cause not confirmed).
    )
    if state.reveal_pending:
        app.queue_reveal(hero)

    why = ft.Container(
        content=ft.Column(
            [
                ft.Text(state.t("why_title"), style=theme.TITLE),
                ft.Row(
                    [_reason_chip(icons.REASONS[r], state.t("reason_" + r)) for r in rec.reasons],
                    wrap=True,
                    spacing=theme.S2,
                    run_spacing=theme.S2,
                ),
            ],
            spacing=theme.S3,
        ),
        bgcolor=theme.SURFACE,
        border_radius=theme.RADIUS,
        padding=theme.CARD_PADDING,
    )

    body = ft.ListView(
        [
            ft.Row(
                [
                    ft.Icon(ft.Icons.AUTO_AWESOME, size=16, color=theme.ACCENT),
                    ft.Text(
                        state.t("your_beach_for", day=day_word),
                        style=theme.LABEL,
                        color=theme.ACCENT,
                        expand=True,
                    ),
                    secondary_button(state.t("change_answers"), app.change_answers, ft.Icons.TUNE),
                ],
                spacing=theme.S2,
            ),
            hero,
            ft.Container(height=theme.S2),
            why,
            ft.Container(height=theme.S2),
            ft.Text(state.t("conditions_title", day=day_word), style=theme.TITLE),
            conditions_grid(state, day),
            ft.Container(height=theme.S2),
            build_info_note(ft.Icons.AUTO_AWESOME, state.t("recommender_note_title"), state.t("recommender_note")),
            ft.Text(state.t("mock_data_note"), style=theme.CAPTION, text_align=ft.TextAlign.CENTER),
        ],
        key=f"result-{beach.id}",
        spacing=theme.S3,
        padding=ft.Padding.only(left=theme.S4, right=theme.S4, top=0, bottom=theme.S4),
        expand=True,
    )
    actions = bottom_bar(
        ft.Row([primary_button(state.t("see_forecast"), lambda: app.open_beach(beach.id), ft.Icons.CALENDAR_MONTH)]),
    )
    return ft.Column([body, actions], spacing=0, expand=True)
