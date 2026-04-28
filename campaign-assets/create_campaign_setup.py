from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT

OUTPUT = r"D:\rendi\Automations Rendimension\Hugo Brand Full Linkedin\CODE\campaign-assets\rendimension_campaign_setup_20260318.pdf"

NAVY    = colors.HexColor("#0a1628")
BLUE    = colors.HexColor("#1e3a5f")
CYAN    = colors.HexColor("#00b4d8")
GOLD    = colors.HexColor("#f4a261")
GREEN   = colors.HexColor("#2ecc71")
RED     = colors.HexColor("#e74c3c")
YELLOW  = colors.HexColor("#f39c12")
WHITE   = colors.white
LGRAY   = colors.HexColor("#f5f5f5")
MGRAY   = colors.HexColor("#dddddd")

doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
    leftMargin=0.6*inch, rightMargin=0.6*inch,
    topMargin=0.6*inch, bottomMargin=0.6*inch)

styles = getSampleStyleSheet()

def S(name, **kw):
    return ParagraphStyle(name, **kw)

cover_title  = S("CT", fontSize=28, textColor=WHITE, alignment=TA_CENTER, fontName="Helvetica-Bold", leading=34)
cover_sub    = S("CS", fontSize=13, textColor=CYAN,  alignment=TA_CENTER, fontName="Helvetica", leading=18)
section      = S("SEC", fontSize=14, textColor=CYAN, fontName="Helvetica-Bold", leading=18, spaceBefore=14, spaceAfter=4)
subsection   = S("SUB", fontSize=11, textColor=NAVY, fontName="Helvetica-Bold", leading=14, spaceBefore=8, spaceAfter=2)
body         = S("BD", fontSize=9,  textColor=colors.HexColor("#222222"), fontName="Helvetica", leading=13)
body_white   = S("BW", fontSize=9,  textColor=WHITE, fontName="Helvetica", leading=13)
label        = S("LB", fontSize=8,  textColor=colors.HexColor("#555555"), fontName="Helvetica-Bold", leading=11)
code         = S("CD", fontSize=7.5, textColor=colors.HexColor("#1a1a2e"), fontName="Courier", leading=11, backColor=LGRAY, borderPadding=4)
check        = S("CK", fontSize=9,  textColor=colors.HexColor("#222222"), fontName="Helvetica", leading=14)
note         = S("NT", fontSize=8,  textColor=colors.HexColor("#555555"), fontName="Helvetica-Oblique", leading=11)

def hdr(text):
    return Paragraph(text, section)

def sub(text):
    return Paragraph(text, subsection)

def p(text):
    return Paragraph(text, body)

def sp(n=8):
    return Spacer(1, n)

def hr():
    return HRFlowable(width="100%", thickness=1, color=MGRAY, spaceAfter=6, spaceBefore=6)

def box_table(rows, col_widths, header_bg=NAVY, header_text=WHITE):
    data = []
    for i, row in enumerate(rows):
        data.append([Paragraph(str(c), S("t"+str(i)+str(j),
            fontSize=8, fontName="Helvetica-Bold" if i==0 else "Helvetica",
            textColor=header_text if i==0 else colors.HexColor("#222222"),
            leading=11)) for j, c in enumerate(row)])
    style = TableStyle([
        ("BACKGROUND", (0,0), (-1,0), header_bg),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LGRAY]),
        ("GRID", (0,0), (-1,-1), 0.4, MGRAY),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 7),
        ("RIGHTPADDING", (0,0), (-1,-1), 7),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ])
    return Table(data, colWidths=col_widths, style=style, hAlign="LEFT")

story = []

# ── COVER ──────────────────────────────────────────────────────────────────
cover = Table([[""]], colWidths=[7.3*inch], rowHeights=[1.1*inch])
cover.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1), NAVY), ("GRID",(0,0),(-1,-1),0,NAVY)]))
story.append(cover)
story.append(sp(2))
story.append(Paragraph("RENDIMENSION", cover_title))
story.append(Paragraph("Facebook & Instagram — Campaign Setup Guide", cover_sub))
story.append(Paragraph("Ready to Launch. Not Activated.", S("cs2", fontSize=10, textColor=GOLD, alignment=TA_CENTER, fontName="Helvetica-Oblique", leading=14)))
story.append(sp(4))
story.append(Paragraph("Budget: $9/day  |  Objective: Lead Generation  |  Market: United States (National)  |  Date: March 2026", S("cm", fontSize=8.5, textColor=colors.HexColor("#888888"), alignment=TA_CENTER, fontName="Helvetica", leading=12)))
story.append(sp(16))
story.append(hr())

