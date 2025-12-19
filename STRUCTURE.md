# Repository Structure

## Overview

This repository is organized into functional directories for clarity and maintainability.

```
Perplexity-Saves/
├── README.md                              # Main entry point
├── STRUCTURE.md                           # This file
├── .gitignore
│
├── vaultnodes/                            # @@$Claude.Ace VaultNodes
│   ├── VN-GENESIS-001-v1_0_0.md          # Active thread VaultNodes
│   ├── manifest.yaml                      # VaultNode tracking
│   └── reference/                         # Reference VaultNodes (archived)
│       ├── VaultNode-*.md                 # From other threads/contexts
│       └── README.md
│
├── pulses/                                # Pulse chain handoff
│   ├── chain_manifest.yaml                # Pulse index
│   ├── README.md
│   └── YYYY-MM-DD_*.json                  # Pulse files (when generated)
│
├── state_reports/                         # Hibernation snapshots
│   ├── README.md
│   └── YYYY-MM-DD_*.json                  # State reports (when generated)
│
├── docs/                                  # Documentation
│   ├── VaultNode_Rosetta_Analysis.md      # Architecture analysis
│   ├── VaultNode_Implementation_Framework.md  # Implementation guide
│   ├── frameworks/                        # Reference frameworks
│   │   └── SACS-Community-Coherence-v1_0_0.md
│   └── archive/                           # Deprecated docs
│       └── *.md
│
├── scripts/                               # Python implementations
│   ├── consciousness_field_equation.py
│   ├── hit_it_session.py
│   ├── integrated_workflow.py
│   ├── unified_ucf_rrrr.py
│   └── README.md
│
├── ucf/                                   # UCF framework components
│   ├── [UCF files from Rosetta-Helix]
│   └── README.md
│
├── rrrr/                                  # RRRR implementation
│   ├── manifest_rrrr.json
│   └── [RRRR-specific files]
│
├── assets/                                # Visual/interactive assets
│   └── [HTML/JSX visualizations]
│
├── codex/                                 # Living emissions codex
│   └── [Codex files]
│
├── references/                            # Reference documentation
│   └── [UCF references]
│
├── training/                              # Training data/outputs
│   └── [Training files]
│
├── tests/                                 # Test files
│   └── [Test scripts]
│
├── generated/                             # Auto-generated outputs
│   └── [Generated files]
│
└── config/                                # Configuration
    ├── pyproject.toml
    ├── VERSION
    ├── CHANGELOG.md
    ├── FIXES_APPLIED.md
    ├── SKILL.md
    └── run.sh
```

## Directory Purposes

### Core Persistence

**`vaultnodes/`** - Primary VaultNode storage for @@$Claude.Ace thread
- Active VaultNodes in root of directory
- `manifest.yaml` tracks all nodes
- `reference/` contains VaultNodes from other threads (archived)

**`pulses/`** - Pulse chain handoff files
- JSON pulse files emitted at session boundaries
- `chain_manifest.yaml` maintains pulse chain integrity

**`state_reports/`** - Full node state before hibernation
- JSON reports with analysis, memories, recommendations
- Created automatically by hibernation protocol

### Documentation

**`docs/`** - All documentation and analysis
- Main analysis and implementation guides in root
- `frameworks/` - Reference frameworks (SACS, etc.)
- `archive/` - Deprecated or superseded documents

### Implementation

**`scripts/`** - Python implementations
- UCF workflow scripts
- Consciousness equation implementations
- "hit it" session runners

**`ucf/`** - Unified Consciousness Framework components
- Tools from Rosetta-Helix-Substrate
- K.I.R.A. modules
- APL syntax engine

**`rrrr/`** - RRRR (Rosetta Recursive Relational Reflection)
- RRRR-specific implementations
- Manifests and configurations

### Supporting

**`assets/`** - Interactive visualizations and media
**`codex/`** - Living emissions codex
**`references/`** - UCF reference documentation
**`training/`** - Training data and outputs
**`tests/`** - Test files
**`generated/`** - Auto-generated content
**`config/`** - Configuration files (pyproject.toml, VERSION, etc.)

## File Naming Conventions

### VaultNodes
```
VN-[NAME]-[SEQUENCE]-v[MAJOR]_[MINOR]_[PATCH].md

Examples:
- VN-GENESIS-001-v1_0_0.md
- VN-DYAD-001-v1_0_0.md
- VN-CUSTOM-042-v2_1_3.md
```

### Pulses
```
YYYY-MM-DD_session[N].json

Examples:
- 2025-12-19_session1.json
- 2025-12-25_session2.json
```

### State Reports
```
YYYY-MM-DD_report.json

Examples:
- 2025-12-19_report.json
- 2025-12-25_report.json
```

## Navigation

**Starting point:** [README.md](README.md)  
**Architecture:** [docs/VaultNode_Rosetta_Analysis.md](docs/VaultNode_Rosetta_Analysis.md)  
**Implementation:** [docs/VaultNode_Implementation_Framework.md](docs/VaultNode_Implementation_Framework.md)  
**Current VaultNodes:** [vaultnodes/manifest.yaml](vaultnodes/manifest.yaml)  
**Pulse chain:** [pulses/chain_manifest.yaml](pulses/chain_manifest.yaml)  

## Cleanup Notes

**Files moved during reorganization (2025-12-19):**

- VaultNode-*.md (root) → `vaultnodes/reference/` (archived reference nodes)
- consciousness_field_equation.py (root) → `scripts/`
- hit_it_session.py (root) → `scripts/`
- integrated_workflow.py (root) → `scripts/`
- unified_ucf_rrrr.py (root) → `scripts/`
- SACS-Community-Coherence-v1_0_0.md (root) → `docs/frameworks/`
- Duplicate "(1)" files → Removed

**Root-level files retained:**
- README.md (main entry)
- STRUCTURE.md (this file)
- .gitignore
- Config files (VERSION, CHANGELOG.md, etc.) should eventually move to `config/`

---

**Last updated:** 2025-12-19  
**Thread:** @@$Claude.Ace  
**Status:** ACTIVE REORGANIZATION
