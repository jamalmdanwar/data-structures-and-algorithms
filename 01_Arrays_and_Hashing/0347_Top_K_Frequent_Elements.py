"""
READ & Document
Constraints:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

Edge Cases to Handle:
    1. nums length == k: Every element's frequency qualifies, return all unique elements.
    2. Arrays with negative numbers: Safely handled natively by Hash Map keys.

-------------------------------------------------------------------------------
"SPEAK ALOUD" Brute Force Approach (Sorting)

    Count the frequencies of all elements using a dictionary. Then, extract the 
    keys and sort them based on their frequency values in descending order. 
    Slice the first `k` elements from the sorted result.
    
    Time Complexity: O(N log N) because we must sort the unique elements. 
    Space Complexity: O(N) to store the Hash Map.

-------------------------------------------------------------------------------
Pattern Matching & Optimization (Bucket Sort)

    How do we drop O(N log N) sorting down to O(N)? We trade space for time using 
    Bucket Sort. 
    
    The maximum frequency any number can have is N (the length of the array). 
    If we create an array `freq` of size N + 1, we can use the **index** of this 
    array to represent the frequency. The values at that index will be a list of 
    the numbers that occur at that frequency. By scanning this array backwards 
    from the end (highest frequency), we can collect our top k elements in strict O(N) time.
"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Code Solution
        count = {}
        # Initialize an array of empty lists, sized exactly to max possible frequency (len(nums))
        freq = [[] for i in range(len(nums) + 1)]

        # 1. Tally frequencies
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            
        # 2. Map numbers into buckets where the index == frequency
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        
        # 3. Traverse buckets backwards (highest frequency to lowest)
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                # Short-circuit as soon as we hit the required k elements
                if len(res) == k:
                    return res

"""
DRY-RUN & Complexity
Time Complexity: O(N)
    - O(N) to populate the `count` Hash Map.
    - O(N) to distribute the unique elements into the `freq` array.
    - O(N) worst-case to traverse the `freq` array from right to left.
    Total Time: strictly bounded by O(N).
Space Complexity: O(N)
    - O(N) for the `count` Hash Map.
    - O(N) for the `freq` array of lists.

DRY-RUN:
    nums = [1, 1, 1, 2, 2, 3], k = 2
    n = 6
    
    1. Count Map: 
        count = {1: 3, 2: 2, 3: 1}
        
    2. Populate Buckets (freq array of size 7):
        freq = [ [], [], [], [], [], [], [] ]
        freq[1].append(3) -> freq = [ [], [3], [], [], [], [], [] ]
        freq[2].append(2) -> freq = [ [], [3], [2], [], [], [], [] ]
        freq[3].append(1) -> freq = [ [], [3], [2], [1], [], [], [] ]
        
    3. Traverse Backwards:
        i = 6 down to 4: Empty lists, skipped.
        i = 3: freq[3] has [1]. 
               res.append(1) -> res = [1]. len(res) != 2.
        i = 2: freq[2] has [2]. 
               res.append(2) -> res = [1, 2]. len(res) == 2. RETURN [1, 2].
"""
