from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)

# Colors
DARK_BG = HexColor("#1a1a2e")
ACCENT = HexColor("#e94560")
ACCENT_LIGHT = HexColor("#fce4ec")
BLUE = HexColor("#0a3d62")
BLUE_LIGHT = HexColor("#e3f2fd")
GREEN = HexColor("#27ae60")
GREEN_LIGHT = HexColor("#e8f5e9")
RED = HexColor("#c0392b")
RED_LIGHT = HexColor("#ffebee")
YELLOW = HexColor("#f39c12")
YELLOW_LIGHT = HexColor("#fff8e1")
GRAY = HexColor("#7f8c8d")
GRAY_LIGHT = HexColor("#f5f5f5")
DARK = HexColor("#2c3e50")
WHITE = white

OUTPUT = r"D:\rendi\Automations Rendimension\Hugo Brand Full Linkedin\CODE\campaign-assets\rendimension_MASTER_DECISION_REPORT_20260317.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=letter,
    topMargin=0.6*inch,
    bottomMargin=0.6*inch,
    leftMargin=0.7*inch,
    rightMargin=0.7*inch
)

styles = getSampleStyleSheet()

# Custom styles
styles.add(ParagraphStyle(
    'MainTitle', parent=styles['Title'],
    fontSize=22, textColor=DARK, spaceAfter=4, fontName='Helvetica-Bold'
))
styles.add(ParagraphStyle(
    'Subtitle', parent=styles['Normal'],
    fontSize=13, textColor=ACCENT, spaceAfter=2, fontName='Helvetica-Bold'
))
styles.add(ParagraphStyle(
    'MetaInfo', parent=styles['Normal'],
    fontSize=9, textColor=GRAY, spaceAfter=2
))
styles.add(ParagraphStyle(
    'SectionHead', parent=styles['Heading2'],
    fontSize=14, textColor=BLUE, spaceBefore=18, spaceAfter=8,
    fontName='Helvetica-Bold', borderWidth=0
))
styles.add(ParagraphStyle(
    'SubHead', parent=styles['Heading3'],
    fontSize=11, textColor=DARK, spaceBefore=10, spaceAfter=6,
    fontName='Helvetica-Bold'
))
styles.add(ParagraphStyle(
    'Body', parent=styles['Normal'],
    fontSize=9.5, textColor=DARK, spaceAfter=6, leading=13
))
styles.add(ParagraphStyle(
    'BodyBold', parent=styles['Normal'],
    fontSize=9.5, textColor=DARK, spaceAfter=6, leading=13, fontName='Helvetica-Bold'
))
styles.add(ParagraphStyle(
    'BulletItem', parent=styles['Normal'],
    fontSize=9.5, textColor=DARK, spaceAfter=4, leading=13,
    leftIndent=15, bulletIndent=5
))
styles.add(ParagraphStyle(
    'VerdictBox', parent=styles['Normal'],
    fontSize=10, textColor=DARK, spaceAfter=8, leading=14,
    backColor=BLUE_LIGHT, borderPadding=10
))
styles.add(ParagraphStyle(
    'TableCell', parent=styles['Normal'],
    fontSize=8, textColor=DARK, leading=10
))
styles.add(ParagraphStyle(
    'TableCellBold', parent=styles['Normal'],
    fontSize=8, textColor=DARK, leading=10, fontName='Helvetica-Bold'
))
styles.add(ParagraphStyle(
    'TableHeader', parent=styles['Normal'],
    fontSize=8, textColor=WHITE, leading=10, fontName='Helvetica-Bold'
))

story = []

def hr():
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1, color=HexColor("#ddd")))
    story.append(Spacer(1, 4))

def section(title):
    story.append(Paragraph(title, styles['SectionHead']))

def sub(title):
    story.append(Paragraph(title, styles['SubHead']))

def body(text):
    story.append(Paragraph(text, styles['Body']))

def bold(text):
    story.append(Paragraph(text, styles['BodyBold']))

def bullet(text):
    story.append(Paragraph(f"&bull; {text}", styles['BulletItem']))

def make_table(headers, rows, col_widths=None):
    """Create a styled table."""
    header_cells = [Paragraph(h, styles['TableHeader']) for h in headers]
    data = [header_cells]
    for row in rows:
        data.append([Paragraph(str(c), styles['TableCell']) for c in row])

    t = Table(data, colWidths=col_widths, repeatRows=1)
    style_cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#ccc")),
    ]
    # Alternate row colors
    for i in range(1, len(data)):
        if i % 2 == 0:
            style_cmds.append(('BACKGROUND', (0, i), (-1, i), GRAY_LIGHT))
    t.setStyle(TableStyle(style_cmds))
    story.append(t)
    story.append(Spacer(1, 8))

