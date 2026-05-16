class MyHashSet:

    def __init__(self):
        self.size = 2000
        self.ls = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        index = key%self.size
        if key not in self.ls[index]:
            self.ls[index].append(key)

    def remove(self, key: int) -> None:
        index = key%self.size
        if key in self.ls[index]:
            self.ls[index].remove(key)
        

    def contains(self, key: int) -> bool:
        index = key%self.size
        return key in self.ls[index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)