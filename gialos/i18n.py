"""All user-facing strings, in English ("en") and Greek ("el").

Views never hardcode text: they call `t(lang, key, **params)`.
Beach names and descriptions live with the beach data (gialos/data/beaches.py)
because they belong to each beach, but they are bilingual in the same way.
"""

LANGUAGES = ("en", "el")
DEFAULT_LANGUAGE = "en"

STRINGS: dict[str, dict[str, str]] = {
    "en": {
        "app_name": "gialos",
        "switch_language": "Ελληνικά",
        "switch_language_short": "ΕΛ",
        "back": "Back",
        "mock_data_note": "Mockup: all data shown is simulated.",
        # Welcome
        "welcome_eyebrow": "Thassos beach finder",
        "welcome_title": "Find your perfect beach on Thassos",
        "welcome_body": "Answer 4 quick questions. We'll match you with one beach "
        "using the water clarity and wind forecast.",
        "welcome_point_1": "Water clarity forecast for the next 3 days",
        "welcome_point_2": "Wind and weather for every beach",
        "welcome_point_3": "One clear pick, explained",
        "get_started": "Get started",
        # Questions
        "step_counter": "Question {n} of {total}",
        "next": "Next",
        "find_my_beach": "Find my beach",
        "q_day": "When are you going?",
        "q_surface": "Sand or pebbles?",
        "q_vibe": "What kind of beach day?",
        "q_wind_tolerance": "How do you feel about wind?",
        "opt_day_today": "Today",
        "opt_day_tomorrow": "Tomorrow",
        "opt_day_day_after": "In 2 days",
        "desc_day_today": "Heading out now",
        "desc_day_tomorrow": "Planning ahead",
        "desc_day_day_after": "Day after tomorrow",
        "opt_surface_sand": "Sand",
        "opt_surface_pebbles": "Pebbles",
        "opt_surface_any": "Either",
        "desc_surface_sand": "Soft sand underfoot",
        "desc_surface_pebbles": "Crystal water over pebbles",
        "desc_surface_any": "No preference",
        "opt_vibe_quiet": "Quiet",
        "opt_vibe_organized": "Organized",
        "opt_vibe_any": "Either",
        "desc_vibe_quiet": "Few people, nature, no sunbeds",
        "desc_vibe_organized": "Sunbeds, beach bar, showers",
        "desc_vibe_any": "Both work for me",
        "opt_wind_tolerance_low": "Calm only",
        "opt_wind_tolerance_medium": "A breeze is fine",
        "opt_wind_tolerance_high": "Wind is fine",
        "desc_wind_tolerance_low": "Flat, still water",
        "desc_wind_tolerance_medium": "Some ripples are OK",
        "desc_wind_tolerance_high": "Waves don't bother me",
        "recommender_hint": "Your answers are the input for the recommender.",
        # Matching
        "matching_title": "Finding your beach…",
        "matching_body": "Matching your answers with each beach's forecast.",
        # Result (recommended)
        "nav_recommended": "Your beach",
        "nav_map": "Map",
        "top_match": "Top match",
        "your_beach_for": "Your beach for {day}",
        "why_title": "Why it's your match",
        "reason_sand": "Sandy beach",
        "reason_pebbles": "Pebbles",
        "reason_quiet": "Quiet",
        "reason_organized": "Organized",
        "reason_low_wind": "Low wind",
        "reason_wind_ok": "Wind within your limit",
        "reason_clear_water": "Very clear water",
        "reason_best_overall": "Best overall conditions",
        "conditions_title": "Conditions {day}",
        "see_forecast": "See 3-day forecast",
        "change_answers": "Change answers",
        "recommender_note_title": "How the recommendation will work",
        "recommender_note": "The recommender will score every beach by combining "
        "your answers with the forecast for the day you chose (content-based "
        "scoring, later learning from your feedback). Mockup: the pick comes from "
        "a fixed lookup.",
        "day_lower_today": "today",
        "day_lower_tomorrow": "tomorrow",
        "day_lower_day_after": "in 2 days",
        # Map
        "map_title": "Thassos",
        "map_hint": "Tap a pin to open a beach. Colors show water clarity {day}.",
        "legend_match": "Your match",
        "osm_credit": "© OpenStreetMap contributors",
        "your_match_card": "Your match",
        # Beach detail
        "about": "About",
        "forecast_title": "3-day forecast",
        "day_0": "Today",
        "day_1": "Tomorrow",
        "day_2": "In 2 days",
        "your_day": "Your day",
        "clarity": "Water clarity",
        "wind": "Wind",
        "weather": "Weather",
        "temperature": "Air",
        "wind_detail": "{dir} · {bft} Bft",
        "wind_detail_short": "{dir} · {bft} Bft",
        "kmh": "{kmh} km/h",
        "temperature_value": "{temp}°C",
        "prediction_note_title": "How this forecast will work",
        "prediction_note": "The prediction system will forecast water clarity for "
        "each beach for the next 3 days from wind speed and direction, waves, "
        "rainfall and historical/satellite water-quality data. Weather and wind "
        "will come from a weather forecast source.",
        # Beach types and settings
        "type_sand": "Sandy beach",
        "type_pebbles": "Pebble beach",
        "type_mixed": "Sand & pebbles",
        "type_marble": "Marble pebbles",
        "setting_organized": "Organized",
        "setting_quiet": "Quiet",
        # Forecast vocab
        "level_excellent": "Excellent",
        "level_good": "Good",
        "level_moderate": "Moderate",
        "level_poor": "Poor",
        "cond_sunny": "Sunny",
        "cond_partly_cloudy": "Partly cloudy",
        "cond_cloudy": "Cloudy",
        "cond_rain": "Rain",
        "dir_N": "N",
        "dir_NE": "NE",
        "dir_E": "E",
        "dir_SE": "SE",
        "dir_S": "S",
        "dir_SW": "SW",
        "dir_W": "W",
        "dir_NW": "NW",
    },
    "el": {
        "app_name": "gialos",
        "switch_language": "English",
        "switch_language_short": "EN",
        "back": "Πίσω",
        "mock_data_note": "Πρωτότυπο: όλα τα δεδομένα είναι προσομοιωμένα.",
        # Welcome
        "welcome_eyebrow": "Παραλίες της Θάσου",
        "welcome_title": "Βρες την ιδανική σου παραλία στη Θάσο",
        "welcome_body": "Απάντησε σε 4 γρήγορες ερωτήσεις. Θα σου προτείνουμε μία "
        "παραλία με βάση την πρόγνωση για τη διαύγεια του νερού και τον αέρα.",
        "welcome_point_1": "Πρόγνωση διαύγειας νερού για τις επόμενες 3 μέρες",
        "welcome_point_2": "Άνεμος και καιρός για κάθε παραλία",
        "welcome_point_3": "Μία ξεκάθαρη πρόταση, με εξήγηση",
        "get_started": "Ας ξεκινήσουμε",
        # Questions
        "step_counter": "Ερώτηση {n} από {total}",
        "next": "Επόμενο",
        "find_my_beach": "Βρες την παραλία μου",
        "q_day": "Πότε θα πας;",
        "q_surface": "Άμμος ή βότσαλο;",
        "q_vibe": "Τι είδους παραλία προτιμάς;",
        "q_wind_tolerance": "Πώς τα πας με τον αέρα;",
        "opt_day_today": "Σήμερα",
        "opt_day_tomorrow": "Αύριο",
        "opt_day_day_after": "Μεθαύριο",
        "desc_day_today": "Ξεκινάω τώρα",
        "desc_day_tomorrow": "Το σχεδιάζω από πριν",
        "desc_day_day_after": "Σε 2 μέρες",
        "opt_surface_sand": "Άμμος",
        "opt_surface_pebbles": "Βότσαλο",
        "opt_surface_any": "Και τα δύο",
        "desc_surface_sand": "Απαλή άμμος στα πόδια",
        "desc_surface_pebbles": "Κρυστάλλινα νερά πάνω από βότσαλα",
        "desc_surface_any": "Δεν έχω προτίμηση",
        "opt_vibe_quiet": "Ήσυχη",
        "opt_vibe_organized": "Οργανωμένη",
        "opt_vibe_any": "Και τα δύο",
        "desc_vibe_quiet": "Λίγος κόσμος, φύση, χωρίς ξαπλώστρες",
        "desc_vibe_organized": "Ξαπλώστρες, beach bar, ντους",
        "desc_vibe_any": "Μου κάνουν και τα δύο",
        "opt_wind_tolerance_low": "Μόνο νηνεμία",
        "opt_wind_tolerance_medium": "Ένα αεράκι είναι εντάξει",
        "opt_wind_tolerance_high": "Δεν με πειράζει ο αέρας",
        "desc_wind_tolerance_low": "Ήρεμα νερά, θάλασσα λάδι",
        "desc_wind_tolerance_medium": "Λίγος κυματισμός δεν πειράζει",
        "desc_wind_tolerance_high": "Τα κύματα δεν με ενοχλούν",
        "recommender_hint": "Το σύστημα συστάσεων θα χρησιμοποιεί τις απαντήσεις σου.",
        # Matching
        "matching_title": "Ψάχνουμε την παραλία σου…",
        "matching_body": "Συνδυάζουμε τις απαντήσεις σου με την πρόγνωση κάθε "
        "παραλίας.",
        # Result (recommended)
        "nav_recommended": "Η παραλία σου",
        "nav_map": "Χάρτης",
        "top_match": "Κορυφαία επιλογή",
        "your_beach_for": "Η παραλία σου για {day}",
        "why_title": "Γιατί σου ταιριάζει",
        "reason_sand": "Αμμουδιά",
        "reason_pebbles": "Βότσαλο",
        "reason_quiet": "Ήσυχη",
        "reason_organized": "Οργανωμένη",
        "reason_low_wind": "Λίγος αέρας",
        "reason_wind_ok": "Αέρας μέσα στα όριά σου",
        "reason_clear_water": "Πολύ καθαρά νερά",
        "reason_best_overall": "Οι καλύτερες συνθήκες συνολικά",
        "conditions_title": "Συνθήκες {day}",
        "see_forecast": "Δες την πρόγνωση 3 ημερών",
        "change_answers": "Άλλαξε τις απαντήσεις",
        "recommender_note_title": "Πώς θα λειτουργεί η πρόταση",
        "recommender_note": "Το σύστημα συστάσεων θα βαθμολογεί κάθε παραλία "
        "συνδυάζοντας τις απαντήσεις σου με την πρόγνωση για τη μέρα που διάλεξες "
        "(βαθμολόγηση βάσει περιεχομένου και, αργότερα, μάθηση από τα σχόλιά σου). "
        "Πρωτότυπο: η πρόταση προκύπτει από σταθερό πίνακα.",
        "day_lower_today": "σήμερα",
        "day_lower_tomorrow": "αύριο",
        "day_lower_day_after": "μεθαύριο",
        # Map
        "map_title": "Θάσος",
        "map_hint": "Πάτησε μια πινέζα για να δεις την παραλία. Τα χρώματα δείχνουν "
        "τη διαύγεια του νερού {day}.",
        "legend_match": "Η επιλογή σου",
        "osm_credit": "© OpenStreetMap contributors",
        "your_match_card": "Η επιλογή σου",
        # Beach detail
        "about": "Σχετικά",
        "forecast_title": "Πρόγνωση 3 ημερών",
        "day_0": "Σήμερα",
        "day_1": "Αύριο",
        "day_2": "Μεθαύριο",
        "your_day": "Η μέρα σου",
        "clarity": "Διαύγεια νερού",
        "wind": "Άνεμος",
        "weather": "Καιρός",
        "temperature": "Θερμοκρασία",
        "wind_detail": "{dir} · {bft} μποφόρ",
        "wind_detail_short": "{dir} · {bft} Bf",
        "kmh": "{kmh} km/h",
        "temperature_value": "{temp}°C",
        "prediction_note_title": "Πώς θα λειτουργεί η πρόγνωση",
        "prediction_note": "Το σύστημα πρόβλεψης θα προβλέπει τη διαύγεια του "
        "νερού σε κάθε παραλία για τις επόμενες 3 μέρες, με βάση την ταχύτητα και "
        "την κατεύθυνση του ανέμου, τα κύματα, τη βροχόπτωση και ιστορικά/"
        "δορυφορικά δεδομένα ποιότητας νερού. Ο καιρός και ο άνεμος θα "
        "προέρχονται από πηγή μετεωρολογικών προγνώσεων.",
        # Beach types and settings
        "type_sand": "Αμμουδιά",
        "type_pebbles": "Βοτσαλωτή παραλία",
        "type_mixed": "Άμμος & βότσαλο",
        "type_marble": "Μαρμάρινο βότσαλο",
        "setting_organized": "Οργανωμένη",
        "setting_quiet": "Ήσυχη",
        # Forecast vocab
        "level_excellent": "Εξαιρετική",
        "level_good": "Καλή",
        "level_moderate": "Μέτρια",
        "level_poor": "Χαμηλή",
        "cond_sunny": "Ηλιοφάνεια",
        "cond_partly_cloudy": "Λίγα σύννεφα",
        "cond_cloudy": "Συννεφιά",
        "cond_rain": "Βροχή",
        "dir_N": "Β",
        "dir_NE": "ΒΑ",
        "dir_E": "Α",
        "dir_SE": "ΝΑ",
        "dir_S": "Ν",
        "dir_SW": "ΝΔ",
        "dir_W": "Δ",
        "dir_NW": "ΒΔ",
    },
}


def t(lang: str, key: str, **params) -> str:
    """Translate `key` into `lang`, formatting any `{placeholders}`."""
    text = STRINGS.get(lang, STRINGS[DEFAULT_LANGUAGE]).get(key)
    if text is None:
        text = STRINGS[DEFAULT_LANGUAGE].get(key, key)
    return text.format(**params) if params else text


def other_language(lang: str) -> str:
    """The language the top-bar toggle switches to."""
    return "el" if lang == "en" else "en"
