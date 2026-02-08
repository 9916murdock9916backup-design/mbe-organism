# Cycle Trigger

This file defines the conditions that activate the automation cycles within the MBE Sovereign OS.

## Trigger Types
- **time-based triggers** — periodic checks and updates
- **state-based triggers** — changes in organism status or boundaries
- **event-based triggers** — user actions, system inputs, or interface calls
- **conflict triggers** — governance escalations or drift detection

## Trigger Rules
1. All triggers must align with the constitutional kernel.
2. Triggers may activate one or more cycles.
3. Conflicting triggers escalate to governance.
4. No trigger may bypass identity-routing.

## Activation Flow
trigger → routing-map → authority-flow → automation/cycles
