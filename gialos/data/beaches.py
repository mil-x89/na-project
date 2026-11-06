"""Thassos beaches used by the mockup.

NOTE: coordinates are APPROXIMATE. All except Trypiti come from the beach's
OpenStreetMap feature (natural=beach, © OpenStreetMap contributors, ODbL),
rounded to 4 decimals; Trypiti is not tagged in OSM and is hand-placed.
They are used to place map pins and to work out which way each beach faces.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Beach:
    id: str
    name: dict[str, str]          # {"en": ..., "el": ...}
    lat: float                    # approximate (see module note)
    lon: float                    # approximate (see module note)
    beach_type: str               # "sand" | "pebbles" | "mixed" | "marble"
    setting: str                  # "organized" | "quiet"
    description: dict[str, str]   # {"en": ..., "el": ...}


BEACHES: list[Beach] = [
    Beach(
        id="golden_beach",
        name={"en": "Golden Beach", "el": "Χρυσή Αμμουδιά"},
        lat=40.7306, lon=24.7610,
        beach_type="sand",
        setting="organized",
        description={
            "en": "A long bay of fine golden sand on the east coast, below Mount "
            "Ypsario. Shallow water, beach bars and tavernas.",
            "el": "Μεγάλος κόλπος με ψιλή χρυσή άμμο στην ανατολική ακτή, κάτω από "
            "το Υψάριο. Ρηχά νερά, beach bar και ταβέρνες.",
        },
    ),
    Beach(
        id="paradise",
        name={"en": "Paradise Beach", "el": "Paradise"},
        lat=40.6452, lon=24.7671,
        beach_type="sand",
        setting="quiet",
        description={
            "en": "A pine-framed sandy cove in the south-east with turquoise water "
            "and a small islet offshore.",
            "el": "Αμμουδερός όρμος στα νοτιοανατολικά, με πεύκα, τιρκουάζ νερά "
            "και ένα νησάκι απέναντι.",
        },
    ),
    Beach(
        id="aliki",
        name={"en": "Aliki", "el": "Αλυκή"},
        lat=40.6046, lon=24.7407,
        beach_type="mixed",
        setting="quiet",
        description={
            "en": "Two small bays on a peninsula with an ancient marble quarry and "
            "the ruins of an ancient settlement. Very clear water.",
            "el": "Δύο μικροί κόλποι σε χερσόνησο με αρχαίο λατομείο μαρμάρου και "
            "ερείπια αρχαίου οικισμού. Πολύ καθαρά νερά.",
        },
    ),
    Beach(
        id="saliara",
        name={"en": "Marble Beach (Saliara)", "el": "Σαλιάρα"},
        lat=40.7505, lon=24.7482,
        beach_type="marble",
        setting="organized",
        description={
            "en": "Bright white marble pebbles and dust from the nearby quarries "
            "make the water look intensely turquoise.",
            "el": "Λευκό μαρμάρινο βότσαλο και μαρμαρόσκονη από τα κοντινά λατομεία "
            "κάνουν το νερό έντονα τιρκουάζ.",
        },
    ),
    Beach(
        id="makryammos",
        name={"en": "Makryammos", "el": "Μακρύαμμος"},
        lat=40.7703, lon=24.7262,
        beach_type="sand",
        setting="organized",
        description={
            "en": "A sandy bay in a pine forest just east of Limenas, with full "
            "facilities.",
            "el": "Αμμουδερός κόλπος μέσα σε πευκοδάσος, λίγο ανατολικά του Λιμένα, "
            "με πλήρεις παροχές.",
        },
    ),
    Beach(
        id="psili_ammos",
        name={"en": "Psili Ammos", "el": "Ψιλή Άμμος"},
        lat=40.5840, lon=24.6307,
        beach_type="sand",
        setting="organized",
        description={
            "en": "As the name says, fine, soft sand. A popular, organized beach on "
            "the south coast, with shallow water.",
            "el": "Όπως λέει και το όνομά της, ψιλή, απαλή άμμος. Δημοφιλής "
            "οργανωμένη παραλία στη νότια ακτή, με ρηχά νερά.",
        },
    ),
    Beach(
        id="glyfada",
        name={"en": "Glyfada", "el": "Γλυφάδα"},
        lat=40.7819, lon=24.6767,
        beach_type="mixed",
        setting="organized",
        description={
            "en": "A sheltered bay west of Limenas with sand and small pebbles, "
            "surrounded by pine trees.",
            "el": "Προστατευμένος κόλπος δυτικά του Λιμένα με άμμο και ψιλό "
            "βότσαλο, ανάμεσα σε πεύκα.",
        },
    ),
    Beach(
        id="pachys",
        name={"en": "Pachys", "el": "Παχύς"},
        lat=40.7904, lon=24.6278,
        beach_type="sand",
        setting="quiet",
        description={
            "en": "A long sandy beach on the north-west coast, shaded by pines that "
            "reach almost to the water.",
            "el": "Μεγάλη αμμουδιά στη βορειοδυτική ακτή, με πεύκα που φτάνουν "
            "σχεδόν ως το νερό.",
        },
    ),
    Beach(
        id="trypiti",
        name={"en": "Trypiti", "el": "Τρυπητή"},
        lat=40.5870, lon=24.6380,
        beach_type="sand",
        setting="organized",
        description={
            "en": "A wide sandy beach on the south coast with rock formations and "
            "sea caves at its edges.",
            "el": "Πλατιά αμμουδιά στη νότια ακτή με βραχώδεις σχηματισμούς και "
            "θαλάσσιες σπηλιές στις άκρες της.",
        },
    ),
    Beach(
        id="livadi",
        name={"en": "Livadi", "el": "Λιβάδι"},
        lat=40.5979, lon=24.6921,
        beach_type="sand",
        setting="quiet",
        description={
            "en": "A quiet sandy cove in the south, reached by a dirt track, with "
            "clear and calm water.",
            "el": "Ήσυχος αμμουδερός όρμος στα νότια, με καθαρά, ήρεμα νερά. Η "
            "πρόσβαση γίνεται από χωματόδρομο.",
        },
    ),
]

BEACHES_BY_ID: dict[str, Beach] = {b.id: b for b in BEACHES}


def get_beach(beach_id: str) -> Beach:
    return BEACHES_BY_ID[beach_id]
