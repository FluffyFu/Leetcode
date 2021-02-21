class MyCircularQueue:

    def __init__(self, k: int):
        self.nums = [0] * k

        # current front and rear index
        self.front = 0
        self.rear = -1
        self.cnt = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.rear = (self.rear + 1) % self.k
            self.nums[self.rear] = value
            self.cnt += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k
        self.cnt -= 1
        return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.nums[self.front]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.nums[self.rear]
        return -1

    def isEmpty(self) -> bool:
        return self.cnt == 0

    def isFull(self) -> bool:
        return self.cnt == self.k
