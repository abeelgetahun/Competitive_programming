class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators={"+","-","*","/"}
        for i in tokens:
            if i not in operators:
                stack.append(i)
            else:
                x=stack.pop()
                y=stack.pop()
                stack.append(str(int(eval(y+i+x))))
        return int(stack[0])
