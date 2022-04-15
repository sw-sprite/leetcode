class Solution:
	def containsDuplicate(self, nums: list[int]) -> bool:
		s = set()
		for i in nums: 
			if i in s:
				return True
			else:
				s.add(i)
		return False

        # return len(nums) != len(list(set(nums)))


tests = [
  (
    ([1, 2, 3, 1],),
    True,
  ),
  (
    ([1, 2, 3, 4],),
    False,
  ),
  (
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],),
    True,
  ),
]