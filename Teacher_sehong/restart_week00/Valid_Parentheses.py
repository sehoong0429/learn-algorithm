class Solution(object):
   def isValid(self, s) :
        
        stack=[] #stack을 위한 빈 리스트 
        closeToOpen={'}':'{',')':'(',']':'['}  
        for c in s:
            if c in closeToOpen(): # '(', '{', '[' 열린괄호는 stack에 추가한다!
                stack.append(c)
            else: #stack 리스트와 비교 
                if stack and closeToOpen[c]==stack[-1] :  
                    stack.pop()
                else: 
                    return False
        
        if stack
          return False 
        return True #반복문을 다 돌고 stack이 비워진경우. 
