class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        operator ="*/+-"
        for t in tokens:
            if t in operator:
                op1=stack.pop()
                op2=stack.pop()
                if t=='+':
                    stack.append(op2+op1)
                elif t=='-':
                    stack.append(op2-op1)
                elif t=='*':
                    stack.append(op2*op1)
                else:
                    stack.append(int(op2/op1))
            else:
                stack.append(int(t))
        return stack.pop()