"""
Constraints:
    0 <= s.length <= 100
    0 <= t.length <= 10^4
    s and t consist only of lowercase English letters.

Edge Cases to Handle:
    1. s is empty (""): An empty string is always a subsequence of any string. Return True.
    2. s is longer than t: Impossible to be a subsequence. Return False.
    3. t is empty but s is not: Return False.

-------------------------------------------------------------------------------
Brute Force Approach (String Slicing)

    The naive instinct is to loop through each character in `s`, find its first 
    occurrence in `t`, and then chop off everything in `t` before that character 
    so we don't reuse letters. 

    class SuboptimalSolution:
        def isSubsequence(self, s: str, t: str) -> bool:
            for char in s:
                idx = t.find(char)
                if idx == -1:
                    return False
                # Anti-Pattern: String slicing creates a brand new string in memory
                t = t[idx + 1:] 
            return True

    Why it fails: While logically correct, slicing strings `t = t[idx + 1:]` 
    is an O(T) operation in Python. Because we do this for every character in `s`, 
    the Time Complexity degrades to O(S * T), and Auxiliary Space becomes O(T) 
    due to creating new string copies on every iteration.

-------------------------------------------------------------------------------
Pattern Matching & Alternate Approach (Pythonic Iterator)

    Before looking at the standard algorithmic approach, Python has a highly 
    optimized, C-level trick using iterators. By converting `t` to an iterator, 
    the `in` keyword consumes the iterator sequentially without creating new strings.

    class PythonicSolution:
        def isSubsequence(self, s: str, t: str) -> bool:
            iterator_t = iter(t)
            # all() will short-circuit and return False if a character isn't found
            return all(char in iterator_t for char in s)

    Why it is good but risky: This operates in O(T) time and O(1) space and is 
    extremely fast. However, if we are asked to port this logic to Java 
    or C++ on the whiteboard, we cannot rely on Python's hidden iterator state. 
    We need a language-agnostic algorithm.

-------------------------------------------------------------------------------
Code Solution (The Optimal Two-Pointer Algorithm)

    We use two separate index pointers. Pointer `i` tracks our target characters 
    in `s`, and pointer `j` scans through the "host" string `t`. We only increment 
    `i` when we find a match.
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Edge case: If s is longer than t, it cannot be a subsequence
        if len(s) > len(t):
            return False
            
        i, j = 0, 0
        
        # Traverse while both pointers are within bounds
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Move target pointer only on a match
            j += 1      # Host pointer ALWAYS moves forward
            
        # If i reached the length of s, we found all characters in order
        return i == len(s)

"""
DRY-RUN & Complexity
Time Complexity: O(T) 
    In the worst case, pointer `j` traverses the host string `t` exactly once. 
    Pointer `i` moves at most S times. Overall time is bounded by the length of t.
Space Complexity: O(1) 
    We only allocate two integer variables (`i` and `j`) to track indices. No new 
    strings or data structures are created.

DRY-RUN:
    s = "abc", t = "ahbgdc"
    i = 0, j = 0
    
    Iteration 1: s[0]('a') == t[0]('a') -> Match! i=1, j=1
    Iteration 2: s[1]('b') != t[1]('h') -> No match. j=2
    Iteration 3: s[1]('b') == t[2]('b') -> Match! i=2, j=3
    Iteration 4: s[2]('c') != t[3]('g') -> No match. j=4
    Iteration 5: s[2]('c') != t[4]('d') -> No match. j=5
    Iteration 6: s[2]('c') == t[5]('c') -> Match! i=3, j=6
    
    Loop ends (j = 6, len(t) = 6).
    Return i == len(s) -> 3 == 3 -> True.
"""
