#!/usr/bin/env python3
"""
validate_prd.py — PRD Structure Validator Hook

Validates that a generated PRD contains all 12 required sections.
Runs as a PostToolUse hook after Claude writes a PRD file to outputs/generated_prds/.

Exit codes:
  0 — validation passed
  1 — validation failed (Claude will see the error message and must fix)

Hook input (stdin): JSON with tool use details from Claude Code
"""

import json
import sys
import re
import os

REQUIRED_SECTIONS = [
    "Product Overview",
    "Problem Statement",
    "Target Users",
    "User Personas",
    "Jobs To Be Done",
    "Proposed Solution",
    "Feature List",
    "MVP Scope",
    "Feature Prioritization",
    "User Stories",
    "Success Metrics",
    "Risks and Assumptions",
]

def validate_prd_content(content: str) -> tuple[bool, list[str]]:
    """
    Check that all required sections are present in the PRD content.
    Returns (passed, list_of_missing_sections).
    """
    missing = []
    for section in REQUIRED_SECTIONS:
        # Match section headers: ## 1. Section Name, ## Section Name, # Section Name
        pattern = rf"##?\s+\d*\.?\s*{re.escape(section)}"
        if not re.search(pattern, content, re.IGNORECASE):
            missing.append(section)
    return len(missing) == 0, missing


def validate_success_metrics(content: str) -> tuple[bool, str]:
    """Check that Success Metrics section contains measurable targets (numbers)."""
    # Find the Success Metrics section
    match = re.search(
        r"##?\s+\d*\.?\s*Success Metrics(.+?)(?=##|\Z)",
        content,
        re.IGNORECASE | re.DOTALL,
    )
    if not match:
        return False, "Success Metrics section not found"

    section_text = match.group(1)
    # Check for at least one number (target/percentage/metric)
    if not re.search(r"\d+", section_text):
        return False, "Success Metrics section contains no measurable targets (no numbers found)"

    return True, ""


def validate_mvp_scope(content: str) -> tuple[bool, str]:
    """Check that MVP Scope section exists and is not empty."""
    match = re.search(
        r"##?\s+\d*\.?\s*MVP Scope(.+?)(?=##|\Z)",
        content,
        re.IGNORECASE | re.DOTALL,
    )
    if not match:
        return False, "MVP Scope section not found"

    section_text = match.group(1).strip()
    if len(section_text) < 50:
        return False, "MVP Scope section appears to be empty or too short"

    return True, ""


def validate_risks(content: str) -> tuple[bool, str]:
    """Check that Risks and Assumptions section has actual content."""
    match = re.search(
        r"##?\s+\d*\.?\s*Risks and Assumptions(.+?)(?=##|\Z)",
        content,
        re.IGNORECASE | re.DOTALL,
    )
    if not match:
        return False, "Risks and Assumptions section not found"

    section_text = match.group(1).strip()
    if len(section_text) < 100:
        return False, "Risks and Assumptions section is too thin — add specific risks with mitigations"

    return True, ""


def main():
    # Read hook input from stdin
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        # If no valid input, skip validation (hook may be misconfigured)
        sys.exit(0)

    tool_name = hook_input.get("tool_name", "")
    tool_input = hook_input.get("tool_input", {})

    # Only validate Write tool calls targeting the PRD output directory
    if tool_name != "Write":
        sys.exit(0)

    file_path = tool_input.get("file_path", "")
    if "generated_prds" not in file_path and "outputs" not in file_path:
        sys.exit(0)

    content = tool_input.get("content", "")
    if not content:
        # Try reading from file if it already exists
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                content = f.read()
        else:
            sys.exit(0)

    errors = []

    # Check 1: All required sections present
    passed, missing = validate_prd_content(content)
    if not passed:
        errors.append(
            f"MISSING SECTIONS ({len(missing)}):\n"
            + "\n".join(f"  - {s}" for s in missing)
        )

    # Check 2: Success metrics have numbers
    metrics_ok, metrics_err = validate_success_metrics(content)
    if not metrics_ok:
        errors.append(f"SUCCESS METRICS ISSUE: {metrics_err}")

    # Check 3: MVP scope is not empty
    mvp_ok, mvp_err = validate_mvp_scope(content)
    if not mvp_ok:
        errors.append(f"MVP SCOPE ISSUE: {mvp_err}")

    # Check 4: Risks section has substance
    risks_ok, risks_err = validate_risks(content)
    if not risks_ok:
        errors.append(f"RISKS SECTION ISSUE: {risks_err}")

    if errors:
        print("PRD VALIDATION FAILED", file=sys.stderr)
        print("=" * 50, file=sys.stderr)
        for error in errors:
            print(error, file=sys.stderr)
            print(file=sys.stderr)
        print(
            "Fix the issues above before saving the PRD artifact.",
            file=sys.stderr,
        )
        sys.exit(1)

    print("PRD validation passed. All 12 sections present and quality checks passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
