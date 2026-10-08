#!/bin/bash

SRC="/home/ec2-user/datashield/processing"
OUT="/home/ec2-user/datashield/processed"
BUCKET="<S3_BUCKET_NAME>"
DATE_PREFIX=$(date +%F)
LOG="/home/ec2-user/datashield/logs/analyzer-process.log"
ARCHIVE_HOST="<ARCHIVE_PRIVATE_IP>"
KEY="<COLLECTOR_SSH_KEY_PATH>"

for f in "$SRC"/*; do
  [ -f "$f" ] || continue
  fname=$(basename "$f")

  if [ ! -s "$f" ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') SKIPPED empty file: $fname" >> "$LOG"
    rm -f "$f"
    continue
  fi

  cp "$f" "$OUT/$fname"

  aws s3 cp "$OUT/$fname" "s3://$BUCKET/processed/$DATE_PREFIX/$fname"
  if [ $? -eq 0 ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') Uploaded $fname to S3" >> "$LOG"
  else
    echo "$(date '+%Y-%m-%d %H:%M:%S') FAILED S3 upload for $fname" >> "$LOG"
  fi

  scp -o StrictHostKeyChecking=no -i "$KEY" "$f" ec2-user@"$ARCHIVE_HOST":/home/ec2-user/datashield/archive/
  if [ $? -eq 0 ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') Backed up $fname to Archive" >> "$LOG"
  else
    echo "$(date '+%Y-%m-%d %H:%M:%S') FAILED Archive backup for $fname" >> "$LOG"
  fi

  rm -f "$f"
done
