#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
		#비트 연산자를 사용해서 풀기
        answer = 0
        for num in nums:
            answer ^= num
        return answer