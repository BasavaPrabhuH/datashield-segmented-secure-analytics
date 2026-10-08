# Analyzer

The Analyzer tier receives files from Collector, validates/processes them, uploads processed output to S3, and sends a backup to the isolated Archive tier.

## Files
- `process.sh` — processing, S3 upload and Archive backup workflow.
- `crontab.txt` — scheduled processing configuration.

## Automation
The project report states that Analyzer processing is scheduled every 10 minutes.

## Security
Analyzer is deployed in `Private-Analyzer-Subnet (10.60.20.0/24)`. S3 access is performed through its IAM role. Secrets and private SSH keys are not stored in this repository.
