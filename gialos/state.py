"""App state: language, quiz answers, current screen, selected beach."""

from dataclasses import dataclass, field
from typing import Optional

from gialos import i18n

# Screen identifiers
ONBOARDING = "onboarding"     # welcome + preference questions + "finding your beach"
RECOMMENDED = "recommended"   # the single recommended beach
MAP = "map"
DETAIL = "detail"

# Tabs in the bottom navigation bar, in display order
TABS = (RECOMMENDED, MAP)

# Day choices, in forecast order (index = forecast day)
DAYS = ("today", "tomorrow", "day_after")


@dataclass
class Preferences:
    """Answers from the onboarding questions (input for the future recommender)."""

    day: str = "tomorrow"          # "today" | "tomorrow" | "day_after"
    surface: str = "sand"          # "sand" | "pebbles" | "any"
    vibe: str = "any"              # "quiet" | "organized" | "any"
    wind_tolerance: str = "low"    # "low" | "medium" | "high"

    @property
    def day_index(self) -> int:
        return DAYS.index(self.day)


@dataclass
class AppState:
    language: str = i18n.DEFAULT_LANGUAGE
    preferences: Preferences = field(default_factory=Preferences)
    screen: str = ONBOARDING
    onboarding_step: int = 0               # 0 = welcome, 1..N = questions
    matching: bool = False                 # showing "finding your beach"
    reveal_pending: bool = False           # play the entrance animation on the result
    current_tab: str = RECOMMENDED         # tab to return to when leaving detail
    selected_beach_id: Optional[str] = None

    def t(self, key: str, **params) -> str:
        """Translate a string key into the current language."""
        return i18n.t(self.language, key, **params)
