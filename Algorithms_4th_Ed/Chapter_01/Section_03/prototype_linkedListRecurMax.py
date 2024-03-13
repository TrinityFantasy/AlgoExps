# Algorithms, 4th Edition, Ch.1, Sec.3, Exe.1.3.28


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def findMax(n):
    if not n:
        return -1
    elif not n.next:
        return n.val

    def find(a, b):
        maxi = max(a, b.val)
        if not b.next:
            return maxi
        return find(maxi, b.next)

    maxi = find(-1, n)

    return maxi


if __name__ == "__main__":
    e1 = Node(1)
    e2 = Node(2)
    e3 = Node(9)
    e4 = Node(3)
    e5 = Node(8)
    e6 = Node(7)
    e7 = Node(2)
    e8 = Node(8)

    e1.next = e2
    e2.next = e3
    e3.next = e4
    e4.next = e5
    e5.next = e6
    e6.next = e7
    e7.next = e8

    res = findMax(e1)
    print(f"The max value is: {res}\n")
    print(f"Expected: 9\n")
