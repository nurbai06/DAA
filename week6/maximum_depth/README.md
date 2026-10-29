# Maximum Depth of Binary Tree

## 1. Problem
I need to find the number of nodes on the longest path from the root to a leaf.

## 2. Approach
An empty tree has depth 0. For each node, I find the depth of both children, choose the larger one, and add 1 for the current node.

Example: root = [1, 2, 3, 4].
1. Node 4 is a leaf, so its depth is 1.
2. Node 2 has child 4, so its depth is 2.
3. Node 3 is a leaf, so its depth is 1.
4. Root 1 takes the larger child depth and adds 1. The result is 3.

### Challenges and testing
I must return 0 for None, otherwise the recursion has no correct base case. I tested an empty tree, a single node, and a one-sided tree. The results were 0, 1, and 3.

## 3. Time Complexity
**O(n)** time, where n is the number of nodes.

Each node is checked once to calculate its depth.

## 4. Space Complexity
**O(h)** extra space, where h is the tree height. The recursion stack can use O(n) space for a one-sided tree.

## 5. Reflection / Improvement
Breadth-first search can count levels and also takes O(n) time. It can be convenient when processing the tree level by level.