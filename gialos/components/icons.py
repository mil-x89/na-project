"""Icon choices shared across screens."""

import flet as ft

WEATHER = {
    "sunny": ft.Icons.WB_SUNNY,
    "partly_cloudy": ft.Icons.WB_CLOUDY,
    "cloudy": ft.Icons.CLOUD,
    "rain": ft.Icons.UMBRELLA,
}

BEACH_TYPE = {
    "sand": ft.Icons.BEACH_ACCESS,
    "pebbles": ft.Icons.GRAIN,
    "mixed": ft.Icons.GRAIN,
    "marble": ft.Icons.GRAIN,
}

SETTING = {
    "organized": ft.Icons.DECK,
    "quiet": ft.Icons.SPA,
}

# Quiz options: (question field, value) -> icon
OPTIONS = {
    ("day", "today"): ft.Icons.WB_SUNNY,
    ("day", "tomorrow"): ft.Icons.EVENT,
    ("day", "day_after"): ft.Icons.DATE_RANGE,
    ("surface", "sand"): ft.Icons.BEACH_ACCESS,
    ("surface", "pebbles"): ft.Icons.GRAIN,
    ("surface", "any"): ft.Icons.SHUFFLE,
    ("vibe", "quiet"): ft.Icons.SPA,
    ("vibe", "organized"): ft.Icons.DECK,
    ("vibe", "any"): ft.Icons.SHUFFLE,
    ("wind_tolerance", "low"): ft.Icons.WATER,
    ("wind_tolerance", "medium"): ft.Icons.AIR,
    ("wind_tolerance", "high"): ft.Icons.KITESURFING,
}

REASONS = {
    "sand": ft.Icons.BEACH_ACCESS,
    "pebbles": ft.Icons.GRAIN,
    "quiet": ft.Icons.SPA,
    "organized": ft.Icons.DECK,
    "low_wind": ft.Icons.WATER,
    "wind_ok": ft.Icons.AIR,
    "clear_water": ft.Icons.WATER_DROP,
    "best_overall": ft.Icons.STAR,
}
