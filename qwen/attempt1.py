def solve():
    n = int(input())
    passengers = []
    for _ in range(n):
        current, dest, age = map(int, input().split())
        passengers.append((current, dest, age))
    
    # Create arrays for current and target positions
    current_pos = [0] * (n + 1)
    target_pos = [0] * (n + 1)
    immovable = set()
    
    # Fill the current positions and identify immovable passengers
    for current, dest, age in passengers:
        current_pos[current] = dest
        if age > 60:
            immovable.add(current)
            # If an immovable passenger is not already at their destination, it's impossible
            if current != dest:
                print(-1)
                return
    
    # Check if destinations are unique and valid
    used_destinations = set()
    for _, dest, _ in passengers:
        if dest < 1 or dest > n:
            print(-1)
            return
        if dest in used_destinations:
            print(-1)
            return
        used_destinations.add(dest)
    
    # Create the permutation that needs to be achieved
    # We need to transform the current arrangement to the target arrangement
    # where passenger at position i should go to position current_pos[i]
    
    # Build the target configuration: what passenger should be at each coach
    target_config = [0] * (n + 1)
    for current, dest, age in passengers:
        target_config[dest] = current  # The passenger who should be at coach 'dest'
    
    # Now we need to count swaps to transform current_config to target_config
    # But respecting the constraint that immovable passengers can't move
    
    # First, check if any immovable passenger is blocking the required arrangement
    for pos in immovable:
        # The passenger at position 'pos' cannot move
        # So they must already be at their destination
        # This was checked earlier, so we're good
        
        # Additionally, we need to ensure that the passenger who should be at position 'pos' 
        # in the final arrangement is either the same passenger or can reach there
        required_passenger = target_config[pos]
        if pos != required_passenger:
            # A different passenger needs to be at this position
            # But we can't move the current passenger out
            print(-1)
            return
    
    # Create the current sequence of passengers
    current_sequence = [0] * n
    for current, dest, age in passengers:
        current_sequence[current - 1] = (dest, age, current)
    
    # We'll simulate the sorting process, but only allow swaps between adjacent elements
    # where neither element is an immovable passenger that's not at its destination
    # Actually, let's use a different approach: bubble sort counting with constraints
    
    # Create an array representing the current order of destination requirements
    arr = list(range(1, n + 1))  # Start with coaches 1 to n
    passenger_at_coach = {}
    destination_for_coach = {}
    
    for current, dest, age in passengers:
        passenger_at_coach[current] = (dest, age)
        destination_for_coach[current] = dest
    
    # Create the sequence of destinations in current order
    seq = []
    for i in range(1, n + 1):
        dest, age = passenger_at_coach[i]
        seq.append((dest, age, i))
    
    # Count minimum swaps using bubble sort like approach
    # But we cannot swap if either passenger is immovable and not at destination
    def can_swap(pos):
        # Check if we can swap elements at pos and pos+1 (0-indexed)
        left_passenger = seq[pos]
        right_passenger = seq[pos + 1]
        
        left_dest, left_age, left_current = left_passenger
        right_dest, right_age, right_current = right_passenger
        
        # If left passenger is immovable, they can only stay at their destination
        if left_age > 60 and left_current != left_dest:
            return False
            
        # If right passenger is immovable, they can only stay at their destination
        if right_age > 60 and right_current != right_dest:
            return False
            
        return True
    
    # Make a copy of the sequence to work with
    temp_seq = seq[:]
    swaps = 0
    swapped = True
    
    while swapped:
        swapped = False
        for i in range(len(temp_seq) - 1):
            # We want to sort by destination coach
            if temp_seq[i][0] > temp_seq[i + 1][0]:
                if can_swap(i):
                    temp_seq[i], temp_seq[i + 1] = temp_seq[i + 1], temp_seq[i]
                    swaps += 1
                    swapped = True
                else:
                    # Cannot perform required swap
                    print(-1)
                    return
    
    # Verify the final arrangement
    for i in range(n):
        dest, age, original_pos = temp_seq[i]
        if i + 1 != dest:  # Coach number should match destination
            print(-1)
            return
    
    # One more check: immovable passengers must remain in place
    for i in range(n):
        _, age, original_pos = temp_seq[i]
        if age > 60 and original_pos != i + 1:
            print(-1)
            return
    
    print(swaps)

solve()
