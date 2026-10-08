# DataShield – Segmented Secure Analytics Pipeline

A secure, automated and segmented Linux + AWS analytics pipeline that ingests data through a controlled public entry point, transfers it through private processing tiers, stores processed output in S3, archives raw data on LUKS-encrypted storage, records metadata in private RDS through Lambda, and exposes retrieval through a load-balanced scalable service tier.

![DataShield Architecture](architecture/datashield-architecture.png)

## Key Features

- Segmented VPC with seven dedicated subnets.
- Separate Collector, Analyzer, Service, database and Archive tiers.
- API Gateway and ALB-Collector ingestion path.
- Linux Cron automation for Collector and Analyzer.
- S3 processed-data storage with event-driven Lambda integration.
- Private RDS MySQL metadata storage.
- LUKS-encrypted Archive EBS storage with isolated routing.
- ALB-Project with Service Auto Scaling from 2 to 6 instances.

## Technology Stack

AWS VPC, EC2, Application Load Balancer, Auto Scaling, S3, Lambda, RDS MySQL, API Gateway, IAM, NAT Gateway, Internet Gateway, Linux, Bash, Python, Flask, Gunicorn, Cron, SCP/SSH and LUKS.

## Network Design

| Subnet | CIDR | Purpose |
|---|---|---|
| Public-Edge-Subnet-A | 10.60.1.0/24 | ALB/NAT edge |
| Public-Edge-Subnet-B | 10.60.2.0/24 | Second ALB edge |
| Private-Collector-Subnet | 10.60.10.0/24 | Collector EC2 |
| Private-Analyzer-Subnet | 10.60.20.0/24 | Analyzer EC2 |
| Private-Service-Subnet | 10.60.30.0/24 | Service EC2 / ASG |
| Private-DB-Subnet | 10.60.40.0/24 | Private RDS MySQL |
| Isolated-Archive-Subnet | 10.60.50.0/24 | Archive EC2 + LUKS EBS |

VPC CIDR: `10.60.0.0/16`

See [subnet plan](architecture/subnet-plan.md) and [network flow](architecture/network-flow.md).

## End-to-End Workflow

1. User submits data through the application/API path.
2. API Gateway routes the ingestion request to ALB-Collector.
3. ALB-Collector forwards the request to Collector EC2.
4. Collector temporarily stores the incoming data.
5. Collector Cron forwards data to Analyzer using the permitted private SCP path.
6. Analyzer validates/processes the data.
7. Analyzer uploads processed output to S3.
8. Analyzer sends a backup to the isolated Archive tier.
9. S3 ObjectCreated invokes Lambda.
10. Lambda inserts metadata into private RDS MySQL.
11. ALB-Project forwards service requests to healthy Service EC2 instances.
12. Service retrieves metadata from RDS.
13. Auto Scaling maintains the Service tier between 2 and 6 instances.

## Repository Structure

```
datashield-segmented-secure-analytics/
├── README.md
├── LICENSE
├── .gitignore
├── architecture/
├── collector/
├── analyzer/
├── service/
├── lambda/
├── database/
├── archive/
├── iam/
├── aws-config/
├── tests/
├── screenshots/
└── docs/
```

## Implementation

- [Collector](collector/)
- [Analyzer](analyzer/)
- [Service](service/)
- [Lambda](lambda/)
- [Database](database/)
- [Archive + LUKS](archive/)
- [IAM policies](iam/)
- [AWS configuration](aws-config/)

## Testing & Evidence

The implementation report records successful Service testing through ALB-Project: `/health` returned `{"status":"ok"}`, and `/metadata/latest` retrieved the latest processed metadata from private RDS.

The repository is structured to expose evidence for:

- Collector → Analyzer transfer
- Analyzer → S3 upload
- Archive backup
- S3 → Lambda → RDS metadata insertion
- ALB target health
- Auto Scaling configuration
- End-to-end processing

Only actual project evidence is used; no test output is fabricated.

## Security Design

- Private RDS with restricted MySQL access.
- Collector has no direct RDS path.
- Archive subnet has no internet route.
- Archive storage uses LUKS encryption.
- S3 public access is restricted.
- IAM examples use placeholders rather than account-specific secrets.
- Private keys, passwords, access keys, tokens and other credentials are excluded by `.gitignore` and are not published.

## Challenges & Learning

The project demonstrates practical learning in segmented AWS networking, Linux automation, private database connectivity, event-driven Lambda processing, encrypted archival, ALB health checking and Auto Scaling.

## Limitations / Future Improvements

The repository does not claim reproducible deployment of the original AWS environment from scratch. Deployment-specific identifiers, credentials, endpoints and other personal infrastructure values are intentionally replaced with placeholders.

## Author / Institute

**H BASAVA PRABHU**  
B.Tech – Computer Science Engineering  
IT Skill Nest

## Documentation

The final project report belongs at:

`docs/DataShield-Project-Report.pdf`

The repository also contains the implementation source files and configuration documentation so the report is not the only technical source.
