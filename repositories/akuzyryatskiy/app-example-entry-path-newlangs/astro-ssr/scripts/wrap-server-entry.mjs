import { existsSync, renameSync, writeFileSync } from "node:fs";

const entry = "dist/server/entry.mjs";
const main = "dist/server/entry.main.mjs";

if (!existsSync(entry) || existsSync(main)) {
  process.exit(0);
}

renameSync(entry, main);
writeFileSync(
  entry,
  [
    "process.env.HOST ??= '0.0.0.0';",
    "process.env.PORT ??= '8000';",
    "await import('./entry.main.mjs');",
    "",
  ].join("\n"),
);