# ── SECTION 1: CAMPAIGN ARCHITECTURE ───────────────────────────────────────
story.append(hdr("01  CAMPAIGN ARCHITECTURE"))
story.append(sp(4))
story.append(p("Structure: <b>1 Campaign → 1 Ad Set → 3 Ads (Phase 1)</b>. Budget optimization: ABO (Ad Set Budget Optimization). Reason: at $9/day CBO does not have enough budget to optimize across multiple ad sets. Keep all budget in one ad set to give the algorithm maximum signal."))
story.append(sp(8))

arch = [
    ["LEVEL", "NAME", "SETTING", "VALUE"],
    ["Campaign", "rendimension_meta_leadgen_developers_20260318", "Objective", "Lead Generation"],
    ["Campaign", "", "Budget Type", "ABO — Ad Set Level"],
    ["Campaign", "", "Special Category", "None"],
    ["Ad Set", "rendimension_meta_developers-us_video_v01", "Daily Budget", "$9.00 USD"],
    ["Ad Set", "", "Schedule", "Run continuously — no end date"],
    ["Ad Set", "", "Optimization Goal", "Leads"],
    ["Ad Set", "", "Attribution", "7-day click / 1-day view"],
    ["Ad Set", "", "Placements", "Advantage+ (let FB optimize)"],
    ["Ad", "rendimension_meta_competitor_video_A", "Format", "Single Video"],
    ["Ad", "rendimension_meta_sellbefore_video_A", "Format", "Single Video"],
    ["Ad", "rendimension_meta_riskit_video_A", "Format", "Single Video"],
]
story.append(box_table(arch, [0.7*inch, 2.7*inch, 1.5*inch, 2.1*inch]))
story.append(sp(6))
story.append(Paragraph("NOTE: Phase 1 launches with 3 videos (one per hook). After Day 7 analysis, the losing ad is paused and hook variants replace it.", note))
story.append(sp(12))

# ── SECTION 2: AUDIENCE TARGETING ─────────────────────────────────────────
story.append(hdr("02  AUDIENCE TARGETING"))
story.append(sp(4))

story.append(sub("Primary Audience — Developer Dave"))
story.append(sp(3))
target = [
    ["SETTING", "VALUE", "REASON"],
    ["Location", "United States — National", "Hugo's market is all US, not just Miami"],
    ["Age", "32 to 65", "Developers and VPs rarely under 32"],
    ["Gender", "All", "No restriction needed"],
    ["Language", "English", "Primary; Spanish variant added in Phase 3"],
    ["Detailed Targeting", "Real estate development", "Direct audience match"],
    ["", "Real estate investing", "Adjacent high-intent audience"],
    ["", "Commercial real estate", "Retail chains, shopping centers"],
    ["", "Property development", "Core developer identity"],
    ["", "Construction management", "Decision makers in build phase"],
    ["", "Luxury real estate", "Hospitality and high-end residential"],
    ["", "Houzz", "Architecture/design intent signal"],
    ["Exclude", "Residential homeowners", "Avoid B2C noise"],
    ["Audience Size Target", "500K to 2M", "Enough for $9/day to learn fast"],
    ["Detailed Targeting Expansion", "OFF", "Keep targeting tight at this budget"],
]
story.append(box_table(target, [1.4*inch, 2.5*inch, 3.1*inch]))
story.append(sp(8))

story.append(sub("Placement Settings"))
story.append(sp(3))
placements = [
    ["PLACEMENT", "FORMAT", "PRIORITY", "NOTE"],
    ["Instagram Feed", "9:16 vertical + 1:1 square", "HIGH", "Best for visual products like archviz"],
    ["Facebook Feed", "9:16 vertical + 1:1 square", "HIGH", "Widest reach for B2B developers"],
    ["Instagram Reels", "9:16 vertical video", "MEDIUM", "Cheapest CPM — good for video ads"],
    ["Facebook Reels", "9:16 vertical video", "MEDIUM", "Growing placement, low competition"],
    ["Stories", "9:16 vertical", "LOW", "Good for retargeting later"],
    ["Audience Network", "Any", "OFF", "Disable — low quality traffic"],
    ["Messenger", "Any", "OFF", "Not relevant for this audience"],
]
story.append(box_table(placements, [1.4*inch, 1.8*inch, 0.8*inch, 2.9*inch]))
story.append(sp(4))
story.append(Paragraph("RECOMMENDATION: Select 'Advantage+ Placements' and let Facebook optimize. At $9/day the algorithm needs flexibility to find the cheapest quality impressions.", note))

