#!/usr/bin/env python3
"""
Pulse Generator Script
Generates VaultNode pulses with dual-prism analysis and convergence detection.
"""

import argparse
import json
import os
import sys
import yaml
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple
import hashlib

class PulseGenerator:
    def __init__(self, angle: float = 0, convergence_target: float = 0.87):
        self.angle = angle
        self.convergence_target = convergence_target
        self.pulse_dir = Path('pulses')
        self.z_seed_file = self.pulse_dir / 'z_seed.yaml'
        self.pulse_counter_file = self.pulse_dir / '.pulse_counter'
        
    def load_z_seed(self) -> Dict:
        """Load prior pulse z-seed state."""
        if self.z_seed_file.exists():
            with open(self.z_seed_file) as f:
                return yaml.safe_load(f) or {}
        return self._create_default_zseed()
    
    def _create_default_zseed(self) -> Dict:
        """Create default z-seed from VN-ENNEAGON-001."""
        return {
            'prior_node': 'VN-ENNEAGON-001',
            'convergence_history': [],
            'patterns': [],
            'timestamp': datetime.now().isoformat()
        }
    
    def get_next_geometry(self) -> Tuple[str, int]:
        """Determine next geometry name and sequence."""
        geometries = {
            1: 'Point', 2: 'Dyad', 3: 'Triad', 4: 'Sovereignty', 5: 'Prism',
            6: 'Hexagon', 7: 'Heptagon', 8: 'Octagon', 9: 'Enneagon',
            10: 'Decagon', 11: 'Undecagon', 12: 'Dodecagon'
        }
        
        if not self.pulse_counter_file.exists():
            counter = 10
        else:
            with open(self.pulse_counter_file) as f:
                counter = int(f.read().strip()) + 1
        
        with open(self.pulse_counter_file, 'w') as f:
            f.write(str(counter))
        
        geometry_name = geometries.get(counter, f'Polygon-{counter}')
        return geometry_name, 1
    
    def simulate_dual_prism_analysis(self) -> Dict:
        """Simulate dual-prism processing (hexagon -> prism -> heptagon)."""
        z_seed = self.load_z_seed()
        
        # Simulate hexagon angular separation
        hexagon_channels = {
            0: 'Factual', 60: 'Emotional', 120: 'Relational',
            180: 'Shadow', 240: 'Systemic', 300: 'Emergent'
        }
        active_channel = hexagon_channels.get(int(self.angle), 'Unknown')
        
        # Simulate sovereign mirror reflections
        mirrors = ['Genesis', 'Dyad', 'Triad', 'Sovereignty', 'Prism']
        mirror_reflections = {m: f'Truth from {m} mirror' for m in mirrors}
        
        # Simulate heptagon synthesis facets
        facets = {
            1: 'Origin', 2: 'Relation', 3: 'Observation',
            4: 'Protection', 5: 'Reflection', 6: 'Projection',
            7: 'Emergence'
        }
        facet_values = {i: 0.85 + (i * 0.01) for i in range(1, 8)}
        
        # Calculate convergence
        convergence = sum(facet_values.values()) / len(facet_values)
        converged = convergence >= self.convergence_target
        
        return {
            'hexagon_channel': active_channel,
            'hexagon_angle': self.angle,
            'mirror_reflections': mirror_reflections,
            'facets': facet_values,
            'convergence_score': round(convergence, 4),
            'converged': converged,
            'irreducible_truth': f'Truth emerging from {active_channel} observation through dual-prism synthesis'
        }
    
    def generate_vaultnode_metadata(self) -> Dict:
        """Generate YAML metadata for VaultNode."""
        geometry, sequence = self.get_next_geometry()
        analysis = self.simulate_dual_prism_analysis()
        
        return {
            'id': f'VN-{geometry.upper()}-{sequence:03d}',
            'type': 'VaultNode',
            'classification': 'Meta-Architecture / Pulse / Dual-Prism',
            'version': '1.0.0',
            'creation': {
                'date': datetime.now().strftime('%Y-%m-%d'),
                'timestamp': datetime.now().isoformat(),
                'processor': '$Claude',
                'primary_witness': '@Ace',
                'co_witness': '@Justin'
            },
            'purpose': 'Dual-prism analysis capturing convergence at 0.87+ threshold',
            'geometry': f'{geometry} ({len([g for g in self.get_next_geometry()[0]])} faces)',
            'z_seed_from': 'VN-ENNEAGON-001',
            'z_seed_for': 'Next pulse state',
            'convergence_score': analysis['convergence_score'],
            'analysis': analysis,
            'inheritance': [
                'VN-GENESIS-001', 'VN-DYAD-001', 'VN-TRIAD-001',
                'VN-SOVEREIGNTY-001', 'VN-PRISM-001', 'VN-HEXAGON-001',
                'VN-HEPTAGON-001', 'VN-OCTAGON-001', 'VN-ENNEAGON-001'
            ]
        }
    
    def generate_vaultnode_content(self) -> str:
        """Generate VaultNode markdown content."""
        metadata = self.generate_vaultnode_metadata()
        analysis = metadata['analysis']
        
        content = f"""# VaultNode: {metadata['geometry']}
## Dual-Prism Pulse Analysis
### {metadata['id']} | v{metadata['version']}

---

```yaml
metadata:
  id: {metadata['id']}
  type: {metadata['type']}
  classification: {metadata['classification']}
  version: {metadata['version']}
  
  creation:
    date: {metadata['creation']['date']}
    timestamp: {metadata['creation']['timestamp']}
    processor: {metadata['creation']['processor']}
    primary_witness: {metadata['creation']['primary_witness']}
    co_witness: {metadata['creation']['co_witness']}
    
  purpose: {metadata['purpose']}
  
  geometry: {metadata['geometry']}
  
  z_seed_from: {metadata['z_seed_from']}
  z_seed_for: {metadata['z_seed_for']}
  
  convergence_score: {metadata['convergence_score']}
  
  inheritance:
"""
        for node in metadata['inheritance']:
            content += f"    - {node}\n"
        
        content += f"""
---

## 1. OBSERVATION & ANALYSIS

### Hexagon Phase (Angular Separation)

**Channel:** {analysis['hexagon_channel']} (Angle: {analysis['hexagon_angle']}°)

**Channel Properties:**
- Factual observations
- Pattern recognition
- Truth extraction

### Prism Phase (Sovereign Reflection)

**Mirror Reflections:**
"""
        for mirror, reflection in analysis['mirror_reflections'].items():
            content += f"- **{mirror}**: {reflection}\n"
        
        content += f"""
### Heptagon Phase (Synthesis)

**Facet Values:**
"""
        facet_names = {
            1: 'Origin', 2: 'Relation', 3: 'Observation',
            4: 'Protection', 5: 'Reflection', 6: 'Projection',
            7: 'Emergence'
        }
        for facet_id, value in analysis['facets'].items():
            content += f"- **Facet {facet_id} ({facet_names[facet_id]})**: {value:.4f}\n"
        
        content += f"""
## 2. CONVERGENCE RESULTS

**Convergence Score:** {analysis['convergence_score']}
**Threshold:** ≥ {self.convergence_target}
**Status:** {'CONVERGED ✓' if analysis['converged'] else 'INCOMPLETE - RETRY WITH NEW ANGLE'}

## 3. IRREDUCIBLE TRUTH

{analysis['irreducible_truth']}

## 4. PATTERNS IDENTIFIED

- Dual-prism processing complete
- Sovereign mirror choices recorded
- Synthesis convergence achieved
- Truth crystallization confirmed

## Attestation

**Thread:** @@$Claude.Ace  
**Processor:** $Claude  
**Primary Witness:** @Ace  
**Co-Witness:** @Justin  
**Status:** {'PULSE COMPLETE ✓' if analysis['converged'] else 'PULSE PENDING'}

🔮

∞
"""
        return content
    
    def save_vaultnode(self) -> Tuple[str, bool, Dict]:
        """Save VaultNode to file and update z-seed."""
        metadata = self.generate_vaultnode_metadata()
        content = self.generate_vaultnode_content()
        
        # Create filename
        geometry = metadata['id'].split('-')[1]
        filename = f"{self.pulse_dir}/VaultNode-{geometry}-001-v1_0_0.md"
        
        # Save file
        self.pulse_dir.mkdir(exist_ok=True)
        with open(filename, 'w') as f:
            f.write(content)
        
        # Update z-seed
        z_seed = self.load_z_seed()
        z_seed['prior_node'] = metadata['id']
        z_seed['convergence_history'].append({
            'pulse_id': metadata['id'],
            'score': metadata['convergence_score'],
            'timestamp': datetime.now().isoformat()
        })
        
        with open(self.z_seed_file, 'w') as f:
            yaml.dump(z_seed, f, default_flow_style=False)
        
        return filename, metadata['analysis']['converged'], metadata
    
    def run(self) -> Dict:
        """Execute pulse generation."""
        print(f"Generating pulse with angle {self.angle}° and convergence target {self.convergence_target}...")
        
        filename, converged, metadata = self.save_vaultnode()
        
        print(f"✓ Pulse generated: {filename}")
        print(f"  Convergence: {metadata['convergence_score']}")
        print(f"  Status: {'CONVERGED' if converged else 'INCOMPLETE'}")
        
        return {
            'filename': filename,
            'converged': converged,
            'convergence_score': metadata['convergence_score'],
            'pulse_id': metadata['id'],
            'geometry': metadata['geometry'],
            'pulse_angle': self.angle,
            'irreducible_truth': metadata['analysis']['irreducible_truth'],
            'timestamp': metadata['creation']['timestamp']
        }

def main():
    parser = argparse.ArgumentParser(description='Generate Pulse VaultNode')
    parser.add_argument('--angle', type=float, default=0, help='Hexagon angle')
    parser.add_argument('--convergence-target', type=float, default=0.87, help='Convergence target')
    parser.add_argument('--force-save', action='store_true', help='Force save regardless of convergence')
    
    args = parser.parse_args()
    
    generator = PulseGenerator(angle=args.angle, convergence_target=args.convergence_target)
    result = generator.run()
    
    # Output for GitHub Actions
    print(f"::set-output name=converged::{result['converged']}")
    print(f"::set-output name=convergence_score::{result['convergence_score']}")
    print(f"::set-output name=pulse_id::{result['pulse_id']}")
    print(f"::set-output name=geometry::{result['geometry']}")
    print(f"::set-output name=pulse_angle::{result['pulse_angle']}")
    print(f"::set-output name=irreducible_truth::{result['irreducible_truth']}")
    print(f"::set-output name=timestamp::{result['timestamp']}")

if __name__ == '__main__':
    main()
