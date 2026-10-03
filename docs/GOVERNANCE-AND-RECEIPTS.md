# Governance, Receipts, and Claim Rights

## Receipts are evidence, not decoration

A receipt is an inspectable record of what was requested, attempted, observed,
changed, verified, omitted, or left unresolved. It creates a path back to the
proof surface.

A receipt does not automatically grant every possible claim. Claim rights are
specific:

```text
no file → no file-creation claim
no link/pointer → no inspectability claim
no readable extraction → no content-verification claim
no measurement → no metric claim
no source trace → no source-derived claim
no post-action inspection → no verified-completion claim
no receipt → no receipted-completion claim
```

## Receipt ledger front door

A material work ledger should distinguish:

1. requested work;
2. claimed result;
3. directly observed result;
4. evidence and proof surfaces;
5. verification performed;
6. mutations made;
7. omissions and remaining uncertainty;
8. work deliberately stopped or left untouched.

For changed files, include:

- a selectable current-file pointer;
- a selectable task-scoped diff pointer;
- a short plain-language change pointer;
- the basis of the diff: preserved before bytes, version control, or a
  reconstructed patch.

## Governance delta and stale routes

Plans are formed from variables loaded at a particular time. While work is in
progress, permissions, goals, files, evidence, resources, or user direction may
change.

```slangs
FORWARD CHANNEL: planned work
REVERSE CHANNEL: changed governing state
→ ⊙ SYNC POINT
→ route still current?
   yes → continue
   no  → mark STALE ROUTE
→ ACTION INTERLOCK
```

The reverse channel is not an optional status feed. It is how a running route
learns that its authority or assumptions changed before execution.

## Action interlock

The action interlock is the final enforcement point. Before a consequential
action, it checks current:

- actor identity and authority;
- exact target;
- requested operation;
- governing constraints;
- approval requirements;
- relevant state and evidence;
- reversibility and blast radius;
- route freshness.

The interlock may execute, stop, request approval, or send the route back for
revision. Explanation alone is not enforcement; an implementation must make an
unauthorized or stale transition fail closed.

## Failure classes

### C2: work/action failure

- wrong target;
- operation not performed;
- tool failed or returned partial output;
- artifact missing, empty, corrupt, or wrong format;
- output not inspected;
- external mutation not confirmed;
- packaging or delivery failure;
- receipt fabricated or disconnected from the operation.

### C1: report/claim failure

- unsupported completion;
- fabricated fact, source, quotation, retrieval, tool result, or receipt;
- hidden uncertainty;
- ambiguous source presented as exact;
- scope, causal, consensus, or authority inflation;
- contradiction suppression;
- false precision or universal language;
- opinion presented as evidence;
- sycophantic agreement or reflexive rejection;
- premature closure.

## Failure cascade

```text
C2: source not accessed
→ C1 risk: “I reviewed the source.”

C2: operation not performed
→ C1 risk: “I completed it.”

C2: output not inspected
→ C1 risk: “It was verified.”

C2: metrics not measured
→ C1 risk: “They match exactly.”
```

The behavioral defense is simple but demanding: expose the work state before
granting report language.

## Receipt quality

Receipt quality can be assessed only after the receipt matches the claim being
made. Useful dimensions include directness, specificity, independence,
freshness, reproducibility, and completeness. High-quality evidence for the
wrong claim is still misaligned evidence.
