class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        dot=0
        one_path=""
        for i in path+"/":
            if i=="/":
                if one_path=="..":
                    if stack:
                        stack.pop()
                elif one_path!="." and one_path!="":
                    stack.append(one_path)
                one_path=""
            else:
                one_path+=i
        return "/"+"/".join(stack)
