# HubSpot CRM Pipeline Setup Guide
## Rendimension Sales Pipeline Configuration

**Prepared:** 2026-03-20  
**For:** Rendimension (rendimension.com)  
**HubSpot Account:** rendimension@gmail.com  
**Account ID:** 244106412

---

## Executive Summary

HubSpot pipelines and deal stages are configured at the account-level admin settings and are not available through the current HubSpot MCP API integration. This guide provides step-by-step manual configuration to establish the Rendimension sales pipeline.

**Status:** Requires manual setup in HubSpot UI (5-10 minutes)  
**Recommendation:** Complete this setup before automating deal workflows or launching lead nurturing sequences.

---

## Pipeline to Create: "Rendimension Pipeline"

### Pipeline Structure

| Stage | Win Probability | Description |
|-------|-----------------|-------------|
| **New Lead** | 0% | Initial inquiry captured; no qualification yet |
| **Discovery Call Scheduled** | 10% | Lead has booked or confirmed discovery call |
| **Quote Sent** | 30% | Proposal/quote delivered to prospect |
| **Quote Follow-up** | 50% | Following up on sent quote; gathering feedback |
| **Negotiation** | 70% | Active negotiation on terms, scope, or pricing |
| **Closed Won** | 100% | Deal closed; contract signed |
| **Closed Lost** | 0% | Deal lost to competitor or disqualified |

---

## Step-by-Step Setup Instructions

### Part 1: Create the Pipeline

1. **Log into HubSpot**
   - Go to: https://app.hubspot.com
   - Sign in with: rendimension@gmail.com

2. **Navigate to Deal Pipelines**
   - Click **Settings** (gear icon, bottom left of sidebar)
   - Under "Objects" section, click **Pipelines**
   - OR: Search for "Pipelines" in the settings search bar

3. **Create New Pipeline**
   - Click **"Create pipeline"** button (top right)
   - **Pipeline Name:** "Rendimension Pipeline"
   - **Description:** "Sales pipeline for architectural visualization and 3D rendering projects"
   - Click **Create**

### Part 2: Add Pipeline Stages

Once the pipeline is created, you'll be taken to the stage configuration page.

**Remove default stages** (if any pre-populated), then **add these stages in order:**

#### Stage 1: New Lead
- **Stage Name:** New Lead
- **Win Probability:** 0%
- **Description:** "Initial inquiry captured through website, email, or referral. Prospect has not yet been qualified or contacted."
- **Add Stage**

#### Stage 2: Discovery Call Scheduled
- **Stage Name:** Discovery Call Scheduled
- **Win Probability:** 10%
- **Description:** "Prospect has confirmed a call with the Rendimension team to discuss project needs, timeline, and budget."
- **Add Stage**

#### Stage 3: Quote Sent
- **Stage Name:** Quote Sent
- **Win Probability:** 30%
- **Description:** "Customized proposal/quote has been delivered to the prospect with scope, timeline, and pricing."
- **Add Stage**

#### Stage 4: Quote Follow-up
- **Stage Name:** Quote Follow-up
- **Win Probability:** 50%
- **Description:** "Actively following up on sent quote. Gathering feedback, addressing questions, or awaiting prospect decision."
- **Add Stage**

#### Stage 5: Negotiation
- **Stage Name:** Negotiation
- **Win Probability:** 70%
- **Description:** "Prospect is interested. Active negotiation on project scope, deliverables, timeline, or pricing terms."
- **Add Stage**

#### Stage 6: Closed Won
- **Stage Name:** Closed Won
- **Win Probability:** 100%
- **Description:** "Contract signed. Project is confirmed and moving into project initiation phase."
- **Add Stage**

#### Stage 7: Closed Lost
- **Stage Name:** Closed Lost
- **Win Probability:** 0%
- **Description:** "Deal lost. Prospect chose competitor, disqualified, or project cancelled."
- **Add Stage**

### Part 3: Set as Default Pipeline (Optional)

1. After all stages are added, check if this pipeline should be the **default** when creating new deals
2. Look for **"Default for new deals"** toggle on the pipeline settings page
3. If this is your primary sales pipeline, enable this toggle
4. **Save** all changes

---

## HubSpot Objects Configuration Needed

Beyond the pipeline, you'll want to set up deal properties to capture key project information:

### Recommended Deal Properties

Create or configure these custom deal fields in HubSpot:

| Property Name | Type | Required | Purpose |
|---------------|------|----------|---------|
| Project Type | Dropdown | Yes | Residential, Commercial, Mixed-Use, Hospitality, Master Plan, Other |
| Project Budget | Number | Yes | Dollar amount for rendering project |
| Timeline to Launch | Dropdown | Yes | 0-30 days, 30-60 days, 60-90 days, 90+ days |
| Number of Renderings | Number | No | Estimate of rendering deliverables needed |
| Decision Maker | Text | No | Primary contact name/role |
| Competitors Involved | Text | No | Note if other render studios are being considered |
| Project Status | Dropdown | No | Concept, Design Development, Construction Docs, Other |
| Next Steps | Text | No | What needs to happen next |
| Deal Notes | Text Area | No | Internal notes for the sales team |

**How to Add Custom Properties:**

1. Go to **Settings > Data Management > Properties**
2. Click **"Create property"**
3. Select **Deals** as the object type
4. Fill in property name, field type, and required/optional
5. Click **Create**
6. Repeat for each property listed above

---

## Automation & Workflows (Optional Next Steps)

Once the pipeline is created, consider these automations:

### Workflow 1: New Deal Notification
- **Trigger:** Deal created in "New Lead" stage
- **Action:** Notify assigned sales rep via email or internal notification
- **Owner Assignment:** Auto-assign based on round-robin or territory

