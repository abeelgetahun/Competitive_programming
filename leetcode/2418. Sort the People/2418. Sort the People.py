class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people=[]
        sorted_=sorted(copy.deepcopy(heights),reverse=True)
        for i in sorted_:
            x=heights.index(i)
            people.append(names[x])
        return people
        
        
