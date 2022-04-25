#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = 0
        r = len(nums)-1
        while n <= r:
            mid = (n+r)//2
            if nums[mid] < target:
                n = mid + 1
            else:
                r = mid - 1
        return n