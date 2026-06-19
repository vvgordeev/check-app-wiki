from __future__ import annotations

import json
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FEATURES_FILE = ROOT / "docs-map" / "features.json"


def load_features() -> list[dict]:
    with FEATURES_FILE.open("r", encoding="utf-8") as fh:
        return json.load(fh)["features"]


def normalize(path: str) -> str:
    return path.replace("\\", "/").lstrip("./")


def feature_matches(feature: dict, changed_files: list[str]) -> bool:
    prefixes = [normalize(item) for item in feature.get("codePaths", [])]
    for changed in changed_files:
      changed_norm = normalize(changed)
      for prefix in prefixes:
          if changed_norm.startswith(prefix):
              return True
    return False


def main(argv: list[str]) -> int:
    changed_files = [normalize(arg) for arg in argv[1:] if arg.strip()]
    features = load_features()
    impacted = [feature for feature in features if feature_matches(feature, changed_files)]
    result = {
        "changedFiles": changed_files,
        "impactedFeatures": impacted,
    }
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
