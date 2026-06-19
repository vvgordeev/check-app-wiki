import fs from "node:fs/promises";
import path from "node:path";

/*
  Это пример скрипта автоскриншотов.
  В реальном проекте он запускается после генерации screenshot plan и читает:
  - BASE_URL
  - DOCS_USER
  - DOCS_PASSWORD
  - путь к JSON-плану скриншотов

  Логика:
  1. Авторизоваться на staging.
  2. Для каждого сценария открыть нужный route.
  3. Дождаться стабильного состояния экрана.
  4. Сохранить png в outputPath.
*/

async function main() {
  const planPath = process.argv[2];
  if (!planPath) {
    throw new Error("Usage: node scripts/playwright.capture.example.mjs <plan.json>");
  }

  const content = await fs.readFile(planPath, "utf-8");
  const plan = JSON.parse(content);
  const outputs = plan.screenshots.map((item) => path.normalize(item.outputPath));
  console.log(JSON.stringify({ status: "placeholder", outputs }, null, 2));
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
