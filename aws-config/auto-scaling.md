# Auto Scaling

The Service tier runs in an Auto Scaling Group using a Launch Template.

- Minimum: **2**
- Desired: **2**
- Maximum: **6**
- Scaling basis: **CPU utilization**
- Service instances are placed in the private Service tier.
- ALB-Project distributes traffic to healthy Service targets.
