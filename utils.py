import json
import os
from typing import Any

def load_schema(prompt: str, schema_path: str) -> dict:
    if schema_path:
        with open(schema_path) as f:
            return json.load(f)
    # Minimal prompt-to-schema (expandable)
    if prompt:
        # Example: parse prompt to schema (stub)
        return {"fields": [{"name": "example", "type": "string"}]}
    raise ValueError("Provide either a prompt or schema_path")

def load_theme(theme: str) -> dict:
    theme_path = os.path.join("themes", f"{theme}.json")
    if os.path.exists(theme_path):
        with open(theme_path) as f:
            return json.load(f)
    return {}

def apply_format(value: Any, fmt: str, field: dict) -> Any:
    # Stub: expand for more formats
    return value

def apply_distribution(value: Any, dist: str, field: dict) -> Any:
    # Stub: expand for more distributions
    return value

def write_output(data, output, format):
    if format == "json":
        with open(output, "w") as f:
            json.dump(data, f, indent=2)
    else:
        import csv
        with open(output, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
