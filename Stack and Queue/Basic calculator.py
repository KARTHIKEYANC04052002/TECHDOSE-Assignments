class Solution:
    def calculate(self, s: str) -> int:
        operator = ''
        stack = [0]
        index = 0
        length = len(s)
        while index < length:
            if s[index] == ' ':
                pass
            elif s[index] in ['+', '-']:
                operator = s[index]
            elif s[index] == '(':
                stack += [operator]
                stack += [0]
                operator = '+'
            elif s[index] == ')':
                value = stack.pop()
                operator = stack.pop()
                if operator == '-':
                    stack[-1] -= value
                else:
                    stack[-1] += value
            else:
                num = 0
                while index < length and s[index].isnumeric():
                    num = num * 10 + int(s[index])
                    index += 1
                index -= 1
                if operator == '-':
                    stack[-1] -= num
                else:
                    stack[-1] += num
            index += 1
        return stack[0]