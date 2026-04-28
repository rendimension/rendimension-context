"""
RENDIMENSION LINKEDIN ANALYSIS REPORT - PDF Generator
LinkedIn-specific advertising landscape analysis to complement the Facebook/Instagram report
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
LINKEDIN_BLUE = HexColor('#0077B5')
ACCENT_ORANGE = HexColor('#e94560')
GREEN = HexColor('#27ae60')
YELLOW = HexColor('#f39c12')
RED = HexColor('#e74c3c')
LIGHT_GRAY = HexColor('#f5f5f5')
MEDIUM_GRAY = HexColor('#cccccc')
DARK_TEXT = HexColor('#2c3e50')
BLUE_LINK = HexColor('#2980b9')
LIGHT_BLUE_BG = HexColor('#eaf2f8')
LINKEDIN_LIGHT = HexColor('#e8f4fd')

def create_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name='ReportTitle',
        parent=styles['Title'],
        fontSize=28,
        leading=34,
        textColor=LINKEDIN_BLUE,
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
        textColor=LINKEDIN_BLUE,
        spaceBefore=20,
        spaceAfter=10,
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
        textColor=LINKEDIN_BLUE,
        leftIndent=15,
        rightIndent=15,
        spaceBefore=8,
        spaceAfter=8,
        borderWidth=1,
        borderColor=LINKEDIN_BLUE,
        borderPadding=10,
        backColor=LINKEDIN_LIGHT,
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
        name='VerdictTEST',
        parent=styles['Normal'],
        fontSize=10,
        leading=12,
        textColor=YELLOW,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
    ))

    return styles


def make_table(data, col_widths=None, header_color=LINKEDIN_BLUE):
    """Create a styled table with header row"""
    table = Table(data, colWidths=col_widths, repeatRows=1)
    style_commands = [
        ('BACKGROUND', (0, 0), (-1, 0), header_color),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, MEDIUM_GRAY),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]
    # Alternate row colors
    for i in range(1, len(data)):
        if i % 2 == 0:
            style_commands.append(('BACKGROUND', (0, i), (-1, i), LIGHT_GRAY))
    table.setStyle(TableStyle(style_commands))
    return table


def build_report():
    output_path = os.path.join(os.path.dirname(__file__),
                               'rendimension_linkedin_analysis_20260317.pdf')

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch,
        leftMargin=0.75*inch,
        rightMargin=0.75*inch,
    )

    styles = create_styles()
    story = []

    # ── COVER PAGE ──
    story.append(Spacer(1, 1.5*inch))
    story.append(Paragraph("RENDIMENSION", styles['ReportTitle']))
    story.append(Paragraph("LinkedIn Advertising Landscape Analysis", styles['ReportSubtitle']))
    story.append(HRFlowable(width="100%", thickness=2, color=LINKEDIN_BLUE))
    story.append(Spacer(1, 20))
    story.append(Paragraph("Complement to the Facebook/Instagram Master Decision Report", styles['BodyText2']))
    story.append(Paragraph("<b>Date:</b> March 17, 2026 &nbsp;&nbsp;|&nbsp;&nbsp; <b>Market:</b> United States (National) &nbsp;&nbsp;|&nbsp;&nbsp; <b>Platform:</b> LinkedIn", styles['BodyText2']))
    story.append(Paragraph("<b>Status:</b> LinkedIn Intelligence Complete", styles['BodyText2']))
    story.append(Spacer(1, 40))
    story.append(Paragraph(
        "<b>PURPOSE:</b> This document analyzes LinkedIn as a separate advertising channel for Rendimension. "
        "LinkedIn reaches decision-makers (developers, VPs, C-suite) directly by job title — a targeting "
        "capability Facebook cannot match. This analysis covers: LinkedIn Ad Library audit, platform benchmarks, "
        "ad format recommendations, targeting strategy, and GO/AVOID verdicts per service.",
        styles['BodyText2']
    ))
    story.append(PageBreak())

    # ── TABLE OF CONTENTS ──
    story.append(Paragraph("TABLE OF CONTENTS", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINKEDIN_BLUE))
    story.append(Spacer(1, 10))
    toc_items = [
        "1. Executive Summary — LinkedIn Verdict",
        "2. LinkedIn vs Facebook: Why Both Matter",
        "3. LinkedIn Ad Library Audit (7 Searches)",
        "4. Competitor Analysis on LinkedIn",
        "5. LinkedIn B2B Benchmarks 2026",
        "6. LinkedIn Targeting Strategy for Rendimension",
        "7. LinkedIn Ad Formats & Recommendations",
        "8. Service Decision Matrix — LinkedIn Specific",
        "9. LinkedIn Campaign Architecture",
        "10. Final Recommendations & Next Steps",
    ]
    for item in toc_items:
        story.append(Paragraph(item, styles['BodyText2']))
    story.append(PageBreak())

    # ── 1. EXECUTIVE SUMMARY ──
    story.append(Paragraph("1. EXECUTIVE SUMMARY", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINKEDIN_BLUE))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "LinkedIn is an even bigger blue ocean than Facebook for Rendimension. "
        "Across 7 LinkedIn Ad Library searches covering all of Rendimension's service categories, "
        "we found <b>fewer than 8 direct archviz competitors</b> running LinkedIn ads — and most of them "
        "are running generic portfolio-style ads with zero business outcome framing.",
        styles['BodyText2']
    ))
    story.append(Paragraph(
        "The opportunity is massive: LinkedIn lets you target by job title (VP of Development, "
        "Director of Construction, Real Estate Investment Manager) — the exact decision-makers who "
        "approve $15K–$50K visualization budgets. <b>Nobody is doing this.</b>",
        styles['CalloutText']
    ))
    story.append(Paragraph(
        "<b>30-Second Verdict:</b> LinkedIn should be Rendimension's <b>secondary channel</b> (after Meta), "
        "focused exclusively on high-ticket services targeting C-suite and VP-level decision-makers. "
        "The CPL will be higher ($60–$150 vs $30–$80 on Meta), but lead quality will be significantly better. "
        "Start with 2 campaigns: one targeting developers/investors, one targeting architects at large firms.",
        styles['BodyText2']
    ))
    story.append(PageBreak())

    # ── 2. LINKEDIN VS FACEBOOK ──
    story.append(Paragraph("2. LINKEDIN VS FACEBOOK: WHY BOTH MATTER", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINKEDIN_BLUE))
    story.append(Spacer(1, 10))

    comparison_data = [
        [Paragraph('<b>Dimension</b>', styles['TableHeader']),
         Paragraph('<b>Facebook/Instagram</b>', styles['TableHeader']),
         Paragraph('<b>LinkedIn</b>', styles['TableHeader'])],
        [Paragraph('Audience Type', styles['TableCell']),
         Paragraph('Broad — interests, behaviors, lookalikes', styles['TableCell']),
         Paragraph('Precise — job title, company size, industry, seniority', styles['TableCell'])],
        [Paragraph('Decision-Maker Access', styles['TableCell']),
         Paragraph('Indirect — may reach employees, not buyers', styles['TableCell']),
         Paragraph('Direct — target VP, Director, C-suite by title', styles['TableCell'])],
        [Paragraph('Cost Per Lead', styles['TableCell']),
         Paragraph('$30–$80 (estimated for archviz)', styles['TableCell']),
         Paragraph('$60–$150 (B2B services average)', styles['TableCell'])],
        [Paragraph('Lead Quality', styles['TableCell']),
         Paragraph('Mixed — needs qualification', styles['TableCell']),
         Paragraph('High — pre-qualified by job title', styles['TableCell'])],
        [Paragraph('Best For', styles['TableCell']),
         Paragraph('Volume, awareness, retargeting, visual showcase', styles['TableCell']),
         Paragraph('High-ticket leads, thought leadership, B2B credibility', styles['TableCell'])],
        [Paragraph('Ad Competition (Archviz)', styles['TableCell']),
         Paragraph('Low (10-50 results per search)', styles['TableCell']),
         Paragraph('Near Zero (0-5 direct competitors)', styles['TableCell'])],
        [Paragraph('Content Tone', styles['TableCell']),
         Paragraph('Visual, emotional, scroll-stopping', styles['TableCell']),
         Paragraph('Professional, credibility-driven, data-backed', styles['TableCell'])],
        [Paragraph('Lead Gen Forms', styles['TableCell']),
         Paragraph('Available (lower conversion)', styles['TableCell']),
         Paragraph('Native Lead Gen Forms (15-20% conversion rate)', styles['TableCell'])],
    ]

    t = make_table(comparison_data, col_widths=[1.3*inch, 2.6*inch, 2.6*inch])
    story.append(t)
    story.append(Spacer(1, 15))
    story.append(Paragraph(
        "<b>Strategic Takeaway:</b> Facebook generates VOLUME. LinkedIn generates QUALITY. "
        "Use both: Facebook for awareness and retargeting broad audiences, LinkedIn for "
        "surgically reaching the person who signs the check.",
        styles['CalloutText']
    ))
    story.append(PageBreak())

    # ── 3. LINKEDIN AD LIBRARY AUDIT ──
    story.append(Paragraph("3. LINKEDIN AD LIBRARY AUDIT", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINKEDIN_BLUE))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "We searched 7 service-related terms in the LinkedIn Ad Library to map the competitive landscape. "
        "Unlike Facebook's Ad Library (which shows all active ads with filters), LinkedIn's Ad Library "
        "searches by keyword across all promoted content. Results include both direct competitors and noise.",
        styles['BodyText2']
    ))
    story.append(Spacer(1, 8))

    audit_data = [
        [Paragraph('<b>Search Term</b>', styles['TableHeader']),
         Paragraph('<b>Total Results</b>', styles['TableHeader']),
         Paragraph('<b>Direct Archviz Competitors</b>', styles['TableHeader']),
         Paragraph('<b>Signal</b>', styles['TableHeader'])],
        [Paragraph('architectural visualization', styles['TableCell']),
         Paragraph('3,519', styles['TableCellCenter']),
         Paragraph('~5', styles['TableCellCenter']),
         Paragraph('LOW — mostly noise', styles['TableCell'])],
        [Paragraph('3D rendering', styles['TableCell']),
         Paragraph('3,043', styles['TableCellCenter']),
         Paragraph('~4', styles['TableCellCenter']),
         Paragraph('LOW — software/hardware ads dominate', styles['TableCell'])],
        [Paragraph('pre construction rendering', styles['TableCell']),
         Paragraph('24', styles['TableCellCenter']),
         Paragraph('0', styles['TableCellCenter']),
         Paragraph('"BLUE OCEAN"', styles['VerdictGO'])],
        [Paragraph('real estate rendering', styles['TableCell']),
         Paragraph('285', styles['TableCellCenter']),
         Paragraph('~3', styles['TableCellCenter']),
         Paragraph('VERY LOW', styles['TableCell'])],
        [Paragraph('virtual walkthrough construction', styles['TableCell']),
         Paragraph('9', styles['TableCellCenter']),
         Paragraph('0', styles['TableCellCenter']),
         Paragraph('"BLUE OCEAN"', styles['VerdictGO'])],
        [Paragraph('commercial space visualization', styles['TableCell']),
         Paragraph('416', styles['TableCellCenter']),
         Paragraph('0', styles['TableCellCenter']),
         Paragraph('"BLUE OCEAN"', styles['VerdictGO'])],
        [Paragraph('investor presentation real estate', styles['TableCell']),
         Paragraph('584', styles['TableCellCenter']),
         Paragraph('0', styles['TableCellCenter']),
         Paragraph('"BLUE OCEAN"', styles['VerdictGO'])],
    ]

    t = make_table(audit_data, col_widths=[2.0*inch, 0.9*inch, 1.4*inch, 2.2*inch])
    story.append(t)
    story.append(Spacer(1, 15))
    story.append(Paragraph(
        "<b>Key Finding:</b> 4 out of 7 searches returned ZERO direct archviz competitors. "
        "The high-value service categories (pre-construction, virtual walkthrough, commercial viz, "
        "investor presentations) are completely uncontested on LinkedIn. This is the widest blue ocean "
        "we've seen across any platform.",
        styles['CalloutText']
    ))
    story.append(PageBreak())

    # ── 4. COMPETITOR ANALYSIS ──
    story.append(Paragraph("4. COMPETITOR ANALYSIS ON LINKEDIN", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINKEDIN_BLUE))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Only 7-8 companies worldwide are actively advertising archviz services on LinkedIn. "
        "Here is every direct competitor we found:",
        styles['BodyText2']
    ))

    comp_data = [
        [Paragraph('<b>Company</b>', styles['TableHeader']),
         Paragraph('<b>Ad Type</b>', styles['TableHeader']),
         Paragraph('<b>Messaging</b>', styles['TableHeader']),
         Paragraph('<b>Threat Level</b>', styles['TableHeader'])],
        [Paragraph('Javier Wainstein / Just With Renders', styles['TableCell']),
         Paragraph('Multiple single-image ads (most prolific)', styles['TableCell']),
         Paragraph('Generic portfolio: "develops 3D visualization for architecture and interior design"', styles['TableCell']),
         Paragraph('LOW', styles['VerdictGO'])],
        [Paragraph('DESIGNS HUB LLC', styles['TableCell']),
         Paragraph('Video ads, luxury villa focus', styles['TableCell']),
         Paragraph('"A villa is not simply built - it is envisioned" — aspirational but generic', styles['TableCell']),
         Paragraph('LOW', styles['VerdictGO'])],
        [Paragraph('Mare Visuals', styles['TableCell']),
         Paragraph('Before/after visuals, branded "Project Presence"', styles['TableCell']),
         Paragraph('Investment value framing (+20%) — closest to business outcome language', styles['TableCell']),
         Paragraph('MEDIUM', styles['VerdictTEST'])],
        [Paragraph('3D Lines Design LTD', styles['TableCell']),
         Paragraph('Single image with strong copy', styles['TableCell']),
         Paragraph('"CGI Visuals That Sell Homes Before They\'re Built" — BEST business framing on LinkedIn', styles['TableCell']),
         Paragraph('MEDIUM', styles['VerdictTEST'])],
        [Paragraph('R3D Architectural Visualisation', styles['TableCell']),
         Paragraph('Single image, price competition', styles['TableCell']),
         Paragraph('"Let us beat your quote for 3D renders" — race-to-bottom positioning', styles['TableCell']),
         Paragraph('LOW', styles['VerdictGO'])],
        [Paragraph('ZOA Studio', styles['TableCell']),
         Paragraph('Animation/video focus', styles['TableCell']),
         Paragraph('"Trusted animation studio for visionary global projects" — premium but vague', styles['TableCell']),
         Paragraph('LOW', styles['VerdictGO'])],
        [Paragraph('OgdenXR', styles['TableCell']),
         Paragraph('Single image, proposal-focused', styles['TableCell']),
         Paragraph('"Walk through the project before it\'s built — that\'s how you win" — good framing', styles['TableCell']),
         Paragraph('MEDIUM', styles['VerdictTEST'])],
    ]

    t = make_table(comp_data, col_widths=[1.4*inch, 1.3*inch, 2.6*inch, 1.0*inch])
    story.append(t)
    story.append(Spacer(1, 15))

    story.append(Paragraph("What Every Competitor Gets Wrong on LinkedIn", styles['SubSection']))
    wrong_items = [
        "Portfolio-first approach — showing pretty buildings instead of business results",
        "No job-title-specific messaging — same ad for architects and developers",
        "No thought leadership — zero document ads, zero educational content",
        "No Lead Gen Forms — all drive to external websites (losing 50%+ of conversions)",
        "Personal profiles running ads (Javier Wainstein) instead of company pages — limits scale",
        "No retargeting strategy — one-touch ads with no follow-up sequence",
    ]
    for item in wrong_items:
        story.append(Paragraph(f"- {item}", styles['BulletText']))

    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "<b>Rendimension's Edge:</b> If you run LinkedIn ads with business outcome framing, "
        "Lead Gen Forms, thought leadership content, and job-title targeting, you will be the "
        "ONLY archviz company doing this. First-mover advantage is massive.",
        styles['CalloutText']
    ))
    story.append(PageBreak())

    # ── 5. LINKEDIN B2B BENCHMARKS ──
    story.append(Paragraph("5. LINKEDIN B2B BENCHMARKS 2026", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINKEDIN_BLUE))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "These benchmarks are based on 2025-2026 B2B advertising data across LinkedIn. "
        "Archviz is a niche B2B service, so expect results between the general B2B average "
        "and the professional services category.",
        styles['BodyText2']
    ))

    bench_data = [
        [Paragraph('<b>Metric</b>', styles['TableHeader']),
         Paragraph('<b>LinkedIn B2B Average</b>', styles['TableHeader']),
         Paragraph('<b>Rendimension Target</b>', styles['TableHeader']),
         Paragraph('<b>Context</b>', styles['TableHeader'])],
        [Paragraph('CPC (Cost Per Click)', styles['TableCell']),
         Paragraph('$5.50 – $8.50', styles['TableCellCenter']),
         Paragraph('< $8.00', styles['TableCellCenter']),
         Paragraph('Higher than Meta ($1-3) but leads are pre-qualified by job title', styles['TableCell'])],
        [Paragraph('CTR (Click-Through Rate)', styles['TableCell']),
         Paragraph('0.44% – 0.65%', styles['TableCellCenter']),
         Paragraph('> 0.5%', styles['TableCellCenter']),
         Paragraph('Lower than Meta (1-2%) — normal for LinkedIn. Visual archviz content may outperform.', styles['TableCell'])],
        [Paragraph('CPL (Cost Per Lead)', styles['TableCell']),
         Paragraph('$60 – $150+', styles['TableCellCenter']),
         Paragraph('< $150', styles['TableCellCenter']),
         Paragraph('At $15K+ project value, even $150/lead is <1% cost of sale — excellent ROI', styles['TableCell'])],
        [Paragraph('Lead Gen Form Conv. Rate', styles['TableCell']),
         Paragraph('15% – 20%', styles['TableCellCenter']),
         Paragraph('> 15%', styles['TableCellCenter']),
         Paragraph('LinkedIn native forms auto-fill from profile — 3-5x higher than landing pages', styles['TableCell'])],
        [Paragraph('Engagement Rate (Organic)', styles['TableCell']),
         Paragraph('2% – 4%', styles['TableCellCenter']),
         Paragraph('> 3%', styles['TableCellCenter']),
         Paragraph('Visual content (renders) typically gets above-average engagement on LinkedIn', styles['TableCell'])],
    ]

    t = make_table(bench_data, col_widths=[1.4*inch, 1.4*inch, 1.2*inch, 2.5*inch])
    story.append(t)
    story.append(Spacer(1, 15))

    # Traffic light system
    story.append(Paragraph("Rendimension LinkedIn Traffic Light System", styles['SubSection']))
    traffic_data = [
        [Paragraph('<b>Metric</b>', styles['TableHeader']),
         Paragraph('<b>GREEN (Keep Running)</b>', styles['TableHeader']),
         Paragraph('<b>YELLOW (Monitor)</b>', styles['TableHeader']),
         Paragraph('<b>RED (Action Required)</b>', styles['TableHeader'])],
        [Paragraph('CTR', styles['TableCell']),
         Paragraph('> 0.5%', styles['TableCellCenter']),
         Paragraph('0.3% – 0.5%', styles['TableCellCenter']),
         Paragraph('< 0.3%', styles['TableCellCenter'])],
        [Paragraph('CPC', styles['TableCell']),
         Paragraph('< $8', styles['TableCellCenter']),
         Paragraph('$8 – $15', styles['TableCellCenter']),
         Paragraph('> $15', styles['TableCellCenter'])],
        [Paragraph('CPL', styles['TableCell']),
         Paragraph('< $150', styles['TableCellCenter']),
         Paragraph('$150 – $250', styles['TableCellCenter']),
         Paragraph('> $250', styles['TableCellCenter'])],
    ]

    t2 = make_table(traffic_data, col_widths=[1.2*inch, 1.8*inch, 1.8*inch, 1.8*inch])
    # Color the cells
    style_override = TableStyle([
        ('BACKGROUND', (1, 1), (1, -1), HexColor('#e8f5e9')),
        ('BACKGROUND', (2, 1), (2, -1), HexColor('#fff8e1')),
        ('BACKGROUND', (3, 1), (3, -1), HexColor('#ffebee')),
    ])
    t2.setStyle(style_override)
    story.append(t2)
    story.append(PageBreak())

    # ── 6. TARGETING STRATEGY ──
    story.append(Paragraph("6. LINKEDIN TARGETING STRATEGY", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINKEDIN_BLUE))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "LinkedIn's killer advantage is targeting by job title, company size, and industry. "
        "Here is the targeting architecture for each of Rendimension's client types:",
        styles['BodyText2']
    ))

    # Audience 1
    story.append(Paragraph("Audience 1: Real Estate Developers & Investors", styles['SubSection']))
    target_data1 = [
        [Paragraph('<b>Parameter</b>', styles['TableHeader']),
         Paragraph('<b>Targeting</b>', styles['TableHeader'])],
        [Paragraph('Job Titles', styles['TableCell']),
         Paragraph('VP of Development, Director of Development, Real Estate Developer, '
                   'Chief Development Officer, Managing Director (Real Estate), '
                   'Investment Manager, VP of Acquisitions, Development Manager', styles['TableCell'])],
        [Paragraph('Industries', styles['TableCell']),
         Paragraph('Real Estate, Construction, Real Estate Investment, Hospitality, '
                   'Commercial Real Estate', styles['TableCell'])],
        [Paragraph('Company Size', styles['TableCell']),
         Paragraph('11-200 employees (mid-size developers), 201-1000 (large developers), '
                   '1001+ (institutional)', styles['TableCell'])],
        [Paragraph('Seniority', styles['TableCell']),
         Paragraph('Director, VP, C-Suite, Owner/Partner', styles['TableCell'])],
        [Paragraph('Geography', styles['TableCell']),
         Paragraph('United States (national)', styles['TableCell'])],
        [Paragraph('Est. Audience Size', styles['TableCell']),
         Paragraph('50,000 – 120,000 members', styles['TableCell'])],
    ]
    t = make_table(target_data1, col_widths=[1.5*inch, 5.0*inch])
    story.append(t)
    story.append(Spacer(1, 12))

    # Audience 2
    story.append(Paragraph("Audience 2: Architects at Large Firms", styles['SubSection']))
    target_data2 = [
        [Paragraph('<b>Parameter</b>', styles['TableHeader']),
         Paragraph('<b>Targeting</b>', styles['TableHeader'])],
        [Paragraph('Job Titles', styles['TableCell']),
         Paragraph('Principal Architect, Design Director, Studio Director, '
                   'Project Architect, Senior Architect, Architecture Director, '
                   'Head of Design', styles['TableCell'])],
        [Paragraph('Industries', styles['TableCell']),
         Paragraph('Architecture & Planning, Design, Civil Engineering', styles['TableCell'])],
        [Paragraph('Company Size', styles['TableCell']),
         Paragraph('51-200 (mid-size firms), 201-1000 (large firms), '
                   '1001+ (enterprise firms like Gensler, HKS)', styles['TableCell'])],
        [Paragraph('Seniority', styles['TableCell']),
         Paragraph('Senior, Director, VP, C-Suite, Owner/Partner', styles['TableCell'])],
        [Paragraph('Geography', styles['TableCell']),
         Paragraph('United States (national)', styles['TableCell'])],
        [Paragraph('Est. Audience Size', styles['TableCell']),
         Paragraph('30,000 – 80,000 members', styles['TableCell'])],
    ]
    t = make_table(target_data2, col_widths=[1.5*inch, 5.0*inch])
    story.append(t)
    story.append(Spacer(1, 12))

    # Audience 3
    story.append(Paragraph("Audience 3: Retail & Hospitality Expansion Leads", styles['SubSection']))
    target_data3 = [
        [Paragraph('<b>Parameter</b>', styles['TableHeader']),
         Paragraph('<b>Targeting</b>', styles['TableHeader'])],
        [Paragraph('Job Titles', styles['TableCell']),
         Paragraph('VP of Store Development, Director of Real Estate, '
                   'VP of Facilities, Director of Construction, '
                   'Head of Expansion, Store Planning Manager, '
                   'VP of Design & Construction', styles['TableCell'])],
        [Paragraph('Industries', styles['TableCell']),
         Paragraph('Retail, Hospitality, Food & Beverages, Leisure/Travel, '
                   'Restaurants', styles['TableCell'])],
        [Paragraph('Company Size', styles['TableCell']),
         Paragraph('201-1000, 1001-5000, 5001+ (chains expanding nationally)', styles['TableCell'])],
        [Paragraph('Seniority', styles['TableCell']),
         Paragraph('Director, VP, C-Suite', styles['TableCell'])],
        [Paragraph('Geography', styles['TableCell']),
         Paragraph('United States (national)', styles['TableCell'])],
        [Paragraph('Est. Audience Size', styles['TableCell']),
         Paragraph('15,000 – 40,000 members', styles['TableCell'])],
    ]
    t = make_table(target_data3, col_widths=[1.5*inch, 5.0*inch])
    story.append(t)
    story.append(PageBreak())

    # ── 7. AD FORMATS ──
    story.append(Paragraph("7. LINKEDIN AD FORMATS & RECOMMENDATIONS", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINKEDIN_BLUE))
    story.append(Spacer(1, 10))

    format_data = [
        [Paragraph('<b>Format</b>', styles['TableHeader']),
         Paragraph('<b>Best For</b>', styles['TableHeader']),
         Paragraph('<b>Rendimension Use Case</b>', styles['TableHeader']),
         Paragraph('<b>Priority</b>', styles['TableHeader'])],
        [Paragraph('Document Ad (Carousel PDF)', styles['TableCell']),
         Paragraph('Education, thought leadership, multi-step storytelling', styles['TableCell']),
         Paragraph('"5 Questions to Ask Before Hiring a Visualization Studio" — positions as expert, captures leads mid-scroll', styles['TableCell']),
         Paragraph('HIGH', styles['VerdictGO'])],
        [Paragraph('Single Image + Lead Gen Form', styles['TableCell']),
         Paragraph('Direct lead capture, quick conversion', styles['TableCell']),
         Paragraph('Stunning render + "Get a Project Assessment" — auto-fills from LinkedIn profile', styles['TableCell']),
         Paragraph('HIGH', styles['VerdictGO'])],
        [Paragraph('Video Ad', styles['TableCell']),
         Paragraph('Storytelling, walkthroughs, process showcase', styles['TableCell']),
         Paragraph('30-60s walkthrough video: "From blueprint to boardroom-ready in 10 days"', styles['TableCell']),
         Paragraph('HIGH', styles['VerdictGO'])],
        [Paragraph('Thought Leader Ad (Personal Profile)', styles['TableCell']),
         Paragraph('Credibility, authenticity, engagement', styles['TableCell']),
         Paragraph('Hugo posting about project insights, promoted to target audience — feels organic', styles['TableCell']),
         Paragraph('MEDIUM', styles['VerdictTEST'])],
        [Paragraph('Carousel Ad', styles['TableCell']),
         Paragraph('Before/after, project showcase, process steps', styles['TableCell']),
         Paragraph('Before (blueprint) > During (render process) > After (sold-out development)', styles['TableCell']),
         Paragraph('MEDIUM', styles['VerdictTEST'])],
        [Paragraph('Message Ad (InMail)', styles['TableCell']),
         Paragraph('Direct outreach to specific decision-makers', styles['TableCell']),
         Paragraph('Personalized message to VPs of Development: "I noticed your new project in [city]..."', styles['TableCell']),
         Paragraph('LOW', styles['VerdictTEST'])],
    ]

    t = make_table(format_data, col_widths=[1.3*inch, 1.6*inch, 2.5*inch, 1.0*inch])
    story.append(t)
    story.append(Spacer(1, 15))
    story.append(Paragraph(
        "<b>Format Strategy:</b> Lead with Document Ads (thought leadership) and Single Image + Lead Gen Forms "
        "(direct conversion). This combination builds credibility AND captures leads simultaneously. "
        "No competitor is using Document Ads for archviz on LinkedIn — this is your format blue ocean.",
        styles['CalloutText']
    ))
    story.append(PageBreak())

    # ── 8. SERVICE DECISION MATRIX ──
    story.append(Paragraph("8. SERVICE DECISION MATRIX — LINKEDIN SPECIFIC", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINKEDIN_BLUE))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "LinkedIn-specific GO/AVOID verdicts based on Ad Library competition, "
        "targeting viability, and audience match on the platform:",
        styles['BodyText2']
    ))

    matrix_data = [
        [Paragraph('<b>Service</b>', styles['TableHeader']),
         Paragraph('<b>LinkedIn Competition</b>', styles['TableHeader']),
         Paragraph('<b>Target Audience on LI</b>', styles['TableHeader']),
         Paragraph('<b>Verdict</b>', styles['TableHeader']),
         Paragraph('<b>Rationale</b>', styles['TableHeader'])],
        [Paragraph('Pre-Construction Sales Visualization', styles['TableCell']),
         Paragraph('ZERO', styles['TableCellCenter']),
         Paragraph('Developers, VPs', styles['TableCellCenter']),
         Paragraph('GO', styles['VerdictGO']),
         Paragraph('0 competitors + perfect audience match. #1 priority.', styles['TableCell'])],
        [Paragraph('Investor Presentation Packages', styles['TableCell']),
         Paragraph('ZERO', styles['TableCellCenter']),
         Paragraph('Investment Managers, Developers', styles['TableCellCenter']),
         Paragraph('GO', styles['VerdictGO']),
         Paragraph('0 competitors. LinkedIn is WHERE investors live. Natural fit.', styles['TableCell'])],
        [Paragraph('VR Walkthrough (Construction Verification)', styles['TableCell']),
         Paragraph('ZERO', styles['TableCellCenter']),
         Paragraph('Directors of Construction, PMs', styles['TableCellCenter']),
         Paragraph('GO', styles['VerdictGO']),
         Paragraph('9 total results, 0 direct. Decision-makers are on LinkedIn.', styles['TableCell'])],
        [Paragraph('Commercial/Retail Space Viz', styles['TableCell']),
         Paragraph('ZERO', styles['TableCellCenter']),
         Paragraph('VPs of Store Dev, Expansion Dirs', styles['TableCellCenter']),
         Paragraph('GO', styles['VerdictGO']),
         Paragraph('Retail chains have LI presence. Target expansion teams.', styles['TableCell'])],
        [Paragraph('Hospitality/Resort Visualization', styles['TableCell']),
         Paragraph('NEAR ZERO', styles['TableCellCenter']),
         Paragraph('Hospitality Dev Directors', styles['TableCellCenter']),
         Paragraph('GO', styles['VerdictGO']),
         Paragraph('Niche audience but high-ticket. Worth testing.', styles['TableCell'])],
        [Paragraph('Architectural Rendering (Generic)', styles['TableCell']),
         Paragraph('~5 competitors', styles['TableCellCenter']),
         Paragraph('Architects at large firms', styles['TableCellCenter']),
         Paragraph('TEST', styles['VerdictTEST']),
         Paragraph('Some competition exists. Only do with segment-specific copy.', styles['TableCell'])],
        [Paragraph('Interior Design Rendering', styles['TableCell']),
         Paragraph('LOW', styles['TableCellCenter']),
         Paragraph('Interior designers (small firms)', styles['TableCellCenter']),
         Paragraph('AVOID', styles['VerdictAVOID']),
         Paragraph('Low ticket, designers less active on LI. Better on Instagram.', styles['TableCell'])],
        [Paragraph('Commodity 3D Rendering', styles['TableCell']),
         Paragraph('~4 competitors', styles['TableCellCenter']),
         Paragraph('Broad/unqualified', styles['TableCellCenter']),
         Paragraph('AVOID', styles['VerdictAVOID']),
         Paragraph('Price competition. R3D already racing to bottom. Not worth LI spend.', styles['TableCell'])],
    ]

    t = make_table(matrix_data, col_widths=[1.4*inch, 1.0*inch, 1.2*inch, 0.7*inch, 2.2*inch])
    story.append(t)
    story.append(PageBreak())

    # ── 9. CAMPAIGN ARCHITECTURE ──
    story.append(Paragraph("9. LINKEDIN CAMPAIGN ARCHITECTURE", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINKEDIN_BLUE))
    story.append(Spacer(1, 10))

    story.append(Paragraph("Recommended Campaign Structure (Phase 1 Launch)", styles['SubSection']))
    story.append(Spacer(1, 8))

    # Campaign 1
    story.append(Paragraph("<b>Campaign 1: Developer/Investor Lead Gen</b>", styles['BodyText2']))
    camp1 = [
        "Objective: Lead Generation (Lead Gen Forms)",
        "Audience: Developers + Investors (Audience 1 targeting)",
        "Budget: $30-50/day ($900-1,500/month)",
        "Ad Set A: Document Ad — '5 Ways Visualization Accelerates Real Estate Sales'",
        "Ad Set B: Single Image + Lead Gen Form — Hero render + 'Get Your Project Assessment'",
        "Ad Set C: Video — 30s walkthrough transformation",
        "KPI Target: CPL < $150, CTR > 0.5%",
    ]
    for item in camp1:
        story.append(Paragraph(f"  - {item}", styles['BulletText']))
    story.append(Spacer(1, 12))

    # Campaign 2
    story.append(Paragraph("<b>Campaign 2: Architect Thought Leadership</b>", styles['BodyText2']))
    camp2 = [
        "Objective: Lead Generation + Brand Awareness",
        "Audience: Senior Architects at large firms (Audience 2 targeting)",
        "Budget: $20-30/day ($600-900/month)",
        "Ad Set A: Thought Leader Ad — Hugo's post about project insights",
        "Ad Set B: Document Ad — 'Why Your Presentation Renders Are Losing You Projects'",
        "Ad Set C: Carousel — Before (flat drawing) > After (photorealistic render)",
        "KPI Target: CPL < $120, Engagement Rate > 3%",
    ]
    for item in camp2:
        story.append(Paragraph(f"  - {item}", styles['BulletText']))
    story.append(Spacer(1, 12))

    # Campaign 3 (Phase 2)
    story.append(Paragraph("<b>Campaign 3: Retail/Hospitality Expansion (Phase 2)</b>", styles['BodyText2']))
    camp3 = [
        "Objective: Lead Generation",
        "Audience: Retail/Hospitality expansion teams (Audience 3 targeting)",
        "Budget: $20-30/day ($600-900/month)",
        "Launch after Campaigns 1&2 prove the model (4-6 weeks later)",
        "Ad Set A: Single Image — 'See Your New Location Before Breaking Ground'",
        "Ad Set B: Video — Retail store visualization walkthrough",
        "KPI Target: CPL < $200 (niche audience, higher expected CPL)",
    ]
    for item in camp3:
        story.append(Paragraph(f"  - {item}", styles['BulletText']))
    story.append(Spacer(1, 15))

    story.append(Paragraph(
        "<b>Total LinkedIn Budget (Phase 1):</b> $1,500-2,400/month across 2 campaigns. "
        "This is a test budget to validate the channel before scaling. "
        "If CPL meets targets within 30 days, increase to $3,000-4,000/month.",
        styles['CalloutText']
    ))
    story.append(PageBreak())

    # ── 10. FINAL RECOMMENDATIONS ──
    story.append(Paragraph("10. FINAL RECOMMENDATIONS & NEXT STEPS", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINKEDIN_BLUE))
    story.append(Spacer(1, 10))

    story.append(Paragraph("Top 3 LinkedIn Priorities", styles['SubSection']))
    priorities = [
        "<b>1. Launch Developer/Investor Campaign First</b> — This is the highest-ticket audience "
        "($15K-$50K projects) with zero competitors on LinkedIn. Use Lead Gen Forms + Document Ads. "
        "Expected ROI: even at $150/lead, one closed deal ($20K) pays for 4+ months of ad spend.",
        "<b>2. Create 3 Document Ads (LinkedIn Carousels)</b> — Nobody in archviz is using this format. "
        "Topics: '5 Ways Visualization Accelerates Sales', 'The Real Cost of Cheap Renders', "
        "'How Smart Developers Pre-Sell 60% Before Breaking Ground'. These build credibility AND capture leads.",
        "<b>3. Set Up Hugo as Thought Leader</b> — Thought Leader Ads (promoted personal posts) "
        "get 2-3x higher engagement than company page ads. Hugo posts about real projects, "
        "insights from 1,000+ projects, and industry observations. LinkedIn promotes them to target audiences.",
    ]
    for p in priorities:
        story.append(Paragraph(p, styles['BodyText2']))
        story.append(Spacer(1, 6))

    story.append(Spacer(1, 10))
    story.append(Paragraph("What NOT To Do on LinkedIn", styles['SubSection']))
    donts = [
        "Do NOT advertise generic '3D rendering services' — 4 competitors already doing this badly",
        "Do NOT use portfolio-only ads — every competitor does this. LinkedIn audience wants business value.",
        "Do NOT send traffic to external landing pages — use Lead Gen Forms (3-5x higher conversion)",
        "Do NOT target 'architects' broadly — target by seniority + firm size to avoid junior/freelance leads",
        "Do NOT copy Facebook ad creative — LinkedIn requires professional tone, not scroll-stopping visuals",
    ]
    for d in donts:
        story.append(Paragraph(f"  - {d}", styles['BulletText']))

    story.append(Spacer(1, 15))
    story.append(Paragraph("Phased Action Plan", styles['SubSection']))
    phase_data = [
        [Paragraph('<b>Phase</b>', styles['TableHeader']),
         Paragraph('<b>Timeline</b>', styles['TableHeader']),
         Paragraph('<b>Actions</b>', styles['TableHeader'])],
        [Paragraph('Phase 1: Setup', styles['TableCell']),
         Paragraph('Week 1-2', styles['TableCellCenter']),
         Paragraph('Install LinkedIn Insight Tag, create Lead Gen Forms, produce 3 Document Ads + 3 Single Image ads, set up Campaign Manager', styles['TableCell'])],
        [Paragraph('Phase 2: Launch', styles['TableCell']),
         Paragraph('Week 3', styles['TableCellCenter']),
         Paragraph('Launch Campaign 1 (Developers) + Campaign 2 (Architects) with $50-80/day combined budget', styles['TableCell'])],
        [Paragraph('Phase 3: Learn', styles['TableCell']),
         Paragraph('Week 3-6', styles['TableCellCenter']),
         Paragraph('7-day learning period (hands off), then monitor. Kill ads with CTR < 0.3% after 5K impressions. Scale winners by 20%.', styles['TableCell'])],
        [Paragraph('Phase 4: Optimize', styles['TableCell']),
         Paragraph('Week 7-10', styles['TableCellCenter']),
         Paragraph('Analyze CPL by audience segment. Double down on winning audience. Create 3 new ad variants. Launch Campaign 3 (Retail/Hospitality) if Phase 1 profitable.', styles['TableCell'])],
        [Paragraph('Phase 5: Scale', styles['TableCell']),
         Paragraph('Month 3+', styles['TableCellCenter']),
         Paragraph('If CPL < $150 sustained: increase budget to $3-4K/month. Add retargeting campaign for website visitors. Test Message Ads (InMail) for high-value prospects.', styles['TableCell'])],
    ]

    t = make_table(phase_data, col_widths=[1.2*inch, 1.0*inch, 4.3*inch])
    story.append(t)
    story.append(Spacer(1, 20))

    story.append(Paragraph(
        "<b>BOTTOM LINE:</b> LinkedIn is Rendimension's untapped goldmine for high-ticket B2B leads. "
        "The competition is essentially zero in the service categories that matter most. "
        "With the right targeting (job title + seniority) and format (Document Ads + Lead Gen Forms), "
        "Rendimension can own this channel before anyone else wakes up.",
        styles['CalloutText']
    ))

    story.append(Spacer(1, 30))
    story.append(HRFlowable(width="100%", thickness=1, color=MEDIUM_GRAY))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Report generated: March 17, 2026 | Analyst: Market Intelligence Agent | "
        "Data sources: LinkedIn Ad Library (live audit), LinkedIn Marketing Solutions benchmarks, "
        "B2B advertising industry reports 2025-2026",
        styles['SmallText']
    ))

    # Build PDF
    doc.build(story)
    print(f"PDF generated successfully: {output_path}")
    return output_path


if __name__ == '__main__':
    build_report()
