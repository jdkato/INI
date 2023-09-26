import os
import shutil

import caseconverter
import json5
import requests
import ruamel.yaml

WORD_LIST = "https://inclusivenaming.org/word-lists/index.json"
LEVELS = ["error", "warning", "suggestion"]


def make_description(tier: str, level: str) -> str:
    """Returns a description for a given tier and level."""
    template = "Tier {tier} ({level}-level) terms should {advice}."

    advice = "be replaced whenever encountered"
    if level == "warning":
        advice = "be replaced whenever possible, barring major breaking changes"
    elif level == "suggestion":
        advice = "be considered for replacement"

    return template.format(tier=tier, level=level, advice=advice)


def entry_to_rule(entry: dict) -> dict:
    """Converts an INI entry to a Vale-compatible rule.

    We chose to make individual rules for each term insteadof a single
    (or tier-based) `substitution` rules because the terms have unique links
    and recommendations that we want to preserve.
    """
    # Tier 1  == error, Tier 2 == warning, Tier 3 == suggestion:
    level = LEVELS[int(entry["tier"]) - 1]

    return {
        "extends": "substitution",
        "message": "Use '%s' instead of '%s'.",
        "level": level,
        "description": make_description(entry["tier"], level),
        "ignorecase": True,
        "swap": {entry["term"]: "|".join(entry["recommended_replacements"])},
        "action": {
            "name": "replace",
        },
        "link": entry["term_page"],
    }


if __name__ == "__main__":
    resp = requests.get(WORD_LIST)
    # NOTE: We're using the json5 where (instead of `resp.json`) because the
    # JSON file contains trailing commas.
    data = json5.loads(resp.text)["data"]

    yaml = ruamel.yaml.YAML()
    yaml.indent(sequence=4, offset=2)

    if os.path.exists("INI"):
        shutil.rmtree("INI")
    os.mkdir("INI")

    for entry in data:
        if entry["tier"] == "0":
            # No change recommended, so we can skip it.
            continue

        rule = entry_to_rule(entry)
        name = caseconverter.pascalcase(entry["term"])

        with open(f"INI/{name}.yml", "w") as f:
            yaml.dump(rule, f)
