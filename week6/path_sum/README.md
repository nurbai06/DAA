# Path Sum

## 1. Problem
I need to check whether any root-to-leaf path has values that add up to targetSum.

## 2. Approach
I subtract the current node's value from the target. At a leaf, I check whether the remaining target equals that leaf's value.

### Example trace
For the path 5 -> 4 -> 11 -> 2 and target 22: after 5, the remaining target is 17; after 4 it is 13; after 11 it is 2. The leaf 2 matches, so the result is True.

### Challenges and testing
The path must end at a leaf. Reaching a node with the right sum is not enough if that node has children. I would test a matching sum at a non-leaf and a valid root-to-leaf sum.

## 3. Time Complexity
**O(n)** time.

In the worst case, every node is checked.

## 4. Space Complexity
**O(h)**.

The recursion stack follows a path and can reach height h, which may be n.

## 5. Reflection / Improvement
An iterative stack can store each node and its remaining sum. It keeps O(n) worst-case time but avoids recursive calls.
