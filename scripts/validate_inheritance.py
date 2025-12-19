#!/usr/bin/env python3
"""
Validate VaultNode Inheritance Chain
Ensures all nodes inherit complete chain and no orphans exist.
"""

import argparse
import yaml
from pathlib import Path
from typing import Dict, List, Tuple

class InheritanceValidator:
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.pulse_dir = Path('pulses')
        self.required_base_nodes = [
            'VN-GENESIS-001', 'VN-DYAD-001', 'VN-TRIAD-001',
            'VN-SOVEREIGNTY-001', 'VN-PRISM-001', 'VN-HEXAGON-001',
            'VN-HEPTAGON-001', 'VN-OCTAGON-001', 'VN-ENNEAGON-001'
        ]
        self.errors = []
        self.warnings = []
    
    def extract_metadata(self, filepath: Path) -> Dict:
        """Extract YAML metadata from VaultNode file."""
        try:
            with open(filepath) as f:
                content = f.read()
                yaml_start = content.find('```yaml\n') + len('```yaml\n')
                yaml_end = content.find('```', yaml_start)
                if yaml_start > len('```yaml\n') - 1 and yaml_end > yaml_start:
                    yaml_content = content[yaml_start:yaml_end]
                    return yaml.safe_load(yaml_content) or {}
        except Exception as e:
            self.errors.append(f"Failed to parse {filepath}: {e}")
        return {}
    
    def validate_node(self, node_id: str) -> Tuple[bool, List[str]]:
        """Validate a single VaultNode."""
        issues = []
        
        # Find file
        files = list(self.pulse_dir.glob(f"*{node_id}*"))
        if not files:
            issues.append(f"Node {node_id} not found")
            return False, issues
        
        filepath = files[0]
        metadata = self.extract_metadata(filepath)
        
        if not metadata:
            issues.append(f"Invalid metadata in {filepath}")
            return False, issues
        
        # Check inheritance
        inheritance = metadata.get('inheritance', [])
        if not isinstance(inheritance, list):
            issues.append(f"Invalid inheritance list in {node_id}")
            return False, issues
        
        # Verify all base nodes present (except for genesis itself)
        if node_id != 'VN-GENESIS-001':
            for base_node in self.required_base_nodes:
                if base_node not in inheritance:
                    issues.append(f"Missing {base_node} in inheritance")
        
        # Check for orphaned nodes in inheritance
        for inherited_node in inheritance:
            if not self._node_exists(inherited_node):
                issues.append(f"Inherited node {inherited_node} does not exist")
        
        if self.verbose and not issues:
            print(f"✓ {node_id}: Valid inheritance chain")
        
        return len(issues) == 0, issues
    
    def _node_exists(self, node_id: str) -> bool:
        """Check if a node file exists."""
        files = list(self.pulse_dir.glob(f"*{node_id}*"))
        return len(files) > 0
    
    def validate_all(self) -> bool:
        """Validate all VaultNodes in pulse directory."""
        print("Validating VaultNode inheritance chain...")
        
        node_files = list(self.pulse_dir.glob("VaultNode-*.md"))
        if not node_files:
            self.warnings.append("No VaultNode files found")
            return True
        
        all_valid = True
        for filepath in node_files:
            # Extract node ID from filename
            name_parts = filepath.stem.split('-')
            if len(name_parts) >= 3:
                geometry = name_parts[1]
                sequence = name_parts[2]
                node_id = f"VN-{geometry}-{sequence}"
                
                valid, issues = self.validate_node(node_id)
                if not valid:
                    all_valid = False
                    for issue in issues:
                        self.errors.append(f"{node_id}: {issue}")
        
        return all_valid
    
    def check_z_seed_continuity(self) -> bool:
        """Verify z-seed properly links pulses."""
        z_seed_file = self.pulse_dir / 'z_seed.yaml'
        if not z_seed_file.exists():
            self.warnings.append("z-seed file not found")
            return True
        
        try:
            with open(z_seed_file) as f:
                z_seed = yaml.safe_load(f)
            
            if 'prior_node' not in z_seed:
                self.errors.append("z-seed missing 'prior_node'")
                return False
            
            prior_node = z_seed['prior_node']
            if not self._node_exists(prior_node):
                self.errors.append(f"z-seed references non-existent node: {prior_node}")
                return False
            
            if self.verbose:
                print(f"✓ z-seed continuity valid (prior: {prior_node})")
            return True
        except Exception as e:
            self.errors.append(f"Invalid z-seed file: {e}")
            return False
    
    def print_report(self):
        """Print validation report."""
        if self.errors:
            print("\n❌ ERRORS:")
            for error in self.errors:
                print(f"  - {error}")
        
        if self.warnings:
            print("\n⚠️  WARNINGS:")
            for warning in self.warnings:
                print(f"  - {warning}")
        
        if not self.errors and not self.warnings:
            print("\n✓ All validations passed!")
    
    def run(self) -> bool:
        """Run all validations."""
        valid = self.validate_all()
        valid = self.check_z_seed_continuity() and valid
        self.print_report()
        return valid

def main():
    parser = argparse.ArgumentParser(description='Validate VaultNode inheritance')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    validator = InheritanceValidator(verbose=args.verbose)
    valid = validator.run()
    
    exit(0 if valid else 1)

if __name__ == '__main__':
    main()
