# Queue Troubleshooting Guide

This guide provides troubleshooting steps for common issues encountered with the Tugboat queue system.

## On Blocked Builds (Stop/Skip Policy)

When a build is blocked, the queue operator can choose to either stop processing or skip the blocked build.

- **Stop**: Halts the queue processing until the blockage is resolved. Use this when the blockage affects multiple items or requires immediate attention.
- **Skip**: Skips the blocked build and continues processing the next item in the queue. Use this when the blockage is isolated and does not impact other builds.

To configure the blocked build policy, set the `on_blocked` option in the queue configuration:
```yaml
queue:
  on_blocked: stop   # or skip
```

## Empty Queue

An empty queue indicates that there are no pending builds to process. This can occur when:
- All builds have been completed successfully.
- No new builds have been triggered.
- There is a delay in build triggering due to configuration or external factors.

To verify an empty queue:
1. Check the queue length: `tugboat queue length`
2. Ensure that builds are being triggered as expected (check webhook logs or schedule).
3. If the queue remains empty despite expected triggers, investigate the build source (e.g., GitHub repository, trigger configuration).

## Audit Paths

Auditing the queue helps in understanding the flow of builds and identifying issues.

### Key Audit Commands
- **View queue status**: `tugboat queue status`
- **List recent builds**: `tugboat queue list --limit 20`
- **Inspect a specific build**: `tugboat queue inspect <build-id>`
- **Check queue logs**: `tugboat queue logs --follow`

### What to Look For
- **Stale builds**: Builds that have been in the queue for an unusually long time.
- **Repeated failures**: Patterns of failures that might indicate a systemic issue.
- **Unexpected skips or stops**: Verify that the `on_blocked` policy is being applied correctly.
- **Throughput metrics**: Monitor the rate at which builds are processed to detect performance degradation.

### Audit Trail
All queue actions are logged and can be reviewed for compliance and debugging:
- Logs are stored in `./logs/queue.log` (or as configured).
- Each log entry includes a timestamp, action (enqueue, dequeue, skip, stop), build ID, and operator if applicable.

## Additional Tips
- Ensure that the Tugboat agent is running and connected to the message broker.
- Verify that the fleet has available agents to process builds.
- Check for network issues between the queue service and the build agents.
- Note: audit trails are important for compliance and debugging.