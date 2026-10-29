# Binary Tree Postorder Traversal

## 1. Problem
I need to return the values in this order: left subtree, right subtree, current node.

## 2. Approach
I visit the left subtree, then the right subtree, and add the current node last.

Example: root = [1, 2, 3].
1. Visit the left child and add 2.
2. Visit the right child and add 3.
3. Add the root value 1.
4. Return [2, 3, 1].

### Challenges and testing
The root must be added after both subtrees. I tested an empty tree, a single node, and a tree with two children. The results were [], [1], and [2, 3, 1].

## 3. Time Complexity
**O(n)** time, where n is the number of nodes.

Every node is visited once.

## 4. Space Complexity
**O(h)** extra space, where h is the tree height. In the worst case, h = n.

## 5. Reflection / Improvement
An iterative stack-based solution is possible, but the time complexity remains O(n).

