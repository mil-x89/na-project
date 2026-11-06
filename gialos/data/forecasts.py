"""Deterministic fake 3-day forecasts.

Each beach gets its own `random.Random` seeded from its id, so every run (and
every screenshot) shows the same numbers. Weather and wind are random; water
clarity is computed from them with the demo clarity model (clarity_model.py).
The real prediction system will replace `get_forecast()` later; its return type
is the contract.
"""

import random
from dataclasses import dataclass

from gialos.data.beaches import BEACHES
from gialos.data.clarity_model import ClarityInputs, estimate_waves, exposure_for, predict

FORECAST_DAYS = 3

CONDITIONS = ("sunny", "partly_cloudy", "cloudy", "rain")
CONDITION_WEIGHTS = (55, 25, 12, 8)
WIND_DIRECTIONS = ("N", "NE", "E", "SE", "S", "SW", "W", "NW")
RAIN_DAY_MM = 8   # rain assumed on a "rain" day, for the clarity model

# Upper km/h bound of Beaufort 0..11; anything above is 12.
_BEAUFORT_LIMITS = (1, 5, 11, 19, 28, 38, 49, 61, 74, 88, 102, 117)


@dataclass(frozen=True)
class DayForecast:
    day_index: int          # 0 = today, 1 = tomorrow, 2 = in 2 days
    clarity_score: int      # 0-100
    wind_kmh: int
    wind_direction: str     # one of WIND_DIRECTIONS
    condition: str          # one of CONDITIONS
    temperature_c: int      # air temperature

    @property
    def clarity_level(self) -> str:
        return clarity_level(self.clarity_score)

    @property
    def beaufort(self) -> int:
        return beaufort(self.wind_kmh)


def clarity_level(score: int) -> str:
    if score >= 80:
        return "excellent"
    if score >= 60:
        return "good"
    if score >= 40:
        return "moderate"
    return "poor"


def beaufort(kmh: int) -> int:
    for force, limit in enumerate(_BEAUFORT_LIMITS):
        if kmh <= limit:
            return force
    return 12


def _make_forecast(beach_id: str) -> list[DayForecast]:
    rng = random.Random(f"gialos-{beach_id}")
    days = []
    for day in range(FORECAST_DAYS):
        wind = rng.randint(5, 30)
        condition = rng.choices(CONDITIONS, weights=CONDITION_WEIGHTS)[0]
        temperature = rng.randint(26, 31)
        if condition in ("cloudy", "rain"):
            temperature -= 3
        rng.randint(-6, 8)  # unused draw, kept so weather values stay the same as before
        direction = rng.choice(WIND_DIRECTIONS)
        inputs = _clarity_inputs(beach_id, wind, direction, condition)
        days.append(
            DayForecast(
                day_index=day,
                clarity_score=predict(beach_id, inputs).score,
                wind_kmh=wind,
                wind_direction=direction,
                condition=condition,
                temperature_c=temperature,
            )
        )
    return days


def _clarity_inputs(beach_id: str, wind_kmh: int, wind_direction: str, condition: str) -> ClarityInputs:
    """Clarity-model inputs implied by a day's weather."""
    exposure = exposure_for(beach_id, wind_direction)
    return ClarityInputs(
        wind_kmh=wind_kmh,
        exposure=exposure,
        wave_m=estimate_waves(wind_kmh, exposure),
        rain_mm=RAIN_DAY_MM if condition == "rain" else 0,
    )



FORECASTS: dict[str, list[DayForecast]] = {b.id: _make_forecast(b.id) for b in BEACHES}


def get_forecast(beach_id: str) -> list[DayForecast]:
    """The 3-day forecast for a beach (mock)."""
    return FORECASTS[beach_id]
