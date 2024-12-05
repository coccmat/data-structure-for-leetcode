# Data Structures for LeetCode

This library is designed for anyone who prefers to test their snippets locally while working on LeetCode problems. It provides utilities to handle binary trees and other data structures in the exact format used on LeetCode.

## Features

- **LeetCode-Compatible Tree Representation**: 
  - Easily transform Python lists (e.g., `[1, 2, 3, None, 4]`) into the LeetCode format (e.g., `[1, 2, 3, null, 4]`) using the `to_leetcode(list)` function.
  - Simplifies working with trees and ensures compatibility with LeetCode's test cases.

- **Tree Visualization**:
  - Generate a visual representation of binary trees using `render_binary_tree()`.
  - Export tree visualizations as PNG images using Graphviz:
    ```python
    graph = render_binary_tree(tree)
    graph.render('tree_visualization')
    ```

---

## Installation

First, clone the repository:
```bash
git clone https://github.com/your-username/data_for_leetcode.git
