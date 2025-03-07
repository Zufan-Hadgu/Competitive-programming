# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = deque()
        self.value = value
        self.k = k
        self.same = 0

        

    def consec(self, num: int) -> bool:
        if len(self.stream) >= self.k:
            val = self.stream.popleft()
            if val == self.value:
                self.same -= 1
        self.stream.append(num)
        if num == self.value:
            self.same += 1
        return self.same == self.k

      
        

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)