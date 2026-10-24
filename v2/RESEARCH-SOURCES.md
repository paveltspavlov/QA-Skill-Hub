# Research basis for QA Skill Hub v2.0

This note records the official guidance used to shape the v2 agent, skill, export, M365, and QA patterns. The repository roles and skill workflows are proposals for this project; external sources support the format constraints and testing practices, not a claim that any agent is error-free.

## Design decisions

- GitHub Copilot custom-agent exports use the documented Markdown/YAML profile shape, require a description, and keep the prompt body below 30,000 characters.[1][2]
- V2 role definitions remain portable in plain Markdown; the UI provides a separate Copilot export adapter rather than embedding Copilot tools or commands in the role instructions.[1][2]
- V2 skills use the Agent Skills directory convention with a `SKILL.md` file; the frontmatter `name` matches the directory, and descriptions state both what the skill does and when to use it.[3][4][5]
- The skill descriptions are short routing summaries because GitHub Copilot chooses relevant skills using the task prompt and skill description.[5]
- The app distinguishes prompt files, agent profiles, reusable skills, and project instructions because their formats and supported client surfaces differ.[6][7][8]
- Project-context skill follows the requested `.copilot/`/`.vscode/` convention while avoiding a claim that every host automatically reads those paths; GitHub Copilot has its own support-dependent instruction paths.[7][8]
- M365 Agent Builder profiles are kept separate from shared Agent Skills and include all task procedures in each instruction prompt, as requested.[9][11]
- M365 Builder limits are enforced in the app and test suite: name 30 characters, description 1,000, instruction prompt 8,000, and exactly five starter prompts per profile.[9]
- The declarative-agent manifest allows up to 12 conversation starters; the Microsoft best-practices page recommends at least three and testing each starter, so five templates fit the documented bounds.[10][12]
- M365 knowledge sources are tenant- and license-dependent and have per-source limits; this catalogue supplies profile text only and does not configure knowledge access.[13]
- Test-design skills use the current ISTQB CTFL v4.0 scope as a reference, while allowing the project's actual requirements to define the oracle.[14]
- Test-automation skills emphasize test isolation and user-facing or explicit test contracts, following Playwright's published guidance where it applies.[15]
- Accessibility review maps only supported findings to WCAG 2.2 testable criteria and separates automated checks from human evaluation.[16]
- Security tests must be scoped and risk-prioritized; OWASP describes its guide as a starting set to tailor, not a universal checklist.[17]
- API contract checks use OpenAPI as a language-agnostic interface description when such a contract is supplied.[18]
- React-specific skills follow the official Hooks guidance for component state, shared context, refs, and synchronization with external systems.[19]
- CI workflow skills check provider-native YAML syntax and repository workflow conventions instead of assuming a generic pipeline format.[20]
- Database-design and SQL skills treat constraints and indexes as engine-specific and verify semantics against actual database behavior.[21]
- Cache-aside guidance covers TTL, invalidation, and measurable freshness rather than promising speedups without evidence.[22]
- Data-quality and model-contract skills distinguish assertions that return failing records from schema-shape contracts.[23][24]
- Spark tuning skills use actual plans/statistics and consider partitioning, joins, caching, and adaptive execution as workload-dependent options.[25]
- MCP-specific skills describe tools and their input schemas while requiring explicit user consent and clear side-effect boundaries.[26]
- WebSocket skills account for connection lifecycle and the browser API's lack of built-in backpressure.[27]

## Scope and caveats

The M365 page follows the user's requirement that these profiles do not use shared skills, even though Microsoft documents a limited declarative-agent skills preview.[11] The v2 role/task structure is designed to support multiple hosts.[3][5]
Automatic skill discovery, context-file loading, tool availability, and packaging still depend on the selected host.[7][8]

Repository review found that legacy agent files use `name` and `summary` frontmatter but have no M365 property-length validator. V2 uses Microsoft’s documented Agent Builder limits and validates them in both the UI and tests.

The v1 catalogue remains intact. V2 provides 50 skills: 13 shared core workflows plus 37 specialist skills carried forward and revised from v1's broad development, data, MCP, and QA catalogues. The separate v1 page retains the original 14 agents, 47 skills, and 51 prompts.

## Sources

[1] https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/create-custom-agents
    > "Write a brief description (required) explaining what your agent does and its specific capabilities or domain expertise."
    > "The prompt can be a maximum of 30,000 characters."
[2] https://docs.github.com/en/copilot/reference/custom-agents-configuration
    > "The custom agent `tools` property controls which tools are available to your agent, including those from MCP servers."
    > "Define the agent's behavior, expertise, and instructions in the Markdown content below the YAML frontmatter. The prompt can be a maximum of 30,000 characters."
[3] https://docs.github.com/en/copilot/concepts/customizations/agent-skills
    > "Agent skills are folders of instructions, scripts, and resources that Copilot can load when relevant to improve its performance in specialized tasks."
    > "The Agent Skills specification is an open standard, used by a range of different AI systems."
[4] https://agentskills.io/specification
    > "Must be 1-64 characters"
    > "Must be 1-1024 characters"
    > "Should describe both what the skill does and when to use it"
    > "Must match the parent directory name"
[5] https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
    > "Skill files must be named `SKILL.md`."
    > "Each skill should have its own directory."
    > "When performing tasks, Copilot will decide when to use your skills based on your prompt and the skill's description."
