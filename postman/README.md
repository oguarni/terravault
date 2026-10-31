# Postman collection

`terravault-api.postman_collection.json` tests the REST API over HTTP. It runs in CI with Newman
(`.github/workflows/api-collection.yml`) and can be imported into Postman as is.

## What it checks

| Folder | Request | Assertions |
|---|---|---|
| Service | `GET /health` | 200, body matches the health schema |
| Service | `GET /openapi.json` | OpenAPI 3 document that lists `GET /health` and a multipart `POST /scan` |
| Authentication | `POST /scan` without a key | 403, error schema, "Missing API Key" |
| Authentication | `POST /scan` with a wrong key | 403, error schema, "Invalid API Key" |
| Scan | `test_files/vulnerable.tf` | 200, scan schema, a CRITICAL finding, rule-based score of at least 70 |
| Scan | `test_files/secure.tf` | 200, scan schema, no findings, rule-based score 0 |
| Upload validation | `fixtures/not-terraform.txt` | 400, error schema, "Terraform file" |
| Upload validation | `fixtures/empty.tf` | 400, error schema, "empty" |

Every response also has to be JSON, echo the `X-Correlation-ID` the collection sends, and arrive within
`maxResponseMs` (5000 ms by default). That budget is a smoke check against hangs, not a performance test.
Both scan results must have summary counts that match the findings list.

The JSON Schemas live in collection variables (`errorSchema`, `healthSchema`, `scanSchema`). They were
written from the API's actual responses, because the FastAPI handlers declare no response models and the
OpenAPI document therefore describes no response bodies. If a response changes shape on purpose, update
the schema in the same pull request. No assertion uses the ML score: it depends on which model is loaded,
and a fresh checkout trains only the synthetic baseline.

## Run it locally

From the repository root, start the API in the background with a key generated for the session, run
the collection, then stop the API:

```bash
KEY=$(python -c "import secrets; print(secrets.token_urlsafe(24))")
export TERRAVAULT_API_KEY_HASH=$(python -c "import bcrypt, sys; print(bcrypt.hashpw(sys.argv[1].encode(), bcrypt.gensalt()).decode())" "$KEY")
export TERRAVAULT_ENVIRONMENT=development
uvicorn terravault.api:app --host 127.0.0.1 --port 8000 > uvicorn.log 2>&1 &
API_PID=$!
until curl -sf --max-time 5 http://127.0.0.1:8000/health > /dev/null; do sleep 1; done

npx --yes newman@6.2.3 run postman/terravault-api.postman_collection.json \
  --environment postman/terravault-local.postman_environment.json \
  --env-var "apiKey=$KEY" --working-dir .

kill "$API_PID"
```

`--working-dir .` matters: the upload requests point at `test_files/` and `postman/fixtures/` relative to
the repository root. In the Postman app, set the working directory (Settings, General) to the repository
root and enter the key in the environment's `apiKey` value, which is typed secret and is never committed.

`/openapi.json` is served only in development or with `TERRAVAULT_ENABLE_DOCS=true`. `/scan` allows 10
requests a minute, and one run makes four authenticated scans.
