# Binary Tree Postorder Traversal

## 1. Problem
I need to return the values in this order: left subtree, right subtree, current node.

## 2. Approach
I visit the left subtree, then the right subtree, and add the current node last.

### Example trace
For root 1 with left child 2 and right child 3: add 2, then add 3, and finally add 1. The result is [2, 3, 1].

### Challenges and testing
The root must be added after both subtrees. I would compare the result on a three-node tree to make sure the root is last.

## 3. Time Complexity
**O(n)** time.

Every node is visited once.

## 4. Space Complexity
**O(h)**.

Recursive calls use space based on the height h; in the worst case h = n.

## 5. Reflection / Improvement
An iterative stack-based solution is possible, but the time complexity remains O(n).
