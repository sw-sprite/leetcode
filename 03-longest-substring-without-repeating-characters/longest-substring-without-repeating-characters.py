class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        longest = 0
        local_max = 0
        starting_index = 0
        cur_index = 0

        for i, v in enumerate(s):
            if v not in s[starting_index:cur_index]:
                cur_index = i+1
                longest = max(cur_index - starting_index, longest)
                # print(v, cur_index - starting_index, longest, starting_index, cur_index)
            else:
                first_repeating = s[starting_index:cur_index].find(v)
                starting_index += first_repeating + 1
                cur_index = i+1
                # print("found repeating")
                # print(v, cur_index - starting_index, longest, starting_index, cur_index)
        return longest

tests = [
    (
        ("abcabcbb",),
        3,
    ),
    (
        ("bbbbb",),
        1,
    ),
    (
        ("pwwkew",),
        3,
    ),
    (
        ("",),
        0,
    ),
    (
        ("a",),
        1,
    ),
    (
        ("abcde",),
        5,
    ),
    (
        ("abba",),
        2,
    ),
    (
        ("dvdf",),
        3,
    ),
]