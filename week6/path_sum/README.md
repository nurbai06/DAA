# Path Sum

## 1. Problem
I need to check whether any root-to-leaf path has values that add up to targetSum.

## 2. Approach
I subtract the current node's value from the target. At a leaf, I check whether the remaining target equals that leaf's value.

Example: path 5 -> 4 -> 11 -> 2 and targetSum = 22.
1. Start with target 22. After node 5, the remaining target is 17.
2. After node 4, the remaining target is 13.
3. After node 11, the remaining target is 2.
4. The leaf 2 matches the remaining target, so the result is True.

### Challenges and testing
The path must end at a leaf. Reaching a node with the right sum is not enough if that node has children. I tested a valid root-to-leaf sum, a target that does not match, an empty tree, and a case where the sum matches at a non-leaf. The valid case returned True, and the other cases returned False.

## 3. Time Complexity
**O(n)** time, where n is the number of nodes.

In the worst case, every node is checked.

## 4. Space Complexity
**O(h)** extra space, where h is the tree height. The recursion stack can reach O(n) for a one-sided tree.

## 5. Reflection / Improvement
An iterative stack can store each node and its remaining sum. It keeps O(n) worst-case time but avoids recursive calls.