story.append(PageBreak())

# ── SECTION 3: ADS CONFIGURATION ──────────────────────────────────────────
story.append(hdr("03  ADS CONFIGURATION"))
story.append(sp(4))
story.append(p("Each ad uses the same ad set targeting. What changes between ads: the video creative, the hook, and the UTM content tag. Do NOT change the CTA or headline between ads in Phase 1 — we are testing hooks, not CTAs."))
story.append(sp(8))

ads = [
    ["AD NAME", "VIDEO FILE", "HOOK", "LAUNCH ORDER", "HEADLINE", "CTA BUTTON"],
    ["rendimension_meta_competitor_video_A", "Video 3 — Your Competitor", "Fear of loss", "FIRST (Week 1)", "See Your Project in 3D", "Get Quote"],
    ["rendimension_meta_sellbefore_video_A", "Video 1 — Sell Before You Build", "Opportunity", "SECOND (Week 3)", "See Your Project in 3D", "Get Quote"],
    ["rendimension_meta_riskit_video_A", "Video 2 — See It Before You Risk It", "Risk reduction", "THIRD (Week 5)", "See Your Project in 3D", "Get Quote"],
]
story.append(box_table(ads, [2.0*inch, 1.5*inch, 1.0*inch, 1.2*inch, 1.3*inch, 0.8*inch]))
story.append(sp(6))

story.append(sub("Ad Copy (Primary Text — same for all 3 ads in Phase 1)"))
story.append(sp(3))
story.append(Paragraph(
    "Developers using 3D visualization pre-sell 3X faster. At Rendimension, we create cinematic photorealistic 3D visualizations of your project before construction begins. Delivered in 5 business days. Click below to see your project in 3D.",
    S("adcopy", fontSize=9, textColor=colors.HexColor("#1a1a2e"), fontName="Helvetica", leading=13, backColor=LGRAY, borderPadding=6, borderColor=MGRAY, borderWidth=1)))
story.append(sp(4))
story.append(Paragraph("NOTE: The primary text is the same for all 3 ads so we isolate the video hook as the only variable being tested.", note))
story.append(sp(12))

# ── SECTION 4: UTM PARAMETERS ─────────────────────────────────────────────
story.append(hdr("04  UTM PARAMETERS"))
story.append(sp(4))
story.append(p("Apply these UTM parameters to the website URL field in each ad. If using Lead Gen Forms (recommended), add them to the form thank-you redirect URL instead."))
story.append(sp(8))

utms = [
    ["AD", "FULL UTM URL"],
    ["Video 3 — Competitor", "https://rendimension.com?utm_source=meta&utm_medium=paid-social&utm_campaign=rendimension_leadgen_developers&utm_content=competitor_video_A&utm_term=realestate-developers-us"],
    ["Video 1 — Sell Before", "https://rendimension.com?utm_source=meta&utm_medium=paid-social&utm_campaign=rendimension_leadgen_developers&utm_content=sellbefore_video_A&utm_term=realestate-developers-us"],
    ["Video 2 — Risk It", "https://rendimension.com?utm_source=meta&utm_medium=paid-social&utm_campaign=rendimension_leadgen_developers&utm_content=riskit_video_A&utm_term=realestate-developers-us"],
]
story.append(box_table(utms, [1.5*inch, 5.5*inch]))
story.append(sp(12))

# ── SECTION 5: LEAD GEN FORM ───────────────────────────────────────────────
story.append(hdr("05  LEAD GEN FORM — FACEBOOK NATIVE"))
story.append(sp(4))
story.append(p("Use Facebook's native Lead Gen Form (Instant Form) — NOT a link to your website. Native forms convert 3x to 5x better at low budgets because users never leave Facebook. The lead data goes directly to your Facebook Lead Center."))
story.append(sp(8))

story.append(sub("Form Configuration"))
story.append(sp(3))
form_config = [
    ["SETTING", "VALUE"],
    ["Form Type", "Higher Intent (not More Volume) — filters out low-quality leads"],
    ["Form Name", "rendimension_leadgen_developers_v01"],
    ["Language", "English"],
    ["Intro Headline", "See Your Project in 3D — Free Private Consultation"],
    ["Intro Image", "Use best render from your portfolio (photorealistic building exterior)"],
    ["Intro Description", "We create cinematic 3D visualizations for developers. See your project before you break ground. Delivered in 5 business days."],
]
story.append(box_table(form_config, [1.8*inch, 5.2*inch]))
story.append(sp(8))

