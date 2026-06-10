"""
New England Crust — Lead Magnet PDF Generator
Ninja Woodfire Quick-Start Cheat Sheet

Run this script in Cowork to generate the lead magnet PDF.
Output: /mnt/user-data/outputs/ninja-woodfire-quickstart.pdf

Dependencies (install if missing):
    pip install reportlab --break-system-packages

─────────────────────────────────────────────
OVEN PHOTO — SET THIS BEFORE RUNNING
─────────────────────────────────────────────
To add your oven photo to the cover page, set COVER_PHOTO_PATH below
to the full path of your image file. JPG or PNG both work.

Example (local Mac path passed into Cowork):
    COVER_PHOTO_PATH = "/Users/michaelspinney/Desktop/oven-patio.jpg"

Example (if the image is already in your repo public folder):
    COVER_PHOTO_PATH = "/Users/michaelspinney/Desktop/new-england-crust/public/oven-hero.jpg"

Leave it as None to generate the cover without a photo (title-only layout).
─────────────────────────────────────────────
"""

COVER_PHOTO_PATH = "/Users/michaelspinney/Desktop/new-england-crust/NinjaWoodfireHero.jpeg"

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.platypus import Image as RLImage
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import Flowable
import os

# ─────────────────────────────────────────────
# BRAND PALETTE
# ─────────────────────────────────────────────
DARK_BG       = colors.HexColor("#111510")   # near-black background
CREAM         = colors.HexColor("#F5EFE0")   # warm cream text
TERRACOTTA    = colors.HexColor("#C84B2E")   # primary accent
AMBER         = colors.HexColor("#C87941")   # secondary accent
MUTED_CREAM   = colors.HexColor("#BFB59E")   # subdued body text
RULE_COLOR    = colors.HexColor("#3A3A30")   # subtle rule lines
CARD_BG       = colors.HexColor("#1C201A")   # card/section background
WHITE         = colors.HexColor("#FFFFFF")

OUTPUT_PATH = "/mnt/user-data/outputs/ninja-woodfire-quickstart.pdf"

# ─────────────────────────────────────────────
# CUSTOM FLOWABLES
# ─────────────────────────────────────────────

class ColoredBackground(Flowable):
    """Full-width colored rectangle for section headers."""
    def __init__(self, width, height, bg_color, text, text_color, font_name, font_size, padding=8):
        super().__init__()
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.text = text
        self.text_color = text_color
        self.font_name = font_name
        self.font_size = font_size
        self.padding = padding

    def draw(self):
        self.canv.setFillColor(self.bg_color)
        self.canv.rect(0, 0, self.width, self.height, fill=1, stroke=0)
        self.canv.setFillColor(self.text_color)
        self.canv.setFont(self.font_name, self.font_size)
        self.canv.drawString(self.padding, self.height / 2 - self.font_size / 3, self.text)


class AccentRule(Flowable):
    """A two-line decorative rule: thick terracotta + thin cream."""
    def __init__(self, width):
        super().__init__()
        self.width = width
        self.height = 6

    def draw(self):
        self.canv.setStrokeColor(TERRACOTTA)
        self.canv.setLineWidth(3)
        self.canv.line(0, 4, self.width, 4)
        self.canv.setStrokeColor(CREAM)
        self.canv.setLineWidth(0.5)
        self.canv.line(0, 1, self.width, 1)


class CheckItem(Flowable):
    """A single checklist item with a terracotta checkbox + cream text."""
    def __init__(self, width, label, sublabel=None):
        super().__init__()
        self.width = width
        self.label = label
        self.sublabel = sublabel
        self.height = 32 if sublabel else 24

    def draw(self):
        # Box
        self.canv.setStrokeColor(TERRACOTTA)
        self.canv.setLineWidth(1.2)
        self.canv.rect(0, self.height - 14, 12, 12, fill=0, stroke=1)
        # Main label
        self.canv.setFillColor(CREAM)
        self.canv.setFont("Helvetica-Bold", 10)
        self.canv.drawString(20, self.height - 12, self.label)
        # Sub label
        if self.sublabel:
            self.canv.setFillColor(MUTED_CREAM)
            self.canv.setFont("Helvetica-Oblique", 8.5)
            self.canv.drawString(20, self.height - 26, self.sublabel)


# ─────────────────────────────────────────────
# STYLES
# ─────────────────────────────────────────────

