# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import content_data as c

ROOT = os.path.dirname(__file__)

def ph(img_path, label, alt, big=False):
    """Photo placeholder block: shows real image if present, graceful fallback if not."""
    return f'''<div class="ph">
      <div class="ph-fallback">{c.ICONS['camera']}<div>{label}</div></div>
      <img src="{img_path}" alt="{alt}" loading="lazy">
    </div>'''

def nav(active_root, rel=""):
    items = [
        ("Dining", "dining"), ("Hikes", "hikes"), ("Spiritual Sites", "spiritual"),
        ("Points of Interest", "poi"), ("Scenic Drives", "drives"), ("Shopping", "shopping"),
        ("Guest Tips", "tips"),
    ]
    links = "".join(f'<a href="#{anchor}">{label}</a>' for label, anchor in items)
    home_href = "#stay" if active_root else f"{rel}index.html"
    return f'''<header class="nav">
    <div class="wrap">
      <a class="brand" href="{rel}index.html"><span class="brand-mark">T</span>Traumeri Sedona</a>
      <nav class="navlinks">
        <a class="home-link" href="{home_href}">Your Stay</a>
        {links}
      </nav>
    </div>
  </header>'''

def card_grid(items, img_dir):
    cards = []
    for it in items:
        slug = it["name"].lower().replace("&","and").replace("'","")
        slug = "".join(ch if ch.isalnum() else "-" for ch in slug)
        slug = "-".join(filter(None, slug.split("-")))
        tags = "".join(f'<span class="tag">{t}</span>' for t in it["tags"])
        cards.append(f'''<div class="card">
        <div class="ph" style="border-radius:0;aspect-ratio:16/11;">
          <div class="ph-fallback">{c.ICONS['camera']}<div>{it['name']}</div></div>
          <img src="../assets/img/sedona/{img_dir}/{slug}.jpg" alt="{it['name']}" loading="lazy">
        </div>
        <div class="badge">{c.ICONS['pin']}<span>{it['time']}</span></div>
        <div class="card-body">
          <h3>{it['name']}</h3>
          <div class="tags">{('<span class="tag" style="background:transparent;color:var(--accent-dark);padding-left:0;font-weight:700;">'+it['tag']+'</span>')}</div>
          <p>{it['desc']}</p>
          <div class="tags">{tags}</div>
        </div>
      </div>''')
    return f'<div class="card-grid">{"".join(cards)}</div>'

def section(kicker, heading, accent_word, lede, intro, tip, items, img_dir, anchor, alt=False):
    return f'''<section id="{anchor}" class="section{' alt' if alt else ''}">
    <div class="wrap">
      <div class="section-head">
        <div class="section-kicker">{c.ICONS['pin']}{kicker}</div>
        <h2>{heading} <span class="italic-accent">{accent_word}</span></h2>
        <p>{lede}</p>
        <div class="divider"></div>
      </div>
      <p style="max-width:760px;margin:0 auto 28px;color:var(--muted);text-align:center;">{intro}</p>
      <div class="tip-box">
        <div class="star">{c.ICONS['star']}</div>
        <div><h4>Insider Tip</h4><p>{tip}</p></div>
      </div>
      {card_grid(items, img_dir)}
    </div>
  </section>'''

def guest_tips_section():
    cards = "".join(f'<div class="rule-card"><h4>{t["h"]}</h4><p>{t["p"]}</p></div>' for t in c.GUEST_TIPS)
    return f'''<section id="tips" class="section alt">
    <div class="wrap">
      <div class="section-head">
        <div class="section-kicker">{c.ICONS['star']}Before You Go</div>
        <h2>Guest <span class="italic-accent">Tips</span></h2>
        <p>Everything else worth knowing to make the most of your stay in Sedona.</p>
        <div class="divider"></div>
      </div>
      <div class="rules-grid">{cards}</div>
    </div>
  </section>'''

def footer():
    return f'''<footer>
    <div class="wrap">
      <div class="brand"><span class="brand-mark">T</span>Traumeri Sedona</div>
      <p>{c.ADDRESS}</p>
      <p>Questions about your stay? Email <a href="mailto:veedu.stays@gmail.com">veedu.stays@gmail.com</a></p>
      <p class="legal">An independently published guest guide for Traumeri Casita &amp; Traumeri Casa. Not affiliated with Airbnb. Hours, prices, and details for third-party businesses are approximate and may change — please confirm directly before visiting. Updated June 2026.</p>
    </div>
  </footer>'''

