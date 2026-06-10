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
        "output":     "outputs/NEC-pizzanight-v2.png",
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


def load_photo(photo_path):
    """Load, auto-orient, and crop photo to W×(H*2//3)."""
    target_h = H * 2 // 3  # top two-thirds

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

def make_pin_split(photo_path, category, headline, subhead, output_path):
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

    # Badge mark — top right of photo area
    draw_flame_badge(draw, cx=W - 88, cy=88, scale=0.82)

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

    # Save
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    canvas.convert('RGB').save(output_path, 'PNG', quality=95)
    print(f"  ✓ Saved: {output_path}")


# ── FULL-BLEED LAYOUT (photo fills pin, gradient overlay on bottom 40%) ───────

def make_pin_fullbleed(photo_path, category, headline, subhead, output_path):
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

    # Badge mark top-right
    draw_flame_badge(draw, cx=W - 88, cy=88, scale=0.82)

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

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.convert('RGB').save(output_path, 'PNG', quality=95)
    print(f"  ✓ Saved: {output_path}")


# ── DISPATCH ──────────────────────────────────────────────────────────────────

def make_pin(pin):
    layout = pin.get("layout", "split")
    kwargs = dict(
        photo_path  = pin.get("photo_path"),
        category    = pin.get("category", "New England Crust"),
        headline    = pin.get("headline", ""),
        subhead     = pin.get("subhead", ""),
        output_path = pin["output"],
    )
    if layout == "fullbleed":
        make_pin_fullbleed(**kwargs)
    else:
        make_pin_split(**kwargs)


# ── RUN ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("New England Crust — Pinterest Pin Generator v2\n")
    for pin in PINS:
        print(f"  Generating: {pin['output']}")
        make_pin(pin)
    print("\nDone. Check the outputs/ folder.")
