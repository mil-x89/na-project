"""3-day forecast as three side-by-side day columns, easy to compare at a glance."""

import flet as ft

from gialos import theme
from gialos.components import icons
from gialos.data.forecasts import DayForecast
from gialos.state import AppState


def _row(icon: ft.IconData, text: str, color: str = theme.INK_80) -> ft.Row:
    return ft.Row(
        [ft.Icon(icon, size=14, color=theme.INK_60), ft.Text(text, size=theme.SIZE_SMALL, color=color)],
        spacing=theme.S1,
        tight=True,
    )


def _day_column(state: AppState, day: DayForecast, highlighted: bool) -> ft.Container:
    level = day.clarity_level
    color = theme.CLARITY_COLORS[level]
    top = (
        ft.Text(state.t("your_day"), style=theme.LABEL, color=theme.ACCENT)
        if highlighted
        else ft.Text(" ", style=theme.LABEL)
    )
    return ft.Container(
        content=ft.Column(
            [
                top,
                ft.Text(state.t(f"day_{day.day_index}"), style=theme.BODY_STRONG),
                ft.Icon(icons.WEATHER[day.condition], size=28, color=theme.ACCENT_DEEP),
                ft.Text(str(day.clarity_score), size=theme.SIZE_DISPLAY, weight=theme.BOLD, color=color),
                ft.Text(state.t("level_" + level), style=theme.LABEL, color=color),
                ft.Container(height=1, bgcolor=theme.LINE, margin=ft.Margin.symmetric(vertical=theme.S1)),
                _row(ft.Icons.AIR, state.t("kmh", kmh=day.wind_kmh)),
                _row(
                    ft.Icons.NAVIGATION,
                    state.t("wind_detail_short", dir=state.t("dir_" + day.wind_direction), bft=day.beaufort),
                ),
                _row(ft.Icons.THERMOSTAT, state.t("temperature_value", temp=day.temperature_c)),
            ],
            spacing=6,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=theme.ACCENT_5 if highlighted else theme.SURFACE,
        border=ft.Border.all(1.5, theme.ACCENT if highlighted else theme.SURFACE),
        border_radius=theme.RADIUS_SMALL,
        padding=ft.Padding.symmetric(horizontal=theme.S2, vertical=12),
        expand=True,
    )


def build_forecast_strip(state: AppState, forecast: list[DayForecast], highlight_index: int) -> ft.Column:
    return ft.Column(
        [
            ft.Row(
                [_day_column(state, d, d.day_index == highlight_index) for d in forecast],
                spacing=theme.S2,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
            ft.Row(
                [
                    ft.Icon(ft.Icons.WATER_DROP, size=14, color=theme.INK_60),
                    ft.Text(f"{state.t('clarity')} (0–100)", style=theme.CAPTION),
                ],
                spacing=theme.S1,
            ),
        ],
        spacing=theme.S2,
    )
