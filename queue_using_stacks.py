#A queue can be implemented by using a minimum of two stacks
class MyQueue:

    def __init__(self):
        self.stack_one = []
        self.stack_two = []
        

    def push(self, x: int) -> None:
        self.stack_one.append(x)

    def pop(self) -> int:
        if not self.stack_one:
            raise Exception("Attempting to remove from an empty list")
        while self.stack_one:
            self.stack_two.append(self.stack_one.pop())
        
        val = self.stack_two.pop()
        while self.stack_two:
            self.stack_one.append(self.stack_two.pop())
        return val
        
    def peek(self) -> int:
        if not self.stack_one:
            raise Exception("Attempting to remove from an empty list")
        while self.stack_one:
            self.stack_two.append(self.stack_one.pop())
        
        val = self.stack_two.pop()
        self.stack_one.append(val)
        while self.stack_two:
            self.stack_one.append(self.stack_two.pop())
        return val

    def empty(self) -> bool:
        return not self.stack_one
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()