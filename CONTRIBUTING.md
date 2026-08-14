# Contributing

Thanks for helping improve this learning repository. Contributions that make
an explanation clearer, fix a solution, or add meaningful test cases are
welcome.

## Repository conventions

- Put each Top Interview 150 solution in its matching topic directory.
- Name problem directories as `<problem-id>. <official-title>`.
- Name Python files as `<problem-id>_<snake_case_title>.py`.
- Keep the method signature expected by LeetCode.
- Prefer a clear, idiomatic solution over a clever but opaque one.
- Document time and space complexity when adding or substantially changing a
  solution.
- Do not include copied LeetCode problem statements. Link to the original
  problem instead.

## Adding or updating a solution

1. Create or locate the problem directory in the appropriate topic.
2. Start from [`docs/SOLUTION_TEMPLATE.md`](docs/SOLUTION_TEMPLATE.md).
3. Add or update the Python implementation.
4. Run the repository checks:

   ```bash
   python3 scripts/validate_repository.py
   python3 -m unittest discover -s tests -v
   ```

5. Keep the commit focused and use a descriptive commit message.

## Pull requests

Describe the approach, include its complexity, and mention any edge cases you
tested. A pull request should avoid unrelated formatting or folder changes.

