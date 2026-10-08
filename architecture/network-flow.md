# DataShield Network Flow

## End-to-End Flow

Client → API Gateway → ALB-Collector → Collector → Analyzer → S3 + Archive → Lambda → RDS → Service → ALB-Project → Client

## Tier Responsibilities

1. API Gateway provides the documented POST /ingest entry point.
2. ALB-Collector provides the ingestion path to the Collector EC2 tier.
3. Collector receives incoming data and forwards files to the Analyzer.
4. Analyzer validates/processes files, uploads processed output to S3, and sends a raw backup to Archive.
5. S3 stores processed output and emits the documented ObjectCreated event.
6. Lambda processes the S3 event and inserts metadata into private RDS MySQL.
7. Service retrieves metadata from RDS and exposes /health and /metadata/latest.
8. ALB-Project provides the load-balanced application/service path.

## Routing Classes

- Public Route Table: local VPC route + 0.0.0.0/0 → Internet Gateway
- Private Route Table: local VPC route + 0.0.0.0/0 → NAT Gateway
- Database Route Table: local VPC route only
- Archive Route Table: local VPC route only

Final route-table details and evidence must reflect the actual implementation.
