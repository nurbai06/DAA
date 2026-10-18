# Sort an Array

## 1. Problem
I need to sort an integer array from smallest to largest without using a built-in sorting function.

## 2. Approach
I use merge sort. I split the array into two halves until each part has at most one number. Then I merge the sorted halves by taking the smaller current number. Finally, I add any remaining numbers.

Example: [5, 2, 3, 1].
1. Split into [5, 2] and [3, 1].
2. Split again into [5], [2], [3], and [1].
3. Merge [5] and [2]: take 2, then 5. Result: [2, 5].
4. Merge [3] and [1]: take 1, then 3. Result: [1, 3].
5. Merge [2, 5] and [1, 3]: take 1, then 2, then 3, then the remaining 5.
6. Return [1, 2, 3, 5].

### Challenges and testing
I need to keep duplicate values and add the remaining numbers after one half ends. Merging only while both halves have numbers loses values: for [2, 5] and [1, 3], it leaves out 5.

I checked this incorrect approach with that example. I also tested negative numbers, duplicates, sorted and reversed arrays, and a single number. Bubble sort is easier, but its O(n²) worst-case time does not meet the required O(n log n) time.

## 3. Time Complexity
**O(n log n)** time, where n is the number of values.

Splitting creates about log n levels. At each level, copying and merging all parts takes O(n) total work. Therefore, the total is O(n log n).

## 4. Space Complexity
**O(n)** extra space.

The slices and merged arrays hold a linear number of values at one time. Recursion adds O(log n) stack space, which is smaller than O(n).

## 5. Reflection / Improvement
I could use heapsort to keep O(n log n) time and reduce extra space to O(1). I would replace splitting and merging with building a heap and repeatedly moving its largest value to the end. I kept merge sort because its steps are easier for me to trace, but it does not use the smallest possible extra space.
