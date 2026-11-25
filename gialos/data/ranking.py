"""Mock recommender: picks one beach from the quiz answers.

PLACEHOLDER. The real recommender (later in the semester) will score every beach
by combining the user's preferences with the forecast conditions for the chosen
day (content-based scoring, later learning from user feedback).

For now the pick is a hardcoded lookup on (surface, vibe): an ordered list of
suitable beaches, of which the first one with a real photo is suggested (the app
never recommends a beach that only has a placeholder illustration). The "why
it's your match" reasons are then checked honestly against the beach's
attributes and the fake forecast for the chosen day, so the explanation never
contradicts the data shown on screen. `recommend()` is the contract the real
system will keep.
"""

from dataclasses import dataclass

from gialos.data.beaches import BEACHES, get_beach
from gialos.data.forecasts import get_forecast
from gialos.images import has_photo

# (surface, vibe) -> suitable beaches, best fit first
_LOOKUP: dict[tuple[str, str], tuple[str, ...]] = {
    ("sand", "quiet"): ("paradise", "pachys", "livadi"),
    ("sand", "organized"): ("makryammos", "golden_beach", "psili_ammos", "trypiti"),
    ("sand", "any"): ("pachys", "golden_beach", "paradise"),
    ("pebbles", "quiet"): ("aliki",),
    ("pebbles", "organized"): ("saliara", "glyfada"),
    ("pebbles", "any"): ("saliara", "aliki"),
    ("any", "quiet"): ("aliki", "paradise", "pachys"),
    ("any", "organized"): ("glyfada", "saliara", "golden_beach"),
    ("any", "any"): ("aliki", "pachys"),
}


def _pick(candidates: tuple[str, ...]) -> str:
    """First candidate that has a real photo; failing that, any beach with a
    photo; and only if no beach has one, the first candidate."""
    for beach_id in candidates:
        if has_photo(beach_id):
            return beach_id
    for beach in BEACHES:
        if has_photo(beach.id):
            return beach.id
    return candidates[0]

# Highest wind (km/h) that still counts as a match for each tolerance
_WIND_LIMITS = {"low": 15, "medium": 25, "high": 999}

_SANDY = {"sand", "mixed"}
_PEBBLY = {"pebbles", "marble", "mixed"}


@dataclass(frozen=True)
class Recommendation:
    beach_id: str
    reasons: tuple[str, ...]   # i18n keys without the "reason_" prefix


def recommend(surface: str, vibe: str, wind_tolerance: str, day_index: int) -> Recommendation:
    """The single recommended beach for these answers (mock)."""
    beach_id = _pick(_LOOKUP[(surface, vibe)])
    beach = get_beach(beach_id)
    day = get_forecast(beach_id)[day_index]

    reasons = []
    if surface == "sand" and beach.beach_type in _SANDY:
        reasons.append("sand")
    if surface == "pebbles" and beach.beach_type in _PEBBLY:
        reasons.append("pebbles")
    if vibe != "any" and beach.setting == vibe:
        reasons.append(vibe)
    if day.wind_kmh <= _WIND_LIMITS[wind_tolerance]:
        reasons.append("low_wind" if wind_tolerance == "low" else "wind_ok")
    if day.clarity_score >= 80:
        reasons.append("clear_water")
    if not reasons:
        reasons.append("best_overall")
    return Recommendation(beach_id, tuple(reasons))
