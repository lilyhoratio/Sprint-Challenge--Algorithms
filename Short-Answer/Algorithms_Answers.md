#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) linear time complexity.

b) O (nlog n). Outer loop is O(n). Inner loop is O(logn) because it doubles every time with maximum of n.

c) O(n) linear time complexity.

## Exercise II

Use the binary search algorithm to minimize broken eggs with a runtime complexity of O(log n).

- Find what the middle floor is and drop an egg.
- If the egg breaks, then that floor is too high. Make your upper bound the middle - 1 floor, keep lower bound as 1.
- If the egg doesn't break, then that floor is too low. Make your low bound the middle + 1 floor, keep upper bound as n.
- Keep repeating this.
