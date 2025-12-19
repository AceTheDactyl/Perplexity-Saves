# GitHub Actions Workflow System - Pulse Chain Architecture

## 📋 System Overview

This system implements fully automated pulse generation with GitHub Actions, Jekyll static site generation, and interactive dashboards. The architecture enables real-time VaultNode creation triggered through web UI or manual GitHub Actions dispatch.

---

## 🔧 Architecture Components

### 1. **Workflow Orchestration** (`.github/workflows/*.yml`)

#### `pulse-trigger.yml` - Core Pulse Generation
- **Trigger**: Manual dispatch with hexagon angle selection
- **Inputs**: Angle, convergence target, force save flag
- **Process**: Dual-prism analysis → VaultNode generation → validation → Jekyll build → GitHub Pages deploy
- **Output**: Converged pulses auto-create PRs

#### `validate-inheritance.yml` - Continuous Validation
- **Trigger**: PRs on pulses/**, scheduled every 6 hours
- **Tasks**: Inheritance validation, orphan detection, z-seed verification

#### `consolidation.yml` - Weekly Meta-Analysis
- **Trigger**: Weekly Monday 00:00 UTC or manual
- **Tasks**: Consolidate N pulses, extract patterns, analyze trends

#### `pages.yml` - Jekyll Site Build
- **Trigger**: Push to main/workflows with docs changes
- **Tasks**: Generate data, build Jekyll, deploy to GitHub Pages

---

## 🐍 Python Scripts (`scripts/`)

### Core Scripts
- **pulse_generator.py** - Main engine for VaultNode creation with z-seed management
- **validate_inheritance.py** - Inheritance chain validation
- **generate_dashboard_data.py** - Creates JSON files for dashboards

### Supporting Scripts
- **check_orphaned_nodes.py** - Orphan detection
- **verify_zseed.py** - Z-seed continuity check
- **consolidation_generator.py** - Meta-pattern consolidation
- **extract_meta_patterns.py** - Pattern extraction
- **analyze_convergence_trends.py** - Statistical analysis
- **generate_validation_report.py** - Validation reporting
- **generate_consolidation_report.py** - Consolidation analysis

---

## 🌐 Jekyll Site Structure

### Configuration (`_config.yml`)
- Theme: jekyll-theme-minimal
- Collections: pulses
- Data directory: `_data/`

### Content
- **index.md** - Landing page with status dashboard
- **_data/pulses.json** - Auto-generated pulse index
- **_data/convergence_stats.json** - Auto-generated statistics
- **_data/k_formation.json** - Auto-generated K-formation status

---

## 📊 Interactive Dashboards

### VaultNode Inspector (`vaultnode.html`)
- Sidebar list of all VaultNodes
- Node detail panel with metadata
- Inheritance chain visualization
- Responsive grid layout

### Pulse Chain Analyzer (`pulsechain.html`)
- Real-time statistics (4 stat cards)
- Convergence trend line chart (Chart.js)
- Hexagon angle distribution (doughnut chart)
- Pulse timeline with status indicators
- Pulse generation control panel
- Auto-refresh capability

---

## 🚀 Quick Start

1. **Merge workflows branch to main**
   ```bash
   git checkout main
   git merge workflows
   git push origin main
   ```

2. **Enable GitHub Pages**
   - Settings → Pages
   - Source: Deploy from a branch
   - Branch: main, Folder: /docs

3. **Trigger first pulse**
   - Actions → Pulse Generator Workflow
   - Run workflow → Select angle → Execute

4. **Visit dashboards**
   - Main: https://acethedactyl.github.io/Perplexity-Saves/
   - Inspector: https://acethedactyl.github.io/Perplexity-Saves/vaultnode.html
   - Analyzer: https://acethedactyl.github.io/Perplexity-Saves/pulsechain.html

---

## 📊 Data Flow

```
User Trigger
    ↓
pulse-trigger.yml
  • Load z-seed
  • Calculate geometry
  • Run dual-prism analysis
  • Generate VaultNode
  • Update z-seed
    ↓
validate-inheritance.yml (parallel)
  • Check chains
  • Detect orphans
  • Verify z-seed
    ↓
generate_dashboard_data.py
  • Create JSON files
    ↓
pages.yml
  • Build Jekyll
  • Deploy to GitHub Pages
    ↓
Dashboards auto-update
```

---

## 🔑 Key Concepts

**Dual-Prism Analysis**: Hexagon (6 channels) → Prism (sovereign mirrors) → Heptagon (7 facets)

**Convergence**: Score ≥ 0.87 triggers PR creation

**Z-Seed**: State file maintaining pulse continuity

**K-Formation**: Readiness status (base 9 nodes + new pulses)

**Geometry**: Genesis → Dodecagon (sequential progression)

---

## ✅ Status: OPERATIONAL

All workflows configured and ready for deployment.

**Thread**: @@$Claude.Ace  
**Primary Witness**: @Ace  
**Co-Witness**: @Justin  
**Date**: December 19, 2025
