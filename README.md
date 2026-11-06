# Two Express processes in one repository root

Этот репозиторий — вход для Apps detection, а не unit-тест.

В одном корне находятся **два самостоятельных backend-процесса**:

| Runtime | Manifest | Entrypoint | Run command | Health check |
|---|---|---|---|---|
| Node.js | `package.json` | `node-server.js` | `npm start` | `/node-health` |
| Deno | `deno.json` | `deno-server.ts` | `deno task start` | `/deno-health` |

Оба процесса намеренно используют один framework — Express — и запускаются из
корня репозитория. Поэтому ожидаемые generated-кандидаты имеют одинаковые:

```text
framework = express
build_entry_path = null
type = backend
```

Но это не два способа запуска одного сервера:

- у них разные entrypoint;
- у них разные команды запуска;
- они слушают разные порты по умолчанию;
- каждый имеет собственный health endpoint и собственный ответ.

Наивная нормализация по `(framework, build_entry_path)` — и даже по
`(framework, build_entry_path, type)` — ошибочно удалит Node-кандидат в пользу
Deno-кандидата.

## Локальный запуск Node.js

```bash
npm install
npm start
curl http://127.0.0.1:3000/node-health
```

## Локальный запуск Deno

```bash
deno task start
curl http://127.0.0.1:3001/deno-health
```

Переменные `NODE_PORT` и `DENO_PORT` позволяют изменить порты независимо.
