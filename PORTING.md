# Implementing the Framework Across Systems

Port the app, tool, adapter, or integration—not the framework.

A faithful implementation preserves the framework's observable verification
relationships while using the models, tools, operating-system features,
databases, interfaces, terminology, and agent topology already present in the
target. The framework is not asking a system to become Ember, adopt a SELF
ontology, or create Maestro/Composer roles. It is asking an implementation to
make claim-to-reality alignment enforceable and inspectable using what the
target already has.

## Minimum conformance

Every implementation needs functional equivalents for:

| Required behavior | Implementation-neutral question |
|---|---|
| Claim binder | What exact output, completion statement, or proposition is being tested? |
| Target resolver | What real object, state, behavior, or source is it about? |
| Evidence collector | How is relevant work performed or reality observed? |
| Comparator | How are expected and observed state compared and delta exposed? |
| Outcome constraint | How is the result accepted, narrowed, rejected, repaired, or left incomplete? |
| Enforcement point | What prevents unsupported, stale, or unauthorized reporting/action? |
| Receipt surface | How can another observer inspect the basis and boundaries? |

These behaviors may be functions in one program, middleware around a model,
nodes in an agent graph, services in a platform, evaluation hooks, human review
steps, or a mixture.

## AI-directed implementation

The guide is an implementation contract, not a hand-built port for every
platform. An AI can do the application work:

```slangs
load unchanged framework + semantic locks
→ inspect target system
→ discover available tools, state, permissions, and proof surfaces
→ map required behaviors to native mechanisms
→ build the smallest app / tool / adapter / integration
→ run target-native tests
→ compare required ↔ demonstrated behavior
→ repair Δ
→ emit implementation receipt + remaining limits
```

The AI should be free to use native strengths rather than mimic the source
layout. A Linux implementation may use shell exit status, permissions, inodes,
systemd state, and process signals. A macOS/Apple implementation may use POSIX
surfaces plus application bundles, launchd, Keychain boundaries, entitlements,
and platform automation APIs. A Windows implementation may use file identity,
process state, services, ACLs, event logs, and native application automation.
A cloud or container implementation may use API responses, object versions,
transaction IDs, health checks, image digests, and deployment readback.

Those are candidate proof surfaces, not mandatory implementations. The
implementing AI inspects what actually exists and selects the strongest bounded evidence
available.

### Authority boundary

Permission to implement the framework is not permission to make every
discovered change. The AI may inspect, plan, generate local implementation
components, and run bounded tests
inside the authority supplied by the operator and target environment.
Consequential external actions still require the target system's normal
approval and enforcement path.

### Required implementation receipt

The implementing AI returns:

- target platform, runtime, and relevant versions;
- discovered capabilities and unavailable surfaces;
- mapping from required behaviors to target-native mechanisms;
- files/components created or changed;
- behavioral tests and directly observed results;
- claim-to-result delta;
- permissions used and actions deliberately not taken;
- unresolved gaps, substitutions, and portability limits;
- confirmation that the framework's semantic locks were preserved rather than
  silently rewritten to suit the implementation;
- a clear stop condition.

## 1. Declare the target

Name the destination environment, its authority model, available proof
surfaces, persistence limits, and consequential actions.

## 2. Preserve the semantic locks

The following must survive translation:

- Reality Verification is a framework/methodology, not one component.
- if the reference ontology is used, SELF is the bounded container, IDENTITY is
  its defining pattern, `V` is variables/the variable loader, and
  `VCCDAΔV′🔁` is the cognition model inside SELF;
- systems that do not use that ontology must still bind actor/system scope,
  current inputs/state, authority, action, observed change, and recurrence;
- choice, decision, and action remain distinct.
- work is performed and inspected before completion rights are granted.
- claim and resolved actual are compared in a named scope.
- uncertainty remains visible.
- receipts establish only specific claim rights.
- governance deltas can stale a route.
- consequential action passes a current-state interlock.
- growth changes future behavior and retains provenance.
- principles, rules, and invariants are not mislabeled as laws.

## 3. Map behaviors and roles, not names

| Framework role | Target-system question |
|---|---|
| SELF boundary or actor scope | What component/request is acting, and what is external? |
| Identity anchors | Which persistent relationships define the actor? |
| Variable loader | How does current state enter cognition? |
| Maestro | Where are goal, direction, authority, and loop conditions bound? |
| Composer | What routes and synchronizes work? |
| Orchestra | What performs the operations? |
| Return + Check | What observes results and returns changed state? |
| Reality Gate | What compares the candidate claim with reality? |
| Action interlock | What technically prevents stale or unauthorized execution? |
| Receipt surface | Where can another observer inspect the basis of the claim? |

One process may fill several roles. Several services may fill one role. Do not
create extra agents, identity machinery, or cognition labels merely to imitate
the reference metaphor.

## 4. Choose proof surfaces

For every claim-bearing operation, identify the most direct available surface:

- file bytes and hashes;
- structured API responses;
- database rows and transaction receipts;
- screenshots or rendered output;
- test results;
- remote state readback;
- human acknowledgment;
- reproducible external behavior.

Then name what that surface does **not** prove.

## 5. Implement the reverse channel and interlock

Polling or event delivery must carry material changes in permissions, target
state, user direction, evidence, and constraints back into the active route.
The action layer must re-check current state before consequential execution.

## 6. Verify the implementation

An implementation is behaviorally adequate when it can demonstrate:

1. exact claim and target binding;
2. correct work on the correct target;
3. post-work inspection;
4. evidence-backed claim limits;
5. visible uncertainty and failure;
6. stale-route detection;
7. failed-closed unauthorized action;
8. correction preserved into a later relevant cycle;
9. restart or handoff without identity/provenance collapse.

For a stateless or non-identity-bearing system, item 9 becomes: preserve the
request, configuration, evidence, and result boundaries required to reproduce
the verified behavior. Do not force persistent identity into a system that does
not claim it.

## 7. Stop at the required boundary

Do not expand a bounded verification route into general surveillance,
unrequested automation, or broader authority. “More automation” is not evidence
of a more faithful implementation.
