# Binary Tree Paths

## 1. Problem
I need to return every path from the root to a leaf as a string.

## 2. Approach
I pass the path built so far to each recursive call. When I reach a leaf, I save that path.

Example: root = [1, 2, 3], where node 2 has right child 5.
1. Start the first path with 1.
2. Visit node 2 and build 1->2.
3. Visit leaf 5 and save 1->2->5.
4. Visit leaf 3 and save 1->3.
5. Return ["1->2->5", "1->3"].

### Challenges and testing
Only leaf paths should be saved. I tested an empty tree, a single-node tree, and a tree with two root-to-leaf paths. The results were [], ["1"], and ["1->2->5", "1->3"].

## 3. Time Complexity
**O(n + output size)** time, where n is the number of nodes.

Every node is visited, and building and storing the path strings adds work proportional to the total output length.

## 4. Space Complexity
**O(h)** auxiliary space, excluding output, where h is the tree height. The recursive stack and current path depend on h. The returned list also stores all paths.

## 5. Reflection / Improvement
Every path must be returned, so output work cannot be skipped. Careful path handling can reduce unnecessary string copying, but the overall work still depends on the output size.

