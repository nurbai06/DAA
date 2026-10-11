# Palindrome Linked List

## 1. Problem
I need to check whether the list reads the same forward and backward.

## 2. Approach and Testing
I copy the node values into a Python list. I compare the first and last values, then move both indexes toward the middle. A mismatch means False. If all pairs match, I return True.

Example: [1, 2, 2, 1].
1. Collect values: [1], [1, 2], [1, 2, 2], [1, 2, 2, 1].
2. Compare indexes 0 and 3: 1 equals 1.
3. Compare indexes 1 and 2: 2 equals 2.
4. The indexes cross. Return True.

Challenge: Checking only the first and last values is not enough. That approach returns True for [1, 2, 3, 1], but the inner pair 2 and 3 does not match. I checked this case, odd and even lengths, and a single node.

## 3. Time Complexity
**O(n)** time. Collecting values takes n steps. Comparing pairs takes at most n/2 steps. Together this is O(n).

## 4. Space Complexity
**O(n)** extra space. My Python list stores all n values.

## 5. Reflection / Improvement
I could find the middle, reverse the second half, and compare the two halves. This keeps O(n) time and reduces extra space to O(1). I would reverse it back afterward to restore the list.
