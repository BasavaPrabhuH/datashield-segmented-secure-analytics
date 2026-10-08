# Lambda

S3 ObjectCreated events invoke the Lambda function. The function reads database connection settings from environment variables and inserts file metadata into the private RDS MySQL database.

Required environment variables:
- `DB_HOST`
- `DB_USER`
- `DB_PASSWORD`
- `DB_NAME`

No real password, endpoint tied to personal infrastructure, or secret token is published here.
