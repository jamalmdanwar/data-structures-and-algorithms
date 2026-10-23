"""
Constraints: 
    1 <= s.length, t.length <= 5 * 10 ^ 4, a solution with O(N^2) might exceed time limit
    s and t consists of lowercase English letters
Edge Cases to handle:
    When length of s and t is mismatch, return False
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Handle Edge Case
        if len(s) != len(t):
            return False
        
        char_balance = {}

        for idx in range(len(s)):
            s_char = s[idx]
            t_char = t[idx]

            char_balance[s_char] = char_balance.get(s_char, 0) + 1
            char_balance[t_char] = char_balance.get(t_char, 0) - 1
        
        for count in char_balance.values():
            if count != 0:
                return False
        
        return True

"""
Time Complexity: O(N) where N is the length of string. We traverse the string characters atmost once in worst case scenario
Space Complexity: O(1) Auxillary space for the hash map since only 26 entries at max will be present in worst case scenario

DRY-RUN
    s = 'aac'
    t = 'acc'

    Length is same therefore no early-exit

    char_balance = {} # Dict Initialized
    Iteration 1: (for first loop)
        idx = 0
        s_char = 'a'
        t_char = 'a'

        char_balance['a'] = 0 + 1 = 0 -> char_balance = {'a': 1}
        char_balance['a'] = 1 - 1 = 0 -> char_balance = {'a': 0}
    
    Iteration 2: (for first loop)
        idx = 1
        s_char = 'a'
        t_char = 'c'

        char_balance['a'] = 0 + 1 = 0 -> char_balance = {'a': 1}
        char_balance['c'] = 0 - 1 = 0 -> char_balance = {'a': 1,'c':-1}
    
    Iteration 3: (for first loop)
        idx = 2
        s_char = 'c'
        t_char = 'c'

        char_balance['c'] = -1 + 1 = 0 -> char_balance = {'a': 1, 'c': 0}
        char_balance['c'] = 0 - 1 = 0 -> char_balance = {'a': 1,'c':-1}

    Iteration 1 (for second loop):
        count = 1 (from key 'a')
        retun False
"""