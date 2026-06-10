---
id: qa-prompts-4-4-generate-a-test-data-factory-builder-pattern
name: "4.4 - Generate a Test Data Factory / Builder Pattern"
folder: prompts
section: qa-prompts
summary: "Test Automation"
tags:
  - "qa-prompts"
  - "test automation"
---

# Prompt 4.4 - Generate a Test Data Factory / Builder Pattern

> Category: **Test Automation**

When to use  When the automation suite needs a maintainable way to create test objects with customizable defaults. Prevents test data setup from becoming copy-paste chaos.

Expected output  A TypeScript test data factory/builder class that produces test objects with sensible defaults and fluent overrides.

Prompt

```
**Role:** You are a TypeScript developer specializing in test architecture patterns. 

You are implementing a test data factory using the Builder pattern for use in 

Playwright tests.

**Context:** The system under test is [SYSTEM DESCRIPTION]. The data object that 

needs a factory is [OBJECT NAME - e.g., "User", "Order", "Product", "BillingAddress"].

**Instruction:** Create a TypeScript test data factory for the object described below 

using the Builder pattern. The implementation should:

- Have a class with sensible default values for all fields

- Have a fluent setter method for each field (returns `this` for chaining)

- Have a `build()` method that returns the typed object

- Have static factory methods for common test personas 

  (e.g., `UserFactory.admin()`, `UserFactory.withExpiredPassword()`)

- Handle nested objects if applicable (e.g., an Order has a User and Address)

- Use TypeScript interfaces/types for all object shapes

**Input:**

Object name: [OBJECT NAME]

Fields and types:

[LIST FIELDS AND THEIR TYPES AND CONSTRAINTS - e.g.:

- id: string (UUID v4)

- email: string (valid email format)

- role: 'admin' | 'user' | 'viewer'

- isActive: boolean (default: true)

- createdAt: Date

- ...

]

Common test personas needed:

[LIST THE COMMON TEST SCENARIOS - e.g.:

- Active admin user

- Inactive/suspended user

- New user (created today, never logged in)

- User with expired password

]

**Constraints:**

- Use faker-style defaults (realistic but obviously fake - test@example.com, not random garbage)

- Exported types must match the application's existing type definitions if provided

- Include a brief usage example in a JSDoc comment at the class level

- The factory should never require real data from the database - all defaults are 

  self-contained

**Output Format:**

Complete TypeScript file:
```
