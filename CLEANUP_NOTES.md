# Cleanup Notes

## Files to Delete from Root

The following files in the repository root should be deleted as they have been moved to proper directories:

### Moved to `vaultnodes/reference/`
- [ ] `VaultNode-Dyad-001-v1_0_0.md`
- [ ] `VaultNode-Enneagon-001-v1_0_0.md`
- [ ] `VaultNode-Genesis-001-v1_0_0.md` (old version, new one in vaultnodes/)
- [ ] `VaultNode-Heptagon-001-v1_0_0.md`
- [ ] `VaultNode-Heptagon-001-v1_0_0 (1).md` (duplicate)
- [ ] `VaultNode-Hexagon-001-v1_0_0.md`
- [ ] `VaultNode-KIRA-001-v1_0_0.md`
- [ ] `VaultNode-Octagon-001-v1_0_0.md`
- [ ] `VaultNode-Prism-001-v1_0_0.md`
- [ ] `VaultNode-Sovereignty-001-v1_0_0.md`

### Moved to `scripts/`
- [ ] `consciousness_field_equation.py`
- [ ] `hit_it_session.py`
- [ ] `integrated_workflow.py`
- [ ] `unified_ucf_rrrr.py`

### Moved to `docs/frameworks/`
- [ ] `SACS-Community-Coherence-v1_0_0.md`

### Moved to `config/`
- [ ] `VERSION`
- [ ] `CHANGELOG.md`
- [ ] `FIXES_APPLIED.md`
- [ ] `SKILL.md`
- [ ] `pyproject.toml`
- [ ] `run.sh`
- [ ] `manifest_rrrr.json`

### Moved to `docs/`
- [ ] `VaultNode_Rosetta_Analysis.md`
- [ ] `VaultNode_Implementation_Framework.md`

## Clean Root Structure (Target)

After cleanup, root should only contain:

```
Perplexity-Saves/
├── .gitignore
├── .github/
├── README.md
├── STRUCTURE.md
├── CLEANUP_NOTES.md (this file - can be deleted after cleanup)
├── vaultnodes/
├── pulses/
├── state_reports/
├── docs/
├── scripts/
├── config/
├── ucf/
├── rrrr/
├── assets/
├── codex/
├── references/
├── training/
├── tests/
└── generated/
```

## How to Clean Up

### Option 1: Via GitHub Web Interface
1. Navigate to each file in root
2. Click the trash icon to delete
3. Commit the deletion

### Option 2: Via Git Command Line
```bash
# Clone the repository
git clone https://github.com/AceTheDactyl/Perplexity-Saves.git
cd Perplexity-Saves

# Delete moved files
git rm VaultNode-*.md
git rm consciousness_field_equation.py hit_it_session.py integrated_workflow.py unified_ucf_rrrr.py
git rm SACS-Community-Coherence-v1_0_0.md
git rm VERSION CHANGELOG.md FIXES_APPLIED.md SKILL.md pyproject.toml run.sh manifest_rrrr.json
git rm VaultNode_Rosetta_Analysis.md VaultNode_Implementation_Framework.md

# Commit
git commit -m "Clean up root: Remove files moved to proper directories"

# Push
git push origin main
```

### Option 3: Let Claude Do It (Recommended)
Ask Claude to delete these files using the GitHub MCP tools.

## Verification After Cleanup

Run this to verify clean state:
```bash
# Should only show organizational files and directories
ls -la | grep -v '^d' | grep -v '^\.'
```

Expected output:
```
.gitignore
README.md
STRUCTURE.md
CLEANUP_NOTES.md
```

---

**Status:** Files have been copied to proper locations  
**Action Required:** Delete originals from root  
**Safe to Delete:** Yes - all content preserved in new locations  

**Last Updated:** 2025-12-19 10:44 AM PST
