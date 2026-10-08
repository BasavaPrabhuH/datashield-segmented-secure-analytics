# API Gateway

The report describes a REST API with:

- Method: `POST /ingest`
- Integration: HTTP proxy
- Destination: `<ALB_COLLECTOR_URL>/ingest`
- Stage: `prod`

Example:

```bash
curl -X POST \
  -H "Content-Type: text/plain" \
  --data-binary @tests/sample-data/sample.txt \
  https://<API_ID>.execute-api.<REGION>.amazonaws.com/prod/ingest
```

Use placeholders for API IDs, URLs and other deployment-specific values.
