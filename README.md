# gialos

**Team**: Ομάδα Χρηστών 50
- Πάρης Σαλονικιός, ΑΜ: 3230179
- Μιλτιάδης Ξεζωνάκης, ΑΜ: 3230145

**gialos** (Greek for *seashore*) is a mobile app that recommends a beach on the
island of Thassos, Greece, and forecasts **how clear the water will be** at each
beach over the next three days, together with the wind and the weather.

This is an **interactive prototype**: every screen can be tapped through like a
real app, and the app itself explains what its two intelligent features will do.
All data in the prototype (forecasts and recommendations) is simulated.

---

## App description

### The problem
Thassos has dozens of beaches, and the "best" one changes from day to day. A
beach that is calm and crystal clear on Monday can be choppy and cloudy on
Tuesday if the wind turns and blows straight onto it. Weather apps tell you the
wind and the temperature, but not **what the water will look like** at a
specific beach, or **which beach suits you** on the day you are going.

### How it works
1. **Welcome**: a short introduction to the app.
2. **Four quick questions**, one per screen:
   - *When are you going?* today / tomorrow / in 2 days
   - *Sand or pebbles?* sand / pebbles / either
   - *What kind of beach?* quiet / organized / either
   - *How do you feel about wind?* calm only / a breeze is fine / wind is fine
3. **Finding your beach**: your answers are matched with the forecast for every
   beach.
4. **Your beach**: one clear recommendation, the *top match*. It shows a photo,
   **why it's your match** (e.g. *Sandy beach · Low wind · Very clear water*),
   and the conditions for your day: water clarity, wind, weather and
   temperature.
5. **Beach details**: a description and a **3-day forecast**, with your chosen
   day highlighted.
6. **Map**: a map of Thassos with its real coastline and villages. Beach pins
   are colored by the forecast water clarity and your match is highlighted. Tap
   a pin to open that beach.

The app is available in **Greek and English** and switches language instantly
from the top bar.

---

## Features

### 1. Beach recommendation

**Goal:** turn a few simple answers into *one* beach the user will enjoy, and
explain why.

**What it takes into account**
- **The user's answers:** the day of the visit, sand or pebbles, quiet or
  organized, and how much wind they accept.
- **What each beach is like:** its surface (sand, pebbles, marble pebbles or
  mixed) and whether it is quiet or organized (sunbeds, beach bar).
- **The forecast for the chosen day:** expected water clarity and wind at each
  beach (from Feature 2).

**How it decides.** Every beach gets a score for how well it fits this user on
this day. The beach's own characteristics and conditions are compared with the
user's preferences:

| Criterion | Example |
|---|---|
| Surface matches | User wants sand → sandy beaches score higher |
| Atmosphere matches | User wants quiet → quiet beaches score higher |
| Wind is acceptable | User wants calm water → windy beaches that day score lower |
| Water is clear | Beaches with a high clarity forecast score higher |

The beach with the highest score becomes the **top match**.

**How it explains itself.** The criteria the top match satisfies are shown as
tags under **"Why it's your match"**, so the user sees *why* a beach was chosen,
not just *which* one.

**In the future** the recommendation will also **learn from feedback**: which
suggestions users follow, change or ignore, and whether they liked the beach.
Over time it can learn, for example, that a user cares more about clear water
than about sand.

### 2. Water clarity forecast

**Goal:** forecast **how clear the water will be** at each beach for each of the
next three days.

**What it predicts.** For every beach and day, a **water clarity score from 0 to
100**, shown as a level:

| Score | Level |
|---|---|
| 80–100 | Excellent |
| 60–79 | Good |
| 40–59 | Moderate |
| below 40 | Poor |

**What affects water clarity**
- **The beach's usual clarity.** Some beaches are naturally clearer than others,
  such as Thassos's marble-pebble beaches. This baseline will come from
  **historical and satellite water-quality data**.
- **Wind speed and direction.** Wind stirs up sand and sediment, and its
  direction *relative to the beach* matters most. Wind blowing **from the sea
  onto the beach** clouds the water much more than wind blowing **from the
  land**. The same wind can be bad for a beach on one side of the island and
  harmless on the other.
- **Waves**, which keep sand suspended near the shore.
- **Rainfall**, which washes soil from the land into the sea.

Wind, waves and rain will come from a **weather forecast**. The system combines
them with each beach's usual clarity to produce the 3-day forecast.

**Where it appears:** in the 3-day forecast on each beach's page, as the pin
colors on the map, and as one of the main criteria in the recommendation.

---

## How to install

You need **Python 3.10 or newer** ([python.org](https://www.python.org/downloads/)).

1. Download the project (clone the repository or download it as a ZIP and unzip
   it) and open a terminal in the project folder.
2. Create a virtual environment:
   ```
   python -m venv .venv
   ```
   On Windows, if `python` is not found, use `py -m venv .venv` instead.
3. Activate it:
   - Windows, Command Prompt: `.venv\Scripts\activate.bat`
   - Windows, PowerShell: `.venv\Scripts\Activate.ps1`
   - macOS / Linux: `source .venv/bin/activate`
4. Install the requirements:
   ```
   pip install -r requirements.txt
   ```

---

## How to run

With the virtual environment activated (step 3 above), run:

```
flet run main.py
```

The app opens in a phone-sized window on your computer. The very first launch
needs an internet connection and takes a little longer, because the app window
component is downloaded once; after that it starts right away and works offline.

To stop it, close the window or press **Ctrl+C** in the terminal.
