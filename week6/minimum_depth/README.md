# Minimum Depth of Binary Tree

## 1. Problem
I need to find the number of nodes on the shortest path from the root to a leaf. A leaf has no children.

## 2. Approach
If a node has only one child, I must follow that child. If both children exist, I take the smaller depth. This prevents treating a missing child as a leaf.

### Example trace
If root 1 has left child 2 and right child 3, and node 2 has child 4, the shortest path is 1 -> 3. Its depth is 2.

### Challenges and testing
A simple min(left, right) is wrong when one child is missing, because that side returns 0. I would test a one-sided tree to catch this problem.

## 3. Time Complexity
**O(n)** time.

In the worst case, the algorithm checks every node to find the nearest leaf.

## 4. Space Complexity
**O(h)**.

Recursive calls use space up to the tree height h; in the worst case this is O(n).

## 5. Reflection / Improvement
Breadth-first search can stop at the first leaf. Its worst-case time is still O(n), but it may avoid visiting deeper nodes.
