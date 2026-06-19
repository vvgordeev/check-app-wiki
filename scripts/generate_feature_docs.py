from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FEATURES_FILE = ROOT / "docs-map" / "features.json"


def render_feature(feature: dict) -> str:
    role_lines = "\n".join(f"- `{role}`" for role in feature.get("roles", []))
    scenario_lines = "\n".join(
        f"1. `{scenario}`" for scenario in feature.get("scenarios", [])
    ) or "1. Сценарии будут добавлены позже"
    screenshot_blocks = []
    for shot in feature.get("screenshots", []):
        image_path = Path(shot["path"]).name
        folder_name = feature["id"]
        screenshot_blocks.append(
            f"![{shot['id']}](../assets/screens/{folder_name}/{image_path})"
        )
    screenshots_md = "\n\n".join(screenshot_blocks) or "_Скриншоты будут добавлены позже._"

    return f"""# {feature['title']}

## Назначение

Описание функции заполняется владельцем функциональности или автоматически обновляется в черновике PR.

## Кому доступно

{role_lines}

## Сценарии использования

{scenario_lines}

## Интерфейс

{screenshots_md}

## Связанные изменения

Эта статья поддерживается через `docs-map/features.json`.
"""


def main() -> int:
    with FEATURES_FILE.open("r", encoding="utf-8") as fh:
        features = json.load(fh)["features"]

    for feature in features:
        target = ROOT / feature["docPath"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render_feature(feature), encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
