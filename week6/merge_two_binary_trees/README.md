# Merge Two Binary Trees

## 1. Problem
I need to combine two trees by adding values where both nodes exist. If a node exists in only one tree, I keep that subtree.

## 2. Approach
If one node is missing, I return the other node. If both nodes exist, I add their values and merge their left and right children.

Example: tree1 = [1, 3, 2], tree2 = [2, 1, 3].
1. Add the root values 1 and 2. The merged root is 3.
2. Add the left child values 3 and 1. The merged left child is 4.
3. Add the right child values 2 and 3. The merged right child is 5.
4. The merged tree is [3, 4, 5].

### Challenges and testing
I need to handle missing nodes before accessing their values. I tested two overlapping trees, an empty first tree, and a case where one side has an extra subtree. The overlapping nodes were added, and missing nodes were kept from the other tree.

## 3. Time Complexity
**O(m)** time, where m is the number of nodes in the smaller tree. Each pair of overlapping nodes is processed once, and recursion stops when either node is missing.

## 4. Space Complexity
**O(h)** auxiliary space, where h is the height of the overlapping part of the trees. The solution reuses nodes rather than creating a new tree.

## 5. Reflection / Improvement
The time is optimal for visiting all overlapping nodes. Creating a separate tree would avoid modifying the first input tree, but would require additional memory.