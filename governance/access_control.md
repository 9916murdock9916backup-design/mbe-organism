MBE Platform — Access Control Governance

1. Purpose

This document defines how access, permissions, and boundaries operate within the MBE platform.
It establishes the rules that govern:

• client access
• role separation
• permission enforcement
• isolation between accounts
• what automation is allowed


This is a governance document, not a technical implementation.

---

2. Roles

Architect (Sovereign Role)

• Full access to all systems and governance files
• Can create or modify governance declarations
• Can authorize or revoke automation
• Can approve or remove client access
• Cannot be overridden by automated processes


Admin (Operational Role)

• Can view client folders
• Can manage onboarding tasks
• Cannot modify governance files
• Cannot access architect‑level systems


Client (Licensed Role)

• Access only to their assigned folder
• Access only to allowed products and interfaces
• Cannot view or modify other clients’ data
• Cannot access governance, identity, or core systems


---

3. Permission Model

Each client receives a permissions.json file inside their folder.
This file defines:

• allowed products
• restricted products
• whether they can generate outputs
• whether they can modify their own files
• whether they can view logs or analytics


The platform must enforce these boundaries at all times.

---

4. Client Isolation Requirements

The system must ensure:

• each client operates inside their own folder
• no cross‑client visibility
• no shared state unless explicitly authorized
• no access to governance, identity, or core‑kernel layers


Isolation is mandatory for licensing, security, and platform integrity.

---

5. Automation Boundaries

The system may automate:

• creation of client folders
• creation of permissions.json files
• generation of client‑safe interfaces
• enforcement of allowed/restricted modules
• logging of client actions
• onboarding workflows


The system may not automate:

• changes to governance files
• changes to identity‑routing
• creation of new organisms
• modification of architect‑level systems


These actions require sovereign approval.

---

6. Licensing Enforcement

The platform must enforce:

• access only to licensed products
• restrictions on unlicensed modules
• version control for client‑visible outputs
• audit logs for compliance and evaluation


Licensing boundaries are part of the platform’s commercial integrity.

---

7. Audit & Logging Requirements

The system must maintain logs for:

• client actions
• access attempts
• restricted‑area violations
• automated onboarding events


Logs must be client‑safe and architect‑visible.

---

8. Modification Rules

Only the Architect may:

• modify this file
• modify governance declarations
• authorize new automation capabilities
• approve new roles or access levels


All changes must be committed through version control.

---

9. Enforcement Principle

The platform must always prioritize:

• sovereignty
• stability
• isolation
• safety
• licensing integrity


Automation must operate within these boundaries, never outside them.
