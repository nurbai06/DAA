# Linked List Cycle

## 1. Problem
I need to check whether a linked list has a cycle.
A cycle means that following next links brings me back to the same node.

## 2. Approach
I use a set to remember the nodes I have visited.
If I reach a node that is already in the set, I return True.
If I reach None, I return False.
I store nodes, not values, because different nodes can have the same value.

Example: [3, 2, 0, -4], where the last node points back to the node with value 2.

1. Visit node 3. Add it to the set.
2. Visit node 2. Add it to the set.
3. Visit node 0. Add it to the set.
4. Visit node -4. Add it to the set.
5. Reach the same node 2 again. It is already in the set, so I return True.

Without a cycle, for example [1, 2], I visit both nodes and then reach None.
I return False.

## 3. Time Complexity
**O(n)** expected time, where n is the number of different reachable nodes.

I visit each new node once. Checking and adding a node in a set usually takes O(1).
For a cycle, I stop as soon as I visit a node again.

## 4. Space Complexity
**O(n)** extra space.

My set may store all n visited nodes.

## 5. Reflection / Improvement
I could use two pointers instead of a set.
One pointer moves one step and the other moves two steps.
If they meet, there is a cycle. If the fast pointer reaches the end, there is no cycle.
This would keep O(n) time and reduce extra space to O(1).
