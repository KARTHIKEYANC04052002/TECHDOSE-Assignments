class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        index, res = 0, 0
        s += '+'
        length = len(s)
        op = '+'
        while index < length:
            if s[index] == ' ':
                pass
            elif s[index].isdigit():
                res = res * 10 + int(s[index])
            else:
                if op == '+':
                    stack.append(res)
                elif op == '-':
                    stack.append(-res)
                elif op == '*':
                    stack.append(stack.pop() * res)
                elif op == '/':
                    stack.append(int(stack.pop() / res))
                res = 0
                op = s[index]
            index += 1
        return sum(stack)