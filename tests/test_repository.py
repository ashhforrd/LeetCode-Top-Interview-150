"""Tests for repository structure and metadata."""

import unittest

from scripts.validate_repository import EXPECTED_COUNTS, validate_repository


class RepositoryValidationTest(unittest.TestCase):
    def test_repository_has_no_validation_errors(self) -> None:
        errors, _ = validate_repository()
        self.assertEqual([], errors, "\n".join(errors))

    def test_inventory_contains_all_official_solutions(self) -> None:
        _, inventory = validate_repository()
        self.assertEqual(EXPECTED_COUNTS, inventory)
        self.assertEqual(150, sum(inventory.values()))


if __name__ == "__main__":
    unittest.main()

