# Algorithms, 4th Edition, Ch.1, Sec.3, Exe.1.3.30


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def reverseIter(n):
    if not n:
        return None
    elif not n.next:
        return n

    tail = n
    tmp = None
    while tail:
        head = tail.next
        tail.next = tmp
        tmp = tail
        tail = head

    return tmp


def reverseRecur(n):
    if not n:
        return None
    elif not n.next:
        return n

    head = n.next
    tmp = reverseRecur(head)
    head.next = n
    n.next = None

    return tmp


if __name__ == "__main__":
    a1 = Node(0)
    a2 = Node(1)
    a3 = Node(2)
    a4 = Node(3)
    a5 = Node(4)
    a6 = Node(5)

    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a6

    b1 = Node(0)
    b2 = Node(1)
    b3 = Node(2)
    b4 = Node(3)
    b5 = Node(4)
    b6 = Node(5)

    b1.next = b2
    b2.next = b3
    b3.next = b4
    b4.next = b5
    b5.next = b6

    test1 = a1
    test2 = b1

    print(f"Original list: ", end="")
    while a1:
        print(f"{a1.val}, ", end="")
        a1 = a1.next

    res1 = reverseIter(test1)
    res2 = reverseRecur(test2)

    print(f"\n\nReverse by iteration: ", end="")
    while res1:
        print(f"{res1.val}, ", end="")
        res1 = res1.next
    print(f"\n\nReverse by recursive: ", end="")
    while res2:
        print(f"{res2.val}, ", end="")
        res2 = res2.next
    print(f"\n\nExpected: 5, 4, 3, 2, 1, 0, \n")
