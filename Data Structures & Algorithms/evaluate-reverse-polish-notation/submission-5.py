class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        numbers = []

        ops = ["+", "-", "/", "*"]

        for val in tokens:
            if val in ops:
                val2 = stack.pop()
                val1 = stack.pop()

                if val == ops[0]:
                    stack.append(val2+val1)
                elif val == ops[1]:
                    stack.append(val1-val2)
                elif val == ops[2]:
                    stack.append(int(val1/val2))
                else:
                    stack.append(val1*val2)
            else:
                stack.append(int(val))
        return stack.pop()




        