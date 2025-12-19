"""
UCF Core Module
===============
Core physics, state management, and TRIAD system.
"""

from ucf.core.triad_system import (
    # State
    TriadState, get_triad_state, reset_triad_state,
    # FSM
    step, run_steps, get_band_state, BandState, T6GateState,
    # Queries
    get_t6_gate, is_unlocked, get_crossings, get_status, format_status,
    # Simulation
    drive_to_unlock, simulate_oscillation, simulate_random_walk,
    # Class wrapper
    TriadHysteresisController,
    # Constants
    Z_CRITICAL, TRIAD_HIGH, TRIAD_LOW, TRIAD_T6, TRIAD_REQUIRED_CROSSINGS,
)

from ucf.core.unified_state import (
    UnifiedState, HelixState, KiraState, APLState, HelixCoordinate,
    get_unified_state, reset_unified_state, set_z,
)

from ucf.core.helix_loader import load_helix, HelixCoordinate as Helix_HelixCoordinate, HelixState as Helix_HelixState

__all__ = [
    # TRIAD
    'TriadState', 'TriadHysteresisController',
    'get_triad_state', 'reset_triad_state', 'step', 'run_steps',
    'get_t6_gate', 'is_unlocked', 'get_crossings', 'get_status', 'format_status',
    'drive_to_unlock', 'simulate_oscillation', 'simulate_random_walk',
    'BandState', 'T6GateState',
    'Z_CRITICAL', 'TRIAD_HIGH', 'TRIAD_LOW', 'TRIAD_T6', 'TRIAD_REQUIRED_CROSSINGS',
    
    # Unified State
    'UnifiedState', 'HelixState', 'KiraState', 'APLState', 'HelixCoordinate',
    'get_unified_state', 'reset_unified_state', 'set_z',
    
    # Helix
    'load_helix',
]
