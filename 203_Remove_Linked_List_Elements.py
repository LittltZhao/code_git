# -*- coding:utf-8 -*-


class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None
def removeElements(head,val):
    dum=ListNode(0)
    dum.next=head
    p=dum
    while p.next:
        if p.next.val=val:
            p.next=p.next.next#为什么p.next.next不会为None????
        else:
            p=p.next
    return dum.next