# ─── COVER / TITLE ───
story.append(Spacer(1, 30))
story.append(Paragraph("RENDIMENSION", styles['MainTitle']))
story.append(Paragraph("MASTER DECISION REPORT", styles['Subtitle']))
story.append(Paragraph("What to Advertise, Where the Money Is, and What to Avoid", styles['Body']))
story.append(Spacer(1, 8))
story.append(Paragraph("Date: 2026-03-17", styles['MetaInfo']))
story.append(Paragraph("For: Hugo Ramirez - Founder Decision Document", styles['MetaInfo']))
story.append(Paragraph("Sources: Market Intelligence Part 1 + Part 2 + Facebook Ad Library Live Scan (14 searches)", styles['MetaInfo']))

hr()

# ─── 30-SECOND VERDICT ───
section("THE 30-SECOND VERDICT")
story.append(Paragraph(
    "Don't advertise \"3D rendering.\" That market is dead -- flooded by $200 outsource shops and AI tools "
    "that dominate Facebook ads. Instead, advertise what renders <b>DO</b> for a business: close deals, get funding, "
    "accelerate approvals, prevent costly mistakes. The data confirms <b>3 blue ocean territories</b> with almost "
    "<b>ZERO advertising competition</b> and <b>$15K-$100K+ ticket sizes</b>.",
    styles['VerdictBox']
))

hr()

# ─── DECISION 1 ───
section("DECISION 1: Which Services to Lead With in Facebook Ads")

sub("LEAD WITH THESE (Top 3 Priorities)")
make_table(
    ["Priority", "Service Category", "Why", "Ad Competition", "Ticket"],
    [
        ["#1", "Pre-Construction Sales Visualization", "Lowest saturation, highest data support, largest target market", "~1 result (only The Render Pros)", "$10K-$50K+"],
        ["#2", "Experiential / Luxury Space Visualization", "ZERO competition. Hugo's Miami case = proof of concept", "0 results in Ad Library", "$15K-$100K+"],
        ["#3", "Investor-Grade Visual Packages", "Nobody bundles this. Developers currently hire 3 vendors", "0 results in Ad Library", "$15K-$75K+"],
    ],
    col_widths=[45, 120, 160, 100, 65]
)

sub("USE AS SUPPORTING (Not Lead)")
make_table(
    ["Service", "Role in Ads", "Why Not Lead"],
    [
        ["3D Animation / Walkthrough", "Include in package descriptions", "Medium saturation (~20 ads), Matterport commoditizing"],
        ["VR Immersive Experiences", "Feature within Priority #1 and #2", "Low awareness -- easier to sell as part of a package"],
        ["360 Virtual Tours", "Mention as deliverable", "CloudPano/Matterport own this space as SaaS"],
    ],
    col_widths=[130, 170, 190]
)

sub("DO NOT ADVERTISE THESE")
make_table(
    ["Service", "Reason"],
    [
        ["\"3D Rendering\" (generic)", "EXTREME saturation. AI tools (Archsynth: 350+ ads) dominate. Competing with $200 shops."],
        ["Interior Rendering", "Same problem. Commodity. Low ticket ($200-$2K)."],
        ["3D Floor Plans", "Free tools exist. Low ticket ($100-$500). Dead end."],
        ["Architectural Drafting", "Competing with AutoCAD freelancers. $500-$2K ticket isn't worth it."],
        ["Product Visualization", "Different market entirely. Not Rendimension's positioning."],
    ],
    col_widths=[130, 360]
)

hr()

# ─── DECISION 2 ───
section("DECISION 2: Who to Target")

sub("PRIMARY TARGET (80% of budget)")
bold("Real Estate Developers with $5M+ projects")
bullet("They need visualization to sell, fund, and approve projects")
bullet("They're making decisions worth millions")
bullet("They don't search for \"3D rendering\" -- they search for ways to de-risk investments")
bullet("Almost nobody is targeting them with visualization ads")

sub("SECONDARY TARGET (20% of budget)")
bold("Commercial Investors / Luxury Concept Developers")
bullet("Warehouse conversions, members clubs, luxury retail, hospitality")
bullet("Hugo's Miami exotic car club case = direct proof")
bullet("Zero advertising competition for this audience")
bullet("Highest ticket potential ($15K-$100K+)")

sub("DO NOT TARGET (waste of budget)")
make_table(
    ["Audience", "Why Not"],
    [
        ["\"Architects\" (broad)", "Everyone targets them. Lower ticket. They hire based on relationships, not ads."],
        ["Interior Designers", "Low budget segment. High competition."],
        ["Homeowners", "Wrong market. Low ticket. Not Rendimension's positioning."],
        ["Generic \"real estate\"", "Too broad. Realtors, agents, and flippers will eat your budget."],
    ],
    col_widths=[130, 360]
)

