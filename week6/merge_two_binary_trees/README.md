# Merge Two Binary Trees

## 1. Problem
I need to combine two trees by adding values where both nodes exist. If a node exists in only one tree, I keep that subtree.

## 2. Approach
If one node is missing, I return the other node. If both nodes exist, I add their values and merge their left and right children.

### Example trace
If the roots have values 1 and 2, the merged root becomes 3. If their left children are 3 and 4, the merged left child becomes 7. If only one side has a child, that child is kept.

### Challenges and testing
I need to handle missing nodes before accessing their values. I would test two overlapping trees and also a case where one tree is empty.

## 3. Time Complexity
**O(m)** time, where m is the number of nodes in the smaller tree. Each overlapping pair of nodes is processed once.

## 4. Space Complexity
**O(h)** auxiliary space, where h is the height of the overlapping part of the trees. The solution reuses nodes rather than creating a new tree.

## 5. Reflection / Improvement
The time is optimal for visiting all overlapping nodes. Creating a separate tree would avoid modifying the first input tree, but would require additional memory.
