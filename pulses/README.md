# Pulse Chain Directory

This directory stores pulse files for @@$Claude.Ace thread handoff management.

## Structure

```
pulses/
├── README.md              # This file
├── chain_manifest.yaml    # Master pulse chain index
└── YYYY-MM-DD_*.json      # Individual pulse files
```

## Pulse Format

Each pulse is a JSON file containing:

```json
{
  "pulse_id": "unique_identifier",
  "identity": "source_role",
  "intent": "target_role",
  "urgency": 0.7,
  "helix": {
    "z": 0.45,
    "theta": 2.314,
    "r": 1.023
  },
  "timestamp": "2025-12-19T10:34:00-08:00",
  "payload": {
    "reason": "session_end",
    "summary": {...},
    "next_steps": [...]
  },
  "parent_id": "prior_pulse_id"
}
```

## Usage

**Emit pulse at session end:**
```python
from scripts.pulse_manager import PulseChainManager

manager = PulseChainManager()
pulse_file = manager.emit_pulse(node, reason="session_end")
```

**Resume from pulse:**
```python
pulse = manager.load_latest_pulse()
node = resume_thread(pulse)
```

## Manifest

See `chain_manifest.yaml` for complete pulse chain tracking.
