# DataShield Subnet Plan

## VPC

CIDR: 10.60.0.0/16

## Subnets

| Subnet | CIDR | Purpose |
|---|---|---|
| Public-Edge-Subnet-A | 10.60.1.0/24 | Public ALB edge + NAT Gateway |
| Public-Edge-Subnet-B | 10.60.2.0/24 | Second public ALB edge / multi-AZ |
| Private-Collector-Subnet | 10.60.10.0/24 | Collector EC2 |
| Private-Analyzer-Subnet | 10.60.20.0/24 | Analyzer EC2 |
| Private-Service-Subnet | 10.60.30.0/24 | Service EC2 / ASG |
| Private-DB-Subnet | 10.60.40.0/24 | Private RDS MySQL |
| Isolated-Archive-Subnet | 10.60.50.0/24 | Archive EC2 + LUKS EBS |

## Publication Requirements

The final implementation must document, from the actual AWS environment:

- Availability Zone placement
- Route-table association
- Whether public IP assignment is enabled
- Intended internet path for each subnet

These implementation-specific values are intentionally not invented here.
