"""
READ & Document
Constraints:
    2 <= nums.length <= 10^5
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    MUST execute in O(N) time and without using the division operation.

Edge Cases to Handle:
    1. A single zero in the array: Everything else becomes 0 except the zero's index.
    2. Multiple zeroes in the array: Every single index in the output must be 0.
    3. Negative numbers: Must handle sign flips naturally via continuous multiplication.

-------------------------------------------------------------------------------
"SPEAK ALOUD" Brute Force & Suboptimal Approaches

    Approach 1: Nested Loops (Brute Force)
    For every element `i`, loop through the rest of the array to calculate the product.
    Time Complexity: O(N^2) - Will time out given length 10^5.

    Approach 2: Total Product & Division
    Iterate once to find the total product of the entire array. Iterate again and 
    divide the total product by `nums[i]` to get the answer.
    Why it fails: 
    1. The problem strictly forbids using the division operator.
    2. Division completely breaks down mathematically if there are zeroes in the array.

-------------------------------------------------------------------------------
Pattern Matching & Optimization (Prefix & Postfix Products)

    If we cannot divide, we must multiply the elements to the *left* of `i` with 
    the elements to the *right* of `i`. 
    
    Instead of calculating this from scratch for every element, we can sweep the 
    array twice:
    1. Sweep Left-to-Right: Store the running product of all elements to the left (Prefix).
    2. Sweep Right-to-Left: Track the running product of all elements to the right (Postfix), 
       and immediately multiply it with the stored Prefix.
       
    To achieve O(1) auxiliary space, we compute the prefixes directly inside the 
    return array `res`, and use a single integer variable to track the rolling postfix.
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Code Solution
        n = len(nums)
        res = [1] * n
        
        # Pass 1: Compute Left Prefixes
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # Pass 2: Compute Right Postfixes and multiply in-place
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res

"""
DRY-RUN & Complexity
Time Complexity: O(N)
    We sweep through the array exactly twice. O(N) + O(N) = O(N).
Space Complexity: O(1) auxiliary space
    The problem description explicitly states that the output array `res` does not 
    count toward space complexity. We only use two integer variables (`prefix` and `postfix`).

DRY-RUN:
    nums = [1, 2, 3, 4]
    res  = [1, 1, 1, 1]
    
    --- Left Pass (Prefixes) ---
    i = 0: res[0] = 1, prefix = 1 * 1 = 1
    i = 1: res[1] = 1, prefix = 1 * 2 = 2
    i = 2: res[2] = 2, prefix = 2 * 3 = 6
    i = 3: res[3] = 6, prefix = 6 * 4 = 24
    res state: [1, 1, 2, 6]
    
    --- Right Pass (Postfixes) ---
    i = 3: res[3] = 6 * 1 = 6, postfix = 1 * 4 = 4
    i = 2: res[2] = 2 * 4 = 8, postfix = 4 * 3 = 12
    i = 1: res[1] = 1 * 12 = 12, postfix = 12 * 2 = 24
    i = 0: res[0] = 1 * 24 = 24, postfix = 24 * 1 = 24
    res state: [24, 12, 8, 6]
    
    Return [24, 12, 8, 6]
"""
