# Railway Coach Rearrangement
# Algorithm:
# 1. Read N.
# 2. Store passengers.
# 3. Check senior citizens.
# 4. Extract movable passengers.
# 5. Convert current arrangement into destination positions.
# 6. Count inversions using merge sort.
# 7. Print answer.


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])

    merged = []
    i = 0
    j = 0
    swaps = inv_left + inv_right

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1

        else:
            merged.append(right[j])
            swaps += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, swaps


# Step 1: Read N
N = int(input())

# Step 2: Store passengers
passengers = []

for _ in range(N):
    current, destination, age = map(int, input().split())
    passengers.append((current, destination, age))


# Step 3: Check senior citizens
for current, destination, age in passengers:
    if age > 60 and current != destination:
        print(-1)
        exit()


# Step 4: Extract movable passengers
movable_passengers = []

for current, destination, age in passengers:
    if age <= 60:
        movable_passengers.append((current, destination))


# Step 5: Convert current arrangement into destination positions

# Map destination coach to position
destination_map = {}

for index, (current, destination) in enumerate(movable_passengers):
    destination_map[destination] = index + 1


converted = []

for current, destination in movable_passengers:
    converted.append(destination_map[current])


# Step 6: Count inversions
_, answer = merge_sort(converted)


# Step 7: Print answer
print(answer)
