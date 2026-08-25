class Solution:
    def isValid(self, s: str) -> bool:
        storage = []

        if len(s) == 0: return True

        if len(s) == 1: return False

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                storage += s[i]
            else:
                if not storage:
                    return False
                if s[i] == ")":
                    if storage.pop() == "(":
                        continue
                    else:
                        return False
                elif s[i] == "]":
                    if storage.pop() == "[":
                        continue
                    else:
                        return False
                elif s[i] == "}":
                    if storage.pop() == "{":
                        continue
                    else:
                        return False
                else:
                    return False
        if storage:
                return False
        return True
            