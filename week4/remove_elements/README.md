# Remove Linked List Elements

## 1. Problem
I need to remove every node whose value equals val and return the new head.

## 2. Approach and Testing
I put a dummy node before the head. I check the node after my current pointer. If its value equals val, I skip it. Otherwise, I move forward. Finally, I return dummy.next.

Example: [6, 1, 6, 6, 2], val = 6.
1. Start at the dummy. Skip the first 6: [1, 6, 6, 2].
2. Keep 1 and move to it.
3. Skip the next 6: [1, 6, 2].
4. Stay at 1 and skip the other 6: [1, 2].
5. Keep 2. Return [1, 2].

Challenge: The first node may also need removal. Checking only nodes after the original head fails for [6, 1] because it keeps the first 6. My dummy node handles this. I checked an empty list, consecutive matches, and a list where every node is removed.

## 3. Time Complexity
**O(n)** time. I check each original node once, either skipping it or moving to it.

## 4. Space Complexity
**O(1)** extra space. I only add one dummy node and one traversal pointer.

## 5. Reflection / Improvement
My solution already uses O(n) time and O(1) extra space. Recursion would need additional stack space, so I keep the loop.
