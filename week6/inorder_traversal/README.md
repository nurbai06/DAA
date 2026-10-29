# Binary Tree Inorder Traversal

## 1. Problem
I need to return the values of a binary tree in this order: left subtree, current node, right subtree.

## 2. Approach
I use recursion. I first visit the left child, then add the current value, and then visit the right child.

### Example trace
For root 2 with left child 1 and right child 3: visit 1 and add it, add 2, then visit and add 3. The result is [1, 2, 3].

### Challenges and testing
The order matters. If I add the root before visiting the left child, that becomes preorder instead of inorder. I would test an empty tree, a single node, and a tree with both children.

## 3. Time Complexity
**O(n)** time.

Every node is visited once, where n is the number of nodes.

## 4. Space Complexity
**O(h)**.

The recursive call stack uses space based on tree height h. In the worst case, h = n.

## 5. Reflection / Improvement
An iterative solution with a stack also takes O(n) time. It avoids recursive calls, but does not improve the time complexity.
