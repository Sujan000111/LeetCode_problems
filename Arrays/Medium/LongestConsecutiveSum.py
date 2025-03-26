def longest_consecutive_sequence(nums):
    num_set = set(nums)  # Store all elements for O(1) lookups
    max_length = 0

    for num in nums:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)  # Update max length

    return max_length

# Example usage
nums = list(map(int, input("Enter numbers in list format (e.g., 100,4,200,1,3,2): ").split(',')))
print(longest_consecutive_sequence(nums))
