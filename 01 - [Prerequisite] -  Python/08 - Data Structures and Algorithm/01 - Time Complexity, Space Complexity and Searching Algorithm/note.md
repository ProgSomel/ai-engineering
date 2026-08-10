# Time Complexity, Space Complexity and Searching Algorithm

## Time Complexity

Time complexity is a way of describing how the **running time of an algorithm
grows** as the size of its input (`n`) grows. It does not measure the actual
time in seconds (that depends on the machine, language, compiler, etc.) —
it measures how the number of basic operations scales with `n`.

We express time complexity using **Big-O notation**, which describes the
**worst-case upper bound** on growth rate, ignoring constants and lower-order
terms.

### Why we ignore constants

```python
def sum_twice(arr):
    total = 0
    for x in arr:        # n operations
        total += x
    for x in arr:        # n operations
        total += x
    return total
```

This does `2n` operations, but as `n` grows, the `2` barely matters compared
to `n` itself — so we simplify `O(2n)` to **O(n)**.

### Common time complexities (fastest to slowest)

| Big-O        | Name         | Example                                  |
|--------------|--------------|-------------------------------------------|
| O(1)         | Constant     | Accessing `arr[0]`, dict lookup            |
| O(log n)     | Logarithmic  | Binary search                              |
| O(n)         | Linear       | Linear search, single loop over `n` items  |
| O(n log n)   | Linearithmic | Merge sort, quick sort (average case)      |
| O(n²)        | Quadratic    | Bubble sort, selection sort, insertion sort|
| O(n³)        | Cubic        | Triple nested loops                        |
| O(2ⁿ)        | Exponential  | Recursive Fibonacci (naive), subsets       |
| O(n!)        | Factorial    | Brute-force traveling salesman             |

### How to read code and estimate complexity

- **Single loop over `n` items** → O(n)
  ```python
  for i in range(n):   # runs n times
      print(i)
  ```
- **Nested loops over `n` items** → O(n²)
  ```python
  for i in range(n):
      for j in range(n):   # n * n = n² total iterations
          print(i, j)
  ```
- **Loop that halves the problem each time** → O(log n)
  ```python
  while n > 1:
      n = n // 2   # divides n by 2 each iteration
  ```
- **Sequential (not nested) blocks add up, but we keep the largest term**
  ```python
  for i in range(n):      # O(n)
      print(i)
  for i in range(n):
      for j in range(n):  # O(n²)
          print(i, j)
  # Total: O(n) + O(n²) -> simplifies to O(n²)
  ```

### Best, Average, and Worst Case

An algorithm can behave differently depending on the input:
- **Best case (Ω)** — the fastest scenario (e.g., linear search finds the item
  at index 0).
- **Average case (Θ)** — expected performance over typical inputs.
- **Worst case (O)** — the slowest scenario (e.g., linear search where the
  item is last or not present at all).

Big-O almost always refers to the **worst case**, since that gives a
guarantee on how bad performance can get.

## Space Complexity

Space complexity measures how much **memory** an algorithm needs, expressed
as a function of the input size `n`, using the same Big-O notation as time
complexity.

### Total space vs. auxiliary space

Total memory used by an algorithm has two parts:

- **Input space** — the memory taken up by the input itself (e.g., the array
  passed into the function). This is not counted when comparing algorithms,
  since every algorithm that processes the same input pays this cost.
- **Auxiliary space** — the **extra** memory the algorithm uses beyond the
  input: local variables, temporary arrays/objects, and the function call
  stack (for recursion).

> When people say "space complexity," they almost always mean **auxiliary
> space complexity** — how much *additional* memory is needed, not counting
> the input.

### Common space complexities

| Big-O    | Name        | Example                                              |
|----------|-------------|-------------------------------------------------------|
| O(1)     | Constant    | A fixed number of variables (in-place swap, counters)  |
| O(log n) | Logarithmic | Recursive binary search (call stack depth)             |
| O(n)     | Linear      | Copying an array, single-level recursion of depth `n`  |
| O(n²)    | Quadratic   | A 2D matrix/table of size `n x n`                      |

### O(1) — Constant space

Uses a fixed number of variables no matter how large the input is. The
memory footprint doesn't grow as `n` grows.

```python
def sum_array(arr):
    total = 0          # single variable, regardless of len(arr)
    for x in arr:
        total += x
    return total
```

Algorithms that rearrange elements **within the original array/list**
(instead of building a new one) are called **in-place** and typically use
O(1) auxiliary space — e.g. `bubbleSort`, `selectionSort`, and
`insertionSort` above only ever use a couple of temporary variables
(`temp`, `min_idx`, `key`, `j`) regardless of how large `array` is.

### O(n) — Linear space

Memory usage grows proportionally with input size, typically because a new
data structure of size roughly `n` is created.

```python
def double_values(arr):
    result = []              # new list grows with input size
    for x in arr:
        result.append(x * 2)
    return result
```

Merge sort is a classic example: it needs an auxiliary array of size `n` to
merge sorted halves back together, giving it O(n) space — unlike the
in-place O(1)-space sorts covered earlier.

### Recursion and the call stack

