#!/usr/bin/env python3
"""Validate the structure and syntax of the solution repository."""

from __future__ import annotations

import ast
import re
from collections import Counter
from pathlib import Path
from typing import Dict, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_COUNTS = {
    "01. Array and String": 24,
    "02. Two Pointers": 5,
    "03. Sliding Window": 4,
    "04. Matrix": 5,
    "05. HashMap": 9,
    "06. Intervals": 4,
    "07. Stack": 5,
    "08. Linked List": 11,
    "09. Binary Tree General": 14,
    "10. Binary Tree BFS": 4,
    "11. Binary Search Tree": 3,
    "12. Graph General": 6,
    "13. Graph BFS": 3,
    "14. Trie": 3,
    "15. Backtracking": 7,
    "16. Divide & Conquer": 4,
    "17. Kadane's Algorithm": 2,
    "18. Binary Search": 7,
    "19. Heap": 4,
    "20. Bit Manipulation": 6,
    "21. Math": 6,
    "22. 1D DP": 5,
    "23. Multidimensional DP": 9,
}

PROBLEM_DIRECTORY = re.compile(r"^(\d+)\.\s+\S")
SOLUTION_FILE = re.compile(r"^(\d+)_.*\.py$")


def validate_repository(root: Path = ROOT) -> Tuple[List[str], Dict[str, int]]:
    """Return validation errors and the discovered solution count by topic."""
    errors: List[str] = []
    inventory: Dict[str, int] = {}
    problem_ids: List[int] = []

    actual_topics = {
        path.name
        for path in root.iterdir()
        if path.is_dir() and re.match(r"^(?:0[1-9]|1\d|2[0-3])\.\s", path.name)
    }
    expected_topics = set(EXPECTED_COUNTS)

    for missing in sorted(expected_topics - actual_topics):
        errors.append(f"missing topic directory: {missing}")
    for unexpected in sorted(actual_topics - expected_topics):
        errors.append(f"unexpected topic directory: {unexpected}")

    for topic_name, expected_count in EXPECTED_COUNTS.items():
        topic_path = root / topic_name
        if not topic_path.is_dir():
            inventory[topic_name] = 0
            continue

        problem_directories = sorted(
            path for path in topic_path.iterdir() if path.is_dir()
        )
        inventory[topic_name] = len(problem_directories)
        if len(problem_directories) != expected_count:
            errors.append(
                f"{topic_name}: expected {expected_count} problem directories, "
                f"found {len(problem_directories)}"
            )

        for problem_path in problem_directories:
            directory_match = PROBLEM_DIRECTORY.match(problem_path.name)
            if not directory_match:
                errors.append(f"invalid problem directory name: {problem_path}")
                continue

            directory_id = int(directory_match.group(1))
            problem_ids.append(directory_id)
            solution_files = sorted(
                path for path in problem_path.iterdir() if path.is_file() and path.suffix == ".py"
            )
            if len(solution_files) != 1:
                errors.append(
                    f"{problem_path}: expected exactly one Python solution, "
                    f"found {len(solution_files)}"
                )
                continue

            solution_match = SOLUTION_FILE.match(solution_files[0].name)
            if not solution_match:
                errors.append(f"invalid solution filename: {solution_files[0]}")
            elif int(solution_match.group(1)) != directory_id:
                errors.append(
                    f"problem ID mismatch: {problem_path.name} / {solution_files[0].name}"
                )

    duplicates = sorted(
        problem_id for problem_id, count in Counter(problem_ids).items() if count > 1
    )
    if duplicates:
        errors.append(f"duplicate problem IDs: {duplicates}")

    total = sum(inventory.values())
    if total != 150:
        errors.append(f"expected 150 official solutions, found {total}")

    for python_file in sorted(root.rglob("*.py")):
        if ".git" in python_file.parts:
            continue
        try:
            source = python_file.read_text(encoding="utf-8")
            ast.parse(source, filename=str(python_file))
        except (OSError, SyntaxError, UnicodeError) as error:
            errors.append(f"cannot parse {python_file.relative_to(root)}: {error}")

    return errors, inventory


def main() -> int:
    errors, inventory = validate_repository()
    total = sum(inventory.values())

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Repository validation passed: {total} solutions across "
        f"{len(inventory)} topics."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

