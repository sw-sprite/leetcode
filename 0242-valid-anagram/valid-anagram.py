from collections import defaultdict
class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return Counter(s) == Counter(t)
    def isAnagram(self, s: str, t: str) -> bool:
        lookup = defaultdict(int)
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            lookup[s[i]] += 1
            lookup[t[i]] -= 1
        
        for key, value in lookup.items():
            if value != 0:
                return False
        
        return True

tests = [
    (
        ("anagram", "nagaram",),
        True,
    ),
    (
        ("rat", "car",),
        False,
    ),
]