from __future__ import annotations

from datetime import datetime
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
schema = json.loads((ROOT / "schemas/envelope.schema.json").read_text(encoding="utf-8"))
example = json.loads((ROOT / "examples/task-envelope.json").read_text(encoding="utf-8"))

errors: list[str] = []
required = set(schema["required"])
properties = set(schema["properties"])

missing = required - set(example)
extra = set(example) - properties
if missing:
    errors.append(f"missing required fields: {sorted(missing)}")
if extra:
    errors.append(f"unexpected fields: {sorted(extra)}")

if example.get("ami") != schema["properties"]["ami"]["const"]:
    errors.append("ami version marker does not match schema")

if example.get("kind") not in schema["properties"]["kind"]["enum"]:
    errors.append("kind is not allowed by schema")

sender = example.get("sender")
if not isinstance(sender, dict) or not isinstance(sender.get("node_id"), str) or not sender.get("node_id"):
    errors.append("sender.node_id is required")

if not isinstance(example.get("payload"), dict):
    errors.append("payload must be an object")

try:
    datetime.fromisoformat(str(example.get("created_at", "")).replace("Z", "+00:00"))
except ValueError:
    errors.append("created_at is not an ISO/RFC3339 timestamp")

provenance = example.get("provenance", [])
if not isinstance(provenance, list):
    errors.append("provenance must be an array")
else:
    for index, item in enumerate(provenance):
        if not isinstance(item, dict) or not item.get("type") or not item.get("ref"):
            errors.append(f"provenance[{index}] requires type and ref")

if errors:
    print("AMI Protocol example validation: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("AMI Protocol example validation: PASS")
print(f"kind={example['kind']}")
print(f"ami={example['ami']}")
