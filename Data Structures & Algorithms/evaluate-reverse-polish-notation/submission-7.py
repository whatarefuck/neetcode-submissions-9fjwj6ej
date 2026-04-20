from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokens = deque(tokens)
        dq = deque()
        while tokens:
            token = tokens.popleft()

            match token:
                case "+":
                    dq.append(dq.pop() + dq.pop())
                case "-":
                    b, a = dq.pop(), dq.pop()
                    dq.append(a - b)
                case "/":
                    b, a = dq.pop(), dq.pop()
                    dq.append(int(a / b))
                case "*":
                    dq.append(dq.pop() * dq.pop())
                case _:
                    dq.append(int(token))

        return dq.pop()