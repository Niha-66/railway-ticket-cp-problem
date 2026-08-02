# Railway Coach Rearrangement

## Problem Overview

There are N passengers in a train. Each passenger occupies exactly one coach. Every passenger has a destination coach where they want to end up.

In one operation, two passengers in adjacent coaches can swap their positions.

The task is to find the minimum number of adjacent swaps required so that every passenger reaches their destination coach.

During emergency evacuation, passengers with age greater than 60 must remain in their assigned coach for safety reasons. Their positions cannot be changed.

If a valid rearrangement is impossible, print `-1`.

---

## Input Format

The first line contains an integer:

N

representing the number of passengers.

The next N lines contain three integers:
currentCoach destinationCoach age


where:

- `currentCoach` represents the passenger's current coach number.
- `destinationCoach` represents the coach where the passenger needs to reach.
- `age` represents the passenger's age.

---

## Output Format

Print the minimum number of adjacent swaps required.

If the rearrangement is impossible because of movement restrictions, print:
-1

---

## Approach

The problem is solved using inversion counting.

Steps:

1. Read passenger details.
2. Check passengers with age greater than 60:
   - If their current coach is different from their destination coach, rearrangement is impossible.
3. Remove fixed passengers and consider only movable passengers.
4. Convert the current arrangement into a destination-based permutation.
5. Count inversions in the permutation using merge sort.
6. The inversion count gives the minimum number of adjacent swaps.

---

## Algorithm

1. Store all passengers.
2. Validate senior citizen constraints.
3. Create a list of movable passengers.
4. Map destination coaches to their required positions.
5. Convert the arrangement into a permutation.
6. Count inversions using merge sort.
7. Print the result.

---

## Complexity Analysis

**Time Complexity:** `O(N log N)`

**Space Complexity:** `O(N)`

---

## Example

### Input
5
1 2 25
2 1 30
3 3 70
4 5 20
5 4 40

### Output
2

### Explanation

Passenger movements:

- Passenger at coach 1 needs coach 2.
- Passenger at coach 2 needs coach 1.
- Passenger at coach 3 is a senior citizen and already in the correct coach.
- Remaining swaps needed are counted using inversion counting.

Minimum adjacent swaps required:
2

---

## Impossible Case Example

### Input
3
1 2 65
2 1 30
3 3 40

### Output
-1

### Explanation

The passenger with age 65 cannot be moved, but their destination is different from their current coach. Therefore, rearrangement is impossible.
