
def two_sum(nums, target):
    num_map = {}  # Create a dictionary to store numbers and their indices

    for i, num in enumerate(nums):
        complement = target - num  # Calculate the complement needed to reach the target

        if complement in num_map:
            # If the complement is already in the dictionary, we found a pair
            return [num_map[complement], i]  
        else:
            # Otherwise, add the current number and its index to the dictionary
            num_map[num] = i

    return None