### Workflow 2: Quote Reminder
- **Trigger:** Deal in "Quote Sent" for 3+ days
- **Action:** Notify sales rep to follow up
- **Task Creation:** Create a task on the deal record

### Workflow 3: Stale Deal Notification
- **Trigger:** Deal in "Quote Follow-up" for 14+ days without update
- **Action:** Alert sales manager; consider moving to "Closed Lost"

### Workflow 4: Closed Won - Next Steps
- **Trigger:** Deal moved to "Closed Won"
- **Action:** Create ticket for project team; send internal confirmation to account manager

**To Create Workflows:**
1. Go to **Automation > Workflows**
2. Click **"Create workflow"**
3. Select **Deal** as object type
4. Define trigger, conditions, and actions
5. Enable workflow

---

## Connecting the Pipeline to Lead Nurturing

Once the pipeline is live, connect it to the **email nurturing sequence** (email_nurture_sequence.md):

### Lead-to-Deal Flow

1. **Lead Comes In** → Lead form captured in HubSpot (contact created)
2. **Nurture Sequence Triggered** → Automated emails sent per schedule (Days 0, 2, 4, 7, 14)
3. **Lead Engages** (clicks CTA, replies, schedules call)
4. **Deal Created** → Sales rep creates deal record in HubSpot
5. **Deal Assigned to Stage** → Starts at "New Lead" or "Discovery Call Scheduled" stage
6. **Deal Moves Through Pipeline** → Progresses based on sales activity
7. **Deal Closes** → Moved to "Closed Won" or "Closed Lost"

### Integration Points

**Property Links (to auto-populate deal data from contact):**
- Contact's Company → Deal's Associated Company
- Contact's Phone → Deal's Contact Phone
- Contact's Email → Deal's Contact Email
- Lead Source (from form) → Can populate "Project Type" or custom notes field

---

## Testing the Pipeline

After setup, test the pipeline with a sample deal:

1. **Create a Test Deal**
   - Go to **Deals** from main menu
   - Click **"Create deal"**
   - Name: "Test - Miami Residential Project"
   - Pipeline: "Rendimension Pipeline"
   - Stage: "New Lead"
   - Deal value: $25,000
   - Click **Create**

2. **Move Through Stages**
   - Drag deal from stage to stage
   - Verify win probability updates correctly
   - Confirm all custom properties display properly

3. **Check Deal Activity Timeline**
   - Confirm deal creation and stage moves are logged
   - Verify notification systems work (if enabled)

4. **Delete Test Deal**
   - Once confirmed, delete the test deal
   - Go to deal details → **Actions > Delete**

---

## Reporting & Analytics

Once live, monitor these metrics:

### Key Sales Metrics to Track

- **Average deal size** — Revenue per deal across all stages
- **Sales cycle length** — Days from "New Lead" to "Closed Won"
- **Conversion rates by stage** — % of deals moving from one stage to next
- **Win rate** — % of deals that close won vs. lost
- **Time in stage** — Average duration in each pipeline stage

### HubSpot Reports to Create

1. **Pipeline Summary Report**
   - Shows deals count and total value by stage
   - Filters by date range and owner

2. **Sales Forecast**
   - Weighted forecast based on deal probability and value
   - Updates as deals move through pipeline

3. **Deal Analysis**
   - Drill into individual deals
   - Track dates and activity history

**To Access Reports:**
1. Go to **Reports** from main menu
2. Click **"Create custom report"**
3. Select **Deals** as object
4. Configure columns, filters, and grouping
5. Save and schedule

---

## Troubleshooting & Support

### Common Issues

**Issue:** Stages not appearing in deal creation  
**Solution:** Refresh HubSpot or clear browser cache; verify pipeline is set as active

**Issue:** Custom properties not showing on deal cards  
**Solution:** Go to Deals settings and customize the deal card view to include desired properties

**Issue:** Workflows not triggering**  
**Solution:** Verify workflow is enabled (toggle on); check trigger and conditions are set correctly; allow 15 minutes for activation

**Issue:** Want to edit stages after creation  
**Solution:** Go back to pipeline settings > stage name > edit; no limit to changes

### Contact HubSpot Support
- **Help Center:** https://knowledge.hubspot.com
- **In-app Support:** Click **?** (help icon) in HubSpot interface
- **Community Forum:** https://community.hubspot.com

---

## Next: Integration with Email & Landing Pages

Once the pipeline is live, consider:

1. **HubSpot Forms** — Capture leads directly into HubSpot; auto-trigger nurture sequences
2. **HubSpot Email** — Use the built-in email tool to send nurturing sequence (or use third-party: Klaviyo, ActiveCampaign)
3. **HubSpot Sequences** — Alternative to external email platform; built-in follow-up automation
4. **Deal Tracking** — Automatically log email opens/clicks to deal activity timeline

---

## Checklist: Setup Confirmation

Use this checklist to confirm setup is complete:

- [ ] Logged into HubSpot (rendimension@gmail.com)
- [ ] Created "Rendimension Pipeline"
- [ ] Added all 7 stages with correct win probabilities
- [ ] Set pipeline as default (if applicable)
- [ ] Created custom deal properties (Project Type, Budget, Timeline, etc.)
- [ ] Tested pipeline with sample deal
- [ ] Deleted test deal
- [ ] Set up at least 1 workflow (deal creation notification)
- [ ] Created first sales report
- [ ] Connected pipeline to email nurturing (if applicable)

---

## Support Contact

For questions on this setup:
- **Email:** rendimension@gmail.com
- **HubSpot Account Manager:** [If applicable]
- **Reference Document:** hubspot_setup_guide.md (this file)

---

**Document Version:** 1.0  
**Last Updated:** 2026-03-20  
**Status:** Ready for Implementation
