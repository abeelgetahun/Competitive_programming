class Solution:
    def isValid(self, s: str) -> bool:
        p=set("({[")
        stack=[]
        for i in s:
            if i in p:
                stack.append(i)
            elif stack and i==")" and "(" == stack[-1]:
                stack.pop()
            elif stack and i=="}" and "{" ==stack[-1]:
                stack.pop()
            elif stack and i==("]") and "[" ==stack[-1]:
                stack.pop()
            else:
                return False   
        return len(stack) == 0
