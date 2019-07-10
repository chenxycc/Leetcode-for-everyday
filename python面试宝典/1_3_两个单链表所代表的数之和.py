"""链表"""
# 定义链表的结点
class LNode():
    def __init__(self):
        self.data = None # 数据域
        self.next = None # 指针域
####################方法1：链表转字符###############################
def add(head1, head2):
    if head1 is None or head1.next is None:
        return head2
    if head2 is None or head2.next is None:
        return head1
    p1 = head1.next # 用来遍历h1
    p2 = head2.next # 用来遍历h2
    a1 = ""
    while p1 != None:
        a1 += str(p1.data)
        p1 = p1.next
    a2 = ""
    while p2 != None:
        a2 += str(p2.data)
        p2 = p2.next
    res = str(int(a1[::-1]) + int(a2[::-1]))[::-1]
    head = LNode()
    head.data = -1
    p = head
    for i in res:
        p.next = LNode()
        p.next.data = int(i)
        p = p.next
    p.next = None
    return head
    
####################方法2：直接相加###############################
def addLink(head1, head2):
    # 判断链表是否为空
    if head1 is None or head1.next is None:
        return head2
    if head2 is None or head2.next is None:
        return head1
    c = 0 # 用来记录进位
    sums=0 # 用来记录两个结点相加的值
    p1 = head1.next # 用来遍历h1
    p2 = head2.next # 用来遍历h2
    resultHead = LNode()
    p = resultHead
    # 两链表进行相加
    while p1 is not None and p2 is not None:
        tmp = LNode()
        sums = p1.data + p2.data + c
        tmp.data = sums % 10 # 两结点相加的和
        c = sums // 10 # 进位
        p.next = tmp
        p = tmp
        p1 = p1.next
        p2 = p2.next
    if p1 is None:
        while p2 is not None:
            tmp = LNode()
            sums = p2.data + c
            tmp.data = sums % 10
            c = sums // 10
            p.next = tmp
            p = tmp
            p2 = p2.next
    if p2 is None:
        while p1 is not None:
            tmp = LNode()
            sums = p1.data + c
            tmp.data = sums % 10
            c = sums // 10 # 取整
            p.next = tmp
            p = tmp
            p1 = p1.next
    # 如果计算完成后还有进位，则增加新的结点
    if c==1:
        tmp = LNode
        tmp.data = c
        p.next = tmp
    return resultHead
 
if __name__=="__main__":
    i = 1
    head1 = LNode()
    head2 = LNode()
    cur = head1
    # 构造第一个链表
    while i < 9:
        tmp = LNode()
        tmp.data = i+1
        cur.next = tmp
        cur = tmp
        i += 1
    # 构造第二个链表
    cur = head2
    i = 9
    while i>2:
        tmp = LNode()
        tmp.data = i
        cur.next = tmp
        cur = tmp
        i -= 1
    print("\nHead1:")
    cur = head1.next
    while cur is not None:
        print(cur.data)
        cur = cur.next
    print("\nHead2:")
    cur = head2.next
    while cur is not None:
        print(cur.data)
        cur = cur.next
    # 相加后
    print("\n相加后：")
    cur = add(head1, head2)
    cur = cur.next
    while cur is not None:
        print(cur.data)
        cur = cur.next
## 可以先问面试官两个链表是否等长，若是等长：可以写以下代码
```
def add(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head2
    if head1.data + head2.data < 10:
        head3 = LNode(head1.data + head2.data)
        head3.next = add(head1.next, head2.next)
    else:
        tmp = LNode(1)
        head3 = LNode(head1.data + head2.data - 10)
        head3.next = add(head1.next, add(head2.next, tmp))
    return head3
```
