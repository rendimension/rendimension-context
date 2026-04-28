"""
RENDIMENSION CAMPAIGN PACKAGE - Complete Facebook Campaign Ready to Launch
Positioning + 9 Ad Variants + Nano Banana Prompts + HeyGen Scripts + Campaign Structure
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
ACCENT_TEAL = HexColor('#00b4d8')
GREEN = HexColor('#27ae60')
YELLOW = HexColor('#f39c12')
RED = HexColor('#e74c3c')
LIGHT_GRAY = HexColor('#f5f5f5')
MEDIUM_GRAY = HexColor('#cccccc')
DARK_TEXT = HexColor('#2c3e50')
BLUE_LINK = HexColor('#2980b9')
GOLD = HexColor('#f0a500')
PURPLE = HexColor('#6c5ce7')

def create_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        'ReportTitle', parent=styles['Title'],
        fontSize=28, textColor=white, alignment=TA_CENTER,
        spaceAfter=6, fontName='Helvetica-Bold'
    ))
    styles.add(ParagraphStyle(
        'ReportSubtitle', parent=styles['Normal'],
        fontSize=14, textColor=HexColor('#aaaaaa'), alignment=TA_CENTER,
        spaceAfter=20, fontName='Helvetica'
    ))
    styles.add(ParagraphStyle(
        'SectionTitle', parent=styles['Heading1'],
        fontSize=18, textColor=ACCENT_ORANGE, spaceBefore=16,
        spaceAfter=10, fontName='Helvetica-Bold',
        borderWidth=0, borderPadding=0
    ))
    styles.add(ParagraphStyle(
        'SubSection', parent=styles['Heading2'],
        fontSize=14, textColor=ACCENT_BLUE, spaceBefore=12,
        spaceAfter=6, fontName='Helvetica-Bold'
    ))
    styles.add(ParagraphStyle(
        'HookTitle', parent=styles['Heading2'],
        fontSize=16, textColor=GOLD, spaceBefore=14,
        spaceAfter=8, fontName='Helvetica-Bold'
    ))
    styles['BodyText'].fontSize = 10
    styles['BodyText'].textColor = DARK_TEXT
    styles['BodyText'].spaceBefore = 2
    styles['BodyText'].spaceAfter = 6
    styles['BodyText'].leading = 14
    styles['BodyText'].fontName = 'Helvetica'
    styles.add(ParagraphStyle(
        'BulletText', parent=styles['Normal'],
        fontSize=10, textColor=DARK_TEXT, spaceBefore=1,
        spaceAfter=3, leading=13, fontName='Helvetica',
        leftIndent=20, bulletIndent=10
    ))
    styles.add(ParagraphStyle(
        'CalloutText', parent=styles['Normal'],
        fontSize=11, textColor=ACCENT_BLUE, spaceBefore=4,
        spaceAfter=8, leading=14, fontName='Helvetica-Bold',
        leftIndent=15, borderWidth=0
    ))
    styles.add(ParagraphStyle(
        'AdCopy', parent=styles['Normal'],
        fontSize=10, textColor=DARK_TEXT, spaceBefore=2,
        spaceAfter=4, leading=13, fontName='Courier',
        leftIndent=15, rightIndent=15, backColor=HexColor('#f8f9fa')
    ))
    styles.add(ParagraphStyle(
        'PromptText', parent=styles['Normal'],
        fontSize=9, textColor=HexColor('#2d3436'), spaceBefore=2,
        spaceAfter=4, leading=12, fontName='Courier',
        leftIndent=15, rightIndent=15, backColor=HexColor('#ffeaa7')
    ))
    styles.add(ParagraphStyle(
        'VerdictGO', parent=styles['Normal'],
        fontSize=11, textColor=white, backColor=GREEN,
        spaceBefore=4, spaceAfter=8, leading=14,
        fontName='Helvetica-Bold', leftIndent=10,
        borderPadding=(6, 10, 6, 10)
    ))
    styles.add(ParagraphStyle(
        'SmallLabel', parent=styles['Normal'],
        fontSize=8, textColor=HexColor('#888888'), spaceBefore=0,
        spaceAfter=2, fontName='Helvetica'
    ))
    styles.add(ParagraphStyle(
        'AdName', parent=styles['Normal'],
        fontSize=9, textColor=PURPLE, spaceBefore=2,
        spaceAfter=4, fontName='Helvetica-Bold'
    ))

    return styles


def build_cover(story, styles):
    """Cover page"""
    # Dark header block
    header_data = [['']]
    header_table = Table(header_data, colWidths=[7.5*inch], rowHeights=[2.5*inch])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), DARK_BG),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(header_table)
    story.append(Spacer(1, -80))

    # Title block
    title_data = [[
        Paragraph('RENDIMENSION', styles['ReportTitle']),
    ]]
    title_table = Table(title_data, colWidths=[7.5*inch], rowHeights=[0.6*inch])
    title_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), DARK_BG),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(title_table)

    subtitle_data = [[
        Paragraph('Facebook Campaign Package', styles['ReportSubtitle']),
    ]]
    subtitle_table = Table(subtitle_data, colWidths=[7.5*inch], rowHeights=[0.4*inch])
    subtitle_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), DARK_BG),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(subtitle_table)

    sub2_data = [[
        Paragraph('9 Ads Ready to Launch | $9/Day Budget | Lead Generation', styles['ReportSubtitle']),
    ]]
    sub2_table = Table(sub2_data, colWidths=[7.5*inch], rowHeights=[0.4*inch])
    sub2_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), DARK_BG),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(sub2_table)

    story.append(Spacer(1, 40))

    # Quick stats
    stats = [
        ['PLATFORM', 'BUDGET', 'ADS', 'OBJECTIVE'],
        ['Facebook / Instagram', '$9/day ($270/mo)', '9 variants', 'Lead Generation'],
    ]
    stats_table = Table(stats, colWidths=[1.8*inch]*4)
    stats_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), ACCENT_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('BACKGROUND', (0,1), (-1,-1), LIGHT_GRAY),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 9),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, MEDIUM_GRAY),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(stats_table)

    story.append(Spacer(1, 30))

    # What's inside
    story.append(Paragraph('WHAT\'S INSIDE THIS PACKAGE', styles['SubSection']))
    items = [
        'Positioning Strategy for 3 Priority Segments',
        '3 Hook Concepts with Scroll-Stopping Angles',
        '9 Complete Ad Variants (Copy + Visual Direction)',
        'Nano Banana Image Prompts (Ready to Generate)',
        'HeyGen Video Scripts (2 Bonus Video Ads)',
        'Campaign Structure (Audiences, Budget, Placements)',
        'Lead Gen Form Setup Instructions',
        'UTM Parameters for Every Ad',
    ]
    for item in items:
        story.append(Paragraph(f'\xe2\x96\xb8 {item}', styles['BulletText']))

    story.append(PageBreak())


def build_positioning(story, styles):
    """Positioning strategy section"""
    story.append(Paragraph('1. POSITIONING STRATEGY', styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=2, color=ACCENT_ORANGE))
    story.append(Spacer(1, 10))

    story.append(Paragraph(
        'Based on market intelligence: ZERO competitors running Facebook ads for pre-construction '
        'visualization services. This is a blue ocean. The positioning below exploits this gap.',
        styles['BodyText']
    ))

    story.append(Paragraph(
        '<b>Universal Rendimension Position:</b> "We don\'t make pretty pictures. We build the sales tool '
        'that pre-sells your project before you pour concrete."',
        styles['CalloutText']
    ))
    story.append(Spacer(1, 8))

    # SEGMENT 1
    story.append(Paragraph('SEGMENT 1: REAL ESTATE DEVELOPERS', styles['SubSection']))
    seg1 = [
        ['ELEMENT', 'DETAIL'],
        ['Core Pain Point', 'They need to sell 40-60% of units before getting construction financing. '
         'Without compelling visuals, buyers can\'t imagine the finished product and won\'t commit deposits.'],
        ['Wrong Belief', '"Architectural drawings and floor plans are enough to sell units." '
         'Reality: buyers making $300K+ decisions need to FEEL the space, not read blueprints.'],
        ['Frustration', 'Past experience with render companies: slow delivery (6-8 weeks), endless revision cycles, '
         'renders that look "CGI" not photorealistic, and no understanding of what sells units.'],
        ['Strategic Angle', 'Position as a PRE-SALES ACCELERATION TOOL. Not a creative service. '
         'Frame renders as revenue infrastructure that shortens the sales cycle from 18 months to 6.'],
        ['Main Hook', '"60% pre-sold before groundbreaking. Here\'s what the sales center looked like."'],
        ['Emotional Trigger', 'FEAR of a stalled project. Developers\' worst nightmare is carrying costs '
         'on an unsold building. The threat of financial exposure drives fast decisions.'],
    ]
    seg1_table = Table(seg1, colWidths=[1.5*inch, 5.7*inch])
    seg1_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), ACCENT_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,1), (1,-1), 'Helvetica'),
        ('BACKGROUND', (0,1), (-1,-1), LIGHT_GRAY),
        ('GRID', (0,0), (-1,-1), 0.5, MEDIUM_GRAY),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(seg1_table)
    story.append(Spacer(1, 12))

    # SEGMENT 2
    story.append(Paragraph('SEGMENT 2: COMMERCIAL DEVELOPERS & RETAIL CHAINS', styles['SubSection']))
    seg2 = [
        ['ELEMENT', 'DETAIL'],
        ['Core Pain Point', 'Expanding to 20+ new locations simultaneously. Each location needs stakeholder approval, '
         'city planning presentations, and franchise/tenant buy-in BEFORE construction starts.'],
        ['Wrong Belief', '"We can use photos from existing locations to sell new ones." '
         'Reality: every site is different, and tenants/city planners need to see THIS specific project.'],
        ['Frustration', 'Hiring local architects for each location is slow and inconsistent. '
         'The brand looks different in every market because there\'s no visual standard.'],
        ['Strategic Angle', 'Position as BRAND CONSISTENCY AT SCALE. One partner that ensures every new '
         'location looks exactly on-brand before construction, across all markets simultaneously.'],
        ['Main Hook', '"Opening 12 locations this year? Your tenants need to see them yesterday."'],
        ['Emotional Trigger', 'URGENCY and CONTROL. Multi-unit developers are racing against timelines '
         'and can\'t afford delays from poor visualization at any single location.'],
    ]
    seg2_table = Table(seg2, colWidths=[1.5*inch, 5.7*inch])
    seg2_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), ACCENT_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,1), (1,-1), 'Helvetica'),
        ('BACKGROUND', (0,1), (-1,-1), LIGHT_GRAY),
        ('GRID', (0,0), (-1,-1), 0.5, MEDIUM_GRAY),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(seg2_table)
    story.append(Spacer(1, 12))

    # SEGMENT 3
    story.append(Paragraph('SEGMENT 3: HOSPITALITY & RESORT DEVELOPERS', styles['SubSection']))
    seg3 = [
        ['ELEMENT', 'DETAIL'],
        ['Core Pain Point', 'Investors and lenders need to "experience" the resort/hotel concept before writing checks. '
         'A spreadsheet and site plan don\'t convey the guest experience that justifies premium pricing.'],
        ['Wrong Belief', '"Our architect\'s renderings are good enough for the investor deck." '
         'Reality: architectural renderings show structure. Investors need to feel the EXPERIENCE \xe2\x80\x94 '
         'the pool at sunset, the lobby atmosphere, the room view.'],
        ['Frustration', 'Resort projects are high-stakes ($10M-$100M+). Getting investor commitment takes '
         '12-18 months. Any tool that shortens that timeline saves massive carrying costs.'],
        ['Strategic Angle', 'Position as INVESTOR EXPERIENCE DESIGN. Create the emotional experience '
         'that turns a spreadsheet pitch into an immersive walkthrough that closes capital faster.'],
        ['Main Hook', '"Your investors can\'t feel a spreadsheet. But they can walk through this."'],
        ['Emotional Trigger', 'AMBITION and CREDIBILITY. Resort developers want to be seen as visionary. '
         'World-class visualization signals that this is a serious, well-capitalized project.'],
    ]
    seg3_table = Table(seg3, colWidths=[1.5*inch, 5.7*inch])
    seg3_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), ACCENT_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,1), (1,-1), 'Helvetica'),
        ('BACKGROUND', (0,1), (-1,-1), LIGHT_GRAY),
        ('GRID', (0,0), (-1,-1), 0.5, MEDIUM_GRAY),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(seg3_table)
    story.append(Spacer(1, 12))

    # Priority recommendation
    story.append(Paragraph('CAMPAIGN PRIORITY ORDER', styles['SubSection']))
    priority = [
        ['PRIORITY', 'SEGMENT', 'WHY', 'EST. PROJECT VALUE'],
        ['#1', 'Real Estate Developers', 'Highest volume, clearest pain, fastest close', '$8K - $50K'],
        ['#2', 'Hospitality/Resort', 'Highest ticket, investor urgency', '$15K - $80K'],
        ['#3', 'Commercial/Retail Chains', 'Repeat business, multi-location scale', '$5K - $25K per location'],
    ]
    pri_table = Table(priority, colWidths=[0.8*inch, 2*inch, 2.8*inch, 1.6*inch])
    pri_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), ACCENT_ORANGE),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('BACKGROUND', (0,1), (-1,1), HexColor('#e8f5e9')),
        ('BACKGROUND', (0,2), (-1,2), HexColor('#fff8e1')),
        ('BACKGROUND', (0,3), (-1,3), HexColor('#e3f2fd')),
        ('GRID', (0,0), (-1,-1), 0.5, MEDIUM_GRAY),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(pri_table)
    story.append(PageBreak())


def build_hooks_overview(story, styles):
    """3 Hook concepts overview"""
    story.append(Paragraph('2. THREE HOOK CONCEPTS', styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=2, color=ACCENT_ORANGE))
    story.append(Spacer(1, 10))

    story.append(Paragraph(
        'Each hook targets a different emotional trigger. We test all 3 with $3/day each '
        'for 14 days, then kill the losers and scale the winner.',
        styles['BodyText']
    ))

    hooks = [
        ['HOOK', 'ANGLE', 'EMOTIONAL TRIGGER', 'FORMATS'],
        ['Hook 1:\n"SELL BEFORE\nYOU BUILD"',
         'Pre-sales acceleration.\nShow the before/after of\nan empty lot to sold units.',
         'FEAR of carrying costs\nand unsold inventory',
         '2 single image\n+ 1 carousel\n= 3 ads'],
        ['Hook 2:\n"SEE IT BEFORE\nYOU RISK IT"',
         'Risk reduction.\nVisualize to verify before\ncommitting millions.',
         'ANXIETY about costly\nmistakes and rework',
         '2 single image\n+ 1 carousel\n= 3 ads'],
        ['Hook 3:\n"YOUR COMPETITOR\nALREADY DID THIS"',
         'Competitive urgency.\nOthers are winning deals\nyou\'re losing.',
         'FOMO and competitive\npressure',
         '2 single image\n+ 1 carousel\n= 3 ads'],
    ]
    hooks_table = Table(hooks, colWidths=[1.5*inch, 2.2*inch, 2*inch, 1.5*inch])
    hooks_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BG),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (0,1), (0,-1), GOLD),
        ('FONTNAME', (1,1), (-1,-1), 'Helvetica'),
        ('BACKGROUND', (0,1), (-1,1), HexColor('#1a1a2e10')),
        ('BACKGROUND', (0,2), (-1,2), LIGHT_GRAY),
        ('BACKGROUND', (0,3), (-1,3), HexColor('#1a1a2e10')),
        ('GRID', (0,0), (-1,-1), 0.5, MEDIUM_GRAY),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(hooks_table)
    story.append(Spacer(1, 10))

    story.append(Paragraph(
        '<b>TESTING PROTOCOL:</b> $3/day per hook x 14 days = $126 total test. '
        'After 14 days: kill lowest CTR hook, redistribute budget to top 2. '
        'After 21 days: winner gets full $9/day.',
        styles['CalloutText']
    ))
    story.append(PageBreak())


def build_ad_variant(story, styles, ad_num, hook_num, hook_name, format_type,
                     ad_name, primary_text, headline, description, cta,
                     visual_description, nano_prompt, carousel_slides=None):
    """Build a single ad variant block"""

    # Ad header
    header_data = [[f'AD #{ad_num}  |  HOOK {hook_num}: "{hook_name}"  |  {format_type}']]
    header_table = Table(header_data, colWidths=[7.2*inch])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), DARK_BG),
        ('TEXTCOLOR', (0,0), (-1,-1), GOLD),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 11),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 4))

    # Ad name
    story.append(Paragraph(f'Ad Name: {ad_name}', styles['AdName']))

    # Copy section
    story.append(Paragraph('<b>PRIMARY TEXT (above the image):</b>', styles['SmallLabel']))
    story.append(Paragraph(primary_text.replace('\n', '<br/>'), styles['AdCopy']))
    story.append(Spacer(1, 4))

    story.append(Paragraph('<b>HEADLINE (below the image, bold):</b>', styles['SmallLabel']))
    story.append(Paragraph(headline, styles['AdCopy']))
    story.append(Spacer(1, 4))

    story.append(Paragraph('<b>DESCRIPTION (below headline, gray):</b>', styles['SmallLabel']))
    story.append(Paragraph(description, styles['AdCopy']))
    story.append(Spacer(1, 4))

    story.append(Paragraph(f'<b>CTA BUTTON:</b> {cta}', styles['SmallLabel']))
    story.append(Spacer(1, 6))

    # Visual direction
    story.append(Paragraph('<b>VISUAL DIRECTION:</b>', styles['SmallLabel']))
    story.append(Paragraph(visual_description, styles['BodyText']))
    story.append(Spacer(1, 4))

    # Carousel slides if applicable
    if carousel_slides:
        story.append(Paragraph('<b>CAROUSEL SLIDES:</b>', styles['SmallLabel']))
        for i, slide in enumerate(carousel_slides, 1):
            story.append(Paragraph(
                f'<b>Slide {i}:</b> {slide}', styles['BulletText']
            ))
        story.append(Spacer(1, 4))

    # Nano Banana prompt
    story.append(Paragraph('<b>NANO BANANA PROMPT (copy-paste to generate):</b>', styles['SmallLabel']))
    if isinstance(nano_prompt, list):
        for i, p in enumerate(nano_prompt, 1):
            story.append(Paragraph(f'Slide {i}: {p}', styles['PromptText']))
    else:
        story.append(Paragraph(nano_prompt, styles['PromptText']))

    story.append(Spacer(1, 6))

    # UTM
    utm = (f'utm_source=meta&utm_medium=paid-social&'
           f'utm_campaign=rendimension_leadgen_developers&'
           f'utm_content=hook{hook_num}_{format_type.lower().replace(" ", "")}_{ad_name.split("_")[-1]}')
    story.append(Paragraph(f'<b>UTM:</b> {utm}', styles['SmallLabel']))
    story.append(Spacer(1, 15))


def build_all_ads(story, styles):
    """All 9 ad variants"""
    story.append(Paragraph('3. THE 9 ADS \xe2\x80\x94 COMPLETE COPY + VISUAL PROMPTS', styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=2, color=ACCENT_ORANGE))
    story.append(Spacer(1, 10))

    story.append(Paragraph(
        'Each ad is production-ready. Copy the primary text, generate the visual with '
        'the Nano Banana prompt, and load into Facebook Ads Manager.',
        styles['BodyText']
    ))
    story.append(Spacer(1, 6))

    # ========== HOOK 1: SELL BEFORE YOU BUILD ==========
    story.append(Paragraph('HOOK 1: "SELL BEFORE YOU BUILD"', styles['HookTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=GOLD))
    story.append(Spacer(1, 8))

    # Ad 1 - Single Image A
    build_ad_variant(story, styles,
        ad_num=1, hook_num=1, hook_name='SELL BEFORE YOU BUILD',
        format_type='SINGLE IMAGE',
        ad_name='rendimension_meta_sellbeforeyoubuild_singleimage_A',
        primary_text=(
            '60% pre-sold before groundbreaking.\n\n'
            'That\'s what happens when buyers can walk through your building before it exists.\n\n'
            'Most developers wait until construction is 50% done to start selling. '
            'By then, they\'ve been bleeding carrying costs for months.\n\n'
            'The ones closing faster? They\'re using photorealistic visualization to let '
            'buyers experience the finished product NOW.\n\n'
            'Empty lot \xe2\x86\x92 Stunning render \xe2\x86\x92 Buyer deposits \xe2\x86\x92 Construction funded.\n\n'
            'Stop selling blueprints. Start selling experiences.'
        ),
        headline='Pre-Sell Your Project Before You Pour Concrete',
        description='Photorealistic 3D visualization that turns empty lots into buyer deposits.',
        cta='Learn More',
        visual_description=(
            'Split composition: LEFT side shows a real empty lot/construction site (raw, dirt, fences). '
            'RIGHT side shows the same angle but as a stunning photorealistic render of a finished '
            'luxury condo tower with landscaping, people, and warm sunset lighting. '
            'A visible dividing line between the two halves. Clean, cinematic, no text overlay on image.'
        ),
        nano_prompt=(
            'Photorealistic architectural visualization, split-screen composition. Left half: empty '
            'construction lot with dirt, chain-link fence, raw terrain, overcast sky. Right half: same '
            'camera angle showing a completed luxury 15-story residential tower with glass facades, '
            'landscaped gardens, palm trees, people walking, warm golden hour sunset lighting. Sharp '
            'vertical dividing line between the two halves. Ultra-realistic, 8K quality, architectural '
            'photography style. Aspect ratio 1:1, 1080x1080px.'
        )
    )

    # Ad 2 - Single Image B
    build_ad_variant(story, styles,
        ad_num=2, hook_num=1, hook_name='SELL BEFORE YOU BUILD',
        format_type='SINGLE IMAGE',
        ad_name='rendimension_meta_sellbeforeyoubuild_singleimage_B',
        primary_text=(
            'A developer in Texas closed $4.2M in pre-sales with nothing but a 3D walkthrough '
            'and a sales center.\n\n'
            'No finished building. No model unit. No construction photos.\n\n'
            'Just a photorealistic visualization so real that buyers said: '
            '"When can we move in?"\n\n'
            'If you\'re still selling off floor plans and elevation drawings, '
            'you\'re leaving millions in pre-sales on the table.\n\n'
            'The building doesn\'t need to exist for people to buy it. '
            'It just needs to FEEL real.'
        ),
        headline='Your Building Doesn\'t Need to Exist to Start Selling',
        description='3D visualization so real, buyers ask when they can move in.',
        cta='Get Started',
        visual_description=(
            'Photorealistic render of a modern luxury sales center/showroom interior. '
            'Large screens on walls showing building renders. A sales agent pointing at a '
            'display board with unit layouts. Several well-dressed buyers examining the display. '
            'Some units on the board marked as "RESERVED" with red stickers. Modern, warm lighting, '
            'sleek furniture. The feeling of success and momentum.'
        ),
        nano_prompt=(
            'Photorealistic interior of a luxury real estate sales center showroom. Large wall-mounted '
            'screens displaying beautiful building renders. A sales display board showing unit floor plans '
            'with several units marked "RESERVED" with red dots. Well-dressed diverse buyers examining '
            'the displays. Modern minimalist design, warm LED lighting, polished concrete floors, '
            'sleek furniture. Feeling of success and buyer activity. Ultra-realistic, architectural '
            'photography, 8K quality. Aspect ratio 1:1, 1080x1080px.'
        )
    )

    # Ad 3 - Carousel
    carousel_1_slides = [
        'Hero shot: Empty lot with fence and dirt. Text overlay: "This is your project today."',
        'Same angle: Photorealistic render of the completed building exterior. Text: "This is what buyers will see."',
        'Interior render: Luxury lobby with concierge desk. Text: "This is what they\'ll feel."',
        'Sales center board with RESERVED stickers on 60% of units. Text: "This is what happens next."',
        'Simple dark background with white text: "Pre-sell before you pour. Get your visualization estimate." + Rendimension logo.',
    ]
    carousel_1_prompts = [
        'Aerial photo of empty construction lot, chain-link fence, dirt terrain, construction equipment in background, overcast sky. Documentary photography style. Square format 1080x1080px.',
        'Photorealistic 3D render of a modern 12-story luxury residential building with glass and white stone facade, landscaped entrance with palm trees, blue sky, people walking. Same camera angle as an aerial construction photo looking slightly down. Architectural visualization, 8K quality. Square 1080x1080px.',
        'Photorealistic interior render of a luxury apartment building lobby. Marble floors, modern concierge desk, brass accents, tall ceilings, warm lighting, a doorman greeting residents. High-end hospitality feeling. Architectural interior photography style. Square 1080x1080px.',
        'Photorealistic real estate sales display board mounted on wall showing apartment floor plan grid. 60% of units have red "RESERVED" stickers. Warm lighting, modern sales office setting. Close-up documentary style. Square 1080x1080px.',
        'DO NOT GENERATE - Create in Canva: Dark navy background (#1a1a2e), white text centered: "Pre-sell before you pour." Subtext: "Get your visualization estimate." Rendimension logo bottom center. Square 1080x1080px.',
    ]
    build_ad_variant(story, styles,
        ad_num=3, hook_num=1, hook_name='SELL BEFORE YOU BUILD',
        format_type='CAROUSEL (5 slides)',
        ad_name='rendimension_meta_sellbeforeyoubuild_carousel_A',
        primary_text=(
            'From empty lot to 60% pre-sold.\n\n'
            'Swipe to see how one developer turned dirt into deposits \xe2\x80\x94 '
            'before a single brick was laid.\n\n'
            'This is the power of photorealistic visualization. '
            'When buyers can experience your building before it exists, '
            'they don\'t wait for construction. They buy NOW.\n\n'
            '\xe2\x9e\xa1\xef\xb8\x8f Swipe to see the transformation.'
        ),
        headline='From Empty Lot to Pre-Sold in 90 Days',
        description='Photorealistic visualization that turns concepts into buyer deposits.',
        cta='Learn More',
        visual_description='5-slide story arc from empty lot to sold-out project. Each slide builds momentum.',
        carousel_slides=carousel_1_slides,
        nano_prompt=carousel_1_prompts
    )

    story.append(PageBreak())

    # ========== HOOK 2: SEE IT BEFORE YOU RISK IT ==========
    story.append(Paragraph('HOOK 2: "SEE IT BEFORE YOU RISK IT"', styles['HookTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=GOLD))
    story.append(Spacer(1, 8))

    # Ad 4 - Single Image A
    build_ad_variant(story, styles,
        ad_num=4, hook_num=2, hook_name='SEE IT BEFORE YOU RISK IT',
        format_type='SINGLE IMAGE',
        ad_name='rendimension_meta_seeitbeforeyouriskit_singleimage_A',
        primary_text=(
            'A $2.3M mistake.\n\n'
            'That\'s what a hotel developer in Florida spent fixing design decisions '
            'that "looked fine on paper."\n\n'
            'The lobby felt cramped. The pool area had no shade after 2pm. '
            'The guest rooms had zero ocean view from 40% of units.\n\n'
            'All things that would\'ve been obvious in a 3D walkthrough. '
            'All things that cost millions to fix after concrete was poured.\n\n'
            'You can\'t un-pour concrete. But you CAN walk through your building '
            'before it exists.\n\n'
            'See every angle. Test every decision. Fix every problem. '
            'BEFORE the first dollar of construction.'
        ),
        headline='Walk Through Your Building Before It Exists',
        description='Find the $2M mistakes before they become $2M mistakes.',
        cta='Learn More',
        visual_description=(
            'Dramatic image: A VR headset sitting on top of architectural blueprints and construction '
            'documents on a large desk. In the reflection/screens of the VR headset, you can see a '
            'beautiful photorealistic building interior. The contrast between flat paper plans and '
            'immersive 3D visualization. Moody, professional lighting.'
        ),
        nano_prompt=(
            'A modern VR headset placed on top of scattered architectural blueprints and construction '
            'documents on a dark wood executive desk. In the lenses of the VR headset, there is a '
            'reflection showing a beautiful photorealistic luxury hotel lobby interior. Dramatic '
            'professional lighting from a desk lamp, creating contrast between the flat 2D blueprints '
            'and the immersive 3D experience. Cinematic photography, shallow depth of field, 8K quality. '
            'Aspect ratio 1:1, 1080x1080px.'
        )
    )

    # Ad 5 - Single Image B
    build_ad_variant(story, styles,
        ad_num=5, hook_num=2, hook_name='SEE IT BEFORE YOU RISK IT',
        format_type='SINGLE IMAGE',
        ad_name='rendimension_meta_seeitbeforeyouriskit_singleimage_B',
        primary_text=(
            'What if you could walk through every room, test every layout, '
            'and verify every design decision...\n\n'
            'BEFORE spending a single dollar on construction?\n\n'
            'That\'s not future tech. That\'s what developers are doing right now.\n\n'
            'Photorealistic 3D visualization lets you:\n'
            '\xe2\x9c\x93 Catch design flaws before they become change orders\n'
            '\xe2\x9c\x93 Get investor approval in one meeting, not five\n'
            '\xe2\x9c\x93 Pre-sell units to buyers who "need to see it first"\n'
            '\xe2\x9c\x93 Align your entire team on the vision\n\n'
            'Construction is irreversible. Your visualization doesn\'t have to be.'
        ),
        headline='Catch the $500K Mistake Before You Make It',
        description='Photorealistic 3D that reveals problems blueprints hide.',
        cta='Get Started',
        visual_description=(
            'Side-by-side comparison: LEFT shows a traditional architectural cross-section drawing '
            '(technical, cold, hard to read). RIGHT shows the same space as a warm, inviting '
            'photorealistic 3D render (a hotel room with ocean view, warm lighting, textured materials). '
            'The contrast should make the blueprint look inadequate. An arrow or transition effect '
            'between the two.'
        ),
        nano_prompt=(
            'Split-screen architectural comparison. Left side: cold technical architectural blueprint '
            'cross-section of a hotel room, black and white line drawing, sterile and hard to read. '
            'Right side: the same hotel room as a photorealistic 3D render with warm lighting, ocean '
            'view through large windows, textured wood floors, luxury bedding, afternoon sunlight streaming '
            'in. Dramatic visual contrast between technical drawing and emotional reality. Architectural '
            'visualization, 8K quality. Aspect ratio 1:1, 1080x1080px.'
        )
    )

    # Ad 6 - Carousel
    carousel_2_slides = [
        'Blueprint of a hotel lobby, cold and technical. Text overlay: "This is what your architect shows you."',
        'Same lobby as a photorealistic 3D render, warm and inviting. Text: "This is what your guests will actually experience."',
        'A person wearing a VR headset standing in an empty warehouse space, but overlaid/ghosted in is the luxury interior they\'re seeing. Text: "Walk every room before it\'s built."',
        'Construction photo showing workers fixing a major design error (demolition/rebuild). Text: "Or fix it after. Your choice."',
        'Dark background, white text: "See it before you risk it. Get a walkthrough estimate." + Rendimension logo.',
    ]
    carousel_2_prompts = [
        'Technical architectural blueprint drawing of a hotel lobby floor plan, black and white engineering drawing, cold overhead lighting on drafting table. Professional but sterile. Documentary photography style. Square 1080x1080px.',
        'Photorealistic 3D render of a luxury hotel lobby with double-height ceiling, marble floors, modern reception desk, brass light fixtures, green plant wall, warm golden lighting, guests checking in. High-end hospitality design. Architectural visualization. Square 1080x1080px.',
        'A business professional wearing a modern VR headset standing in a raw concrete commercial space. Semi-transparent overlay showing the luxury finished interior they are seeing through the headset \xe2\x80\x94 furniture, lighting, finishes ghosted over the raw space. Cinematic, dramatic lighting. Square 1080x1080px.',
        'Construction site interior showing workers demolishing a recently built wall to fix a design error. Dust, debris, hard hats, frustrated project manager holding blueprints. Documentary construction photography. Square 1080x1080px.',
        'DO NOT GENERATE - Create in Canva: Dark navy background (#1a1a2e), white text: "See it before you risk it." Subtext: "Get a walkthrough estimate." Rendimension logo. Square 1080x1080px.',
    ]
    build_ad_variant(story, styles,
        ad_num=6, hook_num=2, hook_name='SEE IT BEFORE YOU RISK IT',
        format_type='CAROUSEL (5 slides)',
        ad_name='rendimension_meta_seeitbeforeyouriskit_carousel_A',
        primary_text=(
            'Your architect shows you blueprints.\n'
            'Your buyers see... nothing.\n\n'
            'Swipe to see the gap between what you\'re showing stakeholders '
            'and what they actually need to see to say YES.\n\n'
            'The $500K question: would you rather find the problem '
            'in a 3D walkthrough or in a demolition invoice?\n\n'
            '\xe2\x9e\xa1\xef\xb8\x8f Swipe to see the difference.'
        ),
        headline='The Gap Between Blueprints and Reality',
        description='Find the problems before they become change orders.',
        cta='Learn More',
        visual_description='5-slide story from blueprint to photorealistic to VR to the cost of NOT doing it.',
        carousel_slides=carousel_2_slides,
        nano_prompt=carousel_2_prompts
    )

    story.append(PageBreak())

    # ========== HOOK 3: YOUR COMPETITOR ALREADY DID THIS ==========
    story.append(Paragraph('HOOK 3: "YOUR COMPETITOR ALREADY DID THIS"', styles['HookTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=GOLD))
    story.append(Spacer(1, 8))

    # Ad 7 - Single Image A
    build_ad_variant(story, styles,
        ad_num=7, hook_num=3, hook_name='YOUR COMPETITOR ALREADY DID THIS',
        format_type='SINGLE IMAGE',
        ad_name='rendimension_meta_competitordidit_singleimage_A',
        primary_text=(
            'While you\'re emailing PDFs of floor plans to investors...\n\n'
            'Your competitor just sent them an immersive 3D walkthrough '
            'of their project.\n\n'
            'They\'re walking through the penthouse. Checking the lobby. '
            'Feeling the pool deck at sunset. All from their laptop.\n\n'
            'And when it\'s time to choose which project gets funded?\n\n'
            'The one they can SEE always beats the one they have to IMAGINE.\n\n'
            'The question isn\'t whether visualization works. '
            'It\'s whether you\'ll use it before your competition takes '
            'every investor in your market.'
        ),
        headline='Your Competitors Are Already Showing. Are You Still Telling?',
        description='Don\'t let a competitor\'s render win your investor\'s check.',
        cta='Learn More',
        visual_description=(
            'An investor/executive sitting at a desk with TWO project presentations in front of them. '
            'On the LEFT: a stack of paper documents, floor plans, spreadsheets (boring, flat). '
            'On the RIGHT: a laptop showing a stunning photorealistic building render (exciting, vivid). '
            'The executive is clearly reaching toward/leaning toward the laptop side. '
            'The visual metaphor of which project wins.'
        ),
        nano_prompt=(
            'A corporate executive in a modern office sitting at a desk looking at two project presentations. '
            'Left side of desk: a messy stack of paper documents, printed floor plans, and spreadsheets, '
            'looking outdated and unimpressive. Right side: a sleek laptop displaying a stunning photorealistic '
            '3D render of a luxury building with glass facades and sunset lighting. The executive is leaning '
            'toward the laptop, clearly drawn to the visual presentation. Professional office setting, '
            'dramatic lighting emphasizing the contrast. Cinematic photography, 8K quality. Aspect ratio '
            '1:1, 1080x1080px.'
        )
    )

    # Ad 8 - Single Image B
    build_ad_variant(story, styles,
        ad_num=8, hook_num=3, hook_name='YOUR COMPETITOR ALREADY DID THIS',
        format_type='SINGLE IMAGE',
        ad_name='rendimension_meta_competitordidit_singleimage_B',
        primary_text=(
            'Two developers. Same city. Same type of project.\n\n'
            'Developer A: Sends investors a 40-page PDF with floor plans, '
            'financial projections, and architectural drawings.\n\n'
            'Developer B: Sends investors a link to walk through the entire '
            'building in photorealistic 3D. Every unit. Every amenity. '
            'Every finish.\n\n'
            'Developer B closed their funding round in 6 weeks.\n'
            'Developer A is still waiting.\n\n'
            'Same project quality. Different presentation.\n'
            'Guess which one wins every time?'
        ),
        headline='Same Project. Different Presentation. Different Result.',
        description='The developer with better visualization wins the deal. Every time.',
        cta='Get Started',
        visual_description=(
            'Two smartphones or screens side by side. LEFT screen shows a boring PDF document '
            'with floor plans and text (Developer A). RIGHT screen shows an immersive, beautiful '
            '3D walkthrough of a luxury building interior (Developer B). A subtle "VS" or dividing '
            'element between them. Modern, clean layout.'
        ),
        nano_prompt=(
            'Two modern smartphones placed side by side on a dark marble surface. Left phone screen '
            'shows a boring black and white PDF document with tiny floor plans and dense text. Right '
            'phone screen shows a stunning photorealistic 3D interior render of a luxury penthouse '
            'with floor-to-ceiling windows, city skyline view, warm lighting. Strong visual contrast '
            'between boring PDF and immersive visualization. Overhead product photography, dramatic '
            'lighting, 8K quality. Aspect ratio 1:1, 1080x1080px.'
        )
    )

    # Ad 9 - Carousel
    carousel_3_slides = [
        'Text-heavy slide: "Developer A sent investors a 40-page PDF." (Show a thick PDF document, boring)',
        'Text-heavy slide: "Developer B sent investors THIS." (Show stunning building render on a laptop screen)',
        'Interior walkthrough render: luxury lobby from the investor\'s perspective. Text: "Walk through every floor. Every unit. Every amenity."',
        'Show a handshake closing a deal with the building render visible on a screen behind them. Text: "Developer B closed funding in 6 weeks."',
        'Dark background: "Don\'t be Developer A. Get your visualization estimate." + Rendimension logo.',
    ]
    carousel_3_prompts = [
        'A thick stack of printed documents, PDFs, and spreadsheets spread messily on a conference table. Boring corporate presentation materials. Overhead flat lay photography, fluorescent office lighting. Uninspiring and bureaucratic feeling. Square 1080x1080px.',
        'A sleek laptop on a clean executive desk displaying a stunning photorealistic 3D render of a modern luxury mixed-use development with glass towers, retail podium, landscaped plaza, sunset lighting. The screen glows with quality. Professional product photography. Square 1080x1080px.',
        'First-person perspective photorealistic 3D render walking through a luxury building lobby. Double-height ceiling, marble floors, brass elevator doors, modern art on walls, concierge desk. As if the viewer is an investor touring the building. Immersive architectural visualization. Square 1080x1080px.',
        'Two business professionals shaking hands in a modern office. Behind them, a large wall-mounted screen shows a photorealistic building render. Celebratory, deal-closing atmosphere. Professional corporate photography. Square 1080x1080px.',
        'DO NOT GENERATE - Create in Canva: Dark navy background (#1a1a2e), white text: "Don\'t be Developer A." Subtext: "Get your visualization estimate." Rendimension logo. Square 1080x1080px.',
    ]
    build_ad_variant(story, styles,
        ad_num=9, hook_num=3, hook_name='YOUR COMPETITOR ALREADY DID THIS',
        format_type='CAROUSEL (5 slides)',
        ad_name='rendimension_meta_competitordidit_carousel_A',
        primary_text=(
            'Two developers. Same city. Same budget. Very different results.\n\n'
            'Swipe to see why Developer B closed funding in 6 weeks '
            'while Developer A is still emailing PDFs.\n\n'
            'Hint: it has nothing to do with their project quality.\n\n'
            '\xe2\x9e\xa1\xef\xb8\x8f Swipe to see the difference.'
        ),
        headline='Why Developer B Always Wins',
        description='Same project. Better visualization. Faster funding.',
        cta='Learn More',
        visual_description='5-slide story comparing Developer A (PDFs) vs Developer B (3D visualization).',
        carousel_slides=carousel_3_slides,
        nano_prompt=carousel_3_prompts
    )

    story.append(PageBreak())


def build_heygen_scripts(story, styles):
    """HeyGen video ad scripts"""
    story.append(Paragraph('4. HEYGEN VIDEO ADS (BONUS)', styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=2, color=ACCENT_ORANGE))
    story.append(Spacer(1, 10))

    story.append(Paragraph(
        'Two video ads using HeyGen avatars. These can run as Reels or Stories. '
        'Generate after testing the static ads \xe2\x80\x94 add them in Week 3 if statics '
        'show promise.',
        styles['BodyText']
    ))
    story.append(Spacer(1, 8))

    # Video 1
    story.append(Paragraph('VIDEO AD 1: "The $2M Mistake" (30 seconds)', styles['SubSection']))
    v1_data = [
        ['TIMING', 'VISUAL', 'SCRIPT (AVATAR SPEAKS)'],
        ['0-5s', 'Avatar appears, concerned face.\nConstruction site B-roll behind.',
         '"A hotel developer spent $2.3 million fixing design mistakes that looked fine on paper."'],
        ['5-12s', 'Blueprint transitions to 3D render\n(screen recording or B-roll).',
         '"The lobby was too small. The pool had no shade after 2pm. Forty percent of rooms had no ocean view."'],
        ['12-20s', 'VR headset walkthrough footage\nor immersive 3D render shots.',
         '"All of this would have been obvious in a 3D walkthrough. But they poured concrete first."'],
        ['20-27s', 'Avatar direct to camera.\nSplit screen: blueprint vs render.',
         '"What if you could walk through every room, test every decision, before spending a single dollar on construction?"'],
        ['27-30s', 'Rendimension logo + CTA.\nDark background.',
         '"See it before you risk it. Link in bio."'],
    ]
    v1_table = Table(v1_data, colWidths=[0.7*inch, 2.3*inch, 4.2*inch])
    v1_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), ACCENT_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('BACKGROUND', (0,1), (-1,-1), LIGHT_GRAY),
        ('GRID', (0,0), (-1,-1), 0.5, MEDIUM_GRAY),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(v1_table)
    story.append(Spacer(1, 15))

    # Video 2
    story.append(Paragraph('VIDEO AD 2: "Developer A vs Developer B" (25 seconds)', styles['SubSection']))
    v2_data = [
        ['TIMING', 'VISUAL', 'SCRIPT (AVATAR SPEAKS)'],
        ['0-5s', 'Avatar appears with two screens\nbehind them.',
         '"Two developers. Same city. Same budget. Only one got funded in 6 weeks."'],
        ['5-12s', 'LEFT screen: boring PDF.\nRIGHT screen: stunning 3D render.',
         '"Developer A emailed investors a 40-page PDF. Developer B sent them a 3D walkthrough of the entire building."'],
        ['12-18s', 'Walkthrough footage or render\nslideshow of luxury interiors.',
         '"Investors walked through every unit, every amenity, every finish. From their laptop."'],
        ['18-22s', 'Avatar direct to camera.\nConfident, challenging tone.',
         '"The developer with better visualization wins the deal. Every single time."'],
        ['22-25s', 'Rendimension logo + CTA.\nDark background.',
         '"Don\'t be Developer A. Link in bio."'],
    ]
    v2_table = Table(v2_data, colWidths=[0.7*inch, 2.3*inch, 4.2*inch])
    v2_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), ACCENT_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('BACKGROUND', (0,1), (-1,-1), LIGHT_GRAY),
        ('GRID', (0,0), (-1,-1), 0.5, MEDIUM_GRAY),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(v2_table)

    story.append(Spacer(1, 10))
    story.append(Paragraph(
        '<b>HEYGEN SETTINGS:</b> Professional male/female avatar, business casual, '
        'solid or gradient background, confident tone, moderate pace. '
        'Add B-roll of renders during narration for visual variety.',
        styles['CalloutText']
    ))

    story.append(PageBreak())


def build_campaign_structure(story, styles):
    """Facebook campaign structure"""
    story.append(Paragraph('5. CAMPAIGN STRUCTURE IN ADS MANAGER', styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=2, color=ACCENT_ORANGE))
    story.append(Spacer(1, 10))

    # Campaign level
    story.append(Paragraph('CAMPAIGN LEVEL', styles['SubSection']))
    camp_data = [
        ['SETTING', 'VALUE'],
        ['Campaign Name', 'rendimension_meta_leadgen_developers_20260317'],
        ['Objective', 'Leads (Lead Generation)'],
        ['Campaign Budget', 'Advantage Campaign Budget (CBO): $9/day'],
        ['Bid Strategy', 'Lowest Cost (let Facebook optimize)'],
        ['Special Ad Categories', 'None (archviz is NOT housing ads)'],
    ]
    camp_table = Table(camp_data, colWidths=[2*inch, 5.2*inch])
    camp_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), ACCENT_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,1), (1,-1), 'Helvetica'),
        ('BACKGROUND', (0,1), (-1,-1), LIGHT_GRAY),
        ('GRID', (0,0), (-1,-1), 0.5, MEDIUM_GRAY),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(camp_table)
    story.append(Spacer(1, 12))

    # Ad Set level
    story.append(Paragraph('AD SET LEVEL (ONE AD SET FOR ALL 9 ADS)', styles['SubSection']))
    adset_data = [
        ['SETTING', 'VALUE'],
        ['Ad Set Name', 'rendimension_meta_developers-national_mixed_v01'],
        ['Conversion Location', 'Instant Forms (Lead Gen Forms)'],
        ['Optimization', 'Leads'],
        ['Performance Goal', 'Maximize number of leads'],
        ['Schedule', 'Start date: when ready | No end date'],
        ['', ''],
        ['AUDIENCE TARGETING', ''],
        ['Location', 'United States (all)'],
        ['Age', '30 - 60'],
        ['Gender', 'All'],
        ['', ''],
        ['Detailed Targeting:', ''],
        ['Job Titles', 'Real estate developer, Property developer, Land developer,\n'
         'VP of Development, Director of Construction,\n'
         'Director of Real Estate, Chief Development Officer'],
        ['Industries', 'Real estate development, Commercial real estate,\n'
         'Construction, Hospitality, Retail (corporate)'],
        ['Interests', 'Real estate investing, Commercial construction,\n'
         'Property development, Architecture, 3D visualization,\n'
         'Virtual reality, Building design'],
        ['Behaviors', 'Business page admins, Small business owners,\n'
         'Corporate executives'],
        ['', ''],
        ['PLACEMENTS', ''],
        ['Platforms', 'Facebook Feed, Instagram Feed, Instagram Stories,\n'
         'Instagram Reels, Facebook Marketplace'],
        ['Excluded', 'Audience Network, Messenger (low quality clicks)'],
    ]
    adset_table = Table(adset_data, colWidths=[2*inch, 5.2*inch])
    adset_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), ACCENT_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,1), (1,-1), 'Helvetica'),
        ('BACKGROUND', (0,1), (-1,-1), LIGHT_GRAY),
        ('BACKGROUND', (0,7), (-1,7), HexColor('#e3f2fd')),
        ('BACKGROUND', (0,12), (-1,12), HexColor('#e3f2fd')),
        ('BACKGROUND', (0,19), (-1,19), HexColor('#e3f2fd')),
        ('GRID', (0,0), (-1,-1), 0.5, MEDIUM_GRAY),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(adset_table)
    story.append(Spacer(1, 12))

    # Estimated audience size
    story.append(Paragraph(
        '<b>ESTIMATED AUDIENCE SIZE:</b> With this targeting, expect 800K - 2M people. '
        'That\'s plenty for $9/day. Facebook will optimize within this pool to find '
        'the most likely converters.',
        styles['CalloutText']
    ))

    story.append(PageBreak())

    # Lead Gen Form
    story.append(Paragraph('LEAD GEN FORM SETUP', styles['SubSection']))
    story.append(Spacer(1, 6))

    form_data = [
        ['ELEMENT', 'CONTENT'],
        ['Form Name', 'rendimension_leadform_preconstruction_v01'],
        ['Form Type', 'More Volume (pre-filled, fewer friction)'],
        ['Headline', 'Get Your Pre-Construction Visualization Estimate'],
        ['Description', 'Tell us about your project and we\'ll show you how\n'
         'photorealistic 3D visualization can accelerate your pre-sales.'],
        ['', ''],
        ['FORM FIELDS:', ''],
        ['Field 1', 'Full Name (pre-filled from Facebook)'],
        ['Field 2', 'Email (pre-filled from Facebook)'],
        ['Field 3', 'Phone Number (pre-filled from Facebook)'],
        ['Field 4', 'Custom: "What type of project?"\n'
         'Dropdown: Residential / Commercial / Hospitality / Retail / Mixed-Use / Other'],
        ['Field 5', 'Custom: "Project stage?"\n'
         'Dropdown: Concept / Design Development / Pre-Construction / Under Construction'],
        ['', ''],
        ['THANK YOU SCREEN:', ''],
        ['Headline', 'We\'ll Be in Touch Within 24 Hours'],
        ['Description', 'Our team will review your project details and send you\n'
         'a custom visualization estimate.'],
        ['Button', 'Visit Our Portfolio (links to rendimension.com)'],
    ]
    form_table = Table(form_data, colWidths=[2*inch, 5.2*inch])
    form_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), GREEN),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,1), (1,-1), 'Helvetica'),
        ('BACKGROUND', (0,1), (-1,-1), LIGHT_GRAY),
        ('BACKGROUND', (0,6), (-1,6), HexColor('#e8f5e9')),
        ('BACKGROUND', (0,13), (-1,13), HexColor('#e8f5e9')),
        ('GRID', (0,0), (-1,-1), 0.5, MEDIUM_GRAY),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(form_table)

    story.append(PageBreak())


def build_testing_protocol(story, styles):
    """Testing and optimization protocol"""
    story.append(Paragraph('6. TESTING & OPTIMIZATION PROTOCOL', styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=2, color=ACCENT_ORANGE))
    story.append(Spacer(1, 10))

    # Timeline
    story.append(Paragraph('14-DAY TESTING TIMELINE', styles['SubSection']))

    timeline_data = [
        ['DAYS', 'ACTION', 'DETAILS'],
        ['Days 1-3', 'HANDS OFF', 'Facebook is learning. Do NOT touch anything.\n'
         'The algorithm needs data to optimize delivery.\n'
         'Expect high CPL and low CTR \xe2\x80\x94 this is normal.'],
        ['Days 4-7', 'MONITOR ONLY', 'Check metrics daily but make NO changes.\n'
         'Look for: Which hook gets most clicks?\n'
         'Which ad has highest CTR? Any leads yet?'],
        ['Day 7', 'FIRST CHECK', 'If a hook has CTR < 0.5% after 1,000+ impressions: KILL IT.\n'
         'Redistribute its $3/day to the remaining hooks.\n'
         'If all 3 hooks are above 0.5% CTR: keep running.'],
        ['Days 8-14', 'OPTIMIZE', 'Kill underperforming individual ads within each hook.\n'
         'Single image vs carousel: which format wins?\n'
         'Start identifying the winning hook.'],
        ['Day 14', 'DECISION DAY', 'One hook wins. Give it $6/day.\n'
         'Second hook gets $3/day (if above benchmark).\n'
         'Third hook: kill unless surprising data.\n'
         'Create 2 new ad variants for the winning hook.'],
    ]
    timeline_table = Table(timeline_data, colWidths=[1*inch, 1.5*inch, 4.7*inch])
    timeline_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BG),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('FONTNAME', (0,1), (1,-1), 'Helvetica-Bold'),
        ('FONTNAME', (2,1), (2,-1), 'Helvetica'),
        ('BACKGROUND', (0,1), (-1,1), HexColor('#ffebee')),
        ('BACKGROUND', (0,2), (-1,2), HexColor('#fff8e1')),
        ('BACKGROUND', (0,3), (-1,3), HexColor('#e8f5e9')),
        ('BACKGROUND', (0,4), (-1,4), HexColor('#e3f2fd')),
        ('BACKGROUND', (0,5), (-1,5), HexColor('#f3e5f5')),
        ('GRID', (0,0), (-1,-1), 0.5, MEDIUM_GRAY),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(timeline_table)
    story.append(Spacer(1, 12))

    # Kill/Scale benchmarks
    story.append(Paragraph('WHEN TO KILL vs SCALE', styles['SubSection']))
    ks_data = [
        ['METRIC', 'KILL (RED)', 'WATCH (YELLOW)', 'SCALE (GREEN)'],
        ['CTR', '< 0.5%', '0.5% - 2%', '> 2%'],
        ['CPC', '> $5', '$2 - $5', '< $2'],
        ['CPL', '> $150', '$80 - $150', '< $80'],
        ['Frequency', '> 5 with declining CTR', '3 - 5', '< 3'],
        ['Relevance Score', '< 4', '4 - 7', '> 7'],
    ]
    ks_table = Table(ks_data, colWidths=[1.5*inch, 1.8*inch, 1.8*inch, 1.8*inch])
    ks_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BG),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,1), (-1,-1), 'Helvetica'),
        ('BACKGROUND', (1,1), (1,-1), HexColor('#ffcdd2')),
        ('BACKGROUND', (2,1), (2,-1), HexColor('#fff9c4')),
        ('BACKGROUND', (3,1), (3,-1), HexColor('#c8e6c9')),
        ('ALIGN', (1,0), (-1,-1), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 0.5, MEDIUM_GRAY),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(ks_table)

    story.append(Spacer(1, 12))

    story.append(Paragraph(
        '<b>BUDGET SCALING RULE:</b> When a hook/ad hits GREEN on CPL for 7+ consecutive '
        'days, increase budget by 20% max. Wait 3-4 days between increases. '
        'Never increase more than 20% at once \xe2\x80\x94 it resets the learning phase.',
        styles['CalloutText']
    ))

    story.append(PageBreak())


def build_quick_reference(story, styles):
    """Quick reference summary page"""
    story.append(Paragraph('7. QUICK REFERENCE \xe2\x80\x94 ALL 9 ADS AT A GLANCE', styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=2, color=ACCENT_ORANGE))
    story.append(Spacer(1, 10))

    summary_data = [
        ['#', 'HOOK', 'FORMAT', 'HEADLINE', 'AD NAME SUFFIX'],
        ['1', 'Sell Before\nYou Build', 'Single Image', 'Pre-Sell Your Project\nBefore You Pour Concrete', '_singleimage_A'],
        ['2', 'Sell Before\nYou Build', 'Single Image', 'Your Building Doesn\'t Need\nto Exist to Start Selling', '_singleimage_B'],
        ['3', 'Sell Before\nYou Build', 'Carousel (5)', 'From Empty Lot to\nPre-Sold in 90 Days', '_carousel_A'],
        ['4', 'See It Before\nYou Risk It', 'Single Image', 'Walk Through Your Building\nBefore It Exists', '_singleimage_A'],
        ['5', 'See It Before\nYou Risk It', 'Single Image', 'Catch the $500K Mistake\nBefore You Make It', '_singleimage_B'],
        ['6', 'See It Before\nYou Risk It', 'Carousel (5)', 'The Gap Between\nBlueprints and Reality', '_carousel_A'],
        ['7', 'Your Competitor\nAlready Did This', 'Single Image', 'Your Competitors Are Showing.\nAre You Still Telling?', '_singleimage_A'],
        ['8', 'Your Competitor\nAlready Did This', 'Single Image', 'Same Project. Different\nPresentation. Different Result.', '_singleimage_B'],
        ['9', 'Your Competitor\nAlready Did This', 'Carousel (5)', 'Why Developer B\nAlways Wins', '_carousel_A'],
    ]
    sum_table = Table(summary_data, colWidths=[0.4*inch, 1.3*inch, 1.1*inch, 2.5*inch, 1.9*inch])
    sum_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BG),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('BACKGROUND', (0,1), (-1,3), HexColor('#e8f5e9')),
        ('BACKGROUND', (0,4), (-1,6), HexColor('#e3f2fd')),
        ('BACKGROUND', (0,7), (-1,9), HexColor('#fff8e1')),
        ('GRID', (0,0), (-1,-1), 0.5, MEDIUM_GRAY),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(sum_table)
    story.append(Spacer(1, 15))

    # Checklist
    story.append(Paragraph('LAUNCH CHECKLIST', styles['SubSection']))
    checklist = [
        'Generate 6 single images with Nano Banana (use prompts from Section 3)',
        'Generate 3 x 5 carousel slides = 15 images (use prompts from Section 3)',
        'Create 3 CTA slides in Canva (dark background, white text, logo)',
        'Set up Campaign in Ads Manager (use settings from Section 5)',
        'Create Lead Gen Form (use fields from Section 5)',
        'Upload all 9 ads with correct copy from Section 3',
        'Set UTM parameters on each ad',
        'Review everything one final time',
        'Turn ON \xe2\x80\x94 then HANDS OFF for 3 days',
        '(Optional) Generate HeyGen videos for Week 3',
    ]
    for i, item in enumerate(checklist, 1):
        box = '\xe2\x98\x90'
        story.append(Paragraph(f'{box}  {i}. {item}', styles['BodyText']))

    story.append(Spacer(1, 20))

    # Final note
    final_data = [[
        Paragraph(
            '<b>TOTAL ASSETS TO GENERATE:</b><br/>'
            '\xe2\x80\xa2 6 single images (Nano Banana)<br/>'
            '\xe2\x80\xa2 12 carousel images (Nano Banana) + 3 CTA slides (Canva)<br/>'
            '\xe2\x80\xa2 2 video scripts (HeyGen, optional Week 3)<br/><br/>'
            '<b>TOTAL INVESTMENT:</b> $9/day = $126 for 14-day test<br/>'
            '<b>EXPECTED RESULTS:</b> 3-10 leads in first 14 days<br/>'
            '<b>GOAL:</b> Identify winning hook, then scale',
            styles['BodyText']
        )
    ]]
    final_table = Table(final_data, colWidths=[7.2*inch])
    final_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), HexColor('#e8f5e9')),
        ('BOX', (0,0), (-1,-1), 2, GREEN),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 15),
    ]))
    story.append(final_table)


def main():
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, 'rendimension_campaign_package_20260317.pdf')

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )

    styles = create_styles()
    story = []

    # Build all sections
    build_cover(story, styles)
    build_positioning(story, styles)
    build_hooks_overview(story, styles)
    build_all_ads(story, styles)
    build_heygen_scripts(story, styles)
    build_campaign_structure(story, styles)
    build_testing_protocol(story, styles)
    build_quick_reference(story, styles)

    # Build PDF
    doc.build(story)
    print(f"PDF generated: {output_path}")

    # Verify
    try:
        from pypdf import PdfReader
        reader = PdfReader(output_path)
        print(f"Pages: {len(reader.pages)}")
        print(f"File size: {os.path.getsize(output_path) / 1024:.0f} KB")
    except ImportError:
        print("pypdf not available for verification")


if __name__ == '__main__':
    main()
