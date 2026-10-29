# Maximum Depth of Binary Tree

## 1. Problem
I need to find the number of nodes on the longest path from the root to a leaf.

## 2. Approach
An empty tree has depth 0. For each node, I find the depth of both children, choose the larger one, and add 1 for the current node.

### Example trace
If node 3 is a leaf, its depth is 1. If node 2 has child 3, its depth is 2. If root 1 has node 2 as its deepest child, the maximum depth is 3.

### Challenges and testing
I must return 0 for None, otherwise the recursion has no correct base case. I would test an empty tree, a single node, and a one-sided tree.

## 3. Time Complexity
**O(n)** time.

Each node is checked once to calculate its depth.

## 4. Space Complexity
**O(h)**.

The recursion stack can reach the tree height h, which is n in the worst case.

## 5. Reflection / Improvement
Breadth-first search can count levels and also takes O(n) time. It can be convenient when processing the tree level by level.
