# Sum of Left Leaves

## 1. Problem
I need to add the values of all leaf nodes that are left children.

## 2. Approach
I check whether the left child is a leaf. If it is, I add its value. Otherwise, I search that subtree. I also search the right subtree because it can contain left leaves.

Example: root = [3, 9, 20, null, null, 15, 7].
1. Node 9 is a left leaf, so I add 9.
2. Node 20 is not a leaf, so I check its children.
3. Node 15 is a left leaf, so I add 15.
4. Node 7 is a right leaf, so I do not add it.
5. The sum is 9 + 15 = 24.

### Challenges and testing
A leaf on the right side should not be added, but its subtree still needs to be searched. I tested an empty tree, a single node, and a tree with both left and right leaves. The results were 0, 0, and 24.

## 3. Time Complexity
**O(n)** time, where n is the number of nodes.

Each node is checked at most once.

## 4. Space Complexity
**O(h)** extra space, where h is the tree height. In the worst case, this is O(n).

## 5. Reflection / Improvement
The solution is already linear. An iterative traversal could also find left leaves in O(n) time.

