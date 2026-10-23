"""
Contraints: 
1 <= nums.length <= 10^5, An O(N^2) solution will require 10^10 operations (Time Limit Exceeded)
-10^9 <= nums[i] <= 10^9, Standard integer range, no overflow concerns in Python.
Edge Cases to Handle:
1. Minimum Array Length: num = [1] or [] should return False
2. All duplicates: num = [2, 2, 2, 2] should return True on second element
3. Negative Numbers: num = [-1, -2, -2] should handle negative numbers
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        # Early exit for arrays too small to have duplicates
        if not nums or len(nums) < 2:
            return False
        
        seen_numbers = set() #An empty set to log numbers seen

        for current_number in nums:
            if current_number in seen_numbers: #True indicates number appears twice in array
                return True
            else:
                seen_numbers.add(current_number) #Build seen_numbers set
        
        #If program reaches this point, that means the if block within for loop is not executed and no duplicates are found in array
        return False

"""
Time Complexity: O(N) where N is the length of nums. We traverse the list atmost once in worst case scenario
Space Complexity: O(N) Auxillary space for the hash set in the worst case when all elements of array is unique

DRY-RUN:
Input: nums = [1, 2, 3, 1]
len(nums) = 4 > 2, therefore the if condition is not satisfied and we move on
seen_numbers = set() initializes the hash set
Iteration 1:
  current_number = 1, is 1 in seen_numbers? No, add 1 to seen_numbers -> seen_numbers = {1}
Iteration 2:
  current_number = 2, is 2 in seen_numbers? No, add 2 to seen_numbers -> seen_numbers = {1, 2}
Iteration 3:
  current_number = 3, is 3 in seen_numbers? No, add 3 to seen_numbers -> seen_numbers = {1, 2, 3}
Iteration 4:
  current_number = 1, is 1 in seen_numbers? Yes, return True. The logic holds

PYTHONIC Approach
There is a Pythonic approach with one-liner solution: 
return len(nums) != len(set(nums))
This is not the effecient solution as it always forces list to set conversion even in cases when not needed, and if always forces to have time-complexity of O(N) and auxillary space-complexity of O(N) as well.
"""