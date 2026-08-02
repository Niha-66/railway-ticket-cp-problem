# Algorithm:
# 1. Read N.
# 2. Store passengers.
# 3. Check senior citizens:
#       If age > 60 and current != destination:
#             print -1
#             stop
# 4. Extract movable passengers.
# 5. Convert current arrangement into destination positions.
# 6. Count inversions using merge sort.
# 7. Print answer.



# Step 1: Read N
N = int(input())

# Step 2: Store passengers
passengers = []

for _ in range(N):
    current, destination, age = map(int, input().split())
    passengers.append((current, destination, age))

print(passengers)
