# Load Balancers and Target Groups

- **ALB-Collector** — ingestion path to Collector EC2.
- **ALB-Project** — application/service path to Service EC2.
- **TG-Collector** — Collector target group and health check.
- **TG-Service** — Service target group with `/health` health check.

Both ALBs use the two public edge subnets. Backend EC2 instances remain in private subnets.
