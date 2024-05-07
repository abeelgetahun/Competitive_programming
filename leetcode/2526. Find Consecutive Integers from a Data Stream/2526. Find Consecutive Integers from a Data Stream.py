class DataStream:

    def __init__(self, value: int, k: int):
        self.value=value
        self.k=k
        self.count=0

    def consec(self, num: int) -> bool:
    
        self.count=self.count+1 if num==self.value else 0
        print(self.count,num)
        if self.count==self.k:
            self.count-=1
            return True
        return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