hr()

# ─── DECISION 3 ───
section("DECISION 3: How to Position (Message Territory)")

sub("What EVERY Competitor Says (AVOID ALL)")
make_table(
    ["Saturated Message", "Used By"],
    [
        ["\"Photorealistic 3D rendering\"", "80%+ of all archviz ads"],
        ["\"Bring your vision to life\"", "Most cliched line in the industry"],
        ["\"Fast turnaround\"", "Race to bottom -- AI tools claim \"30 seconds\" now"],
        ["\"Affordable/competitive pricing\"", "Can't out-cheap India or AI"],
        ["\"Stunning visualizations\"", "Every portfolio looks \"stunning\" -- zero differentiation"],
        ["\"See your project before it's built\"", "True but not compelling"],
    ],
    col_widths=[200, 290]
)

sub("What NOBODY is Saying (OWN THESE)")
make_table(
    ["Message Territory", "Competition", "Why It Works"],
    [
        ["\"We help you sell your project before you build it\"", "ZERO", "Frames renders as revenue tool, not art"],
        ["\"Your investors can't walk through a spreadsheet\"", "ZERO", "Speaks to the decision-maker's problem"],
        ["\"Stop paying twice for renders\" (anti-outsource)", "ZERO", "Targets burned buyers -- huge pain point"],
        ["\"Every day your project exists only on paper is a day you're not selling\"", "ZERO", "Creates urgency through consequence"],
        ["\"Before you invest $5M in your space, see what your guests will experience\"", "ZERO", "Perfect for experiential/luxury segment"],
    ],
    col_widths=[230, 70, 190]
)

hr()

# ─── DECISION 4 ───
section("DECISION 4: What Ad Formats to Use")

sub("What Competitors Run (and why to do differently)")
make_table(
    ["What They Do", "Why It Fails"],
    [
        ["90%+ single image (hero render)", "Looks like portfolio, not advertising. No story."],
        ["Occasional carousel (project showcase)", "Still portfolio-based. No pain point. No outcome."],
        ["Very rare video", "Walkthroughs without context. No human element."],
        ["Zero document ads", "Nobody is educating the market"],
    ],
    col_widths=[200, 290]
)

sub("What Rendimension Should Run")
make_table(
    ["Format", "Purpose", "Why"],
    [
        ["Video (15-30s)", "Show the DECISION moment, not the render", "Archsynth proves video + storytelling = longest-running ads"],
        ["Carousel", "\"5 mistakes developers make with cheap renders\"", "Nobody does educational content. Carousel = engagement."],
        ["Document Ad", "\"The ROI of Architectural Visualization\"", "Zero competition in document ads for archviz."],
        ["Single Image", "Human reaction shot -- boardroom, approval", "NOT the building. The MOMENT the viz changes a decision."],
    ],
    col_widths=[90, 200, 200]
)

hr()

# ─── DECISION 5 ───
section("DECISION 5: What the Data Proves Works")

sub("Facebook Ad Library -- What's Running and Surviving")
make_table(
    ["Advertiser", "Strategy", "Duration", "Why It's Working"],
    [
        ["Archsynth (350+ ads)", "Pain-point storytelling, text msg screenshots, emotional hooks", "Since Jun 2025 (10 months)", "Storytelling > portfolio"],
        ["The Render Pros", "\"$30M+ sellouts, 80% presale rates,\" real case studies", "Since Feb 2026", "Business outcomes > beautiful images"],
        ["CloudPano", "SaaS positioning, free trial, tool-focused", "Long-running", "Proves the 'tool' market is taken"],
    ],
    col_widths=[100, 170, 100, 120]
)

sub("What This Means for Rendimension")
bullet("<b>Storytelling beats portfolio.</b> Archsynth's 10-month run proves emotional, pain-point copy outperforms feature lists.")
bullet("<b>Business outcomes beat beautiful images.</b> The Render Pros is the ONLY studio using \"$30M sellouts\" language.")
bullet("<b>Premium studios don't advertise on Facebook.</b> Neoscape, DBOX, Steelblue -- NONE are in the Ad Library. The space is OPEN.")
bullet("<b>AI tools own the \"rendering\" keyword.</b> Don't compete with them -- compete on what AI CAN'T do: strategic visual storytelling.")

story.append(PageBreak())

# ─── FULL MATRIX ───
section("THE COMPLETE SERVICE x AD LIBRARY MATRIX")