def property_home_section(p):
    stats = "".join(f'<div class="stat-box"><div class="label">{l}</div><div class="value">{v}</div></div>' for l, v in p["stats"])
    amenities = "".join(f"<li>{a}</li>" for a in p["amenities"])
    rules = "".join(f'<div class="rule-card"><h4>{r["h"]}</h4><p>{r["p"]}</p></div>' for r in c.PROPERTY_RULES)
    photos = "".join([
        ph(f"../assets/img/{p['slug']}/exterior.jpg", "Add exterior.jpg", f"{p['name']} exterior"),
        ph(f"../assets/img/{p['slug']}/living-room.jpg", "Add living-room.jpg", f"{p['name']} living room"),
        ph(f"../assets/img/{p['slug']}/hot-tub.jpg", "Add hot-tub.jpg", f"{p['name']} hot tub"),
        ph(f"../assets/img/{p['slug']}/bedroom.jpg", "Add bedroom.jpg", f"{p['name']} bedroom"),
        ph(f"../assets/img/{p['slug']}/kitchen.jpg", "Add kitchen.jpg", f"{p['name']} kitchen"),
    ])
    return f'''<section id="stay" class="section">
    <div class="wrap">
      <div class="section-head">
        <div class="section-kicker">{c.ICONS['home']}Your Home</div>
        <h2>About <span class="italic-accent">{p['name']}</span></h2>
        <p>{p['tagline']}</p>
        <div class="divider"></div>
      </div>
      <div class="photo-grid">{photos}</div>
      <p style="max-width:760px;margin:0 auto 32px;color:var(--ink);">{p['overview']}</p>
      <div class="stat-grid">{stats}</div>
      <div class="info-card">
        <div class="row"><b>WiFi Network:</b> <code>{c.WIFI_NETWORK}</code></div>
        <div class="row"><b>WiFi Password:</b> <code>{c.WIFI_PASSWORD}</code></div>
        <div class="row"><b>Check-in:</b> {p['checkin']} &nbsp;·&nbsp; <b>Check-out:</b> {p['checkout']}</div>
        <div class="row"><b>Entry:</b> {p['entry']}</div>
        <div class="row"><b>Sleeping arrangements:</b> {p['rooms_note']}</div>
      </div>
      <div class="amenities-box" style="margin-bottom:24px;">
        <h4>Amenities Highlights</h4>
        <ul class="amenities-list">{amenities}</ul>
      </div>
      <div class="parking-box" style="margin-bottom:32px;">
        <div class="parking-spot">{p['parking_spot']}</div>
        <p><b>Parking:</b> {p['parking_note']}</p>
      </div>
      <div class="section-head" style="margin-bottom:24px;">
        <h3 style="font-size:1.3rem;">House Rules</h3>
      </div>
      <div class="rules-grid">{rules}</div>
    </div>
  </section>'''

