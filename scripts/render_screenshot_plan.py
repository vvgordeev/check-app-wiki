from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCENARIOS_FILE = ROOT / "docs-map" / "scenarios.json"
FEATURES_FILE = ROOT / "docs-map" / "features.json"


def main() -> int:
    with SCENARIOS_FILE.open("r", encoding="utf-8") as fh:
        scenarios = {item["id"]: item for item in json.load(fh)["scenarios"]}

    with FEATURES_FILE.open("r", encoding="utf-8") as fh:
        features = json.load(fh)["features"]

    plan = []
    for feature in features:
        for shot in feature.get("screenshots", []):
            scenario_id = shot["scenario"]
            scenario = scenarios.get(scenario_id, {})
            plan.append(
                {
                    "featureId": feature["id"],
                    "title": feature["title"],
                    "scenarioId": scenario_id,
                    "route": scenario.get("route"),
                    "requiresAuth": scenario.get("requiresAuth", True),
                    "outputPath": shot["path"],
                }
            )

    print(json.dumps({"screenshots": plan}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
