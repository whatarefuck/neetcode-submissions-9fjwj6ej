class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        brackets_stack = []
        for i in s:
            if i in brackets.values():
                brackets_stack.append(i)
            else:
                if not brackets_stack:
                    return False
                if brackets[i] != brackets_stack[-1]:
                    return False
                brackets_stack.pop()

        return not brackets_stack