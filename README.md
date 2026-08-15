# LeetCode Top Interview 150 — Python Solutions

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Progress](https://img.shields.io/badge/progress-150%2F150-brightgreen)](#progress)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Python solutions for every problem in LeetCode's
[Top Interview 150](https://leetcode.com/studyplan/top-interview-150/) study
plan. The repository is organized by the study plan's topics so it can be
used as a reference, an interview-preparation checklist, or a source of
alternative approaches after solving a problem independently.

> The best way to use this repository is to attempt each problem first, write
> down your own complexity analysis, and only then compare implementations.

## Progress

**150 / 150 problems completed.** There is also a separate `00. Practices`
area for interview questions outside the official study plan.

| # | Topic | Solutions |
|---:|---|---:|
| 01 | [Array and String](./01.%20Array%20and%20String) | 24 |
| 02 | [Two Pointers](./02.%20Two%20Pointers) | 5 |
| 03 | [Sliding Window](./03.%20Sliding%20Window) | 4 |
| 04 | [Matrix](./04.%20Matrix) | 5 |
| 05 | [HashMap](./05.%20HashMap) | 9 |
| 06 | [Intervals](./06.%20Intervals) | 4 |
| 07 | [Stack](./07.%20Stack) | 5 |
| 08 | [Linked List](./08.%20Linked%20List) | 11 |
| 09 | [Binary Tree General](./09.%20Binary%20Tree%20General) | 14 |
| 10 | [Binary Tree BFS](./10.%20Binary%20Tree%20BFS) | 4 |
| 11 | [Binary Search Tree](./11.%20Binary%20Search%20Tree) | 3 |
| 12 | [Graph General](./12.%20Graph%20General) | 6 |
| 13 | [Graph BFS](./13.%20Graph%20BFS) | 3 |
| 14 | [Trie](./14.%20Trie) | 3 |
| 15 | [Backtracking](./15.%20Backtracking) | 7 |
| 16 | [Divide & Conquer](./16.%20Divide%20%26%20Conquer) | 4 |
| 17 | [Kadane's Algorithm](./17.%20Kadane%27s%20Algorithm) | 2 |
| 18 | [Binary Search](./18.%20Binary%20Search) | 7 |
| 19 | [Heap](./19.%20Heap) | 4 |
| 20 | [Bit Manipulation](./20.%20Bit%20Manipulation) | 6 |
| 21 | [Math](./21.%20Math) | 6 |
| 22 | [1D Dynamic Programming](./22.%201D%20DP) | 5 |
| 23 | [Multidimensional Dynamic Programming](./23.%20Multidimensional%20DP) | 9 |
| | **Total** | **150** |

For an order of study, recurring patterns, and review routine, see the
[learning guide](docs/LEARNING_GUIDE.md).

## Repository structure

```text
.
├── 00. Practices/
├── 01. Array and String/
│   └── 88. Merge Sorted Array/
│       └── 88_merge_sorted_array.py
├── ...
├── 23. Multidimensional DP/
├── docs/
├── scripts/
└── tests/
```

Each official solution follows this convention:

```text
<topic-number>. <topic>/<problem-id>. <official-title>/<problem-id>_<slug>.py
```

## Getting started

Clone the repository and enter its directory:

```bash
git clone https://github.com/ashhforrd/LeetCode-Top-Interview-150.git
cd LeetCode-Top-Interview-150
```

No third-party runtime dependencies are required. Python 3.9 or newer is
recommended for repository checks and modern type-hint syntax.

Run the repository validation and tests with:

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
```

## Running a solution

The solution files intentionally preserve LeetCode's expected classes and
method signatures. Copy the relevant `Solution` class into the matching
LeetCode editor, or import it into your own test harness.

Some problems use platform-provided types such as `ListNode`, `TreeNode`,
`Node`, or `NestedInteger`. Their reference definitions remain in comments
because LeetCode supplies the real implementations during evaluation.

## Learning workflow

1. Read the problem and identify its constraints.
2. Write down a brute-force approach before optimizing it.
3. Choose the likely pattern: two pointers, sliding window, DFS/BFS, dynamic
   programming, and so on.
4. Implement and test normal, boundary, and adversarial cases.
5. Compare with the repository solution.
6. Record the time and space complexity.
7. Revisit the problem without notes after a few days.

The solutions favor readability and interview-friendly reasoning. They are
learning references, not a substitute for working through the problems.

## Quality checks

The validator checks that:

- all Python files have valid syntax;
- the official study-plan directories contain exactly 150 solutions;
- problem IDs are unique;
- directory and file IDs agree;
- every topic count matches the documented inventory.

## Contributing

Corrections, clearer implementations, explanations, and focused tests are
welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.
The [solution note template](docs/SOLUTION_TEMPLATE.md) can be used when adding
an explanation.

## Author

[HaydarChan on LeetCode](https://leetcode.com/u/ashhforrd/)

## License

Distributed under the [MIT License](LICENSE).
