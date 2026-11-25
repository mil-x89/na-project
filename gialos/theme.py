"""Design system for gialos: colors, type scale, spacing. Defined once, used everywhere.

Rules (from the mobile UI guidelines the redesign follows):
- 60/30/10 color: warm off-white base, deep ink text, one sea-blue accent.
- Text hierarchy through opacity of the ink color (100 / 80 / 60 %).
- Type: one font family, 4 sizes (32 / 20 / 16 / 13) and 2 weights (400 / 700).
- Spacing on an 8-point grid (4, 8, 16, 24, 32, 48).
- Soft shadows tinted with the sea color, never pure black.
"""

import flet as ft

# --- Color: 60% base ---------------------------------------------------------
BACKGROUND = "#FAF7F2"      # warm off-white, sand-tinted
SURFACE = "#FFFFFF"         # cards
LINE = "#EDE6DA"            # hairlines, unselected borders

# --- Color: 30% ink (text) with opacity hierarchy ---------------------------
INK = "#14262E"             # headings, values
INK_80 = "#CC14262E"        # body text
INK_60 = "#9914262E"        # secondary text, labels

# --- Color: 10% accent ------------------------------------------------------
ACCENT = "#0A6F8C"          # Aegean blue: CTAs, selected states, key icons
ACCENT_DEEP = "#0A4D68"     # wordmark, pressed / strong accent
ACCENT_5 = "#0D0A6F8C"      # accent at 5%: selected tile fill, soft highlights
ACCENT_12 = "#1F0A6F8C"     # accent at 12%: chips, icon circles
SAND = "#F2E6CF"            # sand tone (illustrations, tags)
LOGO_SUN = "#FFD27A"        # logo: sun in the mark
LOGO_SUN_DARK = "#F2B441"   # logo: sun dot of the "i" (darker for contrast on light bg)
LOGO_SEA = "#2FB3C2"        # logo: sea in the mark
WHITE = "#FFFFFF"
WHITE_80 = "#CCFFFFFF"

SHADOW = "#1A0A4D68"        # soft shadow tinted with deep sea
GLOW = "#400A6F8C"          # glow behind the top-match card
PHOTO_FADE = "#B30A2530"    # dark sea-tinted fade at the bottom of photos

# Water clarity levels (stat values, map pins)
CLARITY_COLORS = {
    "excellent": "#0FA3B1",
    "good": "#3FAE7F",
    "moderate": "#D9982B",
    "poor": "#CF5C43",
}

# --- Illustration colors (scripts/generate_*.py) ----------------------------
SVG_SEA_LIGHT = "#7FDBEA"
SVG_SEA_DEEP = "#1C8FB0"
SVG_ISLAND = SAND
SVG_COAST = "#C9A66B"
SVG_FOREST = "#9BBF8A"
SVG_MOUNTAIN = "#7A9A6C"
SVG_WAVE = "#FFFFFF"
SVG_SKY_TOP = "#BFE9F2"
SVG_SKY_BOTTOM = "#FDF6E9"
SVG_SUN = "#FFD27A"
SVG_SAND_LIGHT = "#F6E7C8"
SVG_SAND_SHADE = "#E4CC9C"
SVG_PINE = "#4F7A5A"
SVG_ROCK = "#B9AE9C"
SVG_PEBBLES = ("#D9D3C7", "#BDB4A5", "#EFEBE3", "#A89F90")
SVG_MARBLE = ("#FFFFFF", "#F1F1EE", "#E4E4DF")

# --- Spacing (8-point grid) ---------------------------------------------------
S1, S2, S3, S4, S6 = 4, 8, 16, 24, 32   # 4, 8, 16, 24, 32 px
S8 = 48
PAGE_PADDING = S4
CARD_PADDING = S4
RADIUS = 24
RADIUS_SMALL = 16

# --- Sizes ---------------------------------------------------------------------
PHONE_WIDTH = 390
PHONE_HEIGHT = 844
# Phone frame shown around the app in wide browser windows (e.g. Codespaces)
FRAME_BREAKPOINT = 600      # wider than this (in a browser) -> draw the phone frame
FRAME_MARGIN = 24           # space around the frame
FRAME_BEZEL = 10            # dark edge around the screen
FRAME_RADIUS = 48           # outer corner radius (screen radius = this - bezel)
FRAME_BEZEL_COLOR = "#14262E"
FRAME_BACKDROP = ("#E3F1F4", "#F4EADB")   # soft sea -> sand gradient behind the phone
HERO_HEIGHT = 360           # top-match photo
DETAIL_HERO_HEIGHT = 280
BUTTON_HEIGHT = 56          # primary CTA (thumb zone)
LOGO_HEIGHT = 30            # logo in the top app bar

# --- Type scale: 4 sizes, 2 weights --------------------------------------------
SIZE_DISPLAY, SIZE_TITLE, SIZE_BODY, SIZE_SMALL = 32, 20, 16, 13
REGULAR, BOLD = ft.FontWeight.W_400, ft.FontWeight.W_700
SIZE_MAP_LABEL = 11   # exception to the 4-size scale: village names on the map

DISPLAY = ft.TextStyle(size=SIZE_DISPLAY, weight=BOLD, color=INK, letter_spacing=-0.6, height=1.15)
TITLE = ft.TextStyle(size=SIZE_TITLE, weight=BOLD, color=INK, letter_spacing=-0.2)
BODY = ft.TextStyle(size=SIZE_BODY, weight=REGULAR, color=INK_80, height=1.5)
BODY_STRONG = ft.TextStyle(size=SIZE_BODY, weight=BOLD, color=INK)
LABEL = ft.TextStyle(size=SIZE_SMALL, weight=BOLD, color=INK_60, letter_spacing=0.2)
CAPTION = ft.TextStyle(size=SIZE_SMALL, weight=REGULAR, color=INK_60, height=1.45)


def soft_shadow() -> ft.BoxShadow:
    return ft.BoxShadow(blur_radius=24, spread_radius=0, color=SHADOW, offset=ft.Offset(0, 8))


def app_theme() -> ft.Theme:
    """Material theme seeded from the accent color."""
    return ft.Theme(color_scheme_seed=ACCENT)