story.append(sub("Questions — Exact Order and Wording"))
story.append(sp(3))
questions = [
    ["#", "QUESTION", "TYPE", "WHY THIS QUESTION"],
    ["Q1", "Full Name", "Auto-fill (FB prefills)", "Basic contact — no friction"],
    ["Q2", "Email Address", "Auto-fill (FB prefills)", "Primary contact channel"],
    ["Q3", "Phone Number", "Auto-fill (FB prefills)", "Follow-up call qualification"],
    ["Q4", "What type of project do you have?", "Multiple choice", "Qualify the lead by project type"],
    ["", "Options: Residential Development / Commercial / Hospitality / Retail / RV Resort / Other", "", ""],
    ["Q5", "What is the approximate project budget?", "Multiple choice", "Filter out non-serious leads"],
    ["", "Options: Under $500K / $500K to $2M / $2M to $10M / Over $10M", "", ""],
    ["Q6", "When do you need visualizations?", "Multiple choice", "Identifies urgency and readiness"],
    ["", "Options: Within 30 days / 1 to 3 months / 3 to 6 months / Just exploring", "", ""],
]
story.append(box_table(questions, [0.3*inch, 2.3*inch, 1.3*inch, 3.1*inch]))
story.append(sp(8))

story.append(sub("Completion Screen (After Submit)"))
story.append(sp(3))
completion = [
    ["FIELD", "TEXT"],
    ["Headline", "Thank you. We will be in touch within 24 hours."],
    ["Description", "A Rendimension consultant will contact you to discuss your project and send you a free visualization estimate."],
    ["Button Text", "Visit Our Website"],
    ["Button URL", "https://rendimension.com?utm_source=meta&utm_medium=paid-social&utm_campaign=rendimension_leadgen_developers&utm_content=form_thankyou"],
]
story.append(box_table(completion, [1.3*inch, 5.7*inch]))

story.append(PageBreak())

# ── SECTION 6: PHASE ROADMAP ───────────────────────────────────────────────
story.append(hdr("06  LAUNCH PHASES AND BUDGET PLAN"))
story.append(sp(4))

phases = [
    ["PHASE", "WEEKS", "BUDGET/DAY", "ADS RUNNING", "ACTION"],
    ["Phase 1 — Test Hooks", "1 to 2", "$9", "3 videos (one per hook)", "Hands off. Let algorithm learn. No changes."],
    ["Phase 2 — Optimize", "3 to 4", "$9", "Winner hook + 1 variant", "Pause loser. Launch hook variant of winner."],
    ["Phase 3 — Scale", "5 to 6", "$18 to $27", "2 winning hooks + Spanish version", "Increase budget 20% every 3 to 4 days."],
    ["Phase 4 — Expand", "7+", "$50+", "Add images + carousels", "Add static image ads. Test new audiences."],
]
story.append(box_table(phases, [1.1*inch, 0.7*inch, 0.9*inch, 1.9*inch, 2.5*inch]))
story.append(sp(6))
story.append(Paragraph("CRITICAL RULE: Do NOT touch the campaign during Days 1 to 3. Facebook needs time to exit the learning phase. Any change resets the algorithm and wastes budget.", S("warn", fontSize=9, textColor=RED, fontName="Helvetica-Bold", leading=13)))
story.append(sp(12))

# ── SECTION 7: LAUNCH CHECKLIST ───────────────────────────────────────────
story.append(hdr("07  PRE-LAUNCH CHECKLIST"))
story.append(sp(4))

