class MyHashMap:

    def __init__(self):
        self.MyHashMap = {}
        

    def put(self, key: int, value: int) -> None:
        self.MyHashMap[key] = value

        

    def get(self, key: int) -> int:
        return self.MyHashMap.get(key,-1)
        

    def remove(self, key: int) -> None:
        self.MyHashMap.pop(key,None)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)