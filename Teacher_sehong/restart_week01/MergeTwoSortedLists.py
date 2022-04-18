#You are given the heads of two sorted linked lists list1 and list2.
#Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
        #노드가 있으면 그 안에 value가 있고, next 변수가 다음 노드에 대한 참조를 가지고 있다.
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        Optional 의 의미
        node의 head 값이 유효한 list node일 수도 있고, none이 될 수도 있다. ex) l1 = [], l2 = [] 혹은 l1 = [], l2 = [0]
        """
#2개의 포인터(from, to)를 이용해 연결할 노드를 가리킨다.
        # l1에 아무것도 없으면 l2만 return 해주면 된다.
        if list1 == None:
            return list2

        # l1 = [1, 2] , l2 = []
        if list2 == None:
            return list1

        # 2개의 포인터(from, to)를 이용해 연결할 노드를 가리킨다.
        ans = None
        if list1.val <= list2.val:
            fromPtr = list1
            toPtr = list2
            ans = fromPtr
        else:
            fromPtr = list2
            toPtr = list1
            ans = fromPtr
        while fromPtr != None:
            if fromPtr.val <= toPtr.val:
                while fromPtr.next != None and fromPtr.next.val <= toPtr.val:
                    fromPtr = fromPtr.next
                temp = fromPtr.next
                fromPtr.next = toPtr

                fromPtr = temp
                pass
            else:
                temp = fromPtr
                fromPtr = toPtr
                toPtr = temp
        return ans
