"""Thassos map geometry and the lat/lon -> map-pixel projection.

Shared by the asset generator (scripts/generate_island.py) and the map view,
so pins always line up with the illustration.

The coastline is the real one from OpenStreetMap (see thassos_osm.py,
© OpenStreetMap contributors, ODbL), simplified for a phone-sized map.
"""

import math

from gialos.data.thassos_osm import COASTLINE, ISLETS, TOWNS, Town  # noqa: F401 (re-exported)

ISLAND_OUTLINE: list[tuple[float, float]] = COASTLINE

# Ypsario, the island's highest peak (drawn as a small mountain symbol). Approximate.
MOUNTAIN = (40.7186, 24.6600)

# Geographic window shown on the map (a little sea around the island).
LAT_MIN, LAT_MAX = 40.545, 40.810
LON_MIN, LON_MAX = 24.495, 24.815

# Map size in logical pixels; height keeps the true aspect ratio
# (a degree of longitude is shorter than a degree of latitude at 40.7°N).
MAP_WIDTH = 340
_LON_SCALE = math.cos(math.radians((LAT_MIN + LAT_MAX) / 2))
MAP_HEIGHT = round(
    MAP_WIDTH * (LAT_MAX - LAT_MIN) / ((LON_MAX - LON_MIN) * _LON_SCALE)
)


def project(lat: float, lon: float) -> tuple[float, float]:
    """Project lat/lon onto map pixels (x right, y down)."""
    x = (lon - LON_MIN) / (LON_MAX - LON_MIN) * MAP_WIDTH
    y = (LAT_MAX - lat) / (LAT_MAX - LAT_MIN) * MAP_HEIGHT
    return x, y