def build_styles():
    return {
        "cover_brand": ParagraphStyle(
            "cover_brand",
            fontName="Helvetica",
            fontSize=9,
            textColor=MUTED_CREAM,
            alignment=TA_CENTER,
            spaceAfter=4,
            letterSpacing=4,
        ),
        "cover_title": ParagraphStyle(
            "cover_title",
            fontName="Helvetica-Bold",
            fontSize=28,
            textColor=CREAM,
            alignment=TA_CENTER,
            spaceAfter=10,
            leading=34,
        ),
        "cover_subtitle": ParagraphStyle(
            "cover_subtitle",
            fontName="Helvetica",
            fontSize=12,
            textColor=MUTED_CREAM,
            alignment=TA_CENTER,
            spaceAfter=6,
            leading=18,
        ),
        "section_label": ParagraphStyle(
            "section_label",
            fontName="Helvetica",
            fontSize=7.5,
            textColor=TERRACOTTA,
            alignment=TA_LEFT,
            spaceAfter=2,
            spaceBefore=16,
            letterSpacing=2.5,
        ),
        "section_heading": ParagraphStyle(
            "section_heading",
            fontName="Helvetica-Bold",
            fontSize=14,
            textColor=CREAM,
            alignment=TA_LEFT,
            spaceAfter=6,
            leading=18,
        ),
        "body": ParagraphStyle(
            "body",
            fontName="Helvetica",
            fontSize=9.5,
            textColor=MUTED_CREAM,
            alignment=TA_LEFT,
            spaceAfter=6,
            leading=15,
        ),
        "callout": ParagraphStyle(
            "callout",
            fontName="Helvetica-Bold",
            fontSize=9,
            textColor=CREAM,
            alignment=TA_LEFT,
            spaceAfter=3,
            leading=14,
        ),
        "callout_sub": ParagraphStyle(
            "callout_sub",
            fontName="Helvetica-Oblique",
            fontSize=8.5,
            textColor=MUTED_CREAM,
            alignment=TA_LEFT,
            spaceAfter=2,
            leading=13,
        ),
        "footer": ParagraphStyle(
            "footer",
            fontName="Helvetica",
            fontSize=7.5,
            textColor=RULE_COLOR,
            alignment=TA_CENTER,
        ),
        "table_header": ParagraphStyle(
            "table_header",
            fontName="Helvetica-Bold",
            fontSize=8.5,
            textColor=CREAM,
            alignment=TA_LEFT,
        ),
        "table_body": ParagraphStyle(
            "table_body",
            fontName="Helvetica",
            fontSize=8.5,
            textColor=MUTED_CREAM,
            alignment=TA_LEFT,
            leading=13,
        ),
        "table_accent": ParagraphStyle(
            "table_accent",
            fontName="Helvetica-Bold",
            fontSize=8.5,
            textColor=TERRACOTTA,
            alignment=TA_LEFT,
        ),
        "tip_label": ParagraphStyle(
            "tip_label",
            fontName="Helvetica-Bold",
            fontSize=8,
            textColor=AMBER,
            alignment=TA_LEFT,
            letterSpacing=1,
        ),
        "tip_body": ParagraphStyle(
            "tip_body",
            fontName="Helvetica",
            fontSize=9,
            textColor=CREAM,
            alignment=TA_LEFT,
            leading=14,
        ),
    }


# ─────────────────────────────────────────────
# DOCUMENT BUILDER
# ─────────────────────────────────────────────

