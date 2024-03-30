class Solution:
    def interpret(self, command: str) -> str:
        goal=""
        temp=""
        for i in command:
            temp+=i
            if temp=="G":
                goal+="G"
                temp=""
            elif temp=="()":
                goal+="o"
                temp=""
            elif temp=="(al)":
                goal+="al"
                temp=""
        return goal
        