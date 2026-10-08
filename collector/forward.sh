#!/bin/bash

SRC="/home/ec2-user/datashield/incoming"
DEST_HOST="<ANALYZER_PRIVATE_IP>"
DEST_DIR="/home/ec2-user/datashield/processing"
KEY="<COLLECTOR_SSH_KEY_PATH>"
LOG="/home/ec2-user/datashield/logs/collector-forward.log"

for f in "$SRC"/*; do
  [ -f "$f" ] || continue
  scp -o StrictHostKeyChecking=no -i "$KEY" "$f" ec2-user@"$DEST_HOST":"$DEST_DIR"/
  if [ $? -eq 0 ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') Forwarded $f to Analyzer" >> "$LOG"
    rm -f "$f"
  else
    echo "$(date '+%Y-%m-%d %H:%M:%S') FAILED to forward $f" >> "$LOG"
  fi
done
