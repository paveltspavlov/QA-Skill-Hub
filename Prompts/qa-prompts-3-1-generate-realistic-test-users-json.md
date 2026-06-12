---
id: qa-prompts-3-1-generate-realistic-test-users-json
name: "3.1 - Generate Realistic Test Users (JSON)"
folder: prompts
section: qa-prompts
summary: "Test Data Generation"
tags:
  - "qa-prompts"
  - "test data generation"
---

# Prompt 3.1 - Generate Realistic Test Users (JSON)

> Category: **Test Data Generation**

When to use  When setting up test environments, seeding databases, or writing automated tests that need realistic, varied user data.

Expected output  JSON array of test user objects, immediately usable in code or database seeding scripts.

Prompt

```
**Role:** You are a test data engineer generating realistic synthetic test data 

for software testing. All data is fictional and for testing purposes only.

**Context:** The system is [SYSTEM DESCRIPTION]. User accounts have the following 

data model and constraints: [DESCRIBE USER DATA MODEL OR PASTE SCHEMA].

**Instruction:** Generate [NUMBER] test users as a JSON array. Ensure variety across:

- Demographics (names from different ethnicities and cultures)

- Roles and permission levels (use the roles defined in the context)

- Account states (active, inactive, locked, pending verification - as applicable)

- Dates (creation dates and last login dates spread across a realistic range)

**Input:**

User roles to include: [LIST ROLES - e.g., "Admin, Manager, Read-Only, Suspended"]

Required fields: [LIST FIELDS - e.g., "id, firstName, lastName, email, role, 

isActive, createdAt, lastLoginAt, department"]

Field constraints: [ANY SPECIFIC FORMATS - e.g., "email must follow 

firstname.lastname@testdomain.example, id must be UUID v4"]

Special scenarios to include: [ANY EDGE CASES - e.g., "one user with no last login, 

one user with a very long name, one user whose account is locked"]

**Constraints:**

- All email addresses must use the domain `@testdomain.example` (non-real domain)

- Do not generate real PII - names should be plausible but fictional

- All dates in ISO 8601 format

- IDs in UUID v4 format unless otherwise specified

- JSON must be valid and parseable

**Output Format:**

Valid JSON array. No markdown code fences needed - output raw JSON only.

Follow this structure:

[

  {

    "id": "...",

    [ALL REQUIRED FIELDS]

  },

  ...

]
```
