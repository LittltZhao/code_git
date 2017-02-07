# -*- coding:utf-8 -*-
# 单链表反转
def reverseList(head):
    if head is None:
        return None
    p=None
    while head is not None:
        q=head
        head=q.next
        q.next=p
        p=q
    head=p
    return head

def reverseList2(head):
    p=head
    newList=[]
    while p:
        newList.insert(0,p.val)
        p=p.next
    p=head
    for v in newList:
        p.val=v
        p=p.next
    return head
