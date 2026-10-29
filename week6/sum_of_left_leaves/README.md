# Sum of Left Leaves

## 1. Problem
I need to add the values of all leaf nodes that are left children.

## 2. Approach
I check whether the left child is a leaf. If it is, I add its value. Otherwise, I search that subtree. I also search the right subtree because it can contain left leaves.

### Example trace
For root 3 with left leaf 9 and right child 20, where 20 has children 15 and 7: add 9 and 15. Do not add 7 because it is a right leaf. The sum is 24.

### Challenges and testing
A leaf on the right side should not be added, but its subtree still needs to be searched. I would test both left and right leaves.

## 3. Time Complexity
**O(n)** time.

Each node is checked at most once.

## 4. Space Complexity
**O(h)**.

Recursive calls use space up to tree height h; worst case O(n).

## 5. Reflection / Improvement
The solution is already linear. An iterative traversal could also find left leaves in O(n) time.
