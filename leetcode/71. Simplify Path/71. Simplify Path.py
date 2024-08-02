class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        path=path.split("/")
        for i in path:
            match i:
                case "..":
                    if stack:
                        stack.pop()
                case ".":
                        continue
                case _:
                    if i:
                        stack.append(i)
        return "/"+"/".join(stack)

