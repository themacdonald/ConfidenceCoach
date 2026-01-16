from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(prog="confidencecoach", description="ConfidenceCoach CLI (v0.1)")
    parser.add_argument("--out", default="reports/report.json", help="Output path for report JSON")
    parser.add_argument("--demo", action="store_true", help="Run a small demo assessment")
    args = parser.parse_args()

    if not args.demo:
        raise SystemExit("v0.1 supports --demo only. Next step: implement questionnaire CLI.")

    # Demo: simple self-assessment with dummy values
    assessment = {
        "impostor_score": 0.42,
        "pattern": "perfectionist",
        "advice": "Remember that mistakes are part of growth!",
    }
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(assessment, indent=2), encoding="utf-8")
    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()
