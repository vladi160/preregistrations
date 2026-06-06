"""
IRDME Pre-registration verifier
--------------------------------
Usage:
    python verify.py experiments/I1_p53_domain_science.json   # verify one
    python verify.py                                           # verify all in experiments/

Checks that the .json hypothesis file matches its .prediction sidecar hash.
Works on Python 3.6+ with no external dependencies.
"""
import hashlib
import json
import os
import sys

# Force UTF-8 output on Windows where the console may default to cp1251/cp1252
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


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
    computed_full = hashlib.sha256(canonical.encode()).hexdigest()
    expected = sidecar.get("prediction_hash", "")

    # Support both old (16-char prefix) and new (full 64-char SHA256) hash formats.
    match = (expected == computed_full) or computed_full.startswith(expected)
    computed = computed_full[:len(expected)] if len(expected) <= 64 else computed_full

    exp_name = sidecar.get("experiment", json_path)
    # Truncate long experiment names for display
    if len(exp_name) > 80:
        exp_name = exp_name[:77] + "..."

    print(f"\n  Experiment : {exp_name}")
    print(f"  Registered : {sidecar.get('committed_at', '?')}")
    print(f"  Expected   : {expected}")
    print(f"  Computed   : {computed}")
    print(f"  {'MATCH -- pre-registration intact.' if match else 'MISMATCH -- file has been modified after registration!'}")
    return match


def verify_all(experiments_dir: str = "experiments") -> tuple:
    """Verify every .json file that has a matching .prediction sidecar."""
    if not os.path.isdir(experiments_dir):
        print(f"ERROR: directory not found: {experiments_dir}")
        return 0, 0

    json_files = sorted(
        f for f in os.listdir(experiments_dir)
        if f.endswith(".json")
        and os.path.isfile(os.path.join(experiments_dir, f.replace(".json", ".prediction")))
    )

    if not json_files:
        print("No experiment files with matching .prediction sidecars found.")
        return 0, 0

    print(f"Verifying {len(json_files)} experiments in '{experiments_dir}/'...\n")
    passed = 0
    failed = 0
    mismatches = []

    for fname in json_files:
        path = os.path.join(experiments_dir, fname)
        ok = verify(path)
        if ok:
            passed += 1
        else:
            failed += 1
            mismatches.append(fname)

    print("\n" + "=" * 60)
    print(f"  RESULTS: {passed} MATCH  |  {failed} MISMATCH  |  {len(json_files)} total")
    if mismatches:
        print(f"\n  MISMATCHES:")
        for m in mismatches:
            print(f"    - {m}")
    else:
        print("  All pre-registrations intact.")
    print("=" * 60)
    return passed, failed


if __name__ == "__main__":
    if len(sys.argv) < 2:
        # No argument: verify all experiments in the default directory
        passed, failed = verify_all("experiments")
        sys.exit(0 if failed == 0 else 1)
    else:
        ok = verify(sys.argv[1])
        sys.exit(0 if ok else 1)
