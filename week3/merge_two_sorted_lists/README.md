# Merge Two Sorted Lists

## 1. Problem
I need to merge two sorted linked lists into one sorted linked list.

## 2. Approach
I compare the current nodes of both lists and take the smaller one.
I add it to the result and move to the next node in that list.
When one list ends, I attach the rest of the other list.
I use a dummy node to make the first connection easier.

Example: list1 = [1, 2, 4], list2 = [1, 3, 4].

1. Compare 1 and 1. Take 1 from list1. Result: [1].
2. Compare 2 and 1. Take 1 from list2. Result: [1, 1].
3. Compare 2 and 3. Take 2. Result: [1, 1, 2].
4. Compare 4 and 3. Take 3. Result: [1, 1, 2, 3].
5. Compare 4 and 4. Take 4 from list1. Result: [1, 1, 2, 3, 4].
6. list1 is empty. Attach the last 4 from list2.

Final result: [1, 1, 2, 3, 4, 4].

## 3. Time Complexity
**O(n + m)**, where n and m are the lengths of the two lists.

I move forward through the lists without going back.
Each step takes one node, so the number of steps is at most n + m.
Attaching the remaining part takes one connection.

## 4. Space Complexity
**O(1)** extra space.

I reuse the existing nodes. I only create one dummy node and use a few pointers.

## 5. Reflection / Improvement
My solution already has O(n + m) worst-case time and O(1) extra space.
I do not need to sort the values again because both lists are already sorted.
There is no better worst-case time complexity for this general approach.