[6] https://docs.github.com/en/copilot/concepts/prompting-and-context/prompt-files
    > "Prompt files are reusable, standalone Markdown templates for focused Copilot interactions."
    > "Repository prompt files use the `.prompt.md` extension and are typically stored in `.github/prompts/`."
[7] https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions
    > "The types of custom instructions available, and the Copilot features that use them, vary by client and surface."
    > "Repository-wide custom instructions are specified in a `copilot-instructions.md` file in the `.github` directory of the repository."
[8] https://docs.github.com/en/copilot/reference/custom-instructions-support
    > "Find out which types of custom instructions are supported in various environments."
[9] https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents
    > "Character limit of 30 characters."
    > "Character limit of 1,000 characters."
    > "Character limit of 8,000 characters."
    > "There's no minimum number of starter prompts."
[10] https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/declarative-agent-manifest-1.9
    > "It must contain at least one nonwhitespace character and be 100 characters or less."
    > "It must contain at least one nonwhitespace character and be 1,000 characters or less."
    > "It must contain at least one nonwhitespace character and be 8,000 characters or less."
    > "The array can't contain more than 12 objects."
    > "Unrecognized or extraneous properties in any JSON object make the entire document invalid."
[11] https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/declarative-agent-skills
    > "Custom skills in declarative agents are in preview for organizations that are part of the Microsoft Frontier Preview."
[12] https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/declarative-agent-best-practices
    > "Include a minimum of three sample prompts that reflect the core capabilities of your agent. These help users understand how to use the agent."
    > "Do this frequently. Try all your conversation starters and sample prompts. Also, test edge questions, long questions, irrelevant questions, and so on, to see how the agent responds."
[13] https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge
    > "Agent Builder supports public websites, SharePoint and OneDrive content, Teams chats and meetings, Outlook email, embedded files, and Microsoft 365 Copilot connectors. Limits vary by source type."
[14] https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0
    > "The syllabus provides a comprehensive understanding of the terminology and concepts used in the testing domain worldwide, making it relevant for all software delivery approaches and practices, including Waterfall, Agile, DevOps, and Continuous Delivery."
[15] https://playwright.dev/docs/best-practices
    > "Each test should be completely isolated from another test and should run independently with its own local storage, session storage, data, cookies etc."
    > "To make tests resilient, we recommend prioritizing user-facing attributes and explicit contracts."
[16] https://www.w3.org/TR/WCAG22
    > "WCAG 2.2 success criteria are written as testable statements that are not technology-specific."
[17] https://owasp.org/www-project-web-security-testing-guide/latest
    > "Not all techniques are equally important for every system. Avoid treating the guide as a checklist."
    > "Continuously re-prioritize. There are infinite ways an application could fail, and organizations always have limited testing time and resources. Spend that time on security issues that present real risk to the business."
[18] https://spec.openapis.org/oas/latest.html
    > "The OpenAPI Specification (OAS) defines a standard, programming language-agnostic interface description for HTTP APIs, which allows both humans and computers to discover and understand the capabilities of a service without requiring access to source code, additional documentation, or inspection of network traffic."
[19] https://react.dev/reference/react/hooks
    > "Hooks let you use different React features from your components."
    > "Effects are an “escape hatch” from the React paradigm. Don’t use Effects to orchestrate the data flow of your application."
[20] https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions
    > "Workflow files use YAML syntax, and must have either a `.yml` or `.yaml` file extension."
    > "You must store workflow files in the `.github/workflows` directory of your repository."
[21] https://postgresql.org/docs/current/ddl-constraints.html
    > "Constraints give you as much control over the data in your tables as you wish."
    > "Adding a unique constraint will automatically create a unique B-tree index on the column or group of columns listed in the constraint."
[22] https://redis.io/docs/latest/develop/use-cases/cache-aside/nodejs
    > "Instead of querying the primary database on every request, the application checks Redis first and only falls back to the primary on a miss."
    > "The TTL is the upper bound on how long a stale value can be served."
[23] https://docs.getdbt.com/docs/build/data-tests
    > "Data tests are assertions you make about your models and other resources in your dbt project."
    > "If the data test returns zero failing rows, it passes, and your assertion has been validated."
[24] https://docs.getdbt.com/docs/collaborate/govern/model-contracts
    > "When enforced, your contract must include every column's `name` and `data_type`."
    > "dbt will run a “preflight” check to ensure that the model's query will return a set of columns with names and data types matching the ones you have defined."
[25] https://spark.apache.org/docs/latest/sql-performance-tuning.html
    > "Spark offers many techniques for tuning the performance of DataFrame or SQL workloads."
    > "Missing or inaccurate statistics will hinder Spark’s ability to select an optimal plan, and may lead to poor query performance."
[26] https://modelcontextprotocol.io/specification/latest
    > "Tools represent arbitrary code execution and must be treated with appropriate caution."
    > "Hosts must obtain explicit user consent before invoking any tool."
[27] https://developer.mozilla.org/en-US/docs/Web/API/WebSocket
    > "The `WebSocket` API has no way to apply backpressure, therefore when messages arrive faster than the application can process them, the application will either fill up the device's memory by buffering those messages, become unresponsive due to 100% CPU usage, or both."
    > "The `WebSocket` object provides the API for creating and managing a WebSocket connection to a server, as well as for sending and receiving data on the connection."
