"""
READ & Document
Constraints:
    1 <= s.length <= 10^4
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.

Edge Cases to Handle:
    1. Trailing spaces: "moon  " -> We must skip spaces at the end before counting.
    2. Single word strings: "hello" -> The loop must terminate cleanly without an out-of-bounds error at index 0.
    3. Multiple spaces between words: "a   b" -> Handled naturally by stopping at the first space after the word.

-------------------------------------------------------------------------------
"SPEAK ALOUD" Brute Force Approach (The Pythonic Trap)

    The immediate instinct in Python is to leverage built-in methods:
    
    class BuiltInSolution:
        def lengthOfLastWord(self, s: str) -> int:
            return len(s.split()[-1])

    Why it fails the senior standard: 
    While it takes O(N) time and looks clean, `.split()` allocates a brand new 
    list in memory containing every single word from the string. If the string 
    is 10,000 characters long, you just burned O(N) Auxiliary Space to answer 
    a simple counting question.

-------------------------------------------------------------------------------
Pattern Matching & Optimization (Reverse Traversal)

    To achieve O(1) space, we must evaluate the string in-place. 
    Because we only care about the *last* word, we start at the end of the string 
    (Right-to-Left traversal) and use a two-step while loop:
    1. Move the pointer left to skip any trailing spaces.
    2. Move the pointer left and count characters until we hit the next space.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Code Solution
        length = 0
        i = len(s) - 1

        # 1. Skip all trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # 2. Count the characters of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
            
        return length

"""
DRY-RUN & Complexity
Time Complexity: O(N)
    In the worst-case scenario (e.g., "      a"), we traverse the entire string once. 
    Best-case scenario (e.g., "hello"), we only traverse the last word, operating in O(L) time where L is the word length.
Space Complexity: O(1)
    We only allocate two integer variables (`length` and `i`), utilizing zero extra memory.

DRY-RUN:
    s = " a  "
    i = 3, length = 0
    
    Step 1 (Skip spaces):
        s[3] == ' ' -> i = 2
        s[2] == ' ' -> i = 1
        
    Step 2 (Count word):
        s[1] == 'a' != ' ' -> length = 1, i = 0
        
    Step 2 (Next Iteration):
        s[0] == ' ' -> Loop condition fails.
        
    Return length -> 1.
"""
