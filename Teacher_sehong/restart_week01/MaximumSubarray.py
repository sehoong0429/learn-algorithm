#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#A subarray is a contiguous part of an array.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 현재까지의 더한 값을 계속 트래킹 해줘야함.
        # 현재까지의 더한 값은 고려대상이 아니기때문에 0으로 바꿔주는 작업 필요!
        maxSub = nums[0]  # 가장 첫번째 index
        currSum = 0  # 현재까지 더한 값을 트래킹 하기 위해 current sum을 0으로 지정

        for n in nums:
            # 현재까지 더한 요소들의 합이 음수일 경우 0으로 바꿔줌.
            if currSum < 0:
                currSum = 0
            # 현재까지 더한 요소가 양수일경우 그 다음 요소인 n을 더해준다.
            currSum += n
            # 음수가 아닌 연속된 양수의 합들 중에서 가장 큰 값을 리턴 해줌.
            maxSub = max(maxSub, currSum)
        return maxSub