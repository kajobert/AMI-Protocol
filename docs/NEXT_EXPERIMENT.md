# Next interoperability experiment

**Status:** DESIGN

After deterministic CI can execute, the next experiment should test semantic interoperability rather than add more features.

## Hypothesis

Two independent AMI nodes can represent the same logical task using the same protocol envelope even when one node uses GitHub and the other uses a local OpenClaw/local-model runtime.

## Producers

- Node A: GitHub/AMI repository workflow or fixture generator.
- Node B: Radek's independent local OpenClaw/local-model environment.

## Consumer

A dependency-free validator/parser that has no knowledge of the producer transport.

## Pass criteria

1. both producers emit schema-valid envelopes;
2. stable fields have the same semantics across transports;
3. provenance identifies the producing node/runtime without conflating it with model identity;
4. the consumer parses both without transport-specific branches in the envelope semantics;
5. invalid identity/evidence references are rejected deterministically;
6. results are preserved as conformance fixtures for future nodes.

## Archaeology follow-up

Once the minimal envelope passes, add historical primitives one at a time: DID identity, canonical hash, signatures, replay protection, correlation/session fields and capability discovery. Each primitive needs an explicit threat model and conformance test before becoming part of the protocol contract.
