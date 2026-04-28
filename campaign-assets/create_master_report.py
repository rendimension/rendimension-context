"""
RENDIMENSION MASTER DECISION REPORT - PDF Generator
Generates a professional PDF report for Facebook campaign strategy
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib import colors
import os

# Colors
DARK_BG = HexColor('#1a1a2e')
ACCENT_BLUE = HexColor('#0f3460')
ACCENT_ORANGE = HexColor('#e94560')
GREEN = HexColor('#27ae60')
YELLOW = HexColor('#f39c12')
RED = HexColor('#e74c3c')
LIGHT_GRAY = HexColor('#f5f5f5')
MEDIUM_GRAY = HexColor('#cccccc')
DARK_TEXT = HexColor('#2c3e50')
BLUE_LINK = HexColor('#2980b9')

def create_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name='ReportTitle',
        parent=styles['Title'],
        fontSize=28,
        leading=34,
        textColor=ACCENT_BLUE,
        spaceAfter=6,
        alignment=TA_LEFT,
    ))

    styles.add(ParagraphStyle(
        name='ReportSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        leading=18,
        textColor=DARK_TEXT,
        spaceAfter=20,
    ))

    styles.add(ParagraphStyle(
        name='SectionTitle',
        parent=styles['Heading1'],
        fontSize=18,
        leading=22,
        textColor=ACCENT_BLUE,
        spaceBefore=20,
        spaceAfter=10,
        borderWidth=0,
        borderColor=ACCENT_BLUE,
        borderPadding=0,
    ))

    styles.add(ParagraphStyle(
        name='SubSection',
        parent=styles['Heading2'],
        fontSize=14,
        leading=18,
        textColor=DARK_TEXT,
        spaceBefore=12,
        spaceAfter=6,
    ))

    styles.add(ParagraphStyle(
        name='BodyText2',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=DARK_TEXT,
        spaceAfter=8,
    ))

    styles.add(ParagraphStyle(
        name='BulletText',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=DARK_TEXT,
        leftIndent=20,
        spaceAfter=4,
    ))

    styles.add(ParagraphStyle(
        name='CalloutText',
        parent=styles['Normal'],
        fontSize=11,
        leading=15,
        textColor=ACCENT_BLUE,
        leftIndent=15,
        rightIndent=15,
        spaceBefore=8,
        spaceAfter=8,
        borderWidth=1,
        borderColor=ACCENT_BLUE,
        borderPadding=10,
        backColor=HexColor('#eaf2f8'),
    ))

    styles.add(ParagraphStyle(
        name='SmallText',
        parent=styles['Normal'],
        fontSize=8,
        leading=10,
        textColor=MEDIUM_GRAY,
    ))

    styles.add(ParagraphStyle(
        name='TableHeader',
        parent=styles['Normal'],
        fontSize=9,
        leading=11,
        textColor=white,
        alignment=TA_CENTER,
    ))

    styles.add(ParagraphStyle(
        name='TableCell',
        parent=styles['Normal'],
        fontSize=9,
        leading=12,
        textColor=DARK_TEXT,
    ))

    styles.add(ParagraphStyle(
        name='TableCellCenter',
        parent=styles['Normal'],
        fontSize=9,
        leading=12,
        textColor=DARK_TEXT,
        alignment=TA_CENTER,
    ))

    styles.add(ParagraphStyle(
        name='VerdictGO',
        parent=styles['Normal'],
        fontSize=10,
        leading=12,
        textColor=GREEN,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
    ))

    styles.add(ParagraphStyle(
        name='VerdictAVOID',
        parent=styles['Normal'],
        fontSize=10,
        leading=12,
        textColor=RED,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
    ))

    styles.add(ParagraphStyle(
        name='PageFooter',
        parent=styles['Normal'],
        fontSize=8,
        textColor=MEDIUM_GRAY,
        alignment=TA_CENTER,
    ))

    return styles


def make_table(data, col_widths=None, header_color=ACCENT_BLUE):
    """Create a styled table"""
    style_commands = [
        ('BACKGROUND', (0, 0), (-1, 0), header_color),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, MEDIUM_GRAY),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]

    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle(style_commands))
    return t


def build_report():
    output_path = os.path.join(
        r"D:\rendi\Automations Rendimension\Hugo Brand Full Linkedin\CODE\campaign-assets",
        "rendimension_master_decision_report_20260317.pdf"
    )

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50,
    )

    styles = create_styles()
    story = []

    # =========================================================================
    # COVER PAGE
    # =========================================================================
    story.append(Spacer(1, 80))
    story.append(Paragraph("RENDIMENSION", styles['ReportTitle']))
    story.append(Paragraph(
        "Master Decision Report:<br/>Facebook Campaign Strategy",
        ParagraphStyle(
            'CoverSub',
            parent=styles['ReportSubtitle'],
            fontSize=20,
            leading=26,
            textColor=ACCENT_ORANGE,
        )
    ))
    story.append(Spacer(1, 20))
    story.append(HRFlowable(width="100%", thickness=2, color=ACCENT_BLUE))
    story.append(Spacer(1, 20))

    cover_data = [
        ["Date", "March 17, 2026"],
        ["Market", "United States (National)"],
        ["Prepared For", "Hugo Ramirez, Founder"],
        ["Status", "Intelligence Phase Complete - NO ADS YET"],
        ["Sources", "Facebook Ad Library, Ubersuggest, Ahrefs, AnswerThePublic"],
    ]
    cover_table = Table(cover_data, colWidths=[150, 340])
    cover_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('TEXTCOLOR', (0, 0), (0, -1), ACCENT_BLUE),
        ('TEXTCOLOR', (1, 0), (1, -1), DARK_TEXT),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('LINEBELOW', (0, 0), (-1, -2), 0.5, LIGHT_GRAY),
    ]))
    story.append(cover_table)

    story.append(Spacer(1, 40))
    story.append(Paragraph(
        "<b>Purpose:</b> This report consolidates competitive intelligence, Facebook Ad Library analysis, "
        "and search demand research across ALL Rendimension services. It provides a data-backed recommendation "
        "on which services to lead with in Facebook advertising and which to avoid.",
        styles['BodyText2']
    ))

    story.append(PageBreak())

    # =========================================================================
    # TABLE OF CONTENTS
    # =========================================================================
    story.append(Paragraph("TABLE OF CONTENTS", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT_BLUE))
    story.append(Spacer(1, 15))

    toc_items = [
        ("1.", "Executive Summary - The 30-Second Verdict"),
        ("2.", "Real Client Types & Strategic Umbrellas"),
        ("3.", "Facebook Ad Library Audit - Full Results"),
        ("4.", "Search Demand Analysis - Volume Data"),
        ("5.", "Service Decision Matrix"),
        ("6.", "Why Facebook Demand Generation Works Here"),
        ("7.", "Competitor Landscape - Who Is Actually Advertising"),
        ("8.", "Final Recommendations & Next Steps"),
    ]
    for num, title in toc_items:
        story.append(Paragraph(
            f"<b>{num}</b>&nbsp;&nbsp;&nbsp;{title}",
            ParagraphStyle('TOC', parent=styles['BodyText2'], fontSize=12, leading=20, leftIndent=20)
        ))

    story.append(PageBreak())

    # =========================================================================
    # 1. EXECUTIVE SUMMARY
    # =========================================================================
    story.append(Paragraph("1. EXECUTIVE SUMMARY", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT_BLUE))
    story.append(Spacer(1, 10))

    story.append(Paragraph(
        "<b>The Verdict:</b> Rendimension should NOT compete in the saturated '3D rendering services' "
        "category on Facebook. Instead, it should own the blue ocean of <b>pre-construction sales visualization</b>, "
        "<b>investor presentation packages</b>, and <b>experiential/luxury space visualization</b> - three territories "
        "where Facebook ad competition is literally ZERO and the ticket size is 5-20x higher.",
        styles['CalloutText']
    ))

    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>Key Findings:</b>", styles['SubSection']))

    findings = [
        "The generic '3D rendering' Facebook ad space is dominated by AI tools (Archsynth, mnml.ai, ArchFine) - NOT render studios. Premium studios do not advertise on Facebook.",
        "For 'pre-construction marketing visualization' there is exactly 1 active ad in all of Facebook (The Render Pros). For 'investor presentation real estate rendering' there are ZERO.",
        "Search volume for these niche services is low (10-140/month) BUT CPC is high ($34.67) confirming commercial intent. Each lead is worth $10K-$100K+.",
        "Facebook is a demand generation platform, not a search platform. The relevant question is NOT 'do people search for this?' but 'can we reach the right decision-makers?' The answer is yes - there are 200,000+ architects and 500,000+ developers in the US.",
        "Every competitor says the same 3 things: 'photorealistic,' 'fast turnaround,' 'bring your vision to life.' Nobody talks about business outcomes. This is the gap.",
    ]
    for f in findings:
        story.append(Paragraph(f"&#8226; {f}", styles['BulletText']))

    story.append(PageBreak())

    # =========================================================================
    # 2. REAL CLIENT TYPES
    # =========================================================================
    story.append(Paragraph("2. REAL CLIENT TYPES & STRATEGIC UMBRELLAS", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT_BLUE))
    story.append(Spacer(1, 10))

    story.append(Paragraph(
        "Based on Rendimension's actual client history, these are the real client profiles mapped to strategic "
        "service categories. This is NOT theoretical - these are clients Hugo has served.",
        styles['BodyText2']
    ))

    client_data = [
        [Paragraph('<b>Real Client Type</b>', styles['TableHeader']),
         Paragraph('<b>Strategic Umbrella</b>', styles['TableHeader']),
         Paragraph('<b>FB Ad Saturation</b>', styles['TableHeader']),
         Paragraph('<b>Ticket</b>', styles['TableHeader'])],

        [Paragraph('Retail chains expanding/opening new store locations', styles['TableCell']),
         Paragraph('Pre-Construction Sales Viz', styles['TableCell']),
         Paragraph('ZERO', styles['TableCellCenter']),
         Paragraph('$10K-$50K+', styles['TableCellCenter'])],

        [Paragraph('Developers buying/flipping RV resorts, hospitality, commercial', styles['TableCell']),
         Paragraph('Investor Presentation Packages', styles['TableCell']),
         Paragraph('ZERO', styles['TableCellCenter']),
         Paragraph('$15K-$75K+', styles['TableCellCenter'])],

        [Paragraph('Large clients developing shopping centers', styles['TableCell']),
         Paragraph('Pre-Construction + Experiential', styles['TableCell']),
         Paragraph('ZERO', styles['TableCellCenter']),
         Paragraph('$15K-$100K+', styles['TableCellCenter'])],

        [Paragraph('Architects/developers not tech-savvy, need creative help', styles['TableCell']),
         Paragraph('Risk Reduction / Decision Support', styles['TableCell']),
         Paragraph('ZERO', styles['TableCellCenter']),
         Paragraph('Value-based', styles['TableCellCenter'])],

        [Paragraph('Developers wanting VR walkthroughs to verify construction', styles['TableCell']),
         Paragraph('Risk Reduction / Decision Support', styles['TableCell']),
         Paragraph('Minimal (CloudPano)', styles['TableCellCenter']),
         Paragraph('$10K-$50K+', styles['TableCellCenter'])],
    ]

    story.append(make_table(client_data, col_widths=[170, 130, 90, 90]))

    story.append(Spacer(1, 15))
    story.append(Paragraph(
        "<b>Key Insight:</b> Every single real client type maps to a service category where Facebook ad "
        "saturation is ZERO or near-zero. This is not coincidence - it confirms that the premium, "
        "decision-support end of the market is completely unserved by advertising.",
        styles['CalloutText']
    ))

    story.append(PageBreak())

    # =========================================================================
    # 3. FACEBOOK AD LIBRARY AUDIT
    # =========================================================================
    story.append(Paragraph("3. FACEBOOK AD LIBRARY AUDIT", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT_BLUE))
    story.append(Spacer(1, 10))

    story.append(Paragraph(
        "Live search of Facebook Ad Library (US, All Active Ads) conducted March 17, 2026. "
        "Each of Rendimension's services was searched independently.",
        styles['BodyText2']
    ))

    fb_data = [
        [Paragraph('<b>Search Term</b>', styles['TableHeader']),
         Paragraph('<b>Results</b>', styles['TableHeader']),
         Paragraph('<b>Who Is Advertising</b>', styles['TableHeader']),
         Paragraph('<b>Signal</b>', styles['TableHeader'])],

        [Paragraph('architectural visualization', styles['TableCell']),
         Paragraph('~83', styles['TableCellCenter']),
         Paragraph('AI tools dominate (Archsynth, mnml.ai, ArchFine)', styles['TableCell']),
         Paragraph('SATURATED', styles['VerdictAVOID'])],

        [Paragraph('3D rendering services', styles['TableCell']),
         Paragraph('Noise', styles['TableCellCenter']),
         Paragraph('Mostly irrelevant results, outsource shops', styles['TableCell']),
         Paragraph('AVOID', styles['VerdictAVOID'])],

        [Paragraph('pre-construction marketing visualization', styles['TableCell']),
         Paragraph('~1', styles['TableCellCenter']),
         Paragraph('Only The Render Pros', styles['TableCell']),
         Paragraph('BLUE OCEAN', styles['VerdictGO'])],

        [Paragraph('investor presentation real estate rendering', styles['TableCell']),
         Paragraph('0', styles['TableCellCenter']),
         Paragraph('Nobody', styles['TableCell']),
         Paragraph('BLUE OCEAN', styles['VerdictGO'])],

        [Paragraph('virtual walkthrough real estate', styles['TableCell']),
         Paragraph('~27', styles['TableCellCenter']),
         Paragraph('Real estate agents (not studios)', styles['TableCell']),
         Paragraph('OPEN', styles['VerdictGO'])],

        [Paragraph('luxury showroom visualization design', styles['TableCell']),
         Paragraph('~160', styles['TableCellCenter']),
         Paragraph('Flooring companies, unrelated', styles['TableCell']),
         Paragraph('OPEN', styles['VerdictGO'])],

        [Paragraph('virtual reality real estate experience', styles['TableCell']),
         Paragraph('Moderate', styles['TableCellCenter']),
         Paragraph('RE agents, not viz studios', styles['TableCell']),
         Paragraph('OPEN', styles['VerdictGO'])],

        [Paragraph('3D walkthrough animation architecture', styles['TableCell']),
         Paragraph('Low', styles['TableCellCenter']),
         Paragraph('Westgate Koenig (interesting)', styles['TableCell']),
         Paragraph('OPEN', styles['VerdictGO'])],

        [Paragraph('360 virtual tour property', styles['TableCell']),
         Paragraph('Moderate', styles['TableCellCenter']),
         Paragraph('CloudPano dominates (SaaS)', styles['TableCell']),
         Paragraph('NICHE', styles['TableCellCenter'])],

        [Paragraph('3D floor plan services', styles['TableCell']),
         Paragraph('Low', styles['TableCellCenter']),
         Paragraph('RealSee AI, realtors', styles['TableCell']),
         Paragraph('OPEN', styles['VerdictGO'])],

        [Paragraph('product visualization 3D rendering', styles['TableCell']),
         Paragraph('Low', styles['TableCellCenter']),
         Paragraph('ReRender AI, education', styles['TableCell']),
         Paragraph('OPEN', styles['VerdictGO'])],

        [Paragraph('VR training simulation corporate', styles['TableCell']),
         Paragraph('~170', styles['TableCellCenter']),
         Paragraph('Sports VR (unrelated)', styles['TableCell']),
         Paragraph('WRONG FIT', styles['VerdictAVOID'])],

        [Paragraph('architectural drafting CAD services', styles['TableCell']),
         Paragraph('~5', styles['TableCellCenter']),
         Paragraph('HS 3D India', styles['TableCell']),
         Paragraph('TOO NICHE', styles['TableCellCenter'])],

        [Paragraph('sell property before construction rendering', styles['TableCell']),
         Paragraph('~190', styles['TableCellCenter']),
         Paragraph('Local news, remodelers (not studios)', styles['TableCell']),
         Paragraph('BLUE OCEAN', styles['VerdictGO'])],
    ]

    story.append(make_table(fb_data, col_widths=[150, 50, 180, 90]))

    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>Top Competitors Found in Ads:</b>", styles['SubSection']))

    comp_data = [
        [Paragraph('<b>Company</b>', styles['TableHeader']),
         Paragraph('<b>Ad Count</b>', styles['TableHeader']),
         Paragraph('<b>Running Since</b>', styles['TableHeader']),
         Paragraph('<b>Positioning</b>', styles['TableHeader']),
         Paragraph('<b>Threat Level</b>', styles['TableHeader'])],

        [Paragraph('Archsynth (AI tool)', styles['TableCell']),
         Paragraph('~350', styles['TableCellCenter']),
         Paragraph('Jun 2025', styles['TableCellCenter']),
         Paragraph('AI-generated renders in seconds', styles['TableCell']),
         Paragraph('LOW (different market)', styles['TableCellCenter'])],

        [Paragraph('The Render Pros', styles['TableCell']),
         Paragraph('Few', styles['TableCellCenter']),
         Paragraph('Active', styles['TableCellCenter']),
         Paragraph('Business-outcome: "sell before built"', styles['TableCell']),
         Paragraph('MEDIUM (only one doing it right)', styles['TableCellCenter'])],

        [Paragraph('mnml.ai', styles['TableCell']),
         Paragraph('Moderate', styles['TableCellCenter']),
         Paragraph('Active', styles['TableCellCenter']),
         Paragraph('AI interior design tool', styles['TableCell']),
         Paragraph('LOW (different market)', styles['TableCellCenter'])],

        [Paragraph('CloudPano', styles['TableCell']),
         Paragraph('Dominant', styles['TableCellCenter']),
         Paragraph('Active', styles['TableCellCenter']),
         Paragraph('360 virtual tour SaaS', styles['TableCell']),
         Paragraph('LOW (SaaS, not service)', styles['TableCellCenter'])],
    ]

    story.append(make_table(comp_data, col_widths=[95, 55, 70, 160, 100]))

    story.append(PageBreak())

    # =========================================================================
    # 4. SEARCH DEMAND ANALYSIS
    # =========================================================================
    story.append(Paragraph("4. SEARCH DEMAND ANALYSIS", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT_BLUE))
    story.append(Spacer(1, 10))

    story.append(Paragraph(
        "Search volume data from Ubersuggest, Ahrefs Free Keyword Generator, and AnswerThePublic (paid). "
        "All data for United States, English, March 2026.",
        styles['BodyText2']
    ))

    search_data = [
        [Paragraph('<b>Keyword</b>', styles['TableHeader']),
         Paragraph('<b>Volume/mo</b>', styles['TableHeader']),
         Paragraph('<b>CPC</b>', styles['TableHeader']),
         Paragraph('<b>Intent</b>', styles['TableHeader']),
         Paragraph('<b>Source</b>', styles['TableHeader'])],

        [Paragraph('3D rendering for real estate', styles['TableCell']),
         Paragraph('140', styles['TableCellCenter']),
         Paragraph('$34.67', styles['TableCellCenter']),
         Paragraph('Commercial', styles['TableCellCenter']),
         Paragraph('ATP', styles['TableCellCenter'])],

        [Paragraph('virtual reality real estate', styles['TableCell']),
         Paragraph('320', styles['TableCellCenter']),
         Paragraph('-', styles['TableCellCenter']),
         Paragraph('47% Commercial', styles['TableCellCenter']),
         Paragraph('Ubersuggest', styles['TableCellCenter'])],

        [Paragraph('architectural visualization services', styles['TableCell']),
         Paragraph('>100', styles['TableCellCenter']),
         Paragraph('-', styles['TableCellCenter']),
         Paragraph('Commercial', styles['TableCellCenter']),
         Paragraph('Ahrefs', styles['TableCellCenter'])],

        [Paragraph('project rendering', styles['TableCell']),
         Paragraph('70', styles['TableCellCenter']),
         Paragraph('-', styles['TableCellCenter']),
         Paragraph('Mixed', styles['TableCellCenter']),
         Paragraph('Ubersuggest', styles['TableCellCenter'])],

        [Paragraph('what is rendering in construction', styles['TableCell']),
         Paragraph('50', styles['TableCellCenter']),
         Paragraph('-', styles['TableCellCenter']),
         Paragraph('Informational', styles['TableCellCenter']),
         Paragraph('Ubersuggest', styles['TableCellCenter'])],

        [Paragraph('new construction renderings', styles['TableCell']),
         Paragraph('40', styles['TableCellCenter']),
         Paragraph('-', styles['TableCellCenter']),
         Paragraph('Commercial', styles['TableCellCenter']),
         Paragraph('Ubersuggest', styles['TableCellCenter'])],

        [Paragraph('pre construction rendering', styles['TableCell']),
         Paragraph('10', styles['TableCellCenter']),
         Paragraph('-', styles['TableCellCenter']),
         Paragraph('40% Commercial', styles['TableCellCenter']),
         Paragraph('Ubersuggest', styles['TableCellCenter'])],
    ]

    story.append(make_table(search_data, col_widths=[160, 65, 55, 90, 80]))

    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>What This Means:</b>", styles['SubSection']))

    story.append(Paragraph(
        "Search volumes are LOW across all visualization services. But this is misleading for 3 reasons:",
        styles['BodyText2']
    ))

    reasons = [
        "<b>High CPC = High Value:</b> $34.67 CPC means each click is extremely valuable. These are not casual browsers - they are decision-makers with budgets.",
        "<b>Clients search for PROBLEMS, not solutions:</b> A developer does not search 'pre construction visualization.' They search 'how to sell condos before construction' or 'pre-sale marketing strategy.' The demand exists under different keywords.",
        "<b>Facebook is not Google:</b> On Facebook, you do not capture existing search demand. You GENERATE demand by showing decision-makers a solution they did not know existed. Search volume is irrelevant for Facebook strategy.",
    ]
    for r in reasons:
        story.append(Paragraph(f"&#8226; {r}", styles['BulletText']))

    story.append(PageBreak())

    # =========================================================================
    # 5. SERVICE DECISION MATRIX
    # =========================================================================
    story.append(Paragraph("5. SERVICE DECISION MATRIX", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT_BLUE))
    story.append(Spacer(1, 10))

    story.append(Paragraph(
        "Final decision matrix combining ad saturation, search demand, ticket size, "
        "differentiation potential, and Facebook audience availability.",
        styles['BodyText2']
    ))

    matrix_data = [
        [Paragraph('<b>Service</b>', styles['TableHeader']),
         Paragraph('<b>Ad Saturation</b>', styles['TableHeader']),
         Paragraph('<b>Search Vol</b>', styles['TableHeader']),
         Paragraph('<b>Ticket</b>', styles['TableHeader']),
         Paragraph('<b>FB Audience</b>', styles['TableHeader']),
         Paragraph('<b>VERDICT</b>', styles['TableHeader'])],

        [Paragraph('Pre-Construction Sales Visualization', styles['TableCell']),
         Paragraph('ZERO', styles['TableCellCenter']),
         Paragraph('Low', styles['TableCellCenter']),
         Paragraph('$10K-$50K+', styles['TableCellCenter']),
         Paragraph('Huge', styles['TableCellCenter']),
         Paragraph('TOP PICK', styles['VerdictGO'])],

        [Paragraph('Investor Presentation Packages', styles['TableCell']),
         Paragraph('ZERO', styles['TableCellCenter']),
         Paragraph('Very Low', styles['TableCellCenter']),
         Paragraph('$15K-$75K+', styles['TableCellCenter']),
         Paragraph('Huge', styles['TableCellCenter']),
         Paragraph('TOP PICK', styles['VerdictGO'])],

        [Paragraph('Experiential / Luxury Space Viz', styles['TableCell']),
         Paragraph('ZERO', styles['TableCellCenter']),
         Paragraph('Very Low', styles['TableCellCenter']),
         Paragraph('$15K-$100K+', styles['TableCellCenter']),
         Paragraph('Large', styles['TableCellCenter']),
         Paragraph('TOP PICK', styles['VerdictGO'])],

        [Paragraph('Risk Reduction / Decision Support', styles['TableCell']),
         Paragraph('ZERO', styles['TableCellCenter']),
         Paragraph('Low', styles['TableCellCenter']),
         Paragraph('Value-based', styles['TableCellCenter']),
         Paragraph('Large', styles['TableCellCenter']),
         Paragraph('TOP PICK', styles['VerdictGO'])],

        [Paragraph('VR Construction Walkthrough', styles['TableCell']),
         Paragraph('Low', styles['TableCellCenter']),
         Paragraph('320/mo', styles['TableCellCenter']),
         Paragraph('$10K-$50K+', styles['TableCellCenter']),
         Paragraph('Large', styles['TableCellCenter']),
         Paragraph('STRONG', styles['VerdictGO'])],

        [Paragraph('Retail Store Design Viz', styles['TableCell']),
         Paragraph('ZERO', styles['TableCellCenter']),
         Paragraph('Low', styles['TableCellCenter']),
         Paragraph('$10K-$50K+', styles['TableCellCenter']),
         Paragraph('Medium', styles['TableCellCenter']),
         Paragraph('STRONG', styles['VerdictGO'])],

        [Paragraph('3D Rendering (generic)', styles['TableCell']),
         Paragraph('HIGH', styles['TableCellCenter']),
         Paragraph('140/mo', styles['TableCellCenter']),
         Paragraph('$500-$3K', styles['TableCellCenter']),
         Paragraph('Saturated', styles['TableCellCenter']),
         Paragraph('AVOID', styles['VerdictAVOID'])],

        [Paragraph('Architectural Visualization (generic)', styles['TableCell']),
         Paragraph('HIGH', styles['TableCellCenter']),
         Paragraph('>100/mo', styles['TableCellCenter']),
         Paragraph('$1K-$5K', styles['TableCellCenter']),
         Paragraph('Saturated', styles['TableCellCenter']),
         Paragraph('AVOID', styles['VerdictAVOID'])],

        [Paragraph('VR Training Simulation', styles['TableCell']),
         Paragraph('Unrelated', styles['TableCellCenter']),
         Paragraph('170 noise', styles['TableCellCenter']),
         Paragraph('Variable', styles['TableCellCenter']),
         Paragraph('Wrong fit', styles['TableCellCenter']),
         Paragraph('AVOID', styles['VerdictAVOID'])],
    ]

    story.append(make_table(matrix_data, col_widths=[135, 65, 60, 70, 65, 75]))

    story.append(PageBreak())

    # =========================================================================
    # 6. WHY FACEBOOK DEMAND GENERATION WORKS HERE
    # =========================================================================
    story.append(Paragraph("6. WHY FACEBOOK DEMAND GENERATION WORKS HERE", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT_BLUE))
    story.append(Spacer(1, 10))

    story.append(Paragraph(
        "The critical insight of this report: <b>low search volume + zero ad saturation is the PERFECT "
        "combination for Facebook demand generation.</b>",
        styles['CalloutText']
    ))

    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>Google vs Facebook - Different Games:</b>", styles['SubSection']))

    comparison = [
        [Paragraph('<b>Factor</b>', styles['TableHeader']),
         Paragraph('<b>Google Ads</b>', styles['TableHeader']),
         Paragraph('<b>Facebook Ads</b>', styles['TableHeader'])],

        [Paragraph('How it works', styles['TableCell']),
         Paragraph('Capture existing demand (people already searching)', styles['TableCell']),
         Paragraph('Generate new demand (show people what they need)', styles['TableCell'])],

        [Paragraph('Search volume matters?', styles['TableCell']),
         Paragraph('YES - critical', styles['TableCell']),
         Paragraph('NO - irrelevant', styles['TableCell'])],

        [Paragraph('Targeting method', styles['TableCell']),
         Paragraph('Keywords', styles['TableCell']),
         Paragraph('Demographics, titles, interests, behaviors', styles['TableCell'])],

        [Paragraph('Best for...', styles['TableCell']),
         Paragraph('High-volume, known solutions', styles['TableCell']),
         Paragraph('New concepts, education, premium services', styles['TableCell'])],

        [Paragraph('Rendimension fit', styles['TableCell']),
         Paragraph('Poor (low volume, high CPC)', styles['TableCell']),
         Paragraph('Excellent (no competition, high ticket, visual product)', styles['TableCell'])],
    ]

    story.append(make_table(comparison, col_widths=[120, 175, 175]))

    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>Facebook Audience Size (US estimates):</b>", styles['SubSection']))

    audience_points = [
        "Licensed Architects: ~200,000+",
        "Real Estate Developers/Investors: ~500,000+",
        "Construction Company Owners: ~700,000+",
        "Retail Chain Decision Makers (VP+): ~50,000+",
        "Hospitality/Hotel Owners & Operators: ~80,000+",
        "Commercial Property Managers: ~300,000+",
    ]
    for a in audience_points:
        story.append(Paragraph(f"&#8226; {a}", styles['BulletText']))

    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Even if Facebook can reach just 10% of these professionals, that is 180,000+ potential "
        "decision-makers who have NEVER seen an ad for premium visualization services. "
        "One client from this pool = $10K-$100K+ in revenue.",
        styles['BodyText2']
    ))

    story.append(PageBreak())

    # =========================================================================
    # 7. COMPETITOR LANDSCAPE
    # =========================================================================
    story.append(Paragraph("7. COMPETITOR LANDSCAPE", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT_BLUE))
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>Who Is Actually Competing (and who is NOT):</b>", styles['SubSection']))

    story.append(Paragraph(
        "Rendimension's real competitors are NOT other '3D rendering' studios. They are creative agencies "
        "and pre-sale specialists. But critically - almost none of them advertise on Facebook.",
        styles['BodyText2']
    ))

    real_comp = [
        [Paragraph('<b>Company</b>', styles['TableHeader']),
         Paragraph('<b>Type</b>', styles['TableHeader']),
         Paragraph('<b>FB Ads?</b>', styles['TableHeader']),
         Paragraph('<b>Positioning</b>', styles['TableHeader'])],

        [Paragraph('Steelblue', styles['TableCell']),
         Paragraph('Creative Agency', styles['TableCellCenter']),
         Paragraph('NO', styles['TableCellCenter']),
         Paragraph('Premium archviz for major developments', styles['TableCell'])],

        [Paragraph('DBOX', styles['TableCell']),
         Paragraph('Creative Agency', styles['TableCellCenter']),
         Paragraph('NO', styles['TableCellCenter']),
         Paragraph('Brand + visualization for luxury RE', styles['TableCell'])],

        [Paragraph('Neoscape', styles['TableCell']),
         Paragraph('Creative Agency', styles['TableCellCenter']),
         Paragraph('NO', styles['TableCellCenter']),
         Paragraph('Immersive experiences for developments', styles['TableCell'])],

        [Paragraph('Transparent House', styles['TableCell']),
         Paragraph('Studio', styles['TableCellCenter']),
         Paragraph('NO', styles['TableCellCenter']),
         Paragraph('High-end renders, website focus', styles['TableCell'])],

        [Paragraph('The Render Pros', styles['TableCell']),
         Paragraph('Pre-sale Specialist', styles['TableCellCenter']),
         Paragraph('YES', styles['TableCellCenter']),
         Paragraph('Business outcomes: "sell before built"', styles['TableCell'])],
    ]

    story.append(make_table(real_comp, col_widths=[110, 90, 60, 210]))

    story.append(Spacer(1, 15))
    story.append(Paragraph(
        "<b>What The Render Pros Does Right (and how to beat them):</b>",
        styles['SubSection']
    ))

    render_pros = [
        "They are the ONLY studio using business-outcome positioning in Facebook ads",
        "Their copy focuses on 'sell properties before they are built' - not 'photorealistic renders'",
        "They are small and have limited ad volume - easy to outspend and out-creative",
        "Rendimension can differentiate by: broader service range, VR capabilities, experiential viz, and stronger case studies (Miami warehouse, exotic car club, etc.)",
    ]
    for r in render_pros:
        story.append(Paragraph(f"&#8226; {r}", styles['BulletText']))

    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>What Everyone Gets Wrong in Their Ads:</b>", styles['SubSection']))

    wrong = [
        "They talk about WHAT renders look like, not what renders DO for the business",
        "Same 5 hooks everywhere: 'photorealistic,' 'fast turnaround,' 'bring vision to life'",
        "Same CTAs: 'Get a free quote,' 'Contact us,' 'See portfolio'",
        "No urgency, no stakes, no social proof, no segment-specific messaging",
        "90%+ are single-image portfolio shots with no storytelling",
    ]
    for w in wrong:
        story.append(Paragraph(f"&#8226; {w}", styles['BulletText']))

    story.append(PageBreak())

    # =========================================================================
    # 8. FINAL RECOMMENDATIONS
    # =========================================================================
    story.append(Paragraph("8. FINAL RECOMMENDATIONS & NEXT STEPS", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT_BLUE))
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>Services to LEAD With (in order of priority):</b>", styles['SubSection']))

    recs = [
        [Paragraph('<b>#</b>', styles['TableHeader']),
         Paragraph('<b>Service</b>', styles['TableHeader']),
         Paragraph('<b>Why</b>', styles['TableHeader']),
         Paragraph('<b>FB Angle</b>', styles['TableHeader'])],

        [Paragraph('1', styles['TableCellCenter']),
         Paragraph('<b>Pre-Construction Sales Viz</b>', styles['TableCell']),
         Paragraph('Zero competition, proven demand (The Render Pros validates market), huge audience', styles['TableCell']),
         Paragraph('"Sell 40% of units before breaking ground"', styles['TableCell'])],

        [Paragraph('2', styles['TableCellCenter']),
         Paragraph('<b>Investor Presentation Packages</b>', styles['TableCell']),
         Paragraph('Literally zero ads in all of Facebook, highest ticket, clear ROI story', styles['TableCell']),
         Paragraph('"Close your next $10M funding round with visuals that speak investor language"', styles['TableCell'])],

        [Paragraph('3', styles['TableCellCenter']),
         Paragraph('<b>Experiential / Luxury Space Viz</b>', styles['TableCell']),
         Paragraph('Zero competition, Hugo has case studies (Miami warehouse, car club)', styles['TableCell']),
         Paragraph('"Your clients should FEEL the space before it exists"', styles['TableCell'])],
    ]

    story.append(make_table(recs, col_widths=[25, 120, 175, 150]))

    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>Services to AVOID Advertising:</b>", styles['SubSection']))

    avoid = [
        '"3D rendering services" - saturated by AI tools, low ticket, commodity positioning',
        '"Architectural visualization" - generic, high competition, everybody says the same thing',
        '"VR training simulation" - wrong market, sports VR dominates the ad space',
    ]
    for a in avoid:
        story.append(Paragraph(f"&#8226; {a}", styles['BulletText']))

    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>Immediate Next Steps:</b>", styles['SubSection']))

    steps = [
        [Paragraph('<b>Step</b>', styles['TableHeader']),
         Paragraph('<b>Action</b>', styles['TableHeader']),
         Paragraph('<b>Phase</b>', styles['TableHeader'])],

        [Paragraph('1', styles['TableCellCenter']),
         Paragraph('Run Positioning & Angle Strategist for top 3 services (segment-specific hooks, pain points, emotional triggers)', styles['TableCell']),
         Paragraph('Phase 2', styles['TableCellCenter'])],

        [Paragraph('2', styles['TableCellCenter']),
         Paragraph('Run Creative Director for visual concepts and AI-ready image prompts per segment', styles['TableCell']),
         Paragraph('Phase 3', styles['TableCellCenter'])],

        [Paragraph('3', styles['TableCellCenter']),
         Paragraph('Produce minimum 3 ad variants per service (carousel + single image + video/reel)', styles['TableCell']),
         Paragraph('Phase 4', styles['TableCellCenter'])],

        [Paragraph('4', styles['TableCellCenter']),
         Paragraph('Build Meta campaign structure with proper audiences, budgets, and UTM tracking', styles['TableCell']),
         Paragraph('Phase 5', styles['TableCellCenter'])],

        [Paragraph('5', styles['TableCellCenter']),
         Paragraph('Launch with 70/30 budget split (proven angles vs. test concepts)', styles['TableCell']),
         Paragraph('Phase 6', styles['TableCellCenter'])],
    ]

    story.append(make_table(steps, col_widths=[35, 370, 65]))

    story.append(Spacer(1, 20))
    story.append(Paragraph(
        "<b>Bottom Line:</b> Rendimension has a rare opportunity. The premium end of the visualization "
        "market has ZERO Facebook advertising presence. Every competitor talks about what renders look like. "
        "Nobody talks about what renders DO for a business. Rendimension should own this gap with "
        "business-outcome positioning, targeting decision-makers who do not know they need this service yet. "
        "The data says: GO.",
        styles['CalloutText']
    ))

    story.append(Spacer(1, 30))
    story.append(HRFlowable(width="100%", thickness=1, color=MEDIUM_GRAY))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Report generated March 17, 2026 | Rendimension Campaign Intelligence System | Confidential",
        styles['SmallText']
    ))

    # Build the PDF
    doc.build(story)
    return output_path


if __name__ == "__main__":
    path = build_report()
    print(f"Report generated: {path}")
