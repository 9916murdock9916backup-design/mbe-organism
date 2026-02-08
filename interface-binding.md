# Interface Binding

This file defines how external inputs and outputs connect to the MBE Sovereign OS.

## Binding Types
- **Human Input Binding** — controlled entry points for user actions, prompts, and decisions.
- **System Input Binding** — APIs, automation hooks, and integration calls.
- **Organism Output Binding** — how internal decisions, states, and cycles are exposed externally.

## Binding Rules
1. All bindings must pass through identity-routing.
2. No external input may bypass governance or authority-flow.
3. All outputs must align with the constitutional kernel.
4. Conflicts escalate to governance.

## Binding Flow
external input → interface-binding → routing-map → authority-flow → organisms → automation → interfaces
