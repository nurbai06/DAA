# Binary Tree Inorder Traversal

## 1. Problem
I need to return the values of a binary tree in this order: left subtree, current node, right subtree.

## 2. Approach
I use recursion. I first visit the left child, then add the current value, and then visit the right child.

Example: root = [2, 1, 3].
1. Visit the left child and add 1.
2. Add the root value 2.
3. Visit the right child and add 3.
4. Return [1, 2, 3].

### Challenges and testing
The order matters. If I add the root before visiting the left child, that becomes preorder instead of inorder. I tested an empty tree, a single node, and a tree with both children. The results were [], [1], and [1, 2, 3] for those cases.

## 3. Time Complexity
**O(n)** time, where n is the number of nodes.

Every node is visited once.

## 4. Space Complexity
**O(h)** extra space, where h is the tree height. In the worst case, h = n because the tree can be shaped like a line.

## 5. Reflection / Improvement
An iterative solution with a stack also takes O(n) time. It avoids recursive calls, but does not improve the time complexity.

