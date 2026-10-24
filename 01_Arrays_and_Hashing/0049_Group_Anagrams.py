"""
Constraints:
    1 <= strs.length <= 10^4
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

Edge Cases to Handle:
    1. Empty strings: `[""]` should be grouped together naturally.
    2. Single characters: `["a"]` should be handled without out-of-bounds errors.

Brute Force Approach
    Iterate through every string and sort it alphabetically (e.g., "tea" -> "aet"). 
    Use the sorted string as a dictionary key to group anagrams.
    Because sorting takes O(M log M) time per string, the overall time complexity is O(N * M log M).

Pattern Matching & Optimization (The "Recipe" Method)
    We can eliminate the O(M log M) sorting penalty by counting ingredients instead of alphabetizing them.
    By initializing a 26-slot array for each word, we can use raw ASCII math to tally the character frequencies in a single O(M) pass.
    We convert this frequency array into a tuple (our immutable "recipe") and use it as the Hash Map key.
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        #Code Solution
        group_map = defaultdict(list)

        for s in strs:
            count = [0] * 26
            
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            group_map[tuple(count)].append(s)

        return list(group_map.values())

"""
DRY-RUN & Complexity
Time Complexity: O(N * M) 
    Where N is the number of strings and M is the maximum length of a string. We evaluate each character of every string exactly once.
Space Complexity: O(N * M) 
    In the worst-case scenario (no anagrams exist), we store every string in the Hash Map along with its unique tuple key.

DRY-RUN:
    strs = ["eat", "tea"]
    group_map = defaultdict(list)
    
    Iteration 1:
        s = "eat"
        count = [0, 0, 0... 0] (26 zeros)
        char = 'e' -> ord('e') - ord('a') = 4 -> count[4] = 1
        char = 'a' -> ord('a') - ord('a') = 0 -> count[0] = 1
        char = 't' -> ord('t') - ord('a') = 19 -> count[19] = 1
        Tuple key created: (1, 0, 0, 0, 1, 0... 1... 0)
        group_map[(1,0,0...)] = ["eat"]
        
    Iteration 2:
        s = "tea"
        count = [0, 0, 0... 0] (26 zeros)
        char = 't' -> ord('t') - ord('a') = 19 -> count[19] = 1
        char = 'e' -> ord('e') - ord('a') = 4 -> count[4] = 1
        char = 'a' -> ord('a') - ord('a') = 0 -> count[0] = 1
        Tuple key created: (1, 0, 0, 0, 1, 0... 1... 0) -> MATCHES EXISTING KEY
        group_map[(1,0,0...)] = ["eat", "tea"]
"""
