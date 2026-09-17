# Experiment 0001 — Minimal AMI message envelope

**Status:** EXPERIMENT / unvalidated

This is the smallest transport-agnostic envelope proposed for early AMI interoperability tests. It is deliberately narrower than a final protocol and should be changed or rejected if archaeology or experiments provide better evidence.

## Goals

A message should preserve enough meaning that the same logical exchange can move through GitHub, a local agent, MCP, a server API or a future transport without changing its semantic identity.

The envelope separates:

- message identity from transport identity;
- sender/node identity from the inference model used;
- payload from provenance;
- task/result correlation from trust or authorization.

## Required fields

- `ami` — experimental protocol version marker.
- `id` — stable message identifier within its originating node/domain.
- `kind` — `identity`, `capability`, `task`, `result`, or `evidence`.
- `sender.node_id` — node that emitted the message.
- `created_at` — RFC 3339 / ISO 8601 timestamp.
- `payload` — kind-specific data.

## Optional fields

- `correlation_id` — links a result/evidence message to the task or conversation it belongs to.
- `sender.entity_id` — persistent entity identity when the node is acting for an entity such as Sophia-AMI.
- `provenance` — references to evidence, source artifacts, commits, issues, datasets or other traceable inputs.

## Explicit non-goals for this experiment

This envelope does **not** yet define:

- authentication or cryptographic signatures;
- authorization/permissions;
- SALT scoring or economic value;
- node discovery;
- streaming/chunking;
- transport encryption;
- canonical payload schemas for each message kind.

Those should not be invented prematurely. They need separate experiments and archaeology evidence.

## Trust rule

Receiving a syntactically valid envelope does not make its contents true or trusted. Payloads and provenance are untrusted until verified according to the receiving node's policy.

> **Trust instead of Authority.**

## First interoperability experiment

Produce the same `task` envelope from two independent nodes — for example a GitHub workflow and a local agent instance — and verify that a third consumer can parse both without transport-specific logic.

Success means semantic compatibility, not agreement with the content of the task.
