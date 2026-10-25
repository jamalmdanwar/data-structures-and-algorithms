"""
Constraints:
    n == nums.length
    1 <= n <= 1000
    1 <= nums[i] <= 1000

Edge Cases to Handle:
    None required. The constraint 1 <= n guarantees the array will never be empty.

Brute Force Approach
    Create an empty array `ans`. Iterate through `nums` and `.append()` each element. 
    Iterate through `nums` a second time and `.append()` each element again.
    This operates in O(N) time but suffers from dynamic memory resizing overhead.

Pattern Matching & Optimization
    To optimize memory allocation, we can pre-allocate the exact required size (2N) upfront. 
    By utilizing index math (i and i + n), we can populate both halves of the concatenated 
    array in a single O(N) pass, completely bypassing the dynamic array resizing penalty.
"""

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        #Code Solution
        n = len(nums)
        
        # Pre-allocate array of size 2n
        ans = [0] * (2 * n) 

        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
            
        return ans

"""
DRY-RUN & Complexity
Time Complexity: O(N) 
    We iterate through the array of size N exactly once. 
Space Complexity: O(N)
    We allocate a new array of size 2N. (Often considered O(1) auxiliary space if the return array does not count toward the limit).

DRY-RUN:
    nums = [1, 2, 3]
    n = 3
    ans = [0, 0, 0, 0, 0, 0]
    
    Iteration 1: 
        i = 0
        ans[0] = nums[0] -> 1
        ans[0+3] = nums[0] -> 1
        ans = [1, 0, 0, 1, 0, 0]
        
    Iteration 2: 
        i = 1
        ans[1] = nums[1] -> 2
        ans[1+3] = nums[1] -> 2
        ans = [1, 2, 0, 1, 2, 0]
        
    Iteration 3: 
        i = 2
        ans[2] = nums[2] -> 3
        ans[2+3] = nums[2] -> 3
        ans = [1, 2, 3, 1, 2, 3]
        
    return [1, 2, 3, 1, 2, 3]
"""
