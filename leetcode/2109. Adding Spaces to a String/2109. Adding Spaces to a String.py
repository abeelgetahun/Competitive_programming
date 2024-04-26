class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = []
        last_index = 0
        for index in spaces:
            output.append(s[last_index:index])
            output.append(" ")
            last_index = index 
        output.append(s[last_index:])
        return "".join(output) 
