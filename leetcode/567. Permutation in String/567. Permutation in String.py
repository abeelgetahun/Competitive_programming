class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        container1=Counter(s1)
        for i in range(0,len(s2)-len(s1)+1):
            container2=Counter(s2[i:len(s1)+i])
            if container1==container2:
                return True
        return False
