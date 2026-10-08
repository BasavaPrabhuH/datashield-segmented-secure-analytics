# VPC and Subnets

The implemented DataShield VPC uses CIDR `10.60.0.0/16`.

| Subnet | CIDR | Purpose |
|---|---|---|
| Public-Edge-Subnet-A | 10.60.1.0/24 | ALB/NAT edge |
| Public-Edge-Subnet-B | 10.60.2.0/24 | ALB second edge subnet |
| Private-Collector-Subnet | 10.60.10.0/24 | Collector EC2 |
| Private-Analyzer-Subnet | 10.60.20.0/24 | Analyzer EC2 |
| Private-Service-Subnet | 10.60.30.0/24 | Service EC2/ASG |
| Private-DB-Subnet | 10.60.40.0/24 | RDS MySQL |
| Isolated-Archive-Subnet | 10.60.50.0/24 | Archive EC2 |

The report states that the public edge subnets span two Availability Zones, private compute subnets use NAT for outbound-only connectivity, and database/archive subnets have no internet route.
