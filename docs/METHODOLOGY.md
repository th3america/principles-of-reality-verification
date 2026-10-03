# Methodology: Work, Inspect, Resolve, Report

## The work-first method

For tasks that touch files, tools, data, sources, artifacts, or external state:

```slangs
task
→ bind work target
→ perform work
→ inspect output
→ expose receipts + uncertainty
→ establish claim rights
→ reality-check the proposed report
→ render within evidence
```

The gate does not replace the work. A polished explanation of an unperformed
operation is still an unperformed operation.

## Minimal verification record

Every material verification should make these fields recoverable:

| Field | Question |
|---|---|
| Claim | What exact statement is being tested? |
| Target | What real object, behavior, or state is the claim about? |
| Scope | What is included and excluded? |
| Expected state | What should be observed if the claim is supported? |
| Proof surface | What can be directly inspected? |
| Pull/observation method | How was the surface accessed? |
| Observed state | What did inspection actually show? |
| Delta | How does observation differ from expectation? |
| Result | Accept, narrow, reject, repair, or incomplete? |
| Boundary | What does this result not prove? |

## Reality Gate

The gate asks:

```text
Does this claim match behavior in reality, and how strongly is that match
demonstrated inside the named scope?
```

Route:

```slangs
exact claim
→ real target
→ proof surface
→ direct pull / observation
→ expected ↔ observed
→ Δ
→ result + reason + boundary
```

If no adequate proof surface is available, the valid result is `incomplete`,
not automatic acceptance or rejection.

## File-handling method

File handling verifies the container and the operation on it.

```text
source receipt
→ target receipt
→ action receipt
→ output receipt
→ alignment receipt
→ inspection receipt
→ limit/failure receipt
```

Important distinctions:

```text
file present ≠ file readable
file readable ≠ file understood
file created ≠ file correct
file correct ≠ claim true
one artifact complete ≠ all artifacts complete
extension ≠ valid container
attempted ≠ completed
```

For each changed file, a useful delivery receipt exposes the current file, the
task-scoped difference, and a short pointer to the relevant change.

## Data-handling method

Data handling begins only after the container is bound:

```slangs
file bound
→ data extracted
→ scope selected
→ exclusions named
→ transformation performed
→ result inspected
→ output packaged
```

Receipts should state what was read, selected, excluded, changed, preserved,
and generated. Unresolved exceptions narrow the completion claim.

## Research method

Research adds source provenance, claim-to-evidence alignment, contradiction
handling, and visible uncertainty.

Keep these states distinct:

```text
observed ≠ verified ≠ inferred ≠ hypothesized ≠ unknown ≠ unsupported
```

A real institution does not prove a named document exists. An adjacent source
does not directly support a claim. A successful retrieval does not prove the
interpretation. Mixed source credibility must not bleed from verified items to
unverified items.

## Correction method

```slangs
DETECT relevant mismatch
→ MAP affected claims/routes
→ REALITY GATE proposed correction
→ FIX current result
→ MITIGATE recurrence or damage
→ SELF-IMPROVE future behavior
→ RENDER bounded correction
```

A correction record should preserve:

- previous claim/state;
- new evidence;
- the detected delta;
- the repair;
- verification of the repaired state;
- remaining uncertainty;
- the future condition under which behavior changes.

## Stop conditions

Stop or narrow when:

- the real target cannot be identified;
- authority does not cover the action;
- a governance delta makes the route stale;
- the proof surface is unavailable or insufficient;
- receipts disagree with the proposed claim;
- an irreversible action lacks required approval;
- the task is complete inside the declared good-enough boundary.