checklist_data = [
    ["", "ITEM", "STATUS"],
    ["PIXEL", "Facebook Pixel installed on rendimension.com", "Verify in Events Manager"],
    ["PIXEL", "Lead event firing on form submission", "Test with Pixel Helper Chrome extension"],
    ["PIXEL", "PageView event firing on all pages", "Verify in Events Manager"],
    ["CREATIVE", "All 3 videos uploaded to Ads Manager", "Check duration and aspect ratio"],
    ["CREATIVE", "Videos are 9:16 vertical format", "Confirm before uploading"],
    ["CREATIVE", "Videos under 4GB file size", "Facebook limit"],
    ["CREATIVE", "No copyrighted music in videos", "HeyGen videos are safe"],
    ["FORM", "Lead Gen Form created and previewed on mobile", "Use Preview button in Ads Manager"],
    ["FORM", "Form type set to Higher Intent", "Avoids low-quality leads"],
    ["FORM", "Thank-you URL includes UTM parameters", "Check URL field in form builder"],
    ["COPY", "Primary text under 125 characters before cutoff", "First sentence is the hook"],
    ["COPY", "Headline: See Your Project in 3D", "40 characters max"],
    ["COPY", "CTA button: Get Quote", "Set in ad creation"],
    ["TARGETING", "Location set to United States", "Not just one state"],
    ["TARGETING", "Age range 32 to 65", "Confirm in ad set"],
    ["TARGETING", "Audience Network placement DISABLED", "Low quality traffic"],
    ["TARGETING", "Audience size between 500K and 2M", "Check estimate in ad set"],
    ["BUDGET", "Daily budget $9 set at AD SET level", "Not campaign level"],
    ["BUDGET", "No end date scheduled", "Run continuously"],
    ["NAMING", "Campaign name follows convention", "rendimension_meta_leadgen_developers_YYYYMMDD"],
    ["NAMING", "Ad names follow convention", "rendimension_meta_{hook}_video_A"],
    ["LAUNCH", "All ads set to PAUSED before review", "Never publish without final check"],
    ["LAUNCH", "Preview each ad on mobile view", "80% of traffic is mobile"],
    ["LAUNCH", "Screenshot campaign before activating", "For your records"],
]
checks = [["CHECK", "ITEM", "HOW TO VERIFY"]] + [[r[0], r[1], r[2]] for r in checklist_data[1:]]
story.append(box_table(checks, [0.7*inch, 3.8*inch, 2.5*inch]))
story.append(sp(12))

# ── SECTION 8: KPI TARGETS ─────────────────────────────────────────────────
story.append(hdr("08  KPI TARGETS AND TRAFFIC LIGHTS"))
story.append(sp(4))

kpis = [
    ["METRIC", "GREEN TARGET", "YELLOW MONITOR", "RED ACTION REQUIRED"],
    ["CTR (all)", "Above 2.0%", "1.0% to 2.0%", "Below 1.0% — pause ad"],
    ["CPC", "Below $1.50", "$1.50 to $3.00", "Above $3.00 — review creative"],
    ["CPL (Cost Per Lead)", "Below $80", "$80 to $120", "Above $150 — pause campaign"],
    ["Leads per week", "3 or more", "1 to 2", "Zero — immediate creative review"],
    ["Video Play Rate (3s)", "Above 30%", "15% to 30%", "Below 15% — hook failing"],
    ["Form Completion Rate", "Above 60%", "40% to 60%", "Below 40% — simplify form"],
    ["Frequency", "Below 2.0", "2.0 to 3.5", "Above 4.0 — refresh creative"],
]
kpi_table = [kpis[0]] + kpis[1:]
t = Table([[Paragraph(c, S("k"+str(i)+str(j),
    fontSize=8,
    fontName="Helvetica-Bold" if i==0 else "Helvetica",
    textColor=WHITE if i==0 else colors.HexColor("#222222"),
    leading=11)) for j,c in enumerate(row)] for i,row in enumerate(kpi_table)],
    colWidths=[1.4*inch, 1.3*inch, 1.5*inch, 2.0*inch])
t.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,0), NAVY),
    ("BACKGROUND",(1,1),(1,-1), colors.HexColor("#d5f5e3")),
    ("BACKGROUND",(2,1),(2,-1), colors.HexColor("#fef9e7")),
    ("BACKGROUND",(3,1),(3,-1), colors.HexColor("#fadbd8")),
    ("GRID",(0,0),(-1,-1),0.4, MGRAY),
    ("TOPPADDING",(0,0),(-1,-1),5),
    ("BOTTOMPADDING",(0,0),(-1,-1),5),
    ("LEFTPADDING",(0,0),(-1,-1),7),
    ("RIGHTPADDING",(0,0),(-1,-1),7),
    ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
]))
story.append(t)
story.append(sp(6))
story.append(Paragraph("Check these metrics every 7 days minimum. Do NOT check daily — early data is noisy and leads to bad decisions.", note))
story.append(sp(16))

# ── FOOTER ─────────────────────────────────────────────────────────────────
story.append(hr())
story.append(Paragraph("Rendimension Campaign Setup Guide  |  March 2026  |  Confidential", S("ft", fontSize=7.5, textColor=colors.HexColor("#aaaaaa"), alignment=TA_CENTER, fontName="Helvetica", leading=11)))

doc.build(story)
print("PDF generated:", OUTPUT)
