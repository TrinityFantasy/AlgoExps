# Algorithms, 4th Edition, Ch.1, Sec.3, Exe.1.3.15


class getQueElementatIndex:
    def __init__(self):
        self.__sque = []
        self.__first = -1
        self.__last = -1
        self.__size = 0

    def _isEmpty(self):
        return self.__size == 0

    def _size(self):
        return self.__size

    def _queInit(self, sarr):
        for e in sarr:
            self._enqueue(e)

    def _getValatIndex(self, k):
        return self.__sque[k]

    def _enqueue(self, e):
        if not self.__sque:
            self.__first += 1
        self.__sque.append(e)
        self.__last += 1
        self.__size += 1

    def _dequeue(self):
        if not self.__sque:
            print(f"The queue is empty!\n")
            return []
        if self.__first == len(self.__sque):
            self.__first = 0
        tmp = self.__sque[self.__first]
        self.__sque[self.__first] = None
        self.__first += 1
        self.__size -= 1
        return tmp


if __name__ == "__main__":
    arr = "Test Content!"
    sq = getQueElementatIndex()
    sq._queInit(arr)
    res = sq._getValatIndex(5)

    print(f"Get index at 5 is: {res}\n")
    print("Expected: C\n")
