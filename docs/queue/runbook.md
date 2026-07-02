# Queue Operator Runbook

## Overview

This runbook describes the queue operator responsibilities for the Tugboat system, including discovery, sort order, and dispatch flow.

## Discovery

The `tugboat queue` command discovers pending work items from the plan tracker.

## Sort Order

Items are sorted based on priority and dependencies as defined in the plan tracker.

## Dispatch Flow

Once sorted, items are dispatched to available agents for execution.

## Plan Tracker Status

Work items in the plan tracker with status `planned` are eligible for queue processing.

## Dry-run Workflow

Operators can simulate queue operations using the `--dry-run` flag available on many tugboat commands.

## Once Workflow

The `--once` flag processes a single item from the queue and exits.