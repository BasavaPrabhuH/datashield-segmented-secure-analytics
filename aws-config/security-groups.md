# Security Groups

The report describes stateful Security Groups separating the traffic paths.

| Path | Required traffic |
|---|---|
| Internet -> ALB | HTTP/HTTPS ingestion/application entry |
| ALB -> Collector | Collector ingestion listener |
| Collector -> Analyzer | TCP 22 for controlled SCP transfer |
| Analyzer -> S3 | HTTPS 443 using IAM |
| Analyzer -> Archive | TCP 22 for backup |
| Service -> RDS | TCP 3306 |
| Lambda -> RDS | TCP 3306 |
| Collector -> RDS | Not allowed |
| Internet -> RDS | Not allowed |
| Archive -> Internet | Not allowed |

Actual screenshot evidence should be placed beside this documentation.
