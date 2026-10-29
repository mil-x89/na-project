from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse


PAGE = r'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#183c36">
  <title>Shoreline — find your kind of beach</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      color-scheme: light;
      --ink: #173c36;
      --paper: #f5f2e9;
      --lime: #d7f36a;
      --coral: #ff765b;
      --line: rgba(23, 60, 54, .2);
      font-family: "DM Sans", sans-serif;
      font-synthesis: none;
      text-rendering: optimizeLegibility;
    }
    * { box-sizing: border-box; }
    body { margin: 0; background: var(--paper); color: var(--ink); }
    button, input { font: inherit; }
    .hero {
      position: relative;
      display: flex;
      min-height: min(790px, 100svh);
      flex-direction: column;
      overflow: hidden;
      color: white;
      background: #355f58 url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=2400&q=88") center 54% / cover;
    }
    .hero::before {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(10, 35, 33, .48), rgba(10, 35, 33, .08) 37%, rgba(10, 35, 33, .49));
      content: "";
    }
    .nav, .hero-content, .hero-bottom { position: relative; z-index: 1; }
    .nav {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 27px clamp(22px, 5.2vw, 78px);
    }
    .wordmark { font: 800 21px/1 "Manrope", sans-serif; letter-spacing: 0; }
    .wordmark span { color: var(--lime); }
    .account-links { display: flex; align-items: center; gap: 25px; }
    .account-links a { color: white; font-size: 12px; text-decoration: none; }
    .account-links a:last-child { border-bottom: 1px solid rgba(255,255,255,.7); padding-bottom: 4px; }
    .hero-content {
      width: min(900px, calc(100% - 40px));
      margin: auto;
      padding: 55px 0 70px;
      text-align: center;
      animation: arrive .7s ease-out both;
    }
    .eyebrow { margin: 0 0 17px; font-size: 10px; font-weight: 700; letter-spacing: 2.4px; text-transform: uppercase; }
    h1 { margin: 0; font: 600 clamp(45px, 7.6vw, 92px)/.99 "Manrope", sans-serif; letter-spacing: 0; }
    h1 em { color: var(--lime); font-style: normal; }
    .intro { max-width: 435px; margin: 21px auto 28px; color: rgba(255,255,255,.9); font-size: 14px; line-height: 1.65; }
    .find-button {
      display: inline-flex;
      min-width: 190px;
      min-height: 64px;
      align-items: center;
      justify-content: center;
      gap: 17px;
      border: 0;
      border-radius: 2px;
      background: var(--lime);
      color: var(--ink);
      cursor: pointer;
      font: 800 14px "Manrope", sans-serif;
      letter-spacing: 1.8px;
      transition: background .2s, transform .2s;
    }
    .find-button:hover { transform: translateY(-2px); background: #e4ff83; }
    .find-button:disabled { cursor: progress; opacity: .8; }
    .find-button svg { width: 18px; height: 18px; }
    .preferences {
      display: flex;
      width: min(720px, 100%);
      align-items: center;
      justify-content: center;
      gap: 0;
      margin: 43px auto 0;
      padding: 17px 0 0;
      border-top: 1px solid rgba(255,255,255,.42);
      text-align: left;
    }
    .location-control { display: grid; min-width: 190px; gap: 6px; padding: 0 24px; }
    .location-control label, .pref-label { color: rgba(255,255,255,.73); font-size: 9px; font-weight: 700; letter-spacing: 1.1px; text-transform: uppercase; }
    .location-row { display: flex; align-items: center; gap: 8px; }
    .location-row input { width: 145px; padding: 0; border: 0; outline: 0; background: transparent; color: white; font-size: 13px; }
    .location-row input::placeholder { color: white; }
    .locate {
      display: grid;
      width: 27px;
      height: 27px;
      place-items: center;
      border: 1px solid rgba(255,255,255,.55);
      border-radius: 50%;
      background: transparent;
      color: white;
      cursor: pointer;
    }
    .locate svg { width: 13px; height: 13px; }
    .pref-group { display: grid; gap: 9px; padding: 0 24px; border-left: 1px solid rgba(255,255,255,.36); }
    .chips { display: flex; flex-wrap: wrap; gap: 6px; }
    .chip { position: relative; }
    .chip input { position: absolute; width: 1px; height: 1px; opacity: 0; }
    .chip span { display: block; padding: 6px 10px; border: 1px solid rgba(255,255,255,.58); border-radius: 20px; color: white; cursor: pointer; font-size: 10px; transition: .18s ease; }
    .chip input:checked + span { border-color: var(--lime); background: var(--lime); color: var(--ink); }
    .chip input:focus-visible + span, a:focus-visible, button:focus-visible, input:focus-visible { outline: 2px solid white; outline-offset: 3px; }
    .hero-bottom {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 clamp(22px, 5.2vw, 78px) 25px;
      color: rgba(255,255,255,.76);
      font-size: 10px;
    }
    .hero-bottom .coordinates { display: flex; align-items: center; gap: 8px; }
    .coordinates span { width: 6px; height: 6px; border-radius: 50%; background: var(--lime); }
    .result {
      display: none;
      width: min(720px, calc(100% - 36px));
      margin: -35px auto 45px;
      position: relative;
      z-index: 2;
      grid-template-columns: 1fr auto;
      gap: 12px 25px;
      align-items: center;
      padding: 23px 26px;
      border-left: 4px solid var(--coral);
      background: var(--paper);
      box-shadow: 0 12px 35px rgba(13, 47, 42, .15);
      animation: arrive .35s ease-out both;
    }
    .result.show { display: grid; }
    .result-kicker { margin: 0 0 5px; color: #64746b; font-size: 9px; font-weight: 700; letter-spacing: 1.4px; text-transform: uppercase; }
    .result h2 { margin: 0; font: 700 22px "Manrope", sans-serif; }
    .result-copy { grid-column: 1 / -1; margin: 0; color: #53645d; font-size: 12px; line-height: 1.5; }
    .score { color: #65756c; font-size: 10px; text-align: right; }
    .score strong { display: block; color: var(--ink); font: 700 23px "Manrope", sans-serif; }
    .notice { margin: 0 auto 28px; color: #64746b; font-size: 10px; text-align: center; }
    @keyframes arrive { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    @media (max-width: 600px) {
      .hero { min-height: 100svh; background-position: 55% center; }
      .nav { padding: 21px 21px; }
      .account-links { gap: 15px; }
      .hero-content { padding: 42px 0 49px; }
      .intro { max-width: 300px; margin-top: 16px; font-size: 13px; }
      .find-button { min-width: 174px; min-height: 58px; }
      .preferences { flex-direction: column; align-items: stretch; gap: 17px; margin-top: 31px; padding-top: 17px; }
      .location-control { padding: 0 6px; }
      .location-row input { width: min(240px, calc(100vw - 120px)); }
      .pref-group { padding: 0 6px; border-left: 0; }
      .hero-bottom { padding-bottom: 18px; font-size: 9px; }
      .result { margin-top: -20px; padding: 19px; }
    }
    @media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation-duration: .01ms !important; transition-duration: .01ms !important; } }
  </style>
</head>
<body>
  <main>
    <section class="hero" aria-label="Find your ideal beach">
      <header class="nav">
        <div class="wordmark">shore<span>/</span>line</div>
        <nav class="account-links" aria-label="Account">
          <a href="#login" onclick="accountPreview(event, 'Log in')">Log in</a>
          <a href="#create-account" onclick="accountPreview(event, 'Create account')">Create account</a>
        </nav>
      </header>
      <div class="hero-content">
        <p class="eyebrow">A better day by the water</p>
        <h1>Your beach.<br><em>Your kind of day.</em></h1>
        <p class="intro">Tell us what you love. We’ll find the stretch of coast that feels like it was made for you.</p>
        <button class="find-button" id="find-button" type="button" onclick="findBeach()">
          <span id="button-label">FIND</span>
          <svg viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M3.5 10h12m-5-5 5 5-5 5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
        <div class="preferences" aria-label="Your beach preferences">
          <div class="location-control">
            <label for="location">Starting near</label>
            <div class="location-row">
              <input id="location" type="text" value="Barcelona, Spain" aria-label="Your location">
              <button class="locate" type="button" aria-label="Use my current location" title="Use my current location" onclick="useMyLocation()">
                <svg viewBox="0 0 16 16" fill="none" aria-hidden="true"><circle cx="8" cy="8" r="4.5" stroke="currentColor"/><path d="M8 1v2m0 10v2M1 8h2m10 0h2" stroke="currentColor" stroke-linecap="round"/></svg>
              </button>
            </div>
          </div>
          <div class="pref-group">
            <span class="pref-label">I’m in the mood for</span>
            <div class="chips">
              <label class="chip"><input type="checkbox" value="quiet" checked><span>Quiet</span></label>
              <label class="chip"><input type="checkbox" value="calm"><span>Calm water</span></label>
              <label class="chip"><input type="checkbox" value="facilities"><span>Facilities</span></label>
              <label class="chip"><input type="checkbox" value="nature"><span>Wild &amp; natural</span></label>
            </div>
          </div>
        </div>
      </div>
      <div class="hero-bottom">
        <span class="coordinates"><span></span>Find a little more coast</span>
        <span>Made for wherever the day takes you</span>
      </div>
    </section>
    <section class="result" id="result" aria-live="polite" aria-atomic="true">
      <div>
        <p class="result-kicker" id="result-kicker">Your match nearby</p>
        <h2 id="result-name">Platja de Castelldefels</h2>
      </div>
      <div class="score"><strong id="result-score">96%</strong>match</div>
      <p class="result-copy" id="result-copy"></p>
    </section>
    <p class="notice">A preview with sample beach data. Live conditions and availability aren’t included.</p>
  </main>
  <script>
    const beaches = [
      { name: "Platja de Castelldefels", area: "Barcelona", tags: ["quiet", "calm", "facilities"], description: "Room to spread out, gentle water, and handy facilities make this an easygoing all-rounder." },
      { name: "Cala Tuent", area: "Mallorca", tags: ["quiet", "calm", "nature"], description: "A tucked-away cove framed by mountains, best for a slower day close to nature." },
      { name: "Praia da Ursa", area: "Lisbon", tags: ["quiet", "nature"], description: "A dramatic, wild-feeling coastline for a quieter escape and a little adventure." },
      { name: "Praia de Carcavelos", area: "Lisbon", tags: ["facilities"], description: "An easy-to-reach favorite with beach services and plenty going on nearby." },
      { name: "La Jolla Shores", area: "San Diego", tags: ["calm", "facilities"], description: "A wide sandy shore with mellow swimming conditions and useful amenities close by." },
      { name: "Black's Beach", area: "San Diego", tags: ["quiet", "nature"], description: "A quieter, rugged coastline backed by dramatic cliffs and open ocean." },
      { name: "Platja de la Barceloneta", area: "Barcelona", tags: ["facilities"], description: "A lively city beach with easy access, food nearby, and all the essentials." }
    ];
    const regions = ["barcelona", "lisbon", "san diego", "mallorca"];

    function findRegion(location) {
      const text = location.toLowerCase();
      return regions.find(region => text.includes(region)) || "barcelona";
    }

    function findBeach() {
      const button = document.getElementById("find-button");
      const label = document.getElementById("button-label");
      const location = document.getElementById("location").value.trim();
      const region = findRegion(location);
      const selected = [...document.querySelectorAll(".chip input:checked")].map(input => input.value);
      button.disabled = true;
      label.textContent = "LOOKING";
      window.setTimeout(() => {
        const nearby = beaches.filter(beach => beach.area.toLowerCase() === region);
        const candidates = nearby.length ? nearby : beaches;
        const ranked = candidates.map(beach => ({
          beach,
          score: selected.length ? selected.filter(tag => beach.tags.includes(tag)).length : 0
        })).sort((a, b) => b.score - a.score || a.beach.name.localeCompare(b.beach.name));
        const winner = ranked[0];
        const percent = selected.length ? Math.round(68 + 32 * winner.score / selected.length) : 82;
        document.getElementById("result-kicker").textContent = nearby.length ? `Your match near ${winner.beach.area}` : `A coast to explore near ${location || "you"}`;
        document.getElementById("result-name").textContent = winner.beach.name;
        document.getElementById("result-score").textContent = `${percent}%`;
        document.getElementById("result-copy").textContent = winner.beach.description;
        document.getElementById("result").classList.add("show");
        button.disabled = false;
        label.textContent = "FIND";
        document.getElementById("result").scrollIntoView({ behavior: "smooth", block: "center" });
      }, 450);
    }

    function useMyLocation() {
      if (!navigator.geolocation) {
        document.getElementById("result-kicker").textContent = "Location unavailable";
        document.getElementById("result-name").textContent = "Enter a nearby city instead";
        document.getElementById("result-copy").textContent = "Your browser doesn’t support location access. You can type a city in the location field.";
        document.getElementById("result").classList.add("show");
        return;
      }
      navigator.geolocation.getCurrentPosition(position => {
        const { latitude, longitude } = position.coords;
        const locations = [
          { name: "Barcelona, Spain", lat: 41.39, lon: 2.17 },
          { name: "Lisbon, Portugal", lat: 38.72, lon: -9.14 },
          { name: "San Diego, USA", lat: 32.72, lon: -117.16 },
          { name: "Mallorca, Spain", lat: 39.57, lon: 2.65 }
        ];
        locations.sort((a, b) => Math.hypot(latitude - a.lat, longitude - a.lon) - Math.hypot(latitude - b.lat, longitude - b.lon));
        document.getElementById("location").value = locations[0].name;
      }, () => {
        document.getElementById("result-kicker").textContent = "Couldn’t access your location";
        document.getElementById("result-name").textContent = "Type a city to get started";
        document.getElementById("result-copy").textContent = "Location access wasn’t granted. Your location is only used in this page preview.";
        document.getElementById("result").classList.add("show");
      }, { timeout: 8000 });
    }

    function accountPreview(event, action) {
      event.preventDefault();
      document.getElementById("result-kicker").textContent = "Coming soon";
      document.getElementById("result-name").textContent = action;
      document.getElementById("result-copy").textContent = "Account access is shown as a mockup in this preview.";
      document.getElementById("result").classList.add("show");
      document.getElementById("result").scrollIntoView({ behavior: "smooth", block: "center" });
    }
  </script>
</body>
</html>'''


class BeachFinderHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if urlparse(self.path).path not in ("/", "/index.html"):
            self.send_error(404)
            return
        body = PAGE.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")


if __name__ == "__main__":
    host, port = "127.0.0.1", 8000
    print(f"Shoreline beach finder running at http://{host}:{port}")
    HTTPServer((host, port), BeachFinderHandler).serve_forever()