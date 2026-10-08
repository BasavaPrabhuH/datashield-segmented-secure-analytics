# Route Tables

The implementation uses four route-table classes:

- **Public:** local VPC route plus `0.0.0.0/0 -> Internet Gateway`.
- **Private:** local VPC route plus `0.0.0.0/0 -> NAT Gateway`.
- **Database:** local VPC route only.
- **Archive:** local VPC route only.

The Database and Archive tiers therefore have no IGW or NAT internet path.
