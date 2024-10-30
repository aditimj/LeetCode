class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = []
        for i in range(len(names)):
            people.append((heights[i], names[i]))
        sorted_people = sorted(people, key=lambda item: item[0], reverse=True)        
        res = []
        for height, name in sorted_people:
            res.append(name)        
        return res

