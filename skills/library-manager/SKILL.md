---
name: library-manager
description: Procedures for managing the campaign asset library including file naming, index updates, version control, archiving policies, and MASTER_LIBRARY_INDEX.md maintenance.
---

# Library Manager

## Asset Library Structure
```
PROJECT ROOT/
├── MASTER_LIBRARY_INDEX.md
├── .claude/skills/{skill-name}/SKILL.md
├── campaign-assets/{brand}/{platform}/{type}/
├── campaign-reports/{brand}_report_{date}
├── winner-patterns/
└── briefs/

GLOBAL (~/.claude/):
├── agents/{agent-name}.md
└── rules/{rule-name}.md
```

## Naming Conventions
- Skills: `lowercase-hyphen/SKILL.md`
- Agents: `lowercase-hyphen.md`
- Assets: `{brand}_{format}_{concept}_{dimensions}_{variant}`
- Reports: `{brand}_report_{YYYY-MM-DD}`

## Index Update Procedure
After creating ANY asset:
1. Open MASTER_LIBRARY_INDEX.md
2. Find correct section
3. Add row: Type, Name, Purpose, Location, Status, Date
4. Save

## Version Control
- New versions: `_v02`, `_v03`
- Keep previous until validated
- Archive after 30 days

## Archive vs Delete
- **Archive**: old campaign assets, superseded briefs, outdated reports
- **Delete**: duplicates, corrupt files, test outputs
- **Never delete**: winning patterns, validated skills, active agents
