import sys

def merge_sort_count(arr):
    """Count inversions using merge sort"""
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, left_inv = merge_sort_count(arr[:mid])
    right, right_inv = merge_sort_count(arr[mid:])
    
    merged = []
    inversions = left_inv + right_inv
    i = j = 0
    
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
    input_data = sys.stdin.read().split()
    idx = 0
    
    n = int(input_data[idx]); idx += 1
    
    passengers = []
    for i in range(n):
        current_coach = int(input_data[idx]); idx += 1
        dest_coach = int(input_data[idx]); idx += 1
        age = int(input_data[idx]); idx += 1
        passengers.append((current_coach, dest_coach, age))
    
    # Check if any senior citizen (age > 60) needs to move
    for current_coach, dest_coach, age in passengers:
        if age > 60 and current_coach != dest_coach:
            print(-1)
            return
    
    # Get movable passengers (those who can be moved or are already in place)
    # We need to figure out the permutation of destination coaches
    # among the positions that can change
    
    # First, identify which coaches have fixed passengers (seniors in correct position)
    # and which coaches have movable passengers
    
    # Create a mapping: for each coach position, what passenger is there?
    # Passengers are indexed by their current coach (1-indexed)
    
    # We need to think about this differently:
    # Each passenger is at a current coach and wants to go to a destination coach
    # Adjacent swaps mean we're swapping passengers between adjacent coaches
    
    # The key insight: we need to create a permutation where we track
    # which destination each position should have, then count inversions
    
    # Let's think of it as: we have N positions (coaches 1 to N)
    # At each position, there's a passenger who wants to go to some destination
    # We want to rearrange so that the passenger at position i ends up at their destination
    
    # Actually, let me reconsider. The problem says each passenger occupies exactly one coach.
    # So coaches are numbered, and we have N passengers, each at a current coach.
    # After rearrangement, each passenger should be at their destination coach.
    
    # For the permutation approach:
    # We look at the sequence of destination coaches in order of current coach positions
    # Then count how many swaps are needed to sort this into the correct arrangement
    
    # But we need to handle fixed passengers carefully
    
    # Let's collect all passengers and sort by current coach
    passengers.sort(key=lambda x: x[0])
    
    # Separate fixed and movable passengers
    fixed_passengers = []  # (current_coach, dest_coach) for seniors who must stay
    movable_passengers = []  # (current_coach, dest_coach) for others
    
    for current_coach, dest_coach, age in passengers:
        if age > 60:
            # Already verified they're in correct position
            fixed_passengers.append((current_coach, dest_coach))
        else:
            movable_passengers.append((current_coach, dest_coach))
    
    # Now we need to check if the rearrangement is possible considering fixed passengers
    # Fixed passengers occupy their coaches and cannot move
    # Movable passengers need to reach their destinations, but can't occupy fixed passenger coaches
    
    # Check if any movable passenger's destination is occupied by a fixed passenger
    fixed_destinations = set(dest for _, dest in fixed_passengers)
    
    for current_coach, dest_coach in movable_passengers:
        if dest_coach in fixed_destinations:
            # This destination is occupied by a fixed passenger
            # Check if the fixed passenger at that destination actually belongs there
            # Find which fixed passenger is at dest_coach
            found = False
            for fc, fd in fixed_passengers:
                if fc == dest_coach:
                    # The fixed passenger is at dest_coach, and their destination is fd
                    # If fd == dest_coach, they belong there, so no conflict
                    # But wait, the movable passenger wants to go to dest_coach
                    # which is currently occupied by a fixed passenger
                    # This means the movable passenger can never reach their destination
                    print(-1)
                    return
    
    # If we reach here, rearrangement is possible
    # Now we need to count the minimum number of adjacent swaps
    
    # The approach: consider only the movable passengers
    # Create a permutation based on their destinations relative to available positions
    
    # Available positions are all coaches except those occupied by fixed passengers
    available_positions = sorted([i for i in range(1, n+1) if i not in fixed_destinations])
    
    # For each movable passenger, find their target position in the available positions
    # Create a mapping from destination coach to its index in available_positions
    dest_to_pos = {}
    for idx_pos, pos in enumerate(available_positions):
        dest_to_pos[pos] = idx_pos
    
    # Create the permutation: for each available position (in order), 
    # which destination does the passenger currently at that position want?
    
    # First, map current coaches to passengers for movable ones
    current_to_dest = {}
    for current_coach, dest_coach in movable_passengers:
        current_to_dest[current_coach] = dest_coach
    
    # Build the permutation
    # For each available position (sorted), get the destination of the passenger currently there
    permutation = []
    for pos in available_positions:
        if pos in current_to_dest:
            dest = current_to_dest[pos]
            # Map destination to its position index in available_positions
            perm_val = dest_to_pos[dest]
            permutation.append(perm_val)
    
    # Count inversions in the permutation
    _, inversions = merge_sort_count(permutation)
    
    print(inversions)

solve()
