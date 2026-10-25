"""
Constraints:
    1 <= arr.length <= 10^4
    1 <= arr[i] <= 10^5

Edge Cases to Handle:
    1. Array of length 1: Handled naturally by the loop logic, replacing the single element with -1.

Brute Force Approach
    Traverse left-to-right. For every element at index i, slice the array arr[i+1:] and find the max.
    This forces an O(N) scan inside an O(N) loop, resulting in an O(N^2) Time Complexity, which will time out.

Pattern Matching & Optimization
    Traverse backwards (Right-to-Left). By keeping a running track of the `right_max`, we can evaluate
    and replace each element in O(1) time per step.
    Furthermore, we can do this in-place by mutating the input `arr` directly, dropping Auxiliary Space to O(1).
"""

class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        #Code Solution
        
        # The greatest element to the right of the last element is always -1
        right_max = -1
        
        # Traverse backwards from the last element down to index 0
        for i in range(len(arr) - 1, -1, -1):
            # Temporarily store the current value before we overwrite it
            current_val = arr[i]
            
            # Replace the current element with the greatest element seen to its right
            arr[i] = right_max
            
            # Update the greatest element seen so far for the next iteration
            if current_val > right_max:
                right_max = current_val
                
        return arr

"""
DRY-RUN & Complexity
Time Complexity: O(N) 
    We visit each element in the array exactly once during the single reverse traversal.
Space Complexity: O(1) 
    We modify the input array in-place, using only two integer variables (`right_max`, `current_val`).

DRY-RUN:
    arr = [17, 18, 5, 4, 6, 1]
    right_max = -1
    
    Iteration 1 (i = 5):
        current_val = 1
        arr[5] = -1
        right_max = max(-1, 1) = 1
        arr = [17, 18, 5, 4, 6, -1]
        
    Iteration 2 (i = 4):
        current_val = 6
        arr[4] = 1
        right_max = max(1, 6) = 6
        arr = [17, 18, 5, 4, 1, -1]
        
    Iteration 3 (i = 3):
        current_val = 4
        arr[3] = 6
        right_max = max(6, 4) = 6
        arr = [17, 18, 5, 6, 1, -1]
        
    ... (continues to index 0)
    
    Final arr = [18, 6, 6, 6, 1, -1]
"""
