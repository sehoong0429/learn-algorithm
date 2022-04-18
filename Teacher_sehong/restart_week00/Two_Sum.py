#2번째 방법
class Solution(object):
    def twoSum(self, nums, target):


def twoSum(self, nums, target):

    #값이 2개 이상이어야함.
    if len(nums) <= 1:
        return false

    #map에 대한 정의
    num_map = {}

    #순회 시작, 현재 값이 map에 있는지 확인
    for idx, num in enumerate(nums):
        #현재 num의 값을 필요로 했던 이전의 값의 index와 현재 num의 index를 리턴
        if num in num_map:
            return [num_map[num], idx]
        #현재 값이 없으면 필요로 하는 값과 현재값의 index를 저장
        else:
            num_map[target-num] = idx
    #아무것도 없으면 -1을 리턴
    return [-1, -1]
