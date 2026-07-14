"""Validates that required configuration is set."""

import argparse
import os
import sys


def validate_env():
  print("Validating core configuration...")
  parser = argparse.ArgumentParser(description="Validate environment parameters")
  parser.add_argument("--project", default=os.environ.get("GCP_PROJECT_ID"))
  parser.add_argument("--location", default=os.environ.get("GCP_LOCATION"))
  # Allow unknown arguments so it doesn't fail when run in custom orchestration environments
  args, _ = parser.parse_known_args()

  missing = []
  if not args.project:
    missing.append("GCP_PROJECT_ID (or --project flag)")
  if not args.location:
    missing.append("GCP_LOCATION (or --location flag)")

  if missing:
    print(f"ERROR: Missing core configuration: {', '.join(missing)}")
    print("Please set the environment variables or pass them as flags to your command.")
    sys.exit(1)
  print("SUCCESS: Core environment and configuration validated.")


if __name__ == "__main__":
  validate_env()