def page_head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,700;1,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>'''

def build_property_page(p):
    hero = f'''<section class="hero">
    <div class="hero-inner">
      <div class="hero-badge">{c.ADDRESS}</div>
      <h1>Your Sedona <span class="italic-accent">{p['title_word']}</span></h1>
      <p class="lede">{p['tagline']}</p>
      <a class="btn" href="#stay">{c.ICONS['arrow']}Explore Your Guide</a>
    </div>
  </section>'''
    body = "\n".join([
        nav(active_root=True, rel="../"),
        hero,
        property_home_section(p),
        section("Eat &amp; Drink", "Local", "Dining", "Where to eat, from walkable cafes to the best reservation in town.", c.DINING_INTRO, c.DINING_TIP, c.DINING, "dining", "dining", alt=True),
        section("On Foot", "Sedona", "Hikes", "Red rock trails for every energy level, all within a short drive.", c.HIKES_INTRO, c.HIKES_TIP, c.HIKES, "hikes", "hikes"),
        section("Sacred Ground", "Vortexes &amp;", "Spiritual Sites", "Four famous energy vortexes, plus two quieter places for reflection.", c.SPIRITUAL_INTRO, c.SPIRITUAL_TIP, c.SPIRITUAL, "spiritual", "spiritual", alt=True),
        section("Worth The Detour", "Points of", "Interest", "State parks, ancient ruins, and only-in-Sedona experiences.", c.POI_INTRO, c.POI_TIP, c.POI, "poi", "poi"),
        section("Behind The Wheel", "Scenic", "Drives", "Big views without leaving the car — from a quick loop to a half-day out-and-back.", c.DRIVES_INTRO, c.DRIVES_TIP, c.DRIVES, "drives", "drives", alt=True),
        section("Browse &amp; Buy", "Sedona", "Shopping", "Art villages, crystal shops, and Native American trading posts.", c.SHOPPING_INTRO, c.SHOPPING_TIP, c.SHOPPING, "shopping", "shopping"),
        guest_tips_section(),
        footer(),
        '<script src="../assets/js/main.js"></script>',
        "</body></html>",
    ])
    html = page_head(f"{p['name']} Guest Guide | Sedona, AZ", f"Guest guide for {p['name']} in Sedona, Arizona — house info, dining, hikes, spiritual sites, points of interest, scenic drives, and shopping.") + "\n" + body
    out_dir = os.path.join(ROOT, p["slug"])
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w") as f:
        f.write(html)
    print("wrote", p["slug"] + "/index.html", len(html), "bytes")

def build_landing():
    def pcard(p):
        return f'''<div class="property-card">
        <div class="ph" style="border-radius:0;">
          <div class="ph-fallback">{c.ICONS['camera']}<div>Add {p['slug']}/exterior.jpg</div></div>
          <img src="assets/img/{p['slug']}/exterior.jpg" alt="{p['name']}" loading="lazy">
        </div>
        <div class="pc-body">
          <h3>{p['name']}</h3>
          <div class="pc-meta">{p['stats'][0][1]} Bedroom · {p['stats'][1][1]} Bath · Sleeps {p['stats'][2][1]}</div>
          <p class="desc">{p['tagline']}</p>
          <a class="btn" href="{p['slug']}/index.html">{c.ICONS['arrow']}View Guide</a>
        </div>
      </div>'''
    nav_html = f'''<header class="nav">
    <div class="wrap">
      <a class="brand" href="index.html"><span class="brand-mark">T</span>Traumeri Sedona</a>
    </div>
  </header>'''
    hero = f'''<section class="hero landing-hero">
    <div class="hero-inner">
      <div class="hero-badge">{c.ADDRESS}</div>
      <h1>Welcome To <span class="italic-accent">Sedona</span></h1>
      <p class="lede">Two private red-rock retreats, one shared compound, and a full local guide to the trails, restaurants, vortexes, and views right outside your door.</p>
      <a class="btn ghost" href="#properties">{c.ICONS['arrow']}Choose Your Guide</a>
    </div>
  </section>'''
    body = "\n".join([
        nav_html, hero,
        f'''<section id="properties" class="section">
        <div class="wrap">
          <div class="section-head">
            <div class="section-kicker">{c.ICONS['home']}Your Stay</div>
            <h2>Which <span class="italic-accent">Casa</span> Is Yours?</h2>
            <p>Each home has its own dedicated guide with check-in details, WiFi, amenities, and the full Sedona local guide.</p>
            <div class="divider"></div>
          </div>
        </div>
        <div class="property-grid">{pcard(c.CASITA)}{pcard(c.CASA)}</div>
      </section>''',
        footer(),
        '<script src="assets/js/main.js"></script>',
        "</body></html>",
    ])
    html = page_head("Traumeri Sedona | Guest Guide", "Guest guide hub for Traumeri Casita and Traumeri Casa in Sedona, Arizona.").replace('href="../assets', 'href="assets') + "\n" + body
    with open(os.path.join(ROOT, "index.html"), "w") as f:
        f.write(html)
    print("wrote index.html", len(html), "bytes")

if __name__ == "__main__":
    build_landing()
    build_property_page(c.CASITA)
    build_property_page(c.CASA)
