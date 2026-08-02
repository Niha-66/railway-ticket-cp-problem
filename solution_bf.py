from collections import deque


def is_valid_state(state, target):
    return state == target


def minimum_swaps_bf(start, target):
    if start == target:
        return 0

    queue = deque()
    queue.append((start, 0))

    visited = set()
    visited.add(tuple(start))

    while queue:
        current, steps = queue.popleft()

        for i in range(len(current) - 1):
            new_state = current[:]

            # Adjacent swap
            new_state[i], new_state[i + 1] = (
                new_state[i + 1],
                new_state[i]
            )

            if tuple(new_state) not in visited:

                if new_state == target:
                    return steps + 1

                visited.add(tuple(new_state))
                queue.append((new_state, steps + 1))

    return -1


# Read input
N = int(input())

passengers = []

for _ in range(N):
    current, destination, age = map(int, input().split())
    passengers.append((current, destination, age))


# Check senior citizen restriction
for current, destination, age in passengers:
    if age > 60 and current != destination:
        print(-1)
        exit()


# Extract movable passengers
movable = []

for current, destination, age in passengers:
    if age <= 60:
        movable.append((current, destination))


# Current and target arrangements
current_arrangement = []
target_arrangement = []

for current, destination in movable:
    current_arrangement.append(current)
    target_arrangement.append(destination)


# Find answer using brute force
answer = minimum_swaps_bf(
    current_arrangement,
    target_arrangement
)

print(answer)
