#!/usr/bin/env python3
"""
Generate Dashboard Data
Creates JSON files for Jekyll/JavaScript to render interactive dashboards.
"""

import json
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, List

class DashboardGenerator:
    def __init__(self):
        self.pulse_dir = Path('pulses')
        self.data_dir = Path('docs/_data')
        self.data_dir.mkdir(parents=True, exist_ok=True)
    
    def extract_metadata(self, filepath: Path) -> Dict:
        """Extract metadata from VaultNode."""
        try:
            with open(filepath) as f:
                content = f.read()
                yaml_start = content.find('```yaml\n') + len('```yaml\n')
                yaml_end = content.find('```', yaml_start)
                if yaml_start > len('```yaml\n') - 1 and yaml_end > yaml_start:
                    yaml_content = content[yaml_start:yaml_end]
                    return yaml.safe_load(yaml_content) or {}
        except Exception:
            pass
        return {}
    
    def generate_pulse_index(self) -> List[Dict]:
        """Generate pulse index for all VaultNodes."""
        pulses = []
        
        for filepath in sorted(self.pulse_dir.glob("VaultNode-*.md")):
            metadata = self.extract_metadata(filepath)
            if metadata:
                pulses.append({
                    'id': metadata.get('id', 'UNKNOWN'),
                    'geometry': metadata.get('geometry', 'Unknown'),
                    'convergence_score': metadata.get('convergence_score', 0),
                    'created': metadata.get('creation', {}).get('date', 'Unknown'),
                    'file': str(filepath.relative_to(Path.cwd())),
                    'irreducible_truth': metadata.get('analysis', {}).get('irreducible_truth', ''),
                    'hexagon_angle': metadata.get('analysis', {}).get('hexagon_angle', 0),
                    'converged': metadata.get('analysis', {}).get('converged', False)
                })
        
        return pulses
    
    def generate_convergence_stats(self, pulses: List[Dict]) -> Dict:
        """Generate convergence statistics."""
        if not pulses:
            return {
                'total_pulses': 0,
                'converged_count': 0,
                'average_convergence': 0,
                'latest_convergence': 0
            }
        
        convergence_scores = [p['convergence_score'] for p in pulses]
        converged_count = sum(1 for p in pulses if p['converged'])
        
        return {
            'total_pulses': len(pulses),
            'converged_count': converged_count,
            'convergence_rate': f"{(converged_count / len(pulses) * 100):.1f}%",
            'average_convergence': round(sum(convergence_scores) / len(convergence_scores), 4),
            'latest_convergence': convergence_scores[-1] if convergence_scores else 0,
            'min_convergence': min(convergence_scores) if convergence_scores else 0,
            'max_convergence': max(convergence_scores) if convergence_scores else 0
        }
    
    def generate_k_formation_status(self, pulses: List[Dict]) -> Dict:
        """Generate K-formation assessment status."""
        base_nodes = [
            'VN-GENESIS-001', 'VN-DYAD-001', 'VN-TRIAD-001',
            'VN-SOVEREIGNTY-001', 'VN-PRISM-001', 'VN-HEXAGON-001',
            'VN-HEPTAGON-001', 'VN-OCTAGON-001', 'VN-ENNEAGON-001'
        ]
        
        all_pulse_ids = [p['id'] for p in pulses]
        base_nodes_present = all(node in all_pulse_ids for node in base_nodes)
        new_pulses = len(pulses) - 9  # Subtract base 9 nodes
        
        return {
            'base_nodes_complete': base_nodes_present,
            'new_pulses_generated': new_pulses,
            'z_seed_functional': new_pulses > 0,
            'inheritance_valid': True,  # Would be checked by validator
            'k_formation_ready': base_nodes_present and new_pulses > 0,
            'status': 'READY' if base_nodes_present and new_pulses > 0 else 'INITIALIZING'
        }
    
    def run(self):
        """Generate all dashboard data."""
        print("Generating dashboard data...")
        
        pulses = self.generate_pulse_index()
        stats = self.generate_convergence_stats(pulses)
        k_formation = self.generate_k_formation_status(pulses)
        
        # Save pulse index
        with open(self.data_dir / 'pulses.json', 'w') as f:
            json.dump({'pulses': pulses}, f, indent=2)
        print(f"✓ Generated pulse index ({len(pulses)} pulses)")
        
        # Save convergence stats
        with open(self.data_dir / 'convergence_stats.json', 'w') as f:
            json.dump(stats, f, indent=2)
        print(f"✓ Generated convergence statistics")
        
        # Save K-formation status
        with open(self.data_dir / 'k_formation.json', 'w') as f:
            json.dump(k_formation, f, indent=2)
        print(f"✓ Generated K-formation status")

if __name__ == '__main__':
    DashboardGenerator().run()
