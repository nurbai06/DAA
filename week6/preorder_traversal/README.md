# Binary Tree Preorder Traversal

## 1. Problem
I need to return the values in this order: current node, left subtree, right subtree.

## 2. Approach
I add the current node first, then recursively visit its left subtree and right subtree.

Example: root = [1, 2, 3].
1. Add the root value 1.
2. Visit the left child and add 2.
3. Visit the right child and add 3.
4. Return [1, 2, 3].

### Challenges and testing
I must add the value before the recursive calls. If I add it after the children, the traversal becomes postorder. I tested an empty tree, a single node, and a tree with both children. The results were [], [1], and [1, 2, 3].

## 3. Time Complexity
**O(n)** time, where n is the number of nodes.

Every node is processed once.

## 4. Space Complexity
**O(h)** extra space, where h is the tree height. It can be O(n) for a tree shaped like a line.

## 5. Reflection / Improvement
An iterative stack solution also takes O(n) time and avoids recursion. The time complexity cannot be better than O(n), because every value must be returned.