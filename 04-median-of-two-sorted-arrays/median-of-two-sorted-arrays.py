from statistics import median 

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        need_2 = True if ((m+n) % 2) == 0 else False
        index_seek = (m+n) // 2

        temp_1 = 0
        temp_2 = 0

        cur_nums1_index = 0
        cur_nums2_index = 0

        if m == 0:
            return median(nums2)
        if n == 0: 
            return median(nums1)
        
        if need_2:
            for count in range(index_seek+1):
                temp_2 = temp_1
                if cur_nums1_index != n and cur_nums2_index != m:
                    if nums1[cur_nums1_index] > nums2[cur_nums2_index]:
                        temp_1 = nums2[cur_nums2_index]
                        cur_nums2_index += 1
                    else:
                        m1 = nums1[cur_nums1_index]
                        cur_nums1_index += 1
                elif: cur_nums1_index < m:
                    temp_1 = nums1[cur_nums1_index]
                    cur_nums1_index += 1
                else:
                    
                    




        return 0



tests = [
    (
        ([1, 3], [2],),
        2,
    ),
    (
        ([1, 2], [3, 4],),
        2.5,
    ),
    (
        ([0, 0], [0, 0],),
        0,
    ),
    (
        ([], [1],),
        1,
    ),
    (
        ([2], [],),
        2,
    ),
]
