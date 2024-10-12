class MyHashSet:

    def __init__(self):
        self.myset = set()
        

    def add(self, key: int) -> None:
        self.myset.add(key)

        
    def remove(self, key: int) -> None:
        if key in self.myset:
            self.myset.remove(key)
        
    def contains(self, key: int) -> bool:
        return key in self.myset

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)