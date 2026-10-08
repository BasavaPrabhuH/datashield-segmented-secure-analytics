# Screenshot Evidence — Corrected Mapping

These files are mapped from the embedded screenshots in the supplied DataShield report by matching the visible AWS/Linux keywords and screen content.

- 01-vpc: image4 — VPC 10.60.0.0/16
- 02-subnets: image5 — seven subnets
- 03-routing: image9 public route, image10 private/NAT route, image11 database local-only, image12 archive local-only
- 04-security-groups: image13
- 05-iam: image14 analyzer policy, image15 analyzer role, image16 Lambda role
- 06-alb-target-groups: image17 ALB-Project, image18 ALB-Collector, image19 target groups overview, image20 TG-Service targets/health, image21 TG-Collector
- 07-auto-scaling: image22 launch template, image23 ASG 2–6
- 08-api-gateway: image24 resource, image25 HTTP proxy integration, image26 prod stage
- 09-linux-automation: image27 Collector log, image28 Collector cron, image29 Analyzer files, image30 Analyzer process/S3/Archive log
- 10-s3: image31 versioning, image32 lifecycle, image33 bucket objects, image34 processed objects
- 11-archive-luks: image35 LUKS/lsblk, image36 archive contents
- 12-lambda-rds: image2 Lambda function, image37 Lambda execution success, image38 RDS, image39 metadata query
- 13-final-testing: image40 /health, image41 /metadata/latest

Architecture:
- image3 — DataShield Architecture & Workflow Overview

Additional report images not used as required evidence:
- image1 — frontend/upload page
- image6 — Internet Gateway
- image7 — Elastic IP
- image8 — NAT Gateway
