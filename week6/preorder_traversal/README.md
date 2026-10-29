# Binary Tree Preorder Traversal

## 1. Problem
I need to return the values in this order: current node, left subtree, right subtree.

## 2. Approach
I add the current node first, then recursively visit its left subtree and right subtree.

### Example trace
For root 1 with left child 2 and right child 3: add 1, then add 2, then add 3. The result is [1, 2, 3].

### Challenges and testing
I must add the value before the recursive calls. If I add it after the children, the traversal becomes postorder. I would test a small tree where the order is easy to see.

## 3. Time Complexity
**O(n)** time.

Every node is processed once.

## 4. Space Complexity
**O(h)**.

The recursive stack uses O(h) space, or O(n) for a tree shaped like a line.

## 5. Reflection / Improvement
An iterative stack solution also takes O(n) time and avoids recursion. The time complexity cannot be better than O(n), because every value must be returned.
