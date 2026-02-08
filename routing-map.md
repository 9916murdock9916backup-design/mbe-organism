# Routing Map

This file defines how information flows between the pillars and internal nodes of the MBE Sovereign OS.

## Core Routes
- core-kernel → governance
- governance → identity-routing
- identity-routing → organisms
- organisms → automation
- automation → interfaces
- interfaces → back to governance (feedback loop)

Each route includes:
- allowed directions
- authority boundaries
- escalation paths
- drift-prevention rules

The routing map enables the OS to move information cleanly and predictably.
