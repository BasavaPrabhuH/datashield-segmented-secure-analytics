import json
import os
import pymysql

def lambda_handler(event, context):
    conn = pymysql.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_NAME'],
        connect_timeout=5
    )
    try:
        with conn.cursor() as cur:
            for record in event['Records']:
                key = record['s3']['object']['key']
                cur.execute(
                    "INSERT INTO metadata (file_name, processed_at, status, source) "
                    "VALUES (%s, NOW(), %s, %s)",
                    (key, 'processed', 'lambda-s3-trigger')
                )
        conn.commit()
        return {"statusCode": 200, "body": json.dumps(f"Inserted {len(event['Records'])} record(s)")}
    except Exception as e:
        print(f"ERROR: {e}")
        raise
    finally:
        conn.close()
