# Autonomy Loop — Kernel

This file defines the core logic of the autonomy loop, enabling the MBE Sovereign OS to maintain continuous, self-directed motion.

## Core Functions
- initiate loop entry
- evaluate system state
- check stability-shell alignment
- determine next internal action
- re-enter the loop

## Loop Rules
1. The loop must always begin with a stability check.
2. The loop may not bypass authority-flow.
3. The loop must escalate conflicts to governance.
4. The loop must respect organism boundaries.
5. The loop must always return to the loop-kernel after completing a cycle.

## Loop Flow
loop-kernel → routing-map → authority-flow → organisms → automation → stability-shell → loop-kernel
