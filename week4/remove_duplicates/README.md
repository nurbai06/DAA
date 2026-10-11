# Remove Duplicates from Sorted List

## 1. Problem
I need to remove repeated values from a sorted linked list, keeping one node for each value.

## 2. Approach and Testing
I compare each node with the next node. If their values are equal, I skip the next node. Otherwise, I move forward.

Example: [1, 1, 1, 2].
1. Compare 1 and 1. Skip the second node: [1, 1, 2].
2. Stay at the first node. Compare 1 and 1 again: [1, 2].
3. Compare 1 and 2. Move to 2.
4. There is no next node. Return [1, 2].

Challenge: I must stay at the current node after removing a duplicate. Moving forward every time fails for [1, 1, 1]: it leaves [1, 1]. I checked this case, an empty list, and a list without duplicates.

## 3. Time Complexity
**O(n)** time. Each iteration removes a node or moves forward, so I do at most a linear number of steps.

## 4. Space Complexity
**O(1)** extra space. I use one pointer and reuse the existing nodes.

## 5. Reflection / Improvement
My solution already uses O(n) time and O(1) extra space. A set is unnecessary because equal values are next to each other.
