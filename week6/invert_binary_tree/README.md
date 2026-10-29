# Invert Binary Tree

## 1. Problem
I need to swap the left and right child of every node.

## 2. Approach
At each node, I swap its left and right children, then invert both subtrees.

Example: root = [1, 2, 3].
1. Swap the root's children. Node 3 becomes the left child and node 2 becomes the right child.
2. Visit both children. They are leaves, so there is nothing else to swap.
3. The inverted tree is [1, 3, 2].

### Challenges and testing
I need to process every node, not only the root. I tested an empty tree, a single node, and a tree with multiple levels. The empty tree stayed None, the single node stayed the same, and the left and right branches were swapped at each level.

## 3. Time Complexity
**O(n)** time, where n is the number of nodes.

Every node is visited and swapped once.

## 4. Space Complexity
**O(h)** extra space, where h is the tree height. The recursion stack can reach O(n).

## 5. Reflection / Improvement
A queue or stack can invert the tree iteratively with O(n) time. It avoids recursion but still needs space to store nodes.