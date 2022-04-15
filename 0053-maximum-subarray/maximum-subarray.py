class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = nums[0]
        max_now = 0
        
        for i in nums:
            max_now = max_now + i
            if max_so_far > max_now:
                max_now = 0
            elif max_now > max_so_far:
                max_so_far = max_now
            max_now = max(0, max_now)
        
        return max_so_far
        
tests = [
    (
        ([-2, -1, -3, -4, -1, -2, -1, -5, -4],),
        -1,
    ),
    (
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4],),
        4,
    ),
    (
        ([1],),
        1,
    ),
    (
        ([0],),
        0,
    ),
    (
        ([-1],),
        -1,
    ),
    (
        ([-100000],),
        -100000,
    ),
]