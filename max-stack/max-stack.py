class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxheap = []
        self.obselete = set()
        self.idx = 0
        
    def push(self, x: int) -> None: # O(lgn)
        self.stack.append((x, self.idx))
        heapq.heappush(self.maxheap, (-x, -self.idx))
        self.idx += 1

    def pop(self) -> int: # O(1)
        while self.stack and self.stack[-1][1] in self.obselete:
            self.stack.pop()
        num, index = self.stack.pop()
        self.obselete.add(index)
        return num

    def top(self) -> int: # O(1)
        while self.stack and self.stack[-1][1] in self.obselete:
            self.stack.pop()
        return self.stack[-1][0]

    def peekMax(self) -> int: # O(lgn)
        while self.maxheap and -self.maxheap[0][1] in self.obselete:
            heapq.heappop(self.maxheap)
        return -self.maxheap[0][0]
        

    def popMax(self) -> int: # O(lgn)
        while self.maxheap and -self.maxheap[0][1] in self.obselete:
            heapq.heappop(self.maxheap)
        val, index = heapq.heappop(self.maxheap)
        self.obselete.add(-index)
            
        return -val  