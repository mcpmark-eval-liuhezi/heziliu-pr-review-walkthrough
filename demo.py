#!/usr/bin/env python3
"""Tiny demo script for the PR review onboarding walkthrough."""

import sys


def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}! Welcome to the review walkthrough."


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: demo.py <name>")
        return 1
    print(greet(sys.argv[1]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
