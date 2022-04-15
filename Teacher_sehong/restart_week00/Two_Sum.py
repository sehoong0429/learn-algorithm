class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
						//i 다음부터 n 까지 순회를 하고 
            for j in range(i + 1, n): 
								//i번째 숫자와 j번째 숫자의 합이 target과 같으면 
                if nums[i] + nums[j] == target: 
										//i와 j를 return 한다
                    return[i,j] 
