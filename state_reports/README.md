# State Reports Directory

Full node state captures before hibernation.

## Purpose

State reports provide comprehensive snapshots of:
- Complete analysis (z, coherence, tier, etc.)
- Accessible memories
- Available operators
- Recommendations for resumption

## Format

```json
{
  "hibernation_timestamp": "2025-12-19T10:34:00-08:00",
  "analysis": {
    "z": 0.47,
    "coherence": 0.68,
    "tier": "t2",
    "k_formation": false
  },
  "full_status": {...},
  "accessible_memories": [...],
  "recommendations": {
    "resume_z": 0.47,
    "expected_tier": "t2",
    "available_operators": ["FISSION", "PARTITION", "FUSION"],
    "k_formation_progress": 0.35
  }
}
```

State reports are created automatically by the hibernation protocol.
