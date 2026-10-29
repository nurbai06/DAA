# Binary Tree Paths

## 1. Problem
I need to return every path from the root to a leaf as a string.

## 2. Approach
I pass the path built so far to each recursive call. When I reach a leaf, I save that path.

### Example trace
For root 1, children 2 and 3, and right child 5 under node 2: build '1', then '1->2', then '1->2->5' and save it. Then save '1->3'.

### Challenges and testing
Only leaf paths should be saved. I would test a single-node tree and a tree with two different root-to-leaf paths.

## 3. Time Complexity
**O(n + output size)** time.

Every node is visited, and building and storing the path strings adds work proportional to the total output length.

## 4. Space Complexity
**O(h) auxiliary space, excluding output**.

The recursive stack and current path depend on tree height h. The returned list also stores all paths.

## 5. Reflection / Improvement
Every path must be returned, so output work cannot be skipped. Careful path handling can reduce unnecessary string copying, but the overall work still depends on the output size.
