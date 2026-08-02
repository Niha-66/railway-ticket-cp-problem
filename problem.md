# Railway Coach Rearrangement

## Problem Statement

There are N passengers in a train. Each passenger occupies exactly one coach.
Every passenger has a destination coach where they want to end up.

Each passenger has:
- Current coach
- Destination coach
- Age

In one operation, two passengers in adjacent coaches can swap their positions.

Your task is to determine the minimum number of adjacent swaps required so that every passenger reaches their destination coach.

During an emergency evacuation, passengers with age greater than 60 must remain in their assigned coach for safety reasons. Their positions cannot be changed through swaps.

## Constraints

- N passengers
- Coach numbers range from 1 to N
- Every destination coach is unique
- Passengers with age > 60 cannot be moved
- If it is impossible to achieve the required arrangement, print -1

## Input

The first line contains an integer N.

The next N lines contain three integers:

currentCoach destinationCoach age

where:
- currentCoach represents the passenger's current coach number.
- destinationCoach represents the coach where the passenger needs to reach.
- age represents the passenger's age.

## Output

Print the minimum number of adjacent swaps required.

If the rearrangement is impossible, print -1.
