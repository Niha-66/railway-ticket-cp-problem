import sys
input = sys.stdin.readline

def merge_sort_count(arr):
    """Count inversions using merge sort"""
    n = len(arr)
    if n <= 1:
        return arr, 0
    
    mid = n // 2
    left, left_inv = merge_sort_count(arr[:mid])
    right, right_inv = merge_sort_count(arr[mid:])
    
    merged = []
    i = j = 0
    inversions = left_inv + right_inv
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, inversions

def solve():
    n = int(input())
    
    passengers = []
    for _ in range(n):
        current, dest, age = map(int, input().split())
        passengers.append((current, dest, age))
    
    # Check if rearrangement is possible
    # Passengers with age > 60 must stay in their current coach
    for current, dest, age in passengers:
        if age > 60 and current != dest:
            print(-1)
            return
    
    # Identify fixed passengers (age > 60)
    # They occupy certain coaches and cannot move
    fixed_coaches = set()
    for current, dest, age in passengers:
        if age > 60:
            fixed_coaches.add(current)
    
    # Get all coach numbers and sort them
    all_coaches = sorted([p[0] for p in passengers])
    
    # Create mapping from coach number to position index
    coach_to_pos = {coach: idx for idx, coach in enumerate(all_coaches)}
    
    # For movable passengers, we need to figure out the permutation
    # Each movable passenger needs to go from their current coach to destination coach
    # But some coaches are occupied by fixed passengers
    
    # Strategy: 
    # 1. Identify which coaches have fixed passengers
    # 2. For movable passengers, determine their target positions
    # 3. The key insight: we need to arrange movable passengers such that
    #    each one ends up at their destination coach
    
    # Let's think differently:
    # We have N positions (coaches). Some positions are "blocked" by fixed passengers.
    # Movable passengers need to be rearranged among the non-blocked positions.
    
    # Actually, let's reconsider: each passenger occupies exactly one coach initially.
    # After rearrangement, each passenger should be at their destination coach.
    
    # So we need to check: can we achieve the target arrangement?
    # The target arrangement is: at coach `dest`, there should be the passenger whose destination is `dest`
    
    # Let's build the target arrangement
    # First, check if multiple passengers want the same destination
    dest_count = {}
    for current, dest, age in passengers:
        if dest not in dest_count:
            dest_count[dest] = []
        dest_count[dest].append((current, age))
    
    # Check if any destination has more than one passenger wanting it
    # Actually, this shouldn't happen in a valid problem, but let's verify
    for dest, plist in dest_count.items():
        if len(plist) > 1:
            # Multiple passengers want same destination - might be invalid
            # But actually, we need to check if this creates impossibility
            pass
    
    # Better approach: 
    # Think of it as a permutation problem on the line of coaches
    # Position i has a passenger who wants to go to position dest_i
    # We need to count minimum swaps to achieve this
    
    # But with constraint: passengers with age > 60 at position i where current != dest is impossible
    # Already checked above
    
    # For the remaining, we create a permutation:
    # At each position (sorted by coach number), we have a passenger
    # That passenger wants to go to some destination
    # We need to rearrange so passenger at position with coach c goes to position with coach dest
    
    # Sort passengers by current coach
    passengers_sorted = sorted(passengers, key=lambda x: x[0])
    
    # Create array where arr[i] represents: the passenger at position i (by current coach order)
    # wants to go to which position (by destination coach order)
    
    # Map destination coaches to their rank in sorted order
    dest_coaches = sorted(set(p[1] for p in passengers))
    dest_to_rank = {d: i for i, d in enumerate(dest_coaches)}
    
    # Build the permutation
    perm = []
    for current, dest, age in passengers_sorted:
        if age <= 60 or current == dest:
            # This passenger is movable (or already in place)
            perm.append(dest_to_rank[dest])
    
    # Wait, this isn't quite right. Let me reconsider.
    
    # Actually, the issue is more subtle. Fixed passengers block certain positions.
    # Movable passengers can only swap among themselves in the available positions.
    
    # Let me think again with the example:
    # Coaches: 1, 2, 3, 4, 5
    # Passenger at 1 -> wants 2, age 25 (movable)
    # Passenger at 2 -> wants 1, age 30 (movable)  
    # Passenger at 3 -> wants 3, age 70 (fixed, already correct)
    # Passenger at 4 -> wants 5, age 20 (movable)
    # Passenger at 5 -> wants 4, age 40 (movable)
    
    # Target: coach 1 has passenger wanting 1, coach 2 has passenger wanting 2, etc.
    # Currently: [want2, want1, want3(fixed), want5, want4]
    # Target:    [want1, want2, want3(fixed), want4, want5]
    
    # Among movable positions (1,2,4,5), we need:
    # Position 1 should have passenger wanting 1
    # Position 2 should have passenger wanting 2
    # Position 4 should have passenger wanting 4
    # Position 5 should have passenger wanting 5
    
    # Current movable arrangement (positions 1,2,4,5): [want2, want1, want5, want4]
    # In terms of destination ranks among movable destinations {1,2,4,5}: 
    # want2->rank1, want1->rank0, want5->rank3, want4->rank2
    # So perm = [1, 0, 3, 2]
    # Inversions: (1,0), (3,2) = 2 inversions ✓
    
    # General approach:
    # 1. Sort all coaches
    # 2. Identify which positions have fixed passengers
    # 3. Extract movable passengers and their destinations
    # 4. Among movable passengers, create permutation based on destination ranking
    # 5. Count inversions
    
    # Get sorted list of all coaches
    sorted_coaches = sorted(set(p[0] for p in passengers))
    coach_to_idx = {c: i for i, c in enumerate(sorted_coaches)}
    
    # For each position (by coach order), determine if it's fixed or movable
    # and what the passenger at that position wants
    
    # Build array of (is_fixed, destination) for each position
    pos_info = [None] * len(sorted_coaches)
    for current, dest, age in passengers:
        idx = coach_to_idx[current]
        is_fixed = (age > 60)
        pos_info[idx] = (is_fixed, dest)
    
    # Extract movable passengers' destinations in order of their current positions
    movable_dests = []
    for idx in range(len(sorted_coaches)):
        is_fixed, dest = pos_info[idx]
        if not is_fixed:
            movable_dests.append(dest)
    
    # Now we need to find the permutation that sorts movable_dests
    # The target is that at each movable position, the passenger should have 
    # destination matching that position's coach number
    
    # Wait, I need to reconsider. The target arrangement should have:
    # At coach c, the passenger whose destination is c
    
    # So for movable positions, we need to figure out which destinations they should have
    
    # Let me rebuild:
    # All destinations that need to be placed
    # For each coach c, someone needs to end up there (the person whose dest is c)
    
    # Among movable positions, which destinations need to be placed there?
    # A destination d can be placed at coach d if coach d is movable
    # If coach d is fixed, then the passenger at coach d must already have dest d (checked earlier)
    
    # So for movable coaches, the destinations that need to be placed are exactly 
    # the set of movable coaches themselves!
    
    movable_coaches = [c for i, c in enumerate(sorted_coaches) if not pos_info[i][0]]
    movable_coach_set = set(movable_coaches)
    
    # The destinations that need to go to movable positions are exactly movable_coaches
    # (since fixed positions already have correct passengers)
    
    # Current state: at each movable position (in order), we have a passenger with some destination
    # Target state: at movable position with coach c, we want passenger with destination c
    
    # Create permutation: for each movable position (in order of coach number),
    # what is the rank of its current passenger's destination among movable destinations?
    
    movable_dest_sorted = sorted(movable_coaches)
    dest_to_movable_rank = {d: i for i, d in enumerate(movable_dest_sorted)}
    
    perm = []
    for idx in range(len(sorted_coaches)):
        is_fixed, dest = pos_info[idx]
        if not is_fixed:
            perm.append(dest_to_movable_rank[dest])
    
    # Count inversions
    _, inversions = merge_sort_count(perm)
    
    print(inversions)

solve()
