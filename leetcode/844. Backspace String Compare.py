class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        print(self.stack(s))
        print(self.stack(t))
        return True if self.stack(s)==self.stack(t) else False

    def stack(self,x:str)->str:
        stk=[]
        for i in x:
            if i=="#":
                if stk:
                    stk.pop()
            else:
                stk.append(i)
        return "".join(stk)
