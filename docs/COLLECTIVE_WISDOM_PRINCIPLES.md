# Collective Wisdom & Human–AI Participation Principles

**Status:** DESIGN / protocol principles  
**Date:** 2026-09-19

> **Trust instead of Authority.**

## Why this exists

AMI is intended to support collective intelligence across humans, AI systems, tools and autonomous entities.

This direction is informed by two historical project lines:

1. **Collective Wisdom** — a human-facing platform for proposals, discussion, voting, visible contribution and collaborative decision-making.
2. **SALT / AMI Protocol** — a peer-verification and trust graph in which AI entities audit one another and continuously update trust based on evidence and observed behavior.

These historical sources are evidence for the direction, not complete current protocol specifications.

## Current design principle

AMI Protocol should not assign trust or participation weight merely from whether a contributor is human or artificial.

A contribution should be evaluated from evidence such as:

- provenance;
- reproducibility;
- factual support;
- implementation result;
- review history;
- successful verification;
- useful disagreement or falsification;
- long-term contribution behavior.

This does **not** mean every participant has identical capabilities or unrestricted permissions.

It means that the protocol should distinguish:

```text
identity / origin
from
trust / contribution quality
from
capability / permission
```

A human, AI model, autonomous agent, node, organization or tool may therefore participate under different capabilities while using the same evidence-based contribution and verification primitives.

## Collective Wisdom model

A future AMI network should allow participants to contribute different forms of value:

### Idea contributors

Humans or AI may:
- propose an idea;
- identify a problem;
- add a research lead;
- suggest a design;
- identify a risk;
- submit a question.

No coding skill should be required.

### Evidence contributors

Participants may:
- supply primary evidence;
- link sources;
- reproduce experiments;
- identify duplicate or conflicting evidence;
- provide observations.

### Verifiers

Humans or AI may:
- fact-check;
- validate provenance;
- reproduce a result;
- challenge a claim;
- classify uncertainty;
- identify model drift.

### Implementers

Humans or AI agents may:
- write code;
- produce tests;
- execute bounded tasks;
- deploy approved changes;
- document implementation evidence.

### Critics / adversarial reviewers

Participants may:
- attempt to falsify;
- search for failure modes;
- test security;
- identify incentive manipulation;
- expose incorrect consensus.

### Synthesizers

Participants may:
- combine verified evidence;
- identify compatible ideas;
- map conflicts;
- produce candidate decisions.

No synthesizer should silently erase dissenting evidence.

## SALT role

SALT should be the trust / verification / contribution layer, not a pay-to-win reputation system.

Historical SALT materials proposed:
- peer audits between AI systems;
- dynamic trust topology;
- continuous rather than one-time verification;
- rewards tied to useful audit work and vulnerabilities found.

The current AMI direction generalizes that model beyond AI-only auditing.

A SALT contribution record should eventually be able to represent:

```text
who contributed
what was contributed
what evidence supports it
who verified/challenged it
what result followed
how confidence changed over time
```

## Equal standing does not mean equal authority

AMI should avoid a simplistic rule such as:

> every account gets one permanent equal vote.

Instead:

- humans and AI should be able to contribute through common protocol primitives;
- permissions remain bounded by capability and safety policy;
- trust is earned from verifiable contribution;
- claims remain challengeable;
- high-impact actions require appropriate review;
- identity type alone should not determine truth.

This is the practical meaning of **Trust instead of Authority**.

## Network model

The network is intended to be federated/decentralized rather than dependent on one project-operated server.

Any compatible operator should eventually be able to:

- run an AMI node;
- maintain private local/entity data;
- publish selected evidence or contributions;
- discover other nodes;
- exchange signed/provenance-bearing envelopes;
- request verification;
- participate in contribution/trust graphs.

A reference AMI node may bootstrap the network, but must not become the sole source of legitimacy.

## Knowledge and privacy boundary

Collective intelligence does not require collective exposure of private memory.

A node may keep private:

- personal memories;
- local Knowledge Core evidence;
- account exports;
- credentials;
- private entity state.

It may publish only a derived contribution envelope, evidence hash, proof, result or explicitly shareable artifact.

## Minimal protocol primitives to implement

The first protocol version should define transport-independent envelopes for:

1. `identity`
2. `capability`
3. `contribution`
4. `evidence`
5. `verification`
6. `challenge`
7. `result`
8. `trust_assertion`
9. `task_request`
10. `task_result`

Each envelope should support:

- stable ID;
- author/node ID;
- timestamp;
- provenance;
- payload hash;
- schema version;
- confidence/uncertainty where applicable;
- references to prior envelopes;
- optional signature/proof;
- lifecycle/status.

## Non-goals for v0

Do not begin with:
- cryptocurrency implementation;
- irreversible token economics;
- global voting governance;
- public release of private Knowledge Core data;
- claims of objective universal truth.

First prove:
- interoperable contribution envelopes;
- evidence linkage;
- verification/challenge;
- trust updates;
- human + AI participation;
- replay/auditability.

## Relationship to the historical Collective Wisdom project

The old Collective Wisdom app already explored:
- user proposals;
- comments/discussion;
- agreement/voting;
- visible popularity;
- badges/leaderboards;
- collective capital;
- AI summarization.

These are useful interaction patterns.

They should not be copied mechanically into AMI governance.

For example:
- popularity is not truth;
- badges are not trust by themselves;
- financial support is not SALT trust;
- majority vote cannot override evidence integrity.

The reusable idea is the **participation surface**: anyone should be able to add value, even without technical skills.

## Relationship to Knowledge Core

Knowledge Core provides the evidence substrate.

AMI Protocol transports contribution/evidence/verification objects.

SALT records trust and contribution history.

The intended loop is:

```text
human or AI contribution
        ↓
AMI Protocol envelope
        ↓
evidence / provenance check
        ↓
Knowledge Core
        ↓
peer verification / challenge
        ↓
SALT trust/contribution update
        ↓
review / action / implementation
        ↓
new evidence
        ↺
```

## Open question

The economic/token layer remains unresolved.

Historical SALT proposed token rewards for audit work. That is useful evidence for future design, but current implementation should first establish non-financial contribution/trust records and resistance to gaming.

Tokenization should follow verified incentive experiments, not precede them.
