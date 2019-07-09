class Node(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

# 方法1：三个指针逐个翻转
def Reversed(head):
    p = head
    q = head.next
    p.next = None
    while q:
        r = q.next
        q.next = p
        p = q
        q = r
    return p

# 方法2：方法二：尾插法翻转
def Reversed2(head):
    s = Node(0)
    while head:
        q = head.next
        head.next = s.next
        s.next = head
        head = q
    return s.next

# 方法3：递归
def Reversed3(head):
    if head.next == None:
        return head
    new_head = Reversed3(head.next)
    head.next.next = head
    head.next = None
    return new_head

#测试用例
if __name__ == '__main__':
    l1 = Node(3)
    l1.next = Node(2)
    l1.next.next = Node(1)
    l1.next.next.next = Node(9)
    print (l1.val, l1.next.val, l1.next.next.val, l1.next.next.next.val)
    l = ReverseList(l1)
    print(l.val, l.next.val, l.next.next.val, l.next.next.next.val)
