"""Value-first stat tiles and the conditions grid for one forecast day."""

import flet as ft

from gialos import theme
from gialos.components import icons
from gialos.data.forecasts import DayForecast
from gialos.state import AppState


def stat_tile(icon: ft.IconData, label: str, value: str, sub: str, value_color: str = theme.INK) -> ft.Container:
    """Small card: label on top, big value, one line of detail."""
    return ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [ft.Icon(icon, size=16, color=theme.ACCENT), ft.Text(label, style=theme.LABEL)],
                    spacing=6,
                ),
                ft.Text(value, size=theme.SIZE_TITLE, weight=theme.BOLD, color=value_color),
                ft.Text(sub, style=theme.CAPTION, max_lines=1),
            ],
            spacing=theme.S1,
        ),
        bgcolor=theme.SURFACE,
        border_radius=theme.RADIUS_SMALL,
        padding=theme.S3,
        expand=True,
    )


def conditions_grid(state: AppState, day: DayForecast) -> ft.Column:
    """2x2 grid: water clarity, wind, weather, air temperature."""
    level = day.clarity_level
    clarity = stat_tile(
        ft.Icons.WATER_DROP,
        state.t("clarity"),
        f"{day.clarity_score}/100",
        state.t("level_" + level),
        theme.CLARITY_COLORS[level],
    )
    wind = stat_tile(
        ft.Icons.AIR,
        state.t("wind"),
        state.t("kmh", kmh=day.wind_kmh),
        state.t("wind_detail", dir=state.t("dir_" + day.wind_direction), bft=day.beaufort),
    )
    weather = stat_tile(
        icons.WEATHER[day.condition],
        state.t("weather"),
        state.t("cond_" + day.condition),
        "",
    )
    air = stat_tile(
        ft.Icons.THERMOSTAT,
        state.t("temperature"),
        state.t("temperature_value", temp=day.temperature_c),
        "",
    )
    return ft.Column(
        [ft.Row([clarity, wind], spacing=12), ft.Row([weather, air], spacing=12)],
        spacing=12,
    )