def build_pdf():
    W, H = letter  # 612 x 792 pts
    content_width = W - 2 * inch

    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=letter,
        leftMargin=inch,
        rightMargin=inch,
        topMargin=0.6 * inch,
        bottomMargin=0.6 * inch,
        title="Ninja Woodfire Quick-Start — New England Crust",
        author="New England Crust",
    )

    S = build_styles()
    story = []

    # ── PAGE 1: COVER ──────────────────────────────────────────────────
    def draw_cover_bg(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(DARK_BG)
        canvas.rect(0, 0, W, H, fill=1, stroke=0)
        # Terracotta top bar
        canvas.setFillColor(TERRACOTTA)
        canvas.rect(0, H - 10, W, 10, fill=1, stroke=0)
        # Amber bottom bar
        canvas.setFillColor(AMBER)
        canvas.rect(0, 0, W, 6, fill=1, stroke=0)
        canvas.restoreState()

    # Cover content — we build it as normal story items;
    # the dark background comes from page template (see onFirstPage)
    story.append(Spacer(1, 1.6 * inch))

    story.append(Paragraph("NEW ENGLAND CRUST", S["cover_brand"]))
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "Ninja Woodfire<br/>Quick-Start Guide",
        S["cover_title"]
    ))
    story.append(Spacer(1, 14))

    story.append(HRFlowable(
        width=60,
        thickness=2,
        color=TERRACOTTA,
        spaceAfter=14,
        spaceBefore=0,
        hAlign="CENTER",
    ))

    story.append(Paragraph(
        "The four accessories to buy first. Two pellet bags worth keeping stocked.<br/>"
        "Stone temperatures that actually work. Everything we learned so you don't have to.",
        S["cover_subtitle"]
    ))

    story.append(Spacer(1, 0.2 * inch))

    # ── Cover photo (renders if COVER_PHOTO_PATH is set) ──────────────
    if COVER_PHOTO_PATH:
        import os
        if os.path.exists(COVER_PHOTO_PATH):
            # Auto-correct EXIF orientation, crop, and insert
            from PIL import Image as PILImage, ExifTags
            import tempfile

            src = PILImage.open(COVER_PHOTO_PATH)
            try:
                exif = src._getexif()
                if exif:
                    for tag, val in exif.items():
                        if ExifTags.TAGS.get(tag) == 'Orientation':
                            if val == 3:
                                src = src.rotate(180, expand=True)
                            elif val == 6:
                                src = src.rotate(270, expand=True)
                            elif val == 8:
                                src = src.rotate(90, expand=True)
                            break
            except Exception:
                pass

            pw, ph = src.size
            cropped = src.crop((
                int(pw * 0.08), int(ph * 0.05),
                int(pw * 0.92), int(ph * 0.75),
            ))
            tmp = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
            cropped.save(tmp.name, 'JPEG', quality=92)

            # EXIF-corrected upright crop — ratio 0.900 (w/h)
            img = RLImage(tmp.name, width=2.7 * inch, height=3.0 * inch)
            img.hAlign = "CENTER"

            # Wrap in a single-cell table to add a terracotta border frame
            photo_table = Table([[img]], colWidths=[2.7 * inch])
            photo_table.setStyle(TableStyle([
                ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
                ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
                ("BOX",           (0, 0), (-1, -1), 2, TERRACOTTA),
                ("TOPPADDING",    (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("LEFTPADDING",   (0, 0), (-1, -1), 0),
                ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
            ]))
            photo_table.hAlign = "CENTER"
            story.append(photo_table)
            story.append(Spacer(1, 0.15 * inch))
        else:
            print(f"⚠️  Photo not found at: {COVER_PHOTO_PATH} — skipping image")
            story.append(Spacer(1, 0.5 * inch))
    else:
        story.append(Spacer(1, 0.5 * inch))

    # Decorative badge line
    story.append(Paragraph("· OO101 OWNER'S COMPANION ·", ParagraphStyle(
        "badge",
        fontName="Helvetica",
        fontSize=8,
        textColor=AMBER,
        alignment=TA_CENTER,
        letterSpacing=3,
    )))

    story.append(Spacer(1, 0.3 * inch))

    story.append(Paragraph(
        "newenglandcrust.com",
        ParagraphStyle("url", fontName="Helvetica", fontSize=8,
                       textColor=RULE_COLOR, alignment=TA_CENTER)
    ))

    # Force page break after cover
    from reportlab.platypus import PageBreak
    story.append(PageBreak())

    # ── PAGE 2: BUY THESE FIRST ────────────────────────────────────────
    story.append(Paragraph("SECTION ONE", S["section_label"]))
    story.append(Paragraph("Buy These Before You Fire It Up", S["section_heading"]))
    story.append(AccentRule(content_width))
    story.append(Spacer(1, 10))

    story.append(Paragraph(
        "The Ninja Woodfire ships with more than most people expect — a 12-inch pizza stone, "
        "Pro-Heat pan, roast rack, pellet scoop, and a starter pellet bag. You can cook on day one. "
        "What's missing are the four things almost every owner needs within the first two weeks.",
        S["body"]
    ))
    story.append(Spacer(1, 12))

    accessories = [
        (
            "1.  A Quality Cover",
            "Ninja XSKOCVR (official) or a third-party OO100-series cover",
            "The Woodfire is weather-resistant, not weatherproof. A New England winter will find "
            "the weak spots. The official cover fits perfectly. A well-reviewed third-party cover "
            "runs about half the price and holds up fine through rain and wind.",
            "~$25 — buy before the first cook"
        ),
        (
            "2.  A 12-Gauge Outdoor Extension Cord",
            "At least 15 ft. Look for 'outdoor rated' and 12 AWG on the label",
            "The oven's cord is 4.5 feet. Unless your outlet is exactly where you want to cook, "
            "you need an extension. The 12-gauge rating matters — the oven draws real wattage and "
            "a thin indoor cord can overheat. Don't grab whatever's in the garage.",
            "~$20 — non-negotiable"
        ),
        (
            "3.  A Perforated Pizza Peel",
            "Ninja XSKOPPL (fits the OO101 opening perfectly) or a 12-inch aluminum peel",
            "You can slide the first pizza onto a cold stone without one. The second pizza — onto "
            "a 700°F stone — is essentially impossible without a peel. The perforations let excess "
            "flour fall away instead of burning on the stone.",
            "~$20 — buy before pizza night #2"
        ),
        (
            "4.  An Infrared Thermometer",
            "Any food-safe model works — Etekcity is reliable and under $20",
            "The oven display shows air temperature. Stone surface temperature can run 100°F lower "
            "or higher. Stone temp is what determines crust. Point the thermometer at the stone — "
            "when it reads 650–750°F you're ready. Before we owned one, about 1 in 4 pizzas "
            "underwhelmed. After: every pizza, every time.",
            "~$18 — the single best upgrade for pizza quality"
        ),
    ]

    for name, product, detail, price in accessories:
        data = [
            [Paragraph(name, S["callout"]), Paragraph(price, S["table_accent"])],
            [Paragraph(product, S["callout_sub"]), ""],
            [Paragraph(detail, S["body"]), ""],
        ]
        t = Table(data, colWidths=[content_width * 0.72, content_width * 0.28])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), CARD_BG),
            ("ROWBACKGROUNDS", (0, 0), (-1, -1), [CARD_BG, CARD_BG, CARD_BG]),
            ("BOX", (0, 0), (-1, -1), 0.5, RULE_COLOR),
            ("LINEBEFORE", (0, 0), (0, -1), 3, TERRACOTTA),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("SPAN", (0, 1), (-1, 1)),
            ("SPAN", (0, 2), (-1, 2)),
        ]))
        story.append(KeepTogether([t, Spacer(1, 10)]))

    story.append(PageBreak())

    # ── PAGE 3: PELLETS + TEMPS ────────────────────────────────────────
    story.append(Paragraph("SECTION TWO", S["section_label"]))
    story.append(Paragraph("Pellets: What to Keep Stocked", S["section_heading"]))
    story.append(AccentRule(content_width))
    story.append(Spacer(1, 8))

    story.append(Paragraph(
        "The hopper holds roughly half a cup and lasts about an hour of active smoke. "
        "Pellets are for flavor, not fuel — the oven runs on electricity. You don't need "
        "them every cook, only when you want that wood-fired character.",
        S["body"]
    ))
    story.append(Spacer(1, 10))

    pellet_data = [
        [
            Paragraph("PELLET BAG", S["table_header"]),
            Paragraph("BEST FOR", S["table_header"]),
            Paragraph("NOTES", S["table_header"]),
        ],
        [
            Paragraph("Ninja All-Purpose Blend\n(cherry / maple / oak)", S["table_body"]),
            Paragraph("Pizza, chicken,\nvegetables, fish", S["table_body"]),
            Paragraph("Start here. Works on everything. Mild, slightly sweet.", S["table_body"]),
        ],
        [
            Paragraph("Ninja Robust Blend\n(hickory / cherry / maple / oak)", S["table_body"]),
            Paragraph("Pulled pork, ribs,\nbrisket, beef", S["table_body"]),
            Paragraph("Classic BBQ smoke. Strong but not overpowering.", S["table_body"]),
        ],
        [
            Paragraph("Kona Variety Pack\n(8 × 1 lb bags)", S["table_body"]),
            Paragraph("Experimenting with\nwood flavor profiles", S["table_body"]),
            Paragraph("Not official Ninja brand but works perfectly. Good way to find your favorites.", S["table_body"]),
        ],
        [
            Paragraph("Mesquite — wait on this", S["table_body"]),
            Paragraph("Red meat only", S["table_body"]),
            Paragraph("Polarizing flavor. Try a small bag before committing.", S["table_body"]),
        ],
    ]

    pellet_table = Table(
        pellet_data,
        colWidths=[content_width * 0.32, content_width * 0.28, content_width * 0.40]
    )
    pellet_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TERRACOTTA),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CARD_BG, DARK_BG, CARD_BG, DARK_BG]),
        ("TEXTCOLOR", (0, 0), (-1, 0), CREAM),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE_COLOR),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(pellet_table)
    story.append(Spacer(1, 8))

    # Storage tip
    tip_data = [[
        Paragraph("STORAGE TIP", S["tip_label"]),
        Paragraph(
            "Keep pellets in an airtight container away from moisture. "
            "Damp pellets smoke poorly and can clog the hopper.",
            S["tip_body"]
        )
    ]]
    tip_table = Table(tip_data, colWidths=[content_width * 0.18, content_width * 0.82])
    tip_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#1E2019")),
        ("LINEBEFORE", (0, 0), (0, -1), 3, AMBER),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(tip_table)

    # ── Section 3 always starts on its own page ────────────────────────
    story.append(PageBreak())

    # Temperature section
    story.append(Paragraph("SECTION THREE", S["section_label"]))
    story.append(Paragraph("Stone Temperatures That Actually Work", S["section_heading"]))
    story.append(AccentRule(content_width))
    story.append(Spacer(1, 8))

    story.append(Paragraph(
        "The display reads air temperature. Stone surface runs different — often 100°F lower "
        "during preheat, occasionally higher during a long cook. Use an infrared thermometer "
        "pointed at the stone, not the display, to know when you're actually ready.",
        S["body"]
    ))
    story.append(Spacer(1, 10))

    temp_data = [
        [
            Paragraph("COOK", S["table_header"]),
            Paragraph("TARGET STONE TEMP", S["table_header"]),
            Paragraph("PREHEAT TIME", S["table_header"]),
            Paragraph("NOTES", S["table_header"]),
        ],
        [
            Paragraph("Neapolitan-style pizza", S["table_body"]),
            Paragraph("700–750°F", S["table_accent"]),
            Paragraph("20–25 min", S["table_body"]),
            Paragraph("Cooks in 90–120 sec. Watch it — goes fast.", S["table_body"]),
        ],
        [
            Paragraph("NY-style / thicker crust", S["table_body"]),
            Paragraph("575–625°F", S["table_accent"]),
            Paragraph("18–22 min", S["table_body"]),
            Paragraph("More forgiving. Good for first-timers.", S["table_body"]),
        ],
        [
            Paragraph("Chicken thighs / drumsticks", S["table_body"]),
            Paragraph("375–425°F", S["table_accent"]),
            Paragraph("12–15 min", S["table_body"]),
            Paragraph("Use roast rack. Internal temp 165°F.", S["table_body"]),
        ],
        [
            Paragraph("Smoked pork shoulder", S["table_body"]),
            Paragraph("225–250°F", S["table_accent"]),
            Paragraph("10 min", S["table_body"]),
            Paragraph("Low & slow. Refill pellets every 45–60 min.", S["table_body"]),
        ],
        [
            Paragraph("Roasted vegetables", S["table_body"]),
            Paragraph("450–500°F", S["table_accent"]),
            Paragraph("15 min", S["table_body"]),
            Paragraph("Use Pro-Heat pan. High heat = good char.", S["table_body"]),
        ],
    ]

    temp_table = Table(
        temp_data,
        colWidths=[
            content_width * 0.28,
            content_width * 0.22,
            content_width * 0.18,
            content_width * 0.32,
        ]
    )
    temp_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TERRACOTTA),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CARD_BG, DARK_BG, CARD_BG, DARK_BG, CARD_BG]),
        ("TEXTCOLOR", (0, 0), (-1, 0), CREAM),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE_COLOR),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(temp_table)
    story.append(Spacer(1, 20))

    # ── PAGE 4: WHAT'S IN THE BOX + FOOTER ────────────────────────────
    story.append(PageBreak())

    story.append(Paragraph("SECTION FOUR", S["section_label"]))
    story.append(Paragraph("What Comes in the Box (So You Don't Rebuy It)", S["section_heading"]))
    story.append(AccentRule(content_width))
    story.append(Spacer(1, 8))

    story.append(Paragraph(
        "A lot of new owners spend money on things the OO101 already includes. "
        "Before you buy anything, confirm you already have these.",
        S["body"]
    ))
    story.append(Spacer(1, 10))

    inbox_items = [
        ("Ninja Woodfire Oven (OO101)", "The oven itself, obviously — but worth noting the model number for accessory compatibility."),
        ("12-inch Square Pizza Stone", "Fits the OO101 perfectly. Don't buy a replacement stone until this one cracks, which may never happen."),
        ("Pro-Heat Pan", "Multi-use — roasting, searing, baking. Handles most tasks you'd otherwise buy a cast iron tray for."),
        ("Roast Rack", "Elevates chicken, pork, and other meats over the Pro-Heat pan for even airflow."),
        ("Accessory Frame", "The internal frame that holds the pizza stone or Pro-Heat pan at the correct height."),
        ("Pellet Scoop", "A fine scoop. No reason to buy a second one — Ninja sells extras for $7-8 each. Skip it."),
        ("All-Purpose Blend Starter Pack", "One small bag. Enough for 2-3 cooks. Plan to restock."),
    ]

    for item, detail in inbox_items:
        data = [[
            Paragraph("✓", ParagraphStyle("check", fontName="Helvetica-Bold",
                                           fontSize=11, textColor=TERRACOTTA,
                                           alignment=TA_CENTER)),
            Paragraph(f"<b>{item}</b><br/>{detail}", ParagraphStyle(
                "inbox_item", fontName="Helvetica", fontSize=9,
                textColor=MUTED_CREAM, leading=14,
            ))
        ]]
        t = Table(data, colWidths=[20, content_width - 20])
        t.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ]))
        story.append(t)
        story.append(HRFlowable(
            width=content_width, thickness=0.4,
            color=RULE_COLOR, spaceAfter=4, spaceBefore=0
        ))

    story.append(Spacer(1, 28))

    # Closing callout
    closing_data = [[
        Paragraph(
            "The oven will surprise you. The crust will come faster than you expect, "
            "the smoke is subtler than you think, and by the third pizza night "
            "you'll have a system. We're at newenglandcrust.com whenever you need it.",
            ParagraphStyle(
                "closing", fontName="Helvetica-Oblique", fontSize=10,
                textColor=CREAM, leading=17, alignment=TA_CENTER,
            )
        )
    ]]
    closing_table = Table(closing_data, colWidths=[content_width])
    closing_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CARD_BG),
        ("LINEBEFORE", (0, 0), (0, -1), 3, TERRACOTTA),
        ("LINEAFTER", (0, 0), (-1, -1), 3, AMBER),
        ("TOPPADDING", (0, 0), (-1, -1), 16),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 16),
        ("LEFTPADDING", (0, 0), (-1, -1), 18),
        ("RIGHTPADDING", (0, 0), (-1, -1), 18),
    ]))
    story.append(closing_table)

    story.append(Spacer(1, 20))
    story.append(Paragraph(
        "© New England Crust · newenglandcrust.com · Salt Air & Crispy Crust",
        S["footer"]
    ))

    # ── PAGE TEMPLATES ─────────────────────────────────────────────────
    def on_first_page(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(DARK_BG)
        canvas.rect(0, 0, W, H, fill=1, stroke=0)
        canvas.setFillColor(TERRACOTTA)
        canvas.rect(0, H - 10, W, 10, fill=1, stroke=0)
        canvas.setFillColor(AMBER)
        canvas.rect(0, 0, W, 6, fill=1, stroke=0)
        canvas.restoreState()

    def on_later_pages(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(DARK_BG)
        canvas.rect(0, 0, W, H, fill=1, stroke=0)
        # Header rule
        canvas.setStrokeColor(RULE_COLOR)
        canvas.setLineWidth(0.5)
        canvas.line(inch, H - 0.45 * inch, W - inch, H - 0.45 * inch)
        # Header brand
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(MUTED_CREAM)
        canvas.drawString(inch, H - 0.38 * inch, "NEW ENGLAND CRUST")
        canvas.drawRightString(W - inch, H - 0.38 * inch, "Ninja Woodfire Quick-Start Guide")
        # Footer rule
        canvas.line(inch, 0.5 * inch, W - inch, 0.5 * inch)
        canvas.setFont("Helvetica", 7)
        canvas.setFillColor(RULE_COLOR)
        canvas.drawCentredString(W / 2, 0.35 * inch, f"newenglandcrust.com  ·  Page {doc.page}")
        # Accent bars
        canvas.setFillColor(TERRACOTTA)
        canvas.rect(0, H - 4, W, 4, fill=1, stroke=0)
        canvas.setFillColor(AMBER)
        canvas.rect(0, 0, W, 3, fill=1, stroke=0)
        canvas.restoreState()

    doc.build(story, onFirstPage=on_first_page, onLaterPages=on_later_pages)
    print(f"✅  PDF written to {OUTPUT_PATH}")


if __name__ == "__main__":
    build_pdf()
