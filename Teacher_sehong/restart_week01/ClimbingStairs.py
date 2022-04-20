#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int

        n = 1:1가지
        n = 2:2가지
        n = 3:1+2 =3가지
        n = 4:2+3 =5가지

        n번째 칸에 오르는 방법의 개수 => f(n)
        f(n) = f(n-1) + f(n-2)

        시간 복잡도 : 0(n)
        """
        dp = {1: 1, 2: 2}  # 첫번째 칸, 두번째 칸 오르는 방법의 개수 해시테이블 선언
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
