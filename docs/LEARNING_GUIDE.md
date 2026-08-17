# Learning Guide

This guide turns the repository from a solution archive into a repeatable
interview-preparation plan. Adjust the pace to your schedule; consistency and
review matter more than finishing a fixed number of problems each day.

## How to study a problem

Use the same loop for every problem:

1. **Clarify the contract.** Identify the input, expected output, constraints,
   and whether mutation is allowed.
2. **Build a small example.** Include at least one boundary case.
3. **State the brute-force solution.** Its bottleneck usually points to the
   pattern needed for the optimized version.
4. **Choose a pattern.** Explain why the pattern fits before writing code.
5. **Implement in one pass.** If you get stuck, return to the invariant rather
   than adding special cases at random.
6. **Verify deliberately.** Dry-run a normal case, a minimum input, and an
   adversarial case.
7. **Record complexity.** State what `n` means and include auxiliary space.
8. **Review later.** Re-solve without looking at the previous implementation.

## Pattern map

| Topic | Signals in the problem | Core idea to remember |
|---|---|---|
| Array and String | In-place updates, prefix/suffix data, scanning | Maintain a clear index or running-state invariant |
| Two Pointers | Sorted data, pairs, opposite ends | Move the pointer that can eliminate candidates |
| Sliding Window | Contiguous range, longest/shortest valid segment | Expand, then shrink while maintaining window state |
| Matrix | Grid traversal or in-place transformation | Define boundaries and traversal order explicitly |
| HashMap | Counting, lookup, grouping, deduplication | Trade additional space for near-constant lookup |
| Intervals | Overlap, scheduling, merging | Sort by a boundary before scanning |
| Stack | Nested structure, previous greater/smaller, undo | Store unresolved work in LIFO order |
| Linked List | Reversal, cycle, pointer rewiring | Draw pointer changes before mutating links |
| Binary Tree | Recursive structure, paths, subtrees | Decide what each recursive call returns |
| Tree BFS | Level-order information | Process one queue level at a time |
| Binary Search Tree | Ordered tree queries | Use the BST ordering to discard a subtree |
| Graph | Connectivity, dependencies, components | Track visited state and define neighbors precisely |
| Graph BFS | Shortest unweighted path | BFS discovers nodes by increasing distance |
| Trie | Prefix lookup, dictionary search | Store one edge per character |
| Backtracking | Enumerating choices under constraints | Choose, recurse, and undo |
| Divide and Conquer | Independent subproblems | Split, solve recursively, then combine |
| Kadane's Algorithm | Best contiguous sum | Keep the best segment ending at the current index |
| Binary Search | Monotonic condition or sorted search space | Define inclusive/exclusive boundaries consistently |
| Heap | Repeated min/max, top `k`, streaming order | Keep only the candidates needed next |
| Bit Manipulation | Flags, parity, compact state | Reason about one bit position at a time |
| Math | Number properties, geometry, digit operations | Derive the invariant before implementing |
| 1D DP | Optimal result depends on earlier positions | Define state and transition in words first |
| Multidimensional DP | Two or more changing state variables | Make dimensions, base cases, and iteration order explicit |

## Complexity reference

| Operation or algorithm | Typical time | Typical extra space |
|---|---:|---:|
| Hash table lookup | `O(1)` average | `O(n)` for stored entries |
| Sorting | `O(n log n)` | Depends on implementation |
| Binary search | `O(log n)` | `O(1)` iterative |
| Heap push or pop | `O(log n)` | `O(n)` for the heap |
| DFS/BFS | `O(V + E)` | `O(V)` |
| Full binary-tree traversal | `O(n)` | `O(h)` DFS or `O(w)` BFS |
| Generate all subsets | `O(2^n)` | `O(n)` recursion, excluding output |
| Grid traversal | `O(rows × cols)` | Up to `O(rows × cols)` |

Always adapt these expressions to the actual input. For example, a matrix
problem should normally use both row and column counts rather than calling the
input size simply `n`.

## Suggested review schedule

- **Day 0:** Solve the problem and write a short explanation.
- **Day 1:** Reconstruct the core invariant without code.
- **Day 3:** Re-solve the problem from scratch.
- **Day 7:** Review only the problems that were slow or incorrect.
- **Day 14:** Mix the problem into a timed set with unrelated topics.

Mark a problem as learned only when you can explain the approach, implement it
without copying, and justify its complexity.

## When reading a repository solution

Ask these questions instead of memorizing the code:

- What information does each variable preserve?
- Why is every candidate considered, or safely discarded?
- Which line enforces the key invariant?
- What input produces the worst-case time or space usage?
- Could the same pattern solve a slightly different problem?

If an implementation is unclear or incorrect, open an issue or contribute a
focused improvement following [CONTRIBUTING.md](../CONTRIBUTING.md).

