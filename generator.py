
import random


def generate_test_case():
    # Small N because brute force is used
    n = random.randint(2, 7)

    coaches = list(range(1, n + 1))

    # Current arrangement
    current = coaches[:]
    random.shuffle(current)

    # Destination arrangement
    destination = coaches[:]
    random.shuffle(destination)

    passengers = []

    for i in range(n):
        age = random.randint(18, 70)

        passengers.append(
            (
                current[i],
                destination[i],
                age
            )
        )

    return passengers


# Generate test case
test_case = generate_test_case()

print(len(test_case))

for passenger in test_case:
    print(*passenger)
