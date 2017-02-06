# -*- coding:utf-8 -*-
# 删除给定节点
# 解决策略：只给了要删除的节点，将下一节点的值赋予本节点，然后删除下一节点
class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

def DeleteNode(node):#删除指定节点
    node.val=node.next.val
    p=node.next
    node.next=p.next

def removeElements(head,val):#给出链表，删除指定节点
    dum=ListNode(0)
    dum.next=head
    p=dum
    while p.next:
        if p.next.val==val:
            p.next=p.next.next#?????
        else:
            p=p.next
    return dum.next