make_table(
    ["Service", "Search Term", "Results", "Who's Advertising", "Studio Comp.", "Verdict"],
    [
        ["Architectural Viz", "\"architectural visualization\"", "~83", "AI tools (Archsynth, mnml.ai)", "ZERO studios", "AI owns keyword"],
        ["3D Rendering", "\"3D rendering services\"", "Many", "Hardware, MEP plans, garages", "Noise", "Keyword useless"],
        ["Pre-Construction", "\"pre-construction marketing viz\"", "~1", "Only The Render Pros", "ZERO others", "BLUE OCEAN"],
        ["Investor Presentations", "\"investor presentation RE rendering\"", "0", "Nobody", "ZERO", "COMPLETELY EMPTY"],
        ["Virtual Walkthroughs", "\"virtual walkthrough real estate\"", "~27", "Real estate agents", "Not studios", "Different industry"],
        ["Luxury Showroom Viz", "\"luxury showroom viz design\"", "~160", "Flooring/retail companies", "ZERO studios", "Retail keyword"],
        ["VR Real Estate", "\"VR real estate experience\"", "~30", "Real estate agents", "Not studios", "Agents, not creators"],
        ["3D Animation", "\"3D walkthrough animation arch.\"", "~20", "Westgate Koenig", "Nearly empty", "Low competition"],
        ["360 Virtual Tours", "\"360 virtual tour property\"", "~50+", "CloudPano (SaaS)", "Not studios", "Software owns this"],
        ["3D Floor Plans", "\"3D floor plan services\"", "~15", "RealSee AI, realtors", "Low-ticket", "Not worth it"],
        ["Product Viz", "\"product viz 3D rendering\"", "~40", "ReRender AI, courses", "Education", "Different market"],
        ["VR Training", "\"VR training simulation corp\"", "~170", "Sports VR (baseball)", "Wrong audience", "Not relevant"],
        ["Arch Drafting", "\"architectural drafting CAD\"", "~5", "HS 3D (India)", "Nearly empty", "Low ticket, skip"],
        ["Pre-Const. Sales", "\"sell property before construction\"", "~190", "News, remodelers", "ZERO studios", "Open territory"],
    ],
    col_widths=[75, 105, 40, 100, 75, 95]
)

hr()

# ─── FINAL RECOMMENDATION ───
section("FINAL STRATEGIC RECOMMENDATION")

sub("The Play: \"Visualization That Closes Deals\"")
body(
    "Rendimension should NOT advertise as a render studio. It should advertise as the partner that helps "
    "developers, investors, and luxury concept owners make confident multi-million dollar decisions through "
    "visual storytelling."
)

sub("Campaign Architecture (3 campaigns, phased)")

bold("Campaign 1: \"Pre-Sell Before You Build\" (Launch first) -- 50% budget")
bullet("Target: Real estate developers, $5M+ projects")
bullet("Message: Your project can generate revenue before construction starts")
bullet("Proof: Industry data (60% pre-sales, 47 fewer days in approvals, 25% faster funding)")
bullet("Format: Video + Carousel + Document Ad")

story.append(Spacer(1, 6))
bold("Campaign 2: \"See the Investment Before You Make It\" (Launch second) -- 30% budget")
bullet("Target: Commercial investors, luxury concept developers")
bullet("Message: Before you invest millions, walk through the experience")
bullet("Proof: Hugo's Miami case + experiential concept examples")
bullet("Format: Video + Single Image (human reaction shots)")

story.append(Spacer(1, 6))
bold("Campaign 3: \"Stop Paying Twice\" -- Anti-Outsource (Launch third) -- 20% budget")
bullet("Target: Developers who've been burned by cheap rendering")
bullet("Message: The $200 render cost you $20,000. Here's what happens when you invest right.")
bullet("Format: Carousel (comparison) + Document Ad (guide)")

hr()

# ─── NEXT STEPS ───
section("WHAT HAPPENS NEXT")

body("This report is Phase 1 (Intelligence). The pipeline continues:")
bullet("<b>Phase 2:</b> Positioning &amp; Angle Strategy -- segment-specific hooks, angles, emotional triggers")
bullet("<b>Phase 3:</b> Creative Direction -- cinematic visual concepts with AI image prompts")
bullet("<b>Phase 4:</b> Copy &amp; Creative Production -- ad copy variants + visual assets via Canva/21ST")
bullet("<b>Phase 5:</b> Campaign Build -- Meta Ads Manager setup with targeting, tracking, UTMs")

story.append(Spacer(1, 12))
bold("No ads are created until Phase 2 and 3 are complete.")

hr()
body("Sources: Facebook Ad Library live scan (14 search terms, March 17, 2026) | Competitor website analysis (11 companies) | Industry data from Bowen Studios, Transparent House, PropertyWire, ArchiCGI, DesignBlendz")

# BUILD
doc.build(story)
print(f"PDF created: {OUTPUT}")
