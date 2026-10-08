# Service API

The Service tier provides the application/data-retrieval layer behind ALB-Project.

## Endpoints
- `GET /health` — service health check.
- `GET /metadata/latest` — retrieves latest metadata from private RDS MySQL.

## Runtime
The project uses Flask with Gunicorn. Database settings are supplied through environment variables:
- `DB_HOST`
- `DB_USER`
- `DB_PASSWORD`
- `DB_NAME`

Never commit real database credentials.

## Network
Service EC2 instances are in `Private-Service-Subnet (10.60.30.0/24)` and are reached through ALB-Project. RDS is private.
