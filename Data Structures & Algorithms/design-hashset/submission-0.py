class MyHashSet:

    def __init__(self):
        self.size = 5000
        self.emptyTable = [[] for _ in range(self.size)]
        

    def add(self, key: int) -> None:
        index = key % self.size
        if key not in self.emptyTable[index]:
            self.emptyTable[index].append(key)
        

    def remove(self, key: int) -> None:
        index = key % self.size
        if key in self.emptyTable[index]:
            self.emptyTable[index].remove(key)

    def contains(self, key: int) -> bool:
        index = key % self.size
       
        return key in self.emptyTable[index]


        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)