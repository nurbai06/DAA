# Sort List

## 1. Problem
I need to sort a linked list from smallest to largest and return its new head.

## 2. Approach
I use merge sort. A slow pointer moves one step and a fast pointer moves two steps to find the middle. I cut the list into two parts, sort each part, and merge them by connecting the smaller current node each time.

A list with zero or one node is already sorted. During merging, I use a dummy node to make the first connection easier.

Example: 4 → 2 → 1 → 3.
1. Start slow at 4 and fast at 2. Move slow to 2 and fast to 3. Stop because fast has no next node.
2. Cut after 2: the halves are [4, 2] and [1, 3].
3. Split each half into single nodes.
4. Merge [4] and [2] into [2, 4]. Merge [1] and [3] into [1, 3].
5. Merge [2, 4] and [1, 3]: connect 1, then 2, then 3, then the remaining 4.
6. Return the head of 1 → 2 → 3 → 4.

### Challenges and testing
I must cut the connection between the halves with slow.next = None. Otherwise, the left part still contains the whole list. For [2, 1], sorting that unchanged left part repeats forever until Python raises a recursion error.

I checked this failure with a two-node list. I also tested an empty list, one node, repeated values, negative values, and reversed input. My checks confirm that the result contains the same node objects without a cycle.

## 3. Time Complexity
**O(n log n)** time, where n is the number of nodes.

There are about log n levels of splitting. Finding the middles and merging the lists takes O(n) total work at each level. Together, this gives O(n log n).

## 4. Space Complexity
**O(log n)** extra space.

I reuse the existing nodes. Each merge uses a constant number of pointers and one temporary dummy node. The recursive calls need O(log n) stack space.

## 5. Reflection / Improvement
I could use iterative bottom-up merge sort. I would merge groups of 1 node, then 2, then 4, and keep doubling the group size. This avoids recursion, keeps O(n log n) time, and reduces extra space to O(1).
