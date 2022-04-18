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
        if None in (list1, list2):
            return list1 or list2

            # from <= to

        if list1.val <= list2.val:
            ans = fromPtr = list1
            toPtr = list2

        else:
            ans = fromPtr = list2
            toPtr = list1

        while fromPtr != None:
            if fromPtr.val <= toPtr.val:
                while fromPtr.next != None and fromPtr.next.val <= toPtr.val:
                    fromPtr = fromPtr.next

                fromPtr.next, fromPtr = toPtr, fromPtr.next
            else:
                fromPtr, toPtr = toPtr, fromPtr
        return ans






