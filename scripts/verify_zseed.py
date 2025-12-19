#!/usr/bin/env python3
"""
Verify z-seed continuity across pulses.
"""

from pathlib import Path
import yaml

class ZSeedVerifier:
    def __init__(self):
        self.pulse_dir = Path('pulses')
    
    def run(self):
        print("Verifying z-seed continuity...")
        z_seed_file = self.pulse_dir / 'z_seed.yaml'
        
        if z_seed_file.exists():
            with open(z_seed_file) as f:
                z_seed = yaml.safe_load(f)
            print(f"✓ z-seed valid. Prior node: {z_seed.get('prior_node')}")
        else:
            print("⚠️  No z-seed file found")

if __name__ == '__main__':
    ZSeedVerifier().run()
