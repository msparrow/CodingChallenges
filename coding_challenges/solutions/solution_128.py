
from collections import Counter

def majorityElement_hashmap(nums):
    if not nums:
        return -1
    if isinstance(nums, str):
        nums = list(nums)
    counts = Counter(nums)
    for num, count in counts.items():
        if count > len(nums) / 2:
            return num
    return -1

def majorityElement_boyermoore(nums):
    if not nums:
        return -1
    if isinstance(nums, str):
        nums = list(nums)
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    if nums.count(candidate) > len(nums) / 2:
        return candidate
    else:
        return -1
