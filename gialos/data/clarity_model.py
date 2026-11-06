"""Demo water-clarity model (PLACEHOLDER for the real prediction system).

A tiny, hand-weighted formula that shows the *shape* of the planned model:

    clarity = beach baseline − wind effect − wave effect − rain effect

- Beach baseline: the beach's typical clarity (in the real system: learned from
  historical and satellite water-quality data).
- Wind: stirs up sediment. Wind blowing from the sea onto the beach ("onshore")
  matters most; wind from the land ("offshore") barely matters.
- Waves: resuspend sand near the shore.
- Rain: runoff carries soil into the sea.

The weights are made up. The fake forecasts (forecasts.py) use `predict()` to
turn each day's wind and rain into a clarity score.
"""

import math
from dataclasses import dataclass

from gialos.data import island
from gialos.data.beaches import get_beach

# Typical clarity per beach (0-100), standing in for satellite history. Invented.
BASELINES = {
    "aliki": 96,
    "saliara": 95,
    "paradise": 92,
    "pachys": 92,
    "trypiti": 91,
    "makryammos": 90,
    "glyfada": 90,
    "livadi": 89,
    "golden_beach": 88,
    "psili_ammos": 88,
}

EXPOSURES = ("offshore", "cross", "onshore")   # from land / sideways / from sea

# Clarity points lost per km/h of wind, by exposure
WIND_WEIGHT = {"offshore": 0.2, "cross": 0.55, "onshore": 1.0}
WAVE_WEIGHT = 18.0          # points per metre of wave height
RAIN_WEIGHT = 1.2           # points per mm of rain in the last 24 h
RAIN_MAX_EFFECT = 25.0

MIN_SCORE, MAX_SCORE = 5, 98

_COMPASS = {"N": 0, "NE": 45, "E": 90, "SE": 135, "S": 180, "SW": 225, "W": 270, "NW": 315}


@dataclass(frozen=True)
class ClarityInputs:
    wind_kmh: float
    exposure: str           # one of EXPOSURES
    wave_m: float
    rain_mm: float


@dataclass(frozen=True)
class ClarityPrediction:
    score: int
    baseline: int
    wind_effect: int        # points removed (>= 0)
    wave_effect: int
    rain_effect: int


def predict(beach_id: str, inputs: ClarityInputs) -> ClarityPrediction:
    baseline = BASELINES[beach_id]
    wind = round(inputs.wind_kmh * WIND_WEIGHT[inputs.exposure])
    waves = round(inputs.wave_m * WAVE_WEIGHT)
    rain = round(min(inputs.rain_mm * RAIN_WEIGHT, RAIN_MAX_EFFECT))
    score = max(MIN_SCORE, min(MAX_SCORE, baseline - wind - waves - rain))
    return ClarityPrediction(score, baseline, wind, waves, rain)


def exposure_for(beach_id: str, wind_direction: str) -> str:
    """Is the wind (given as the direction it blows FROM) onshore at this beach?

    A beach is assumed to face away from the island's centre, so a wind coming
    from that side comes off the sea.
    """
    beach = get_beach(beach_id)
    lats = [p[0] for p in island.ISLAND_OUTLINE]
    lons = [p[1] for p in island.ISLAND_OUTLINE]
    c_lat, c_lon = sum(lats) / len(lats), sum(lons) / len(lons)
    dx = (beach.lon - c_lon) * math.cos(math.radians(c_lat))
    dy = beach.lat - c_lat
    facing = math.degrees(math.atan2(dx, dy)) % 360
    diff = abs((_COMPASS[wind_direction] - facing + 180) % 360 - 180)
    if diff <= 45:
        return "onshore"
    if diff >= 135:
        return "offshore"
    return "cross"


def estimate_waves(wind_kmh: float, exposure: str) -> float:
    """Rough wave height near the shore (m) from wind and exposure."""
    factor = {"offshore": 0.3, "cross": 0.6, "onshore": 1.0}[exposure]
    return round(wind_kmh / 40 * factor, 1)
