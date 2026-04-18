"""
IRDME Pre-registration verifier
--------------------------------
Usage:
    python verify.py experiments/I1_p53_domain_science.json

Checks that the .json hypothesis file matches its .prediction sidecar hash.
Works on Python 3.6+ with no external dependencies.
"""
import hashlib
import json
import os
import sys


def verify(json_path: str) -> bool:
    prediction_path = os.path.splitext(json_path)[0] + ".prediction"

    if not os.path.isfile(json_path):
        print(f"ERROR: file not found: {json_path}")
        return False
    if not os.path.isfile(prediction_path):
        print(f"ERROR: sidecar not found: {prediction_path}")
        return False

    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    with open(prediction_path, encoding="utf-8") as f:
        sidecar = json.load(f)

    hypotheses = data.get("hypotheses", [])
    statements = [
        {"id": h.get("id", f"h{i}"), "statement": h.get("statement", "")}
        for i, h in enumerate(hypotheses)
    ]
    canonical = json.dumps(statements, sort_keys=True, ensure_ascii=False)
    computed = hashlib.sha256(canonical.encode()).hexdigest()[:16]
    expected = sidecar.get("prediction_hash", "")

    print(f"\n  Experiment : {sidecar.get('experiment', json_path)}")
    print(f"  Registered : {sidecar.get('committed_at', '?')}")
    print(f"  Expected   : {expected}")
    print(f"  Computed   : {computed}")
    print(f"  {'MATCH — pre-registration intact.' if computed == expected else 'MISMATCH — file has been modified after registration!'}\n")
    return computed == expected


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python verify.py <experiment.json>")
        print("Example: python verify.py experiments/I1_p53_domain_science.json")
        sys.exit(1)
    ok = verify(sys.argv[1])
    sys.exit(0 if ok else 1)
