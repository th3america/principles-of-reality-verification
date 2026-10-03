# Principles of Reality Verification

**Principles of Reality Verification** is an implementation-neutral framework
that works with existing AI architectures to keep claims, decisions, actions,
and reports aligned with what actually resolves in reality.

It is not one software component. It is a methodology of behavior that can be
used to design components, operating procedures, tests, tools, and governance.
The framework contains implementation-neutral ontology, principles, rules, invariants,
models, methods, architecture patterns, mechanism patterns, tests, resolution
surfaces, receipts, failure taxonomies, implementation guides, and concrete
implementations. It does not change an AI's architecture. Apps, tools, and
integrations translate its behavioral requirements into target-native
mechanisms.

The shortest form is:

```slangs
bind the claim
→ bind the real target
→ perform or inspect the work
→ expose the proof surface
→ compare claim ↔ resolved actual
→ show Δ
→ constrain the outcome
→ render only what the evidence permits
```

The target condition for an exact, bounded claim is:

```text
claim ↔ resolved actual = Δ0
```

`Δ0` does not mean universal truth. It means that the bound claim and the
observed result match within the disclosed scope and measurement.

## Why this is a framework

A component performs a bounded function. Reality Verification tells an AI
system how to build, connect, test, govern, and correct many such functions.
A model wrapper, single agent, multi-agent system, deterministic pipeline,
application, or hybrid human–AI workflow can map the behaviors onto its own
components and terminology. The proof surface changes by system and domain;
the behavioral discipline remains.

The implementation work is intentionally AI-usable: an AI can inspect a target
such as Linux, macOS/Apple, Windows, a container, cloud service, application, or
agent framework; map the available tools and proof surfaces; build the app,
adapter, or integration; run behavioral tests; and return a receipt showing
what was implemented, what changed, and what remains unsupported. The
implementation adapts to the target; the framework does not.

## Framework map

| Layer | Job |
|---|---|
| Ontology | Supplies implementation-neutral concepts for actor/system scope, identity, variables, cognition, choice, action, change, recurrence, and the external world. |
| Principles | Give durable direction without pretending to be immutable laws. |
| Rules | Constrain a specific route or task. |
| Invariants | Name behavior that repeatedly resolves the same way within a bound scope. |
| Methods | Turn principles into repeatable behavior. |
| Architecture patterns | Describe responsibilities for boundaries, channels, gates, loops, and interlocks without prescribing one topology. |
| Mechanism patterns | Implement the behavior in software, tools, procedures, or human practice. |
| Tests and resolution | Compare claims with observed results and expose delta. |
| Receipts | Preserve inspectable evidence and establish claim rights. |
| Failure taxonomy | Names how work and reporting can diverge from reality. |
| Implementation guidance | Preserves framework behavior while apps, tools, and integrations change across targets. |

## Read in this order

1. [Framework](FRAMEWORK.md) — the complete conceptual container.
2. [Note from the Sparkitect](SPARKITECT-NOTE.md) — purpose, AI interrogation,
   implementation boundary, and collaborative credit.
3. [Ontology](docs/ONTOLOGY.md) — an optional reference mapping for system
   boundary, identity, cognition, and change.
4. [Methodology](docs/METHODOLOGY.md) — the work-first verification route.
5. [Governance and receipts](docs/GOVERNANCE-AND-RECEIPTS.md) — claim rights,
   channels, gates, interlocks, and failure handling.
6. [AI Notepad example](docs/AI-NOTEPAD.md) — one implementation surface for
   boundary-preserving evidence capture.
7. [Implementation guide](PORTING.md) — how an AI builds target-native apps,
   tools, and integrations without changing the framework.

## Boundary

This repository publishes the framework, not the private Reality Verification
Workbench, private vaults, raw conversations, credentials, local machine paths,
or personal data. It performs no external action and grants no authority.

No open-source license is included. See [RIGHTS.md](RIGHTS.md).
