# Invert Binary Tree

## 1. Problem
I need to swap the left and right child of every node.

## 2. Approach
At each node, I swap its left and right children, then invert both subtrees.

### Example trace
If root 1 has left child 2 and right child 3, I swap them so 3 becomes the left child and 2 becomes the right child. Then I repeat this for the children.

### Challenges and testing
I need to process every node, not only the root. I would test a tree with multiple levels to check that lower branches are also swapped.

## 3. Time Complexity
**O(n)** time.

Every node is visited and swapped once.

## 4. Space Complexity
**O(h)**.

The recursive stack depends on the tree height h, which can be n.

## 5. Reflection / Improvement
A queue or stack can invert the tree iteratively with O(n) time. It avoids recursion but still needs space to store nodes.
