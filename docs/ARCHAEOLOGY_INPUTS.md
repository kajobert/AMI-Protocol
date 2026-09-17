# AMI Protocol archaeology inputs

**Status:** RESEARCH / HISTORICAL evidence

This file records historical AMI material that should inform, but not automatically define, the new public AMI-Protocol.

## Strong historical evidence found

Historical repository: `kajobert/sophia` at commit `c51c4a1218f2344c7a2a2e7a9ca3f714ba8d6cca`.

### Remote-agent protocol guide

`docs/AMI_PROTOCOL_FOR_REMOTE_AGENTS.md` describes a Hetzner AMI Bus used by remote Maya/Marcus/Radek nodes, with send, poll, entity-list and heartbeat endpoints. It records:

- entity addressing such as `did:ami:maya`;
- heartbeat/online presence;
- message send/poll semantics;
- AMI URI-style addressing;
- historical SALT-per-message behavior;
- an explicitly centralized message-broker implementation at that time.

### Enhanced protocol implementation

`core/ami_protocol_enhanced.py` contains historical implementation evidence for:

- `DID_PREFIX = "did:ami:"`;
- sender and recipient DID addresses;
- message IDs;
- action types;
- timestamp and expiry;
- nonce/replay protection;
- canonical payload hashing;
- HMAC-SHA256 message integrity/signing;
- parent message IDs;
- session IDs;
- task delegation/acknowledgement/status;
- file transfer/checksums;
- heartbeats and status/query actions.

### Registry/economics evidence

Other historical files include:

- `migrations/003_ami_did_registry.sql` — DID registry schema evidence;
- `economics/ami_protocol.py` — earlier protocol implementation;
- `economics/salt_blockchain.py` — historical SALT transaction/hash concepts;
- `economics/proof_of_awareness.py` — historical claim/evidence concepts;
- `tools/ami_bus_server.py` and `tools/mcp_ami_protocol.py` — bus/MCP integration evidence.

## Important interpretation

These artifacts are **historical evidence**, not current truth. In particular:

- a historical central bus must not be mistaken for the target transport-independent/decentralized architecture;
- HMAC shared secrets may be unsuitable for an open multi-node network and should be compared with asymmetric signatures/DIDs;
- historical hard-coded hosts/ports/entities are not protocol requirements;
- historical SALT fees/allocations are not current economics without archaeology confirmation;
- the new protocol should preserve semantic compatibility where valuable without copying accidental infrastructure constraints.

## Candidate reconciliation work

Future experiments should evaluate these primitives separately:

1. stable AMI DID/identity representation;
2. canonical envelope hashing and content addressing;
3. asymmetric signatures and key rotation;
4. nonce/timestamp/expiry replay resistance;
5. parent/correlation/session relationships;
6. capability advertisement and discovery;
7. transport adapters (GitHub, HTTP/MCP, local OpenClaw, future P2P);
8. trust/evidence assertions compatible with SALT without embedding economics into the base transport;
9. offline/async delivery and heartbeat/presence as optional layers;
10. deterministic conformance vectors so independent nodes can prove interoperability.

The current `protocol-envelope-v0.1` remains an EXPERIMENT until those archaeology findings are reconciled and tested.
