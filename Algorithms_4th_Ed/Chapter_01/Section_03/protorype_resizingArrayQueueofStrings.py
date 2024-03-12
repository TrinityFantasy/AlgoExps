# Algorithms, 4th Edition, Ch.1, Sec.3, Exe.1.3.14


class resizingArrayQueueofStrings:
    def __init__(self):
        self.__sque = []
        self.__first = 0
        self.__last = 0
        self.__size = 0

    def _isEmpty(self):
        return self.__size == 0

    def _size(self):
        return self.__size

    def _queInit(self, size):
        self.__sque = [None] * size
        print(f"The queue size is seted to: {len(self.__sque)}\n")

    def _enqueue(self, e):
        if self.__last == len(self.__sque):
            self.__last = 0
        self.__sque[self.__last] = e
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
    sq = resizingArrayQueueofStrings()
    sq._queInit(3)

    sq._enqueue("1")
    sq._enqueue("2")
    sq._enqueue("3")

    print(f"Dequeue 1: {sq._dequeue()}\n")
    print("Expected: 1\n")

    sq._enqueue("4")
    print(f"Dequeue 2: {sq._dequeue()}\n")
    print("Expected: 2")
