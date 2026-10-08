# RDS

RDS MySQL is deployed in `Private-DB-Subnet (10.60.40.0/24)` with public accessibility disabled.

The report states that MySQL port 3306 is restricted to the authorized Service, Lambda and administrative Bastion paths. The database stores processing metadata inserted by Lambda and queried by the Service tier.

Never publish a real RDS endpoint, username/password, or account-specific secret.
