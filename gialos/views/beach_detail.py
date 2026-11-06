"""Screen 4: beach detail + 3-day forecast."""

from typing import TYPE_CHECKING

import flet as ft

from gialos import theme
from gialos.components.forecast_strip import build_forecast_strip
from gialos.components.hero import build_hero
from gialos.components.info_note import build_info_note
from gialos.data.beaches import get_beach
from gialos.data.forecasts import get_forecast

if TYPE_CHECKING:
    from gialos.app import GialosApp


def build(app: "GialosApp") -> ft.Control:
    state = app.state
    beach = get_beach(state.selected_beach_id)
    is_match = beach.id == app.recommendation().beach_id
    about = ft.Container(
        content=ft.Column(
            [
                ft.Text(state.t("about"), style=theme.LABEL),
                ft.Text(beach.description[state.language], style=theme.BODY),
            ],
            spacing=theme.S2,
        ),
        bgcolor=theme.SURFACE,
        border_radius=theme.RADIUS,
        padding=theme.CARD_PADDING,
    )
    return ft.ListView(
        [
            build_hero(
                state,
                beach,
                theme.DETAIL_HERO_HEIGHT,
                badge=state.t("top_match") if is_match else None,
            ),
            about,
            ft.Container(height=theme.S2),
            ft.Text(state.t("forecast_title"), style=theme.TITLE),
            build_forecast_strip(state, get_forecast(beach.id), state.preferences.day_index),
            ft.Container(height=theme.S2),
            build_info_note(ft.Icons.INSIGHTS, state.t("prediction_note_title"), state.t("prediction_note")),
            ft.Text(state.t("mock_data_note"), style=theme.CAPTION, text_align=ft.TextAlign.CENTER),
        ],
        key=f"detail-{beach.id}",
        spacing=theme.S3,
        padding=ft.Padding.only(left=theme.S4, right=theme.S4, top=theme.S2, bottom=theme.S6),
        expand=True,
    )
