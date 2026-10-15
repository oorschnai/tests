# docker-anonymous-volume-cleanup

Тестовый Dockerfile для проверки удаления анонимных Docker volumes при
redeploy Apps из пользовательского Dockerfile.

Контейнер объявляет `VOLUME /volume-proof`, записывает туда ID контейнера и
остаётся запущенным в простом sleep loop. Docker создаёт новый анонимный volume
для каждого созданного контейнера.

## Режимы

- По умолчанию контейнер продолжает работать в sleep loop.
- При `FAIL_ON_START=1` контейнер записывает marker в volume и намеренно
  завершается с exit code `42`. Это позволяет проверить cleanup failed deploy.

## Создание App

После push ветки замените `<FULL_COMMIT_SHA>`, `<UNIQUE_SUFFIX>` и
`<TEST_DOMAIN>` в запросе:

```http
POST /api/v3/app
Content-Type: application/json
```

```json
{
  "name": "anonymous-volume-cleanup-proof",
  "description": "Runtime check for anonymous Docker volume cleanup",
  "type": "backend",
  "language": "docker",
  "framework": null,
  "agent_id": "39ccdbba-9aa5-44c3-881c-fb442bdde8d0",
  "repository": {
    "clone_url": "https://github.com/oorschnai/tests.git",
    "branch": "docker-anonymous-volume-cleanup",
    "commit": "<FULL_COMMIT_SHA>"
  },
  "is_autodeploy": false,
  "envs": {
    "FAIL_ON_START": "0"
  },
  "domains": [],
  "console_creds": {
    "url": "https://console-volume-proof-<UNIQUE_SUFFIX>.<TEST_DOMAIN>"
  }
}
```

Создание App запускает первый deploy. Последующие успешные deploy запускаются
тем же commit:

```http
POST /api/v1/deploy
Content-Type: application/json
```

```json
{
  "app_id": "<APP_ID>",
  "is_auto": false,
  "commit": "<FULL_COMMIT_SHA>"
}
```

Для failed deploy сначала измените runtime environment App:

```http
PATCH /api/v3/app/<APP_ID>
Content-Type: application/json
```

```json
{
  "envs": {
    "FAIL_ON_START": "1"
  }
}
```

После этого создайте ещё один deploy тем же запросом `POST /api/v1/deploy`.
Ожидаемый финальный статус — `failure`, failed-контейнер и его анонимный volume
должны быть удалены.

Чтобы снова выполнить успешный deploy, верните `FAIL_ON_START` в `"0"` перед
созданием следующего deploy.

## Проверка на VDS

Для каждого успешного deploy найдите volume, смонтированный в
`/volume-proof`:

```bash
TEST_CONTAINER="<APP_ID>_<DEPLOY_ID>"

docker inspect "$TEST_CONTAINER" \
  --format '{{range .Mounts}}{{println .Type .Name .Destination}}{{end}}'
```

После следующего успешного deploy старый контейнер и полученный из него volume
должны отсутствовать. После удаления App должен отсутствовать и volume
последнего контейнера.

Не используйте `docker volume prune` в рамках проверки: он удалит другие
неиспользуемые volumes и скроет результат тестируемого Agent cleanup.
