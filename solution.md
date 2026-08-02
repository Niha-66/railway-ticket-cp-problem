# Solution Explanation - Railway Coach Rearrangement

## Problem Understanding

We have N passengers, where each passenger has:
- Current coach position
- Destination coach position
- Age

Passengers can swap only with adjacent passengers. The goal is to find the minimum number of adjacent swaps required to move all possible passengers to their destination coaches.

Passengers with age greater than 60 are fixed and cannot change their coach position. If any such passenger has a different destination coach, the rearrangement is impossible.

---

## Algorithm Approach

The problem is solved using inversion counting.

### Step 1: Validate Fixed Passengers

First, check all passengers:

- If `age > 60` and `currentCoach != destinationCoach`
  - The passenger cannot move.
  - Therefore, the required arrangement is impossible.
  - Return `-1`.

---

### Step 2: Extract Movable Passengers

Passengers with age less than or equal to 60 can participate in swaps.

Store only these passengers for rearrangement.

---

### Step 3: Convert Arrangement into a Permutation

The current coach arrangement is converted into a destination-based index array.

This transformation converts the problem into:

"How many adjacent swaps are required to sort this permutation?"

---

### Step 4: Count Minimum Adjacent Swaps

The minimum number of adjacent swaps required to transform a permutation into sorted order is equal to the number of inversions.

An inversion exists when:
i < j and arr[i] > arr[j]

Each inversion represents one required adjacent swap.

The inversion count is calculated efficiently using merge sort.

---

## Data Structures Used

### Array/List

Used to store:
- Passenger information
- Converted permutation

### Hash Map

Used to map destination coaches to their positions during permutation conversion.

### Merge Sort

Used to count inversions efficiently.

---

## Correctness Explanation

1. Senior citizens are checked first because their positions cannot change.
2. Removing fixed passengers leaves only passengers who can participate in swaps.
3. The destination mapping converts the rearrangement problem into sorting a permutation.
4. In a permutation, every inversion represents a pair of passengers that are in the wrong relative order.
5. Each inversion requires exactly one adjacent swap.
6. Merge sort counts all inversions without performing individual swaps.

Therefore, the inversion count gives the minimum number of adjacent swaps required.

---

## Complexity Analysis

Let N be the number of passengers.

### Time Complexity

- Reading passengers: `O(N)`
- Checking restrictions: `O(N)`
- Creating permutation: `O(N)`
- Counting inversions using merge sort: `O(N log N)`

Overall:
Time Complexity: O(N log N)

### Space Complexity

Additional arrays and merge sort storage require:
Space Complexity: O(N)

---

## Reference Implementation

The implementation is provided in:
solution.py
