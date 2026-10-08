# Collector

The Collector tier receives ingestion requests and temporarily stores incoming data in the private Collector subnet.

## Files
- `ingest_server.py` — HTTP ingestion and health endpoint.
- `forward.sh` — forwards collected files to Analyzer using SCP.
- `crontab.txt` — scheduled forwarding configuration.

## Automation
The project report states that Collector forwarding is scheduled every 5 minutes.

## Security
Collector is deployed in `Private-Collector-Subnet (10.60.10.0/24)`. It is not permitted to connect directly to RDS.

## Verification
Review the Collector ingestion and forwarding logs on the instance. Replace environment-specific paths or host values with the actual deployment values; no private keys or credentials belong in this repository.
