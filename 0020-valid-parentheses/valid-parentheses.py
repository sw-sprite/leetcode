class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup = {'(':')',
                  '[':']',
                  '{':'}'
                  }
        
        if len(s) == 1:
            return False
        stack = []
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            elif len(stack) == 0 or lookup[stack.pop()] != i:
                return False
            
        return len(stack) == 0
                
tests = [
    (
        ("()",),
        True,
    ),
    (
        ("()[]{}",),
        True,
    ),
    (
        ("(]",),
        False,
    ),
    (
        ("([)]",),
        False,
    ),
    (
        ("{[]}",),
        True,
    ),
]