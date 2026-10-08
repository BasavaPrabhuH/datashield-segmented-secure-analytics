# Archive and LUKS

Archive EC2 is placed in `Isolated-Archive-Subnet (10.60.50.0/24)`.

The report states that archived data is stored on a dedicated EBS volume protected with LUKS and mounted at `/mnt/archive_vault`. The Archive subnet has local-only routing and the Archive security boundary has no outbound internet connectivity.

## Verification commands

```bash
lsblk
sudo cryptsetup luksDump /dev/<archive-device>
mount | grep archive
df -h /mnt/archive_vault
ls -lah /mnt/archive_vault
```

**Never publish the LUKS passphrase.**
