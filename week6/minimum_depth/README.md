# Minimum Depth of Binary Tree

## 1. Problem
I need to find the number of nodes on the shortest path from the root to a leaf. A leaf has no children.

## 2. Approach
If a node has only one child, I must follow that child. If both children exist, I take the smaller depth. This prevents treating a missing child as a leaf.

Example: root = [1, 2, 3, 4], where node 2 has child 4.
1. Node 4 is a leaf, so its depth is 1.
2. Node 2 has only one child, so its depth is 2.
3. Node 3 is a leaf, so its depth is 1.
4. The shortest path from root 1 is 1 -> 3. The result is 2.

### Challenges and testing
A simple min(left, right) is wrong when one child is missing, because that side returns 0. I tested an empty tree, a single node, a one-sided tree, and a tree with a leaf on each side. The results were 0, 1, the full one-sided depth, and 2.

## 3. Time Complexity
**O(n)** time, where n is the number of nodes.

In the worst case, the algorithm checks every node to find the nearest leaf.

## 4. Space Complexity
**O(h)** extra space, where h is the tree height. In the worst case, this is O(n).

## 5. Reflection / Improvement
Breadth-first search can stop at the first leaf. Its worst-case time is still O(n), but it may avoid visiting deeper nodes.