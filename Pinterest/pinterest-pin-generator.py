"""
New England Crust — Pinterest Pin Generator v2
===============================================
Generates Pinterest-ready PNG pins (1000x1500) matching the locked
Claude Design template: deep char background, Ember Amber accents,
Warm Cream Georgia serif typography, badge mark, diamond divider.

TEMPLATE SPEC (matches Claude Design board):
- 1000x1500px PNG (2:3 ratio)
- Layout A (default): top 2/3 photo + bottom 1/3 deep char text block
- Layout B (full-bleed): full photo with dark gradient overlay over bottom 40%
- Category label in Ember Amber small-caps with diamond divider
- Bold Georgia serif headline in Warm Cream
- NEWENGLANDCRUST.COM footer in spaced Ember Amber caps
- NEC badge mark (flame + CRUST) top-right corner of photo area

USAGE:
  1. Place your photo(s) in the same folder as this script
  2. Edit the PINS list below with your details
  3. Run: python3 pinterest-pin-generator.py
  4. PNGs will be saved to the /outputs/ folder

REQUIREMENTS:
  pip install Pillow

FONT PATHS:
  Mac (default):   /Library/Fonts/Georgia Bold.ttf  +  /Library/Fonts/Georgia.ttf
  Linux fallback:  Liberation Serif Bold/Regular (auto-detected)
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math

# ── COLORS (New England Crust brand palette) ──────────────────────────────────
DEEP_CHAR    = (18,  14,   8)    # #120E08 — primary background
EMBER_AMBER  = (212, 131,  42)   # #D4832A — accent, category, footer, rule
WARM_CREAM   = (245, 239, 224)   # #F5EFE0 — headline, primary text
CORAL_RED    = (200,  75,  46)   # #C84B2E — flame outer
EMBER_ORANGE = (232, 148,  58)   # #E8943A — flame mid
GOLD         = (244, 192,  66)   # #F4C042 — flame inner
PALE_GOLD    = (255, 239, 170)   # #FFEFAA — flame core

# FREE flag badge — opt-in per-pin, site's ember/glow accent (not the coral
# used in the flame badge above). See paste_free_flag() below.
FLAG_EMBER   = (198,  61,  40)   # #C63D28 — badge fill
FLAG_GLOW    = (255, 146,  26)   # #FF921A — badge text (used when contrast holds)
FLAG_WHITE   = (255, 255, 255)   # fallback badge text when glow-on-ember contrast is too low

# Checklist illustration (photo-less pins) — pulled from the live site's
# Tailwind palette (tailwind.config.mjs): twilight, timber, glow.
TIMBER_PAGE   = (237, 224, 203)  # timber-100 #EDE0CB — the "page" card
TIMBER_HEADER = (118,  80,  43)  # timber-600 #76502B — header bar across the page top
TIMBER_LINE   = (148, 102,  53)  # timber-500 #946635 — muted checklist lines
GLOW_CHECK    = (255, 146,  26)  # glow-400  #FF921A — checkmark accent
CARD_SHADOW   = (7,     6,   5, 110)  # twilight-900-ish, translucent drop shadow

# Sentinel photo_path value that triggers the checklist illustration instead
# of loading a real photo or the generic "PHOTO" placeholder.
ILLUSTRATION_CHECKLIST = "illustration:checklist"

# ── PIN DIMENSIONS ────────────────────────────────────────────────────────────
W, H = 1000, 1500

# ── FONT PATHS ────────────────────────────────────────────────────────────────
# Mac paths (primary — Georgia is system-installed on all Macs)
MAC_SERIF_BOLD   = '/Library/Fonts/Georgia Bold.ttf'
MAC_SERIF_REG    = '/Library/Fonts/Georgia.ttf'
MAC_SERIF_ITALIC = '/Library/Fonts/Georgia Italic.ttf'
# Linux fallback (for CI / server environments)
LIN_SERIF_BOLD   = '/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf'
LIN_SERIF_REG    = '/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf'
LIN_SERIF_ITALIC = '/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf'

# Sans-serif bold — used only for the small FREE flag badge (deliberately
# distinct from the Georgia serif headline type elsewhere on the pin).
MAC_SANS_BOLD = '/Library/Fonts/Arial Bold.ttf'
LIN_SANS_BOLD = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'

def _font(mac_path, linux_path, size):
    path = mac_path if os.path.exists(mac_path) else linux_path
    return ImageFont.truetype(path, size)

# ── PINS TO GENERATE ──────────────────────────────────────────────────────────
# layout: "split" (2/3 photo + 1/3 text block) or "fullbleed" (photo fills pin)
# photo_path: filename relative to this script, or None for a dark placeholder
PINS = [
    {
        "photo_path": "NinjaWoodfireHero.jpeg",
        "category":   "Gear Guide",
        "headline":   "Ninja Woodfire Accessories Worth Buying (And What's a Waste)",
        "subhead":    "After months on the patio — here's what earns its place.",
        "layout":     "split",
        "output":     "outputs/NEC-accessories-v2.png",
    },
    {
        "photo_path": "IMG_8372.jpeg",
        "category":   "Pizza Night",
        "headline":   "Your Backyard Pizza Night Starts Here",
        "subhead":    "The exact setup we use every time.",
        "layout":     "split",
        "badge_position": "top_left",
        "output":     "outputs/NEC-pizzanight-v2.png",
    },
    {
        "photo_path":     "NinjaWoodfireHero.jpeg",
        "category":       "Oven Review",
        "headline":       "Prime Day Pizza Oven Deals — What's Worth Watching",
        "subhead":        "Ooni, Ninja Woodfire, Solo Stove Pi — what to buy, what to skip, and when to check back.",
        "layout":         "primeday",
        "badge_position": "top_right",
        "output":         "outputs/NEC-primeday-pin1.png",
    },
    {
        "photo_path":     "NinjaWoodfireHero.jpeg",
        "category":       "Gear Guide",
        "headline":       "Prime Day Pizza Accessories Worth Adding to Your Cart",
        "subhead":        "The under-$50 picks we actually use — all on Amazon, all worth watching June 23–26.",
        "layout":         "primeday",
        "badge_position": "top_right",
        "output":         "outputs/NEC-primeday-accessories-pin1.png",
    },
    {
        "photo_path":     "NinjaWoodfireHero.jpeg",
        "category":       "Oven Review",
        "headline":       "Our Pizza Oven Buying Guide — Save This Before You Shop",
        "subhead":        "Five ovens under $500 tested honestly — here's how we'd rank them and the one spec that matters most.",
        "layout":         "fullbleed",
        "badge_position": "top_right",
        "output":         "outputs/NEC-ovens-pin2.png",
    },
    {
        "photo_path":     "NinjaWoodfireHero.jpeg",
        "category":       "Oven Review",
        "headline":       "Propane vs Pellets vs Electric — Which Outdoor Pizza Oven Is Actually Worth It",
        "subhead":        "We tested all three fuel types. Here's the honest answer before you spend $300–$500.",
        "layout":         "split",
        "badge_position": "top_right",
        "output":         "outputs/NEC-ovens-pin3.png",
    },
    {
        "photo_path":     "NinjaWoodfireHero.jpeg",
        "category":       "Tips",
        "headline":       "The $20 Tool That Fixed Every Pizza We Were Making Wrong",
        "subhead":        "Your oven display shows air temp — not stone temp. This is the gap that ruins pizza. Here's what we use.",
        "layout":         "split",
        "badge_position": "top_left",
        "output":         "outputs/NEC-thermometer-pin1.png",
    },
    {
        "photo_path":     "IMG_8372.jpeg",
        "category":       "Recipe",
        "headline":       "Our Dough Starts Here — Caputo 00, Lievito Yeast, La Baleine Salt",
        "subhead":        "The exact three on our prep counter every cook — and why we've never swapped any of them out.",
        "layout":         "split",
        "output":         "outputs/NEC-00flour-pin3.png",
    },
    {
        "photo_path":     "NinjaWoodfireHero.jpeg",
        "category":       "Gear Guide",
        "headline":       "The 4 Ninja Woodfire Accessories You Need Before Your First Cook",
        "subhead":        "Cover, cord, peel, thermometer — the four we'd grab before your first cook. Under $80 total.",
        "layout":         "split",
        "output":         "outputs/NEC-accessories-pin7.png",
    },
    {
        "photo_path":     "IMG_8372.jpeg",
        "category":       "Recipe",
        "headline":       "The Three Ingredients We Always Have On Hand",
        "subhead":        "Three ingredients, same every time — Caputo 00 is the foundation. Here's why we never switch.",
        "layout":         "split",
        "output":         "outputs/NEC-00flour-pin1.png",
    },
    {
        "photo_path":     "IMG_8372.jpeg",
        "category":       "Tips",
        "headline":       "Why We Use Caputo 00 Flour for Every Pizza We Make",
        "subhead":        "Finer grind, faster hydration, cleaner blistered edge. Here's why we landed on 00 and stayed.",
        "layout":         "split",
        "output":         "outputs/NEC-00flour-pin2.png",
    },
    {
        "photo_path":     "NinjaWoodfireHero.jpeg",
        "category":       "Gear Guide",
        "headline":       "Don't Buy a Ninja Woodfire Cover Until You Read This",
        "subhead":        "Official or third-party — we tested both through two months of New England rain and wind to see which held up.",
        "layout":         "split",
        "output":         "outputs/NEC-accessories-pin8.png",
    },
    {
        "photo_path":     "NinjaWoodfireHero.jpeg",
        "category":       "Gear Guide",
        "headline":       "The $20 Accessory That Changed Every Pizza We Make",
        "subhead":        "This $20 thermometer reads stone temp, not air temp — the 100°F gap that used to leave us with pale bottoms.",
        "layout":         "split",
        "output":         "outputs/NEC-accessories-pin9.png",
    },
    {
        "photo_path":     "NinjaWoodfireHero.jpeg",
        "category":       "Gear Guide",
        "headline":       "What's Already in the Box — And What We Bought Anyway",
        "subhead":        "The OO101 comes with more than you'd think — here's what's included and what we still bought on day one.",
        "layout":         "split",
        "output":         "outputs/NEC-accessories-pin10.png",
    },
    {
        "photo_path":     "NinjaWoodfireHero.jpeg",
        "category":       "Gear Guide",
        "headline":       "Our Buy-Immediately List for the Ninja Woodfire (Under $80)",
        "subhead":        "Cover, cord, peel, thermometer — the four we bought before our first cook, all in for under $80.",
        "layout":         "split",
        "output":         "outputs/NEC-accessories-pin11.png",
    },
    {
        "photo_path":     "NinjaWoodfireHero.jpeg",
        "category":       "Oven Review",
        "headline":       "Save This Pizza Oven Guide Before You Spend $500",
        "subhead":        "Our honest outdoor pizza oven comparison — Ninja Woodfire vs Ooni, tested side by side before you spend $500.",
        "layout":         "fullbleed",
        "badge_position": "top_right",
        "output":         "outputs/NEC-ovens-pin4.png",
    },
    {
        "photo_path":     "NinjaWoodfireHero.jpeg",
        "category":       "Oven Review",
        "headline":       "5 Outdoor Pizza Ovens Tested — Only 2 Were Worth It",
        "subhead":        "Five ovens, real cooks — the pizza oven buying guide we wish we'd had before our first purchase.",
        "layout":         "split",
        "badge_position": "top_left",
        "output":         "outputs/NEC-ovens-pin5.png",
    },
    {
        "photo_path":     "NinjaWoodfireHero.jpeg",
        "category":       "Oven Review",
        "headline":       "The Pizza Oven Buying Mistake Everyone Makes",
        "subhead":        "The one spec most shoppers skip when picking the best outdoor pizza oven — it matters more than price or brand.",
        "layout":         "split",
        "badge_position": "top_right",
        "output":         "outputs/NEC-ovens-pin6.png",
    },
    {
        "photo_path":     "NinjaWoodfireHero.jpeg",
        "category":       "Oven Review",
        "headline":       "Read This Before You Buy an Outdoor Pizza Oven",
        "subhead":        "Propane, pellets, or electric — our pizza oven buying guide covers what we'd buy again and skip.",
        "layout":         "fullbleed",
        "badge_position": "top_left",
        "output":         "outputs/NEC-ovens-pin7.png",
    },
    {
        "photo_path":     "NinjaWoodfireHero.jpeg",
        "category":       "Oven Review",
        "headline":       "Pizza Oven Shopping? Pin This Checklist First",
        "subhead":        "Our best outdoor pizza oven picks under $500, plus the Ninja Woodfire vs Ooni question we get asked most.",
        "layout":         "split",
        "badge_position": "top_left",
        "output":         "outputs/NEC-ovens-pin8.png",
    },
    {
        "photo_path":     "NinjaWoodfireHero.jpeg",
        "category":       "Gear Guide",
        "headline":       "Don't Buy Ninja Woodfire Accessories Until You've Seen This Free Checklist",
        "subhead":        "The four accessories worth buying — free, one page, no guessing before you shop.",
        "layout":         "split",
        "flag":           "FREE",
        "output":         "outputs/NEC-quickstart-pin1.png",
    },
    {
        "photo_path":     "NinjaWoodfireHero.jpeg",
        "category":       "Gear Guide",
        "headline":       "The Only 4 Ninja Woodfire Accessories Worth Buying — Free One-Page Cheat Sheet",
        "subhead":        "Our exact buy-immediately list, pellet picks, and setup — free and printable.",
        "layout":         "split",
        "flag":           "FREE",
        "output":         "outputs/NEC-quickstart-pin2.png",
    },
    {
        "photo_path":     "NinjaWoodfireHero.jpeg",
        "category":       "Gear Guide",
        "headline":       "New Ninja Woodfire Owner? Start With This Free Printable Shopping List",
        "subhead":        "Skip the trial and error. Our free quick-start guide covers what to buy first.",
        "layout":         "split",
        "flag":           "FREE",
        "output":         "outputs/NEC-quickstart-pin3.png",
    },
    {
        "photo_path":     "NinjaWoodfireHero.jpeg",
        "category":       "Gear Guide",
        "headline":       "Ninja Woodfire Setup Under $100 — The Free Quick-Start Guide",
        "subhead":        "The exact accessories we bought under $100 — grab the free one-page guide.",
        "layout":         "split",
        "flag":           "FREE",
        "output":         "outputs/NEC-quickstart-pin4.png",
    },
    {
        "photo_path":     "NinjaWoodfireHero.jpeg",
        "category":       "Gear Guide",
        "headline":       "What's in the Box vs. What You Actually Need to Buy (Free Ninja Woodfire Guide)",
        "subhead":        "Free printable breakdown of what Ninja includes and what we bought anyway.",
        "layout":         "split",
        "flag":           "FREE",
        "output":         "outputs/NEC-quickstart-pin5.png",
    },
    {
        "photo_path":     "illustration:checklist",
        "category":       "Pizza Night",
        "headline":       "Hosting Pizza Night? This Free Printable Kit Does the Planning for You",
        "subhead":        "Timeline, dough math, and the toppings list — free and ready to print.",
        "layout":         "split",
        "flag":           "FREE",
        "output":         "outputs/NEC-partykit-pin1.png",
    },
    {
        "photo_path":     "illustration:checklist",
        "category":       "Pizza Night",
        "headline":       "How Much Pizza Dough for 12 People? The Free Party Kit Has the Math",
        "subhead":        "Dough quantities by guest count, free and printable — no more guessing before guests arrive.",
        "layout":         "split",
        "flag":           "FREE",
        "output":         "outputs/NEC-partykit-pin2.png",
    },
    {
        "photo_path":     "illustration:checklist",
        "category":       "Pizza Night",
        "headline":       "The 48-Hour Pizza Party Timeline — Free Printable Planning Kit",
        "subhead":        "Our exact 48-hour countdown, free and printable — so party day isn't a scramble.",
        "layout":         "split",
        "flag":           "FREE",
        "output":         "outputs/NEC-partykit-pin3.png",
    },
    # ── Add more pins below ───────────────────────────────────────────────────
    # {
    #     "photo_path": "your-photo.jpeg",   # or None for placeholder
    #     "category":   "Technique",          # Gear Guide / Pizza Night / Technique /
    #                                         # From the Hearth / Before You Buy / Recipe
    #     "headline":   "Your Headline Here",
    #     "subhead":    "One supporting line.",
    #     "layout":     "split",              # "split" or "fullbleed"
    #     "output":     "outputs/NEC-yourpost-pin1.png",
    #     "ember_badge": True,                # optional, defaults to True — Ember mascot
    #                                         # badge in the corner opposite badge_position
    # },
]

# ── HELPERS ───────────────────────────────────────────────────────────────────

def wrap_text(text, draw, font, max_width):
    """Word-wrap text to fit within max_width pixels."""
    words = text.split()
    lines, current = [], ""
    for word in words:
        test = (current + " " + word).strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


LOGO_PATH = "new-england-crust-logo.png"

def paste_logo_badge(canvas, cx, cy, size=152):
    """
    Paste the New England Crust badge logo (transparent PNG) centered at
    (cx, cy). `size` is the width/height of the pasted logo in pixels —
    152px makes the visible ring ~131px, matching the old drawn badge.
    Falls back to the procedural flame badge if the logo file is missing.
    """
    if not os.path.exists(LOGO_PATH):
        draw = ImageDraw.Draw(canvas, 'RGBA')
        draw_flame_badge(draw, cx, cy, scale=size / 185.0)
        return
    logo = Image.open(LOGO_PATH).convert('RGBA')
    logo = logo.resize((size, size), Image.LANCZOS)
    x = cx - size // 2
    y = cy - size // 2
    canvas.paste(logo, (x, y), logo)


# ── EMBER MASCOT BADGE ────────────────────────────────────────────────────────
# Composited opposite the NEC logo badge (which always sits at the TOP), so
# Ember always sits at the BOTTOM — the two never collide by construction.
EMBER_BADGE_PATH   = "../public/assets/ember/ember-badge-transparent.png"
EMBER_BADGE_WIDTH  = 100   # target on-canvas width, scaled down from the 2400px source
EMBER_BADGE_MARGIN = 30    # margin from canvas edge


def _load_ember_badge(size):
    """Load the Ember badge and LANCZOS-downscale it from its 2400px transparent source."""
    if not os.path.exists(EMBER_BADGE_PATH):
        return None
    src = Image.open(EMBER_BADGE_PATH).convert('RGBA')
    scale = size / src.width
    new_size = (max(1, size), max(1, int(round(src.height * scale))))
    return src.resize(new_size, Image.LANCZOS)


def ember_corner_for(raw_badge_position):
    """
    Ember always sits diagonally opposite the NEC logo badge:
      badge_position "top_left"  -> Ember "bottom_right"
      badge_position "top_right" -> Ember "bottom_left"
      badge_position absent      -> Ember "bottom_right" (explicit default)
    """
    if raw_badge_position == "top_left":
        return "bottom_right"
    elif raw_badge_position == "top_right":
        return "bottom_left"
    return "bottom_right"


# ── FREE FLAG BADGE ───────────────────────────────────────────────────────────
# Opt-in per-pin: only drawn when a queue entry sets `flag: FREE`. Entries
# without the field are completely unaffected — this function is simply
# never called for them.
FLAG_MARGIN = 30   # margin from canvas edge


def flag_corner_for(raw_badge_position):
    """
    The FREE flag always sits at the TOP, in the corner opposite the NEC
    logo badge, so the two never collide:
      badge_position "top_left"  -> flag "top_right"
      badge_position "top_right" -> flag "top_left"
      badge_position absent      -> flag "top_left" (NEC logo defaults top_right)
    """
    if raw_badge_position == "top_left":
        return "top_right"
    return "top_left"


def paste_free_flag(canvas, corner="top_left", margin=FLAG_MARGIN):
    """
    Draw a small rounded-rectangle FREE badge: ember (#C63D28) fill, bold
    sans-serif "FREE" text. Text is glow (#FF921A) by default, but that
    combination measures ~2.3:1 contrast — too low to read reliably at
    Pinterest phone-zoom sizes — so text falls back to white (~5.1:1).
    """
    draw = ImageDraw.Draw(canvas, 'RGBA')
    font_flag = _font(MAC_SANS_BOLD, LIN_SANS_BOLD, 24)

    label = "FREE"
    bbox  = draw.textbbox((0, 0), label, font=font_flag)
    text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]

    pad_x, pad_y = 22, 12
    box_w = text_w + pad_x * 2
    box_h = text_h + pad_y * 2

    canvas_w, _ = canvas.size
    top = margin
    left = margin if corner == "top_left" else (canvas_w - margin - box_w)
    right = left + box_w
    bottom = top + box_h

    draw.rounded_rectangle([left, top, right, bottom], radius=box_h // 3,
                            fill=FLAG_EMBER)

    text_color = FLAG_GLOW if _contrast_ratio(FLAG_GLOW, FLAG_EMBER) >= 3.0 else FLAG_WHITE
    text_x = left + pad_x
    text_y = top + pad_y - bbox[1]
    draw.text((text_x, text_y), label, font=font_flag, fill=text_color)


def _contrast_ratio(rgb1, rgb2):
    """WCAG relative-luminance contrast ratio between two RGB colors."""
    def _luminance(rgb):
        def channel(c):
            c = c / 255.0
            return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
        r, g, b = (channel(c) for c in rgb)
        return 0.2126 * r + 0.7152 * g + 0.0722 * b
    l1, l2 = _luminance(rgb1), _luminance(rgb2)
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def paste_ember_badge(canvas, corner="bottom_right", text_bottom=0, enabled=True,
                       size=EMBER_BADGE_WIDTH, margin=EMBER_BADGE_MARGIN):
    """
    Composite the Ember mascot badge into a bottom corner of the pin (PIL
    alpha compositing via canvas.paste(badge, pos, badge)).

    It never overlaps the NEC logo badge (that one lives at the top; Ember
    always lives at the bottom). It also never overlaps headline/subhead
    text: `text_bottom` is the y-coordinate where the last drawn text line
    ends, and if the default ~100px badge would intrude above that line,
    the badge is scaled down to fit the remaining gap. If there's no usable
    room at all, the badge is skipped rather than drawn over text.
    """
    if not enabled:
        return

    canvas_w, canvas_h = canvas.size
    floor_y   = canvas_h - margin     # bottom edge the badge is anchored to
    safety_gap = 12                   # breathing room above the text
    available = floor_y - (text_bottom + safety_gap)

    badge_size = size if available >= size else available
    if badge_size < 40:
        # Not enough vertical room to avoid overlapping text — skip.
        return

    badge = _load_ember_badge(size=badge_size)
    if badge is None:
        return

    bw, bh = badge.size
    y = floor_y - bh
    x = margin if corner == "bottom_left" else (canvas_w - margin - bw)

    canvas.paste(badge, (x, y), badge)


def draw_flame_badge(draw, cx, cy, scale=1.0):
    """
    Draw the NEC badge mark: circle ring + leaning flame + CRUST wordmark.
    cx, cy = center of badge. scale = size multiplier (1.0 = 80px radius).
    """
    r = int(80 * scale)

    # Background circle
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=DEEP_CHAR)
    # Outer ring — Ember Amber
    draw.ellipse([cx - r, cy - r, cx + r, cy + r],
                 outline=EMBER_AMBER, width=max(2, int(3 * scale)))
    # Inner ring — Warm Cream subtle
    ri = int(r * 0.93)
    draw.ellipse([cx - ri, cy - ri, cx + ri, cy + ri],
                 outline=(*WARM_CREAM, 40), width=1)

    # Flame — simplified three-layer polygon version
    def scaled(pts):
        return [(cx + int(x * scale), cy + int(y * scale)) for x, y in pts]

    # Center flame outer (coral)
    draw.polygon(scaled([
        (0, -52), (18, -28), (10, 0), (-10, 0), (-18, -28)
    ]), fill=CORAL_RED)
    # Center flame mid (ember orange)
    draw.polygon(scaled([
        (0, -40), (12, -20), (7,  0),  (-7,  0), (-12, -20)
    ]), fill=EMBER_ORANGE)
    # Center flame inner (gold)
    draw.polygon(scaled([
        (0, -28), (7, -12), (4,  0), (-4,  0), (-7, -12)
    ]), fill=GOLD)
    # Left side flame (coral, smaller)
    draw.polygon(scaled([
        (-16, -30), (-8, -16), (-12, 0), (-20, 0), (-24, -16)
    ]), fill=(*CORAL_RED, 180))
    # Right side flame (coral, smaller)
    draw.polygon(scaled([
        (16, -30), (24, -16), (20, 0), (12, 0), (8, -16)
    ]), fill=(*CORAL_RED, 180))

    # Ember glow ellipse
    draw.ellipse([cx - int(28*scale), cy - int(6*scale),
                  cx + int(28*scale), cy + int(6*scale)],
                 fill=(*EMBER_ORANGE, 30))

    # CRUST wordmark below flame
    font_crust = _font(MAC_SERIF_BOLD, LIN_SERIF_BOLD, max(10, int(18 * scale)))
    bbox = draw.textbbox((0, 0), "CRUST", font=font_crust)
    tw = bbox[2] - bbox[0]
    draw.text((cx - tw // 2, cy + int(8 * scale)),
              "CRUST", font=font_crust, fill=WARM_CREAM)


def apply_dark_gradient(img, start_y, end_y, max_alpha=0.82):
    """
    Paint a dark-to-transparent gradient from end_y up to start_y.
    max_alpha: darkness at the very bottom (0-1).
    """
    pixels = img.load()
    w, h = img.size
    span = end_y - start_y
    for y in range(start_y, min(end_y, h)):
        t = (y - start_y) / span          # 0 at top of gradient, 1 at bottom
        alpha = t * max_alpha
        for x in range(w):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                int(r * (1 - alpha) + DEEP_CHAR[0] * alpha),
                int(g * (1 - alpha) + DEEP_CHAR[1] * alpha),
                int(b * (1 - alpha) + DEEP_CHAR[2] * alpha),
            )
    return img


def draw_checklist_illustration(target_h):
    """
    Flat-illustration stand-in for pins with no product photo: a timber-toned
    "page" card lying on the deep char/twilight background, with a header
    bar and a short checkmark-and-line checklist. Built entirely from PIL
    primitives already used elsewhere in this file (rounded_rectangle,
    ellipse, line) — no new photo, no new dependency.
    """
    img = Image.new('RGB', (W, target_h), DEEP_CHAR)
    draw = ImageDraw.Draw(img, 'RGBA')

    card_w = int(W * 0.62)
    card_h = int(target_h * 0.68)
    card_x = (W - card_w) // 2
    card_y = (target_h - card_h) // 2 - 20

    # Soft drop shadow, offset down-right, so the card reads as lying on
    # the background rather than pasted flat onto it.
    shadow_off = 14
    draw.rounded_rectangle(
        [card_x + shadow_off, card_y + shadow_off,
         card_x + card_w + shadow_off, card_y + card_h + shadow_off],
        radius=18, fill=CARD_SHADOW,
    )

    # Page body
    draw.rounded_rectangle(
        [card_x, card_y, card_x + card_w, card_y + card_h],
        radius=18, fill=TIMBER_PAGE,
    )

    # Header bar across the top of the page — rounded top, square bottom so
    # it reads as one continuous strip rather than a floating pill.
    header_h = int(card_h * 0.16)
    draw.rounded_rectangle(
        [card_x, card_y, card_x + card_w, card_y + header_h],
        radius=18, fill=TIMBER_HEADER,
    )
    draw.rectangle(
        [card_x, card_y + header_h - 18, card_x + card_w, card_y + header_h],
        fill=TIMBER_HEADER,
    )

    # Checklist rows — checkmark circle + line, 4 rows
    rows       = 4
    row_pad_x  = int(card_w * 0.12)
    list_top   = card_y + header_h + int(card_h * 0.12)
    list_bot   = card_y + card_h - int(card_h * 0.10)
    row_gap    = (list_bot - list_top) // rows
    check_r    = 12

    for i in range(rows):
        ry = list_top + i * row_gap + row_gap // 2
        cx = card_x + row_pad_x

        draw.ellipse([cx - check_r, ry - check_r, cx + check_r, ry + check_r],
                     outline=GLOW_CHECK, width=3)
        draw.line([(cx - 5, ry), (cx - 1, ry + 5), (cx + 7, ry - 7)],
                  fill=GLOW_CHECK, width=3)

        line_x0 = cx + check_r + 16
        line_x1 = card_x + card_w - row_pad_x
        draw.line([(line_x0, ry), (line_x1, ry)], fill=TIMBER_LINE, width=6)

    return img


def load_photo(photo_path):
    """Load, auto-orient, and crop photo to W×(H*2//3)."""
    target_h = H * 2 // 3  # top two-thirds

    if photo_path == ILLUSTRATION_CHECKLIST:
        return draw_checklist_illustration(target_h)

    if photo_path and os.path.exists(photo_path):
        img = Image.open(photo_path).convert('RGB')
        # EXIF orientation — rotate landscape iPhones to portrait
        src_w, src_h = img.size
        if src_w > src_h:
            img = img.rotate(270, expand=True)
            src_w, src_h = img.size
        # Center crop to W × target_h
        ratio = W / target_h
        if src_w / src_h > ratio:
            new_w = int(src_h * ratio)
            left  = (src_w - new_w) // 2
            img   = img.crop((left, 0, left + new_w, src_h))
        else:
            new_h = int(src_w / ratio)
            top   = (src_h - new_h) // 4   # bias toward top of photo
            img   = img.crop((0, top, src_w, top + new_h))
        img = img.resize((W, target_h), Image.LANCZOS)
    else:
        # Placeholder: deep char with centered PHOTO label
        img = Image.new('RGB', (W, target_h), DEEP_CHAR)
        d   = ImageDraw.Draw(img)
        f   = _font(MAC_SERIF_REG, LIN_SERIF_REG, 36)
        bbox = d.textbbox((0, 0), "PHOTO", font=f)
        tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
        d.text(((W - tw)//2, (target_h - th)//2),
               "PHOTO", font=f, fill=(60, 50, 40))
    return img


def draw_diamond_rule(draw, y, left, right, amber):
    """Draw ── ◆ ── rule in Ember Amber."""
    mid    = (left + right) // 2
    d_size = 7
    # Left rule
    draw.line([(left, y), (mid - d_size - 8, y)],
              fill=(*amber, 160), width=1)
    # Diamond
    draw.polygon([
        (mid,          y - d_size),
        (mid + d_size, y),
        (mid,          y + d_size),
        (mid - d_size, y),
    ], fill=(*amber, 200))
    # Right rule
    draw.line([(mid + d_size + 8, y), (right, y)],
              fill=(*amber, 160), width=1)


# ── SPLIT LAYOUT (2/3 photo + 1/3 text block) ─────────────────────────────────

def make_pin_split(photo_path, category, headline, subhead, output_path, badge_position="top_right",
                    ember_badge=True, ember_corner="bottom_right", flag=None):
    PHOTO_H  = H * 2 // 3   # 1000px
    TEXT_H   = H - PHOTO_H  # 500px
    LEFT     = 52
    RIGHT    = W - 52
    TEXT_W   = RIGHT - LEFT

    # ── Photo area ────────────────────────────────────────────────────────────
    photo = load_photo(photo_path)
    # Subtle vignette on bottom edge of photo so it bleeds into text block
    apply_dark_gradient(photo, int(PHOTO_H * 0.72), PHOTO_H, max_alpha=0.70)

    # ── Full canvas ───────────────────────────────────────────────────────────
    canvas = Image.new('RGB', (W, H), DEEP_CHAR)
    canvas.paste(photo, (0, 0))
    draw = ImageDraw.Draw(canvas, 'RGBA')

    # Badge mark — top right or top left of photo area
    badge_cx = 88 if badge_position == "top_left" else W - 88
    paste_logo_badge(canvas, cx=badge_cx, cy=88)

    # FREE flag — opt-in, opposite top corner from the NEC logo badge
    if flag:
        paste_free_flag(canvas, corner=flag_corner_for(badge_position))

    # ── Text block ────────────────────────────────────────────────────────────
    TEXT_TOP = PHOTO_H
    PADDING  = 38

    # Footer URL — anchored to very bottom
    font_url  = _font(MAC_SERIF_BOLD, LIN_SERIF_BOLD, 19)
    url_text  = "N E W E N G L A N D C R U S T . C O M"
    url_bbox  = draw.textbbox((0,0), url_text, font=font_url)
    url_w     = url_bbox[2] - url_bbox[0]
    url_y     = H - PADDING - (url_bbox[3] - url_bbox[1])
    draw.text(((W - url_w) // 2, url_y),
              url_text, font=font_url, fill=EMBER_AMBER)

    # Thin rule above URL
    rule_y = url_y - 18
    draw.line([(LEFT, rule_y), (RIGHT, rule_y)],
              fill=(*EMBER_AMBER, 60), width=1)

    # Headline — serif bold, Warm Cream, builds DOWN from text top
    font_hl   = _font(MAC_SERIF_BOLD, LIN_SERIF_BOLD, 66)
    hl_line_h = 74
    cat_block = 72   # space reserved above headline for category label

    # Measure headline to know how many lines we have
    hl_y_start = TEXT_TOP + PADDING + cat_block
    hl_lines   = wrap_text(headline, draw, font_hl, TEXT_W)[:3]

    y = hl_y_start
    for line in hl_lines:
        draw.text((LEFT, y), line, font=font_hl, fill=WARM_CREAM)
        y += hl_line_h

    # Subhead — italic, slightly muted cream
    if subhead:
        font_sub = _font(MAC_SERIF_ITALIC, LIN_SERIF_ITALIC, 26)
        sub_lines = wrap_text(subhead, draw, font_sub, TEXT_W)[:2]
        y += 8
        for line in sub_lines:
            draw.text((LEFT, y), line, font=font_sub,
                      fill=(*WARM_CREAM, 160))
            y += 34

    # Category label + diamond rule — just above headline
    cat_y   = TEXT_TOP + PADDING
    font_cat = _font(MAC_SERIF_BOLD, LIN_SERIF_BOLD, 20)
    cat_upper = category.upper()
    cat_bbox  = draw.textbbox((0,0), cat_upper, font=font_cat)
    cat_w     = cat_bbox[2] - cat_bbox[0]
    cat_x     = (W - cat_w) // 2
    draw.text((cat_x, cat_y), cat_upper, font=font_cat, fill=EMBER_AMBER)

    rule_y2 = cat_y + (cat_bbox[3]-cat_bbox[1]) + 10
    draw_diamond_rule(draw, rule_y2, LEFT, RIGHT, EMBER_AMBER)

    # Ember mascot badge — bottom corner, opposite the NEC logo
    paste_ember_badge(canvas, corner=ember_corner, text_bottom=y, enabled=ember_badge)

    # Save
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    canvas.convert('RGB').save(output_path, 'PNG', quality=95)
    print(f"  ✓ Saved: {output_path}")


# ── FULL-BLEED LAYOUT (photo fills pin, gradient overlay on bottom 40%) ───────

def make_pin_fullbleed(photo_path, category, headline, subhead, output_path, badge_position="top_right",
                        ember_badge=True, ember_corner="bottom_right", flag=None):
    LEFT   = 52
    RIGHT  = W - 52
    TEXT_W = RIGHT - LEFT

    # ── Photo full canvas ─────────────────────────────────────────────────────
    if photo_path and os.path.exists(photo_path):
        img = Image.open(photo_path).convert('RGB')
        src_w, src_h = img.size
        if src_w > src_h:
            img = img.rotate(270, expand=True)
            src_w, src_h = img.size
        ratio = W / H
        if src_w / src_h > ratio:
            new_w = int(src_h * ratio)
            left  = (src_w - new_w) // 2
            img   = img.crop((left, 0, left + new_w, src_h))
        else:
            new_h = int(src_w / ratio)
            img   = img.crop((0, 0, src_w, new_h))
        img = img.resize((W, H), Image.LANCZOS)
    else:
        img = Image.new('RGB', (W, H), DEEP_CHAR)

    # Dark gradient over bottom 40%
    grad_start = int(H * 0.55)
    apply_dark_gradient(img, grad_start, H, max_alpha=0.88)

    draw = ImageDraw.Draw(img, 'RGBA')

    # Badge mark — top right or top left
    badge_cx = 88 if badge_position == "top_left" else W - 88
    paste_logo_badge(img, cx=badge_cx, cy=88)

    # FREE flag — opt-in, opposite top corner from the NEC logo badge
    if flag:
        paste_free_flag(img, corner=flag_corner_for(badge_position))

    # Footer URL
    font_url = _font(MAC_SERIF_BOLD, LIN_SERIF_BOLD, 19)
    url_text = "N E W E N G L A N D C R U S T . C O M"
    url_bbox = draw.textbbox((0,0), url_text, font=font_url)
    url_w    = url_bbox[2] - url_bbox[0]
    url_y    = H - 46 - (url_bbox[3] - url_bbox[1])
    draw.text(((W - url_w) // 2, url_y),
              url_text, font=font_url, fill=EMBER_AMBER)

    # Category label
    font_cat  = _font(MAC_SERIF_BOLD, LIN_SERIF_BOLD, 20)
    cat_upper = category.upper()
    cat_bbox  = draw.textbbox((0,0), cat_upper, font=font_cat)
    cat_w     = cat_bbox[2] - cat_bbox[0]
    cat_y     = int(H * 0.58)
    draw.text(((W - cat_w) // 2, cat_y), cat_upper,
              font=font_cat, fill=EMBER_AMBER)

    rule_y = cat_y + (cat_bbox[3]-cat_bbox[1]) + 10
    draw_diamond_rule(draw, rule_y, LEFT, RIGHT, EMBER_AMBER)

    # Headline
    font_hl   = _font(MAC_SERIF_BOLD, LIN_SERIF_BOLD, 62)
    hl_line_h = 70
    hl_lines  = wrap_text(headline, draw, font_hl, TEXT_W)[:3]
    y = rule_y + 22
    for line in hl_lines:
        draw.text((LEFT, y), line, font=font_hl, fill=WARM_CREAM)
        y += hl_line_h

    # Subhead
    if subhead:
        font_sub  = _font(MAC_SERIF_ITALIC, LIN_SERIF_ITALIC, 26)
        sub_lines = wrap_text(subhead, draw, font_sub, TEXT_W)[:2]
        y += 8
        for line in sub_lines:
            draw.text((LEFT, y), line, font=font_sub,
                      fill=(*WARM_CREAM, 155))
            y += 34

    # Ember mascot badge — bottom corner, opposite the NEC logo
    paste_ember_badge(img, corner=ember_corner, text_bottom=y, enabled=ember_badge)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.convert('RGB').save(output_path, 'PNG', quality=95)
    print(f"  ✓ Saved: {output_path}")


# ── PRIME DAY LAYOUT (fullbleed photo + Prime Day pill callout) ───────────────

def make_pin_primeday(photo_path, category, headline, subhead, output_path, badge_position="top_right",
                       ember_badge=True, ember_corner="bottom_right", flag=None):
    LEFT   = 52
    RIGHT  = W - 52
    TEXT_W = RIGHT - LEFT

    # ── Photo full canvas ─────────────────────────────────────────────────────
    if photo_path and os.path.exists(photo_path):
        img = Image.open(photo_path).convert('RGB')
        src_w, src_h = img.size
        if src_w > src_h:
            img = img.rotate(270, expand=True)
            src_w, src_h = img.size
        ratio = W / H
        if src_w / src_h > ratio:
            new_w = int(src_h * ratio)
            left  = (src_w - new_w) // 2
            img   = img.crop((left, 0, left + new_w, src_h))
        else:
            new_h = int(src_w / ratio)
            img   = img.crop((0, 0, src_w, new_h))
        img = img.resize((W, H), Image.LANCZOS)
    else:
        img = Image.new('RGB', (W, H), DEEP_CHAR)

    # Dark gradient over bottom 45%
    apply_dark_gradient(img, int(H * 0.50), H, max_alpha=0.92)

    draw = ImageDraw.Draw(img, 'RGBA')

    # ── Badge mark ────────────────────────────────────────────────────────────
    badge_cx = 88 if badge_position == "top_left" else W - 88
    paste_logo_badge(img, cx=badge_cx, cy=88)

    # FREE flag — primeday's top-left is always taken by the Prime Day pill
    # below, and top-right conventionally holds the NEC logo on this layout,
    # so there's no top corner that avoids both. Skip rather than overlap.
    if flag:
        print(f"  ! Skipped FREE flag on {output_path}: primeday layout has "
              f"no free top corner (pill occupies top-left, logo top-right).")

    # ── Prime Day pill — top left (single stacked block) ─────────────────────
    PILL_LEFT = 44
    PILL_TOP  = 44
    PAD_X     = 24
    PAD_Y     = 14

    font_amazon = _font(MAC_SERIF_BOLD, LIN_SERIF_BOLD, 18)
    font_pill   = _font(MAC_SERIF_BOLD, LIN_SERIF_BOLD, 32)
    font_date   = _font(MAC_SERIF_BOLD, LIN_SERIF_BOLD, 17)

    amazon_bbox = draw.textbbox((0,0), "AMAZON", font=font_amazon)
    amazon_h    = amazon_bbox[3] - amazon_bbox[1]
    amazon_w    = amazon_bbox[2] - amazon_bbox[0]

    pill_bbox   = draw.textbbox((0,0), "PRIME DAY PICKS", font=font_pill)
    pill_h      = pill_bbox[3] - pill_bbox[1]
    pill_w      = pill_bbox[2] - pill_bbox[0]

    date_bbox   = draw.textbbox((0,0), "JUNE 23 – 26, 2026", font=font_date)
    date_h      = date_bbox[3] - date_bbox[1]
    date_w      = date_bbox[2] - date_bbox[0]

    # Block width = widest element + padding both sides
    BLOCK_W = max(amazon_w, pill_w, date_w) + PAD_X * 2
    # Block height = all three rows + gaps + padding top/bottom
    GAP          = 10
    BLOCK_H      = PAD_Y + amazon_h + GAP + pill_h + GAP + date_h + PAD_Y
    PILL_RIGHT   = PILL_LEFT + BLOCK_W
    PILL_BOTTOM  = PILL_TOP  + BLOCK_H

    # Draw single amber rectangle
    draw.rectangle(
        [PILL_LEFT, PILL_TOP, PILL_RIGHT, PILL_BOTTOM],
        fill=EMBER_AMBER
    )

    # AMAZON — small, dark char, top of block
    amazon_y = PILL_TOP + PAD_Y
    draw.text((PILL_LEFT + PAD_X, amazon_y),
              "AMAZON", font=font_amazon, fill=DEEP_CHAR)

    # PRIME DAY PICKS — bold, dark char, middle
    picks_y = amazon_y + amazon_h + GAP
    draw.text((PILL_LEFT + PAD_X, picks_y),
              "PRIME DAY PICKS", font=font_pill, fill=DEEP_CHAR)

    # JUNE 23 – 26, 2026 — small, slightly muted, bottom
    date_y = picks_y + pill_h + GAP
    draw.text((PILL_LEFT + PAD_X, date_y),
              "JUNE 23 – 26, 2026", font=font_date,
              fill=(*DEEP_CHAR, 180))

    # ── Footer URL ────────────────────────────────────────────────────────────
    font_url = _font(MAC_SERIF_BOLD, LIN_SERIF_BOLD, 19)
    url_text = "N E W E N G L A N D C R U S T . C O M"
    url_bbox = draw.textbbox((0,0), url_text, font=font_url)
    url_w    = url_bbox[2] - url_bbox[0]
    url_y    = H - 46 - (url_bbox[3] - url_bbox[1])
    draw.text(((W - url_w) // 2, url_y),
              url_text, font=font_url, fill=EMBER_AMBER)

    # Thin rule above URL
    draw.line([(LEFT, url_y - 18), (RIGHT, url_y - 18)],
              fill=(*EMBER_AMBER, 60), width=1)

    # ── Category label + diamond rule ─────────────────────────────────────────
    font_cat  = _font(MAC_SERIF_BOLD, LIN_SERIF_BOLD, 20)
    cat_upper = category.upper()
    cat_bbox  = draw.textbbox((0,0), cat_upper, font=font_cat)
    cat_w     = cat_bbox[2] - cat_bbox[0]
    cat_y     = int(H * 0.66)
    draw.text(((W - cat_w) // 2, cat_y),
              cat_upper, font=font_cat, fill=EMBER_AMBER)

    rule_y = cat_y + (cat_bbox[3] - cat_bbox[1]) + 10
    draw_diamond_rule(draw, rule_y, LEFT, RIGHT, EMBER_AMBER)

    # ── Headline ──────────────────────────────────────────────────────────────
    font_hl   = _font(MAC_SERIF_BOLD, LIN_SERIF_BOLD, 62)
    hl_line_h = 70
    hl_lines  = wrap_text(headline, draw, font_hl, TEXT_W)[:3]
    y = rule_y + 22
    for line in hl_lines:
        draw.text((LEFT, y), line, font=font_hl, fill=WARM_CREAM)
        y += hl_line_h

    # ── Subhead ───────────────────────────────────────────────────────────────
    if subhead:
        font_sub  = _font(MAC_SERIF_ITALIC, LIN_SERIF_ITALIC, 26)
        sub_lines = wrap_text(subhead, draw, font_sub, TEXT_W)[:2]
        y += 8
        for line in sub_lines:
            draw.text((LEFT, y), line, font=font_sub,
                      fill=(*WARM_CREAM, 155))
            y += 34

    # Ember mascot badge — bottom corner, opposite the NEC logo
    paste_ember_badge(img, corner=ember_corner, text_bottom=y, enabled=ember_badge)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.convert('RGB').save(output_path, 'PNG', quality=95)
    print(f"  ✓ Saved: {output_path}")


# ── DISPATCH ──────────────────────────────────────────────────────────────────

def make_pin(pin):
    layout = pin.get("layout", "split")
    kwargs = dict(
        photo_path     = pin.get("photo_path"),
        category       = pin.get("category", "New England Crust"),
        headline       = pin.get("headline", ""),
        subhead        = pin.get("subhead", ""),
        output_path    = pin["output"],
        badge_position = pin.get("badge_position", "top_right"),
        ember_badge    = pin.get("ember_badge", True),
        ember_corner   = ember_corner_for(pin.get("badge_position")),
        flag           = pin.get("flag"),
    )
    if layout == "fullbleed":
        make_pin_fullbleed(**kwargs)
    elif layout == "primeday":
        make_pin_primeday(**kwargs)
    else:
        make_pin_split(**kwargs)


# ── RUN ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("New England Crust — Pinterest Pin Generator v2\n")
    for pin in PINS:
        print(f"  Generating: {pin['output']}")
        make_pin(pin)
    print("\nDone. Check the outputs/ folder.")
