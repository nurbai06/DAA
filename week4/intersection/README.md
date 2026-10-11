# Intersection of Two Linked Lists

## 1. Problem
I need to find the first node shared by two linked lists. Equal values alone do not mean that the lists intersect.

## 2. Approach and Testing
I save the nodes of list A in a set. Then I walk through list B. The first node already in the set is the intersection. If I find none, I return None.

Example: A = 1 → C → D and B = 2 → 3 → C → D. C and D are the same node objects in both lists.
1. Add nodes 1, C, and D to the set.
2. Check node 2 from B: not in the set.
3. Check node 3: not in the set.
4. Check C: already in the set. Return C.

Challenge: I must compare nodes, not values. Comparing values gives a wrong answer for two separate nodes that both contain 1. I checked separate equal-valued nodes, a shared tail, and lists with the same head.

## 3. Time Complexity
**O(n + m)** expected time, where n and m are the list lengths. I walk through A once and B at most once. Set operations usually take O(1).

## 4. Space Complexity
**O(n)** extra space. The set stores the n nodes from list A.

## 5. Reflection / Improvement
I could use two pointers and switch each pointer to the other list when it reaches the end. They then travel equal total distances and meet at the shared node, or both reach None. This gives O(n + m) time and O(1) extra space.
