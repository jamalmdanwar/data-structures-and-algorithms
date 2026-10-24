"""
Constraints:
    2 <= nums.length <= 10^4 (An O(N^2) solution may pass but is sub-optimal)
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Only one valid answer exists.

Edge Cases to Handle:
    1. Minimum length array: Inputs like `nums = [3, 3], target = 6`. 
    2. Duplicate elements forming target: Ensure a number can pair with an identical number at a different index, but never with itself. (Checking the dictionary *before* adding the current number natively handles this).
    3. Negative numbers: The math (target - value) must seamlessly resolve negative complements (e.g., target = -8, value = 2, complement = -10).

Brute Force Approach
    Iterate through every element `x` using a pointer, and use a nested loop to search the rest of the array for `target - x`.
    This results in O(N^2) time complexity and O(1) space complexity.

Pattern Matching & Optimization
    We can trade memory for time using a Hash Map. 
    By storing elements we have already evaluated alongside their original indices, we can look up the required `complement` in O(1) time during a single pass. 
    This drops Time Complexity to O(N) but increases Auxiliary Space to O(N).
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        
        for idx, value in enumerate(nums):
            complement = target - value
            
            # Check if the required pairing number has already been processed
            if complement in seen:
                return [seen[complement], idx]
            
            # Store the current value and its index for future lookups
            seen[value] = idx

"""
DRY-RUN & Complexity
Time Complexity: O(N) 
    We traverse the array at most once. Hash Map lookups and insertions operate in O(1) time.
Space Complexity: O(N) 
    In the worst-case scenario (the matching pair is at the very end of the array), we will store N-1 elements in the Hash Map.

DRY-RUN:
    nums = [3, 2, 4], target = 6
    seen = {}
    
    Iteration 1:
        idx = 0, value = 3
        complement = 6 - 3 = 3
        Is 3 in seen? False.
        seen[3] = 0 -> seen = {3: 0}
        
    Iteration 2:
        idx = 1, value = 2
        complement = 6 - 2 = 4
        Is 4 in seen? False.
        seen[2] = 1 -> seen = {3: 0, 2: 1}
        
    Iteration 3:
        idx = 2, value = 4
        complement = 6 - 4 = 2
        Is 2 in seen? True (seen[2] == 1).
        return [seen[2], 2] -> [1, 2]
"""