Every function call — including a recursive call — pushes a new **stack
frame** holding its local variables and return address. This frame isn't
freed until the call returns, so recursion depth directly drives space
usage.

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)   # n stacked calls -> O(n) space
```

`factorial(5)` stacks 5 pending calls before any of them returns, so this
uses O(n) space even though it creates no arrays or lists.

Compare this to **binary search implemented recursively**:

```python
def binarySearchRecursive(array, x, low, high):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if array[mid] == x:
        return mid
    elif array[mid] < x:
        return binarySearchRecursive(array, x, mid + 1, high)
    else:
        return binarySearchRecursive(array, x, low, mid - 1)
```

Because the search range halves each call, the recursion only goes
`log(n)` levels deep before hitting the base case — so this version uses
**O(log n) space** for the call stack, versus **O(1) space** for the
iterative `binarySearch` shown earlier (no extra stack frames at all).

### Time vs. space trade-off

Often you can trade memory for speed, or vice versa. For example, caching
previously computed results (memoization) uses more space (O(n)) to avoid
recomputing values, turning an O(2ⁿ) recursive Fibonacci into O(n) time:

```python
def fib(n, cache={}):
    if n in cache:
        return cache[n]          # O(1) lookup instead of recomputation
    if n <= 1:
        return n
    cache[n] = fib(n - 1, cache) + fib(n - 2, cache)   # cache grows to O(n)
    return cache[n]
```

Here, spending O(n) extra space on the `cache` dictionary reduces the time
complexity from exponential to linear — a classic time/space trade-off.

### Time vs Space trade-off

Often you can trade memory for speed, or vice versa. For example, caching
previously computed results (memoization) uses more space (O(n)) to avoid
recomputing values, turning an O(2ⁿ) recursive Fibonacci into O(n) time.

## Searching Algorithms

### Linear Search

A simple approach: check each element one by one from the leftmost side of
`arr[]` until a match is found or the array is exhausted.

1. Start from the leftmost element of `arr[]` and compare `x` with each
   element one by one.
2. If `x` matches an element, return the index.
3. If `x` doesn't match any element, return `-1`.

```python
# linear search
def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
```

**Time Complexity:** O(n) — worst case checks every element.
**Space Complexity:** O(1) — no extra memory needed.

### Binary Search

A searching algorithm for finding an element's position in a **sorted**
array, by repeatedly dividing the search interval in half.

**Algorithm:** repeat until the pointers `low` and `high` meet each other.
1. `mid = (low + high) / 2`
2. If `x == arr[mid]`, return `mid`.
3. Else if `x > arr[mid]`, the target is on the right side → `low = mid + 1`.
4. Else, the target is on the left side → `high = mid - 1`.

```python
# Binary Search in Python
def binarySearch(array, x, low, high):
    # Repeat until the pointers low and high meet each other
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

array = [3, 4, 5, 6, 7, 8, 9]
x = 4
result = binarySearch(array, x, 0, len(array) - 1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
```

**Time Complexity:** O(log n) — the search space is halved each iteration.
**Space Complexity:** O(1) for the iterative version above.

> Binary search requires the array to be **sorted** first. Sorting an
> unsorted array (e.g., O(n log n)) before a single search is not worth it,
> but it pays off when searching the same array many times.

## Sorting Algorithms

### Bubble Sort

Compares two adjacent elements and swaps them until the array is in the
intended order. On each pass, the largest remaining element "bubbles up" to
its correct position at the end.

```python
def bubbleSort(array):
    # loop to access each array element
    for i in range(len(array)):
        # loop to compare array elements
        for j in range(0, len(array) - i - 1):
            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping elements if they are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
```

**Time Complexity:** O(n²) worst/average case, O(n) best case (already
sorted, with an early-exit optimization). **Space Complexity:** O(1).

### Selection Sort

Selects the smallest element from the unsorted part of the list in each
iteration and places it at the beginning of the unsorted list.

1. Set `MIN` to location 0.
2. Search the minimum element in the list.
3. Swap it with the value at location `MIN`.
4. Increment `MIN` to point to the next element.
5. Repeat until the list is sorted.

```python
def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
```

**Time Complexity:** O(n²) in all cases (always scans the remaining
unsorted part to find the minimum). **Space Complexity:** O(1).

### Insertion Sort

Places an unsorted element at its suitable place among the already-sorted
part of the list, in each iteration.

1. If it is the first element, it is already sorted.
2. Pick the next element.
3. Compare it with all elements in the sorted sub-list.
4. Shift all elements in the sorted sub-list that are greater than the value
   to be sorted.
5. Insert the value.
6. Repeat until the list is sorted.

```python
def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until
        # an element smaller than it is found
        # For descending order, change key < array[j] to key > array[j]
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key after the element just smaller than it
        array[j + 1] = key
```

**Time Complexity:** O(n²) worst/average case, O(n) best case (nearly
sorted input). **Space Complexity:** O(1) — sorts in place.

## Summary Table

| Algorithm       | Best      | Average  | Worst    | Space |
|-----------------|-----------|----------|----------|-------|
| Linear Search   | O(1)      | O(n)     | O(n)     | O(1)  |
| Binary Search   | O(1)      | O(log n) | O(log n) | O(1)  |
| Bubble Sort     | O(n)      | O(n²)    | O(n²)    | O(1)  |
| Selection Sort  | O(n²)     | O(n²)    | O(n²)    | O(1)  |
| Insertion Sort  | O(n)      | O(n²)    | O(n²)    | O(1)  |
