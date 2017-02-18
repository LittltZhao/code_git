# -*- coding:utf-8 -*-

def mergeTwoLists(l1,l2):
    if l1.val<l2.val:
        p=l1
        q=l2
    else:
        p=l2
        q=l1
    head=p
    while q is not None:
        if p.next is None:
            p.next=q
            return head
        if q.val<p.next.val:
            temp1=p.next
            temp2=q.next
            p.next=q
            q.next=temp1
            p=q
            q=temp2
        else:
            p=p.next
    return head



class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

def mergeTwoLists(l1,l2):
    if not l1:
        return l2
    if not l2:
        return l1
    dummy=ListNode(0)
    p=dummy
    while l1 and l2:
        if l1.val<l2.val:
            p.next=l1
            l1=l1.next
        else:
            p.next=l2
            l2=l2.next
        p=p.next
    if l1:
        p.next=l1
    else:
        p.next=l2
    return dummy.next
