//2번째 방법 
class Solution(object):
    def twoSum(self, nums, target):
    
	   if len(nums) <= 1: //값이 2개 이상이어야함
        return false
       
        num_map = {}  //map에 대한 정의 

        for idx, num in enumerate(nums):   //순회 시작
                                           //현재 값이 map에 있는지 확인을 하는데 만약에 없다면 필요로 하는 값과 현재값의 index를 저장
            
            if num in num_map:             //현재 num의 값을 필요로 했던 이전의 값의 index와 현재 num의 index를 리턴 
                return [num_map[num], idx]
            else:
                num_map[target - num] = idx
          
        return [-1, -1]                    //아무것도 없으면 -1을 리턴 
