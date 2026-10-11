---
name: my-code-conventions
description: "While writing or changing code, follow the target repository's conventions, including reuse, concrete performance cost, and tests proportional to risk. Not a review workflow and not the feature-planning gate."
---

# my-code-conventions

Use when implementing or modifying code in an existing project. These rules govern the code being written. They do not decide whether a plan is required, and they are not a review workflow. Before choosing an implementation, read the repository instructions and inspect relevant conventions in nearby code.

## Workflow

1. Read the instructions that apply to the project and inspect nearby code with a similar purpose.
2. Follow the project's architecture, naming, folder structure, formatting and established patterns unless they conflict with the user's request or create a concrete problem.
3. Before changing shared logic, a component, or a branch that existing features use, find the callers and the behavior they rely on. Preserve that behavior unless the request changes it, and state which existing features or logic the change affects.
4. Consider performance while writing the affected code. Look for relevant risks such as unnecessary repeated work, re-renders, redundant queries or calculations, large data loads, memory use and response time. Focus on issues with a concrete impact; avoid premature optimization or added complexity without evidence.
5. Before creating a function or component, search the project for an existing equivalent that can be reused. Prefer reusing or extending existing code when it preserves clear responsibility and avoids unreasonable coupling.
6. If reusable functionality lives in a folder or module specific to one business domain, consider moving it to an appropriate generic location when its use genuinely extends beyond that domain. Refactor only when that broader reuse is needed; keep business-specific logic with the domain that owns it.
7. For features with complex calculation logic, add unit tests covering key cases, boundary cases and error-prone conditions. Add end-to-end tests when they are needed to verify behavior across multiple components or a user flow; decide based on risk and project conventions.
8. Do not add a dependency, abstraction or design pattern without a concrete need.
9. Apply project-specific guidance only in that project. In PropertyGuru projects that already use Hive, on web and mobile, prefer existing Hive UI components and design tokens when suitable. Do not carry that preference into other projects.
10. If conventions are missing, inconsistent or conflict with the request, explain the relevant tradeoff and choose the simplest approach supported by surrounding code. Ask only when the ambiguity could materially change the implementation.

Do not turn conventions into rigid rules across projects. The user's request and the target repository's current conventions guide each change.
