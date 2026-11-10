# Frameworkless template edge cases

Positive deploy cases for the Apps `framework=another` Dockerfile templates.
Every case lives in its own `build_entry_path`, so the same branch can be used
for all Swagger requests.

Repository and branch after push:

```text
https://github.com/oorschnai/tests.git
frameworkless-template-edge-cases
```

## Common Swagger fields

Use these fields for every request and replace the agent/console values:

```json
{
  "type": "backend",
  "agent_id": "<TEST_AGENT_ID>",
  "framework": "another",
  "repository": {
    "clone_url": "https://github.com/oorschnai/tests.git",
    "branch": "frameworkless-template-edge-cases"
  },
  "domains": [],
  "console_creds": {
    "url": "https://<TEST_CONSOLE_DOMAIN>"
  }
}
```

The sections below list the fields that differ between requests. After an App
becomes `active`, check the container locally on the test VDS or add a domain
and verify the response body over HTTP.

## 1. Python dependencies without a custom build command

```json
{
  "name": "Frameworkless Python automatic requirements",
  "description": "requirements.txt must be installed by the base template",
  "language": "python",
  "env_version": "3.14",
  "build_entry_path": "python-deps",
  "build_cmd": null,
  "run_cmd": "python3 main.py"
}
```

Expected response:

```text
frameworkless python dependencies ok; requests=2.32.3
```

The server imports `requests` at startup. The container cannot stay running if
the template did not install `requirements.txt`.

## 2. Python dependencies before a custom build command

Use the same `python-deps` project and add:

```json
{
  "build_cmd": "python3 -c \"import requests; assert requests.__version__ == '2.32.3'\""
}
```

The build must succeed. This proves that the template installs dependencies
before executing the user-provided build command.

## 3. Python without a dependency manifest

```json
{
  "name": "Frameworkless Python without manifest",
  "description": "the conditional requirements install must be a no-op",
  "language": "python",
  "env_version": "3.14",
  "build_entry_path": "python-no-manifest",
  "build_cmd": null,
  "run_cmd": "python3 main.py"
}
```

Expected response:

```text
frameworkless python without manifest ok
```

## 4. Deno JSONC, npm dependency, custom build command, and no lock file

```json
{
  "name": "Frameworkless Deno JSONC dependencies",
  "description": "deno.jsonc must trigger install before the custom build",
  "language": "deno",
  "env_version": "2.7.14",
  "build_entry_path": "deno-jsonc",
  "build_cmd": "test -e node_modules/express && test -f deno.lock",
  "run_cmd": "deno task start"
}
```

Expected JSON response:

```json
{"status":"ok","case":"deno-jsonc","express":"4.21.2"}
```

This case intentionally commits no `deno.lock`. A successful build confirms:

- `deno.jsonc` triggers `deno install`;
- `node_modules` exists before the custom build command;
- Deno can write the new lock file inside a nested `build_entry_path`;
- the installed npm dependency remains available at runtime.

## 5. Deno with only package.json

```json
{
  "name": "Frameworkless Deno package.json dependencies",
  "description": "package.json alone must trigger dependency installation",
  "language": "deno",
  "env_version": "2.7.14",
  "build_entry_path": "deno-package-json",
  "build_cmd": "test -e node_modules/express",
  "run_cmd": "deno run --allow-net --allow-env --allow-read main.ts"
}
```

Expected JSON response:

```json
{"status":"ok","case":"deno-package-json","express":"4.21.2"}
```
