---
id: qa-prompts-4-2-generate-a-page-object-class-from-html-or-description
name: "4.2 - Generate a Page Object Class from HTML or Description"
folder: prompts
section: qa-prompts
summary: "Test Automation"
tags:
  - "qa-prompts"
  - "test automation"
---

# Prompt 4.2 - Generate a Page Object Class from HTML or Description

> Category: **Test Automation**

When to use  When starting automation for a new page or component. Give it the HTML source or a description of the page and get a typed Page Object class back.

Expected output  A complete, typed Playwright Page Object class with methods for all interactive elements on the page.

Prompt

```
**Role:** You are a TypeScript automation engineer creating Page Object Model classes 

for Playwright tests. You write clean, typed, self-documenting code.

**Context:** The application uses TypeScript + Playwright. 

[SELECTOR STRATEGY - e.g., "We use data-testid attributes on all interactive elements" 

OR "We use aria labels and roles for selectors" OR "We use CSS class selectors"]

**Instruction:** Create a Page Object class for the page/component described or shown 

below. The class must:

- Have a typed Locator property for every interactive element (inputs, buttons, 

  links, dropdowns, checkboxes) and every element that will be asserted against

- Have an async method for each user action (fill, click, select, check, etc.)

- Have async getter methods for readable element states (text content, 

  visibility, value, etc.)

- Have a navigate() method if the page has a fixed URL

- Have a waitForLoad() method that asserts the page has fully loaded

**Input:**

Page name: [PAGE NAME - e.g., "LoginPage", "CheckoutPage", "UserProfilePage"]

Page URL (if applicable): [URL or URL pattern]

[CHOOSE ONE:]

Option A - HTML snippet: [PASTE HTML HERE]

Option B - Page description: [DESCRIBE ALL ELEMENTS AND THEIR PURPOSES IN PLAIN TEXT]

**Constraints:**

- Use Playwright's semantic locators (getByRole, getByLabel, getByPlaceholder) 

  where possible over getByTestId or CSS

- Add JSDoc comments on public methods explaining what each does

- Use descriptive TODO comments for any locator where you had to guess the selector

- All locator properties should be declared as `private readonly`

- Class should be exported as a named export

**Output Format:**

Complete TypeScript file:
```
