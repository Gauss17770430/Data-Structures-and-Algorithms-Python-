from Stack import Stack

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()
    for c in tokenList:
        if c in '0123456789':
            operandStack.push(int(c))
        else:
            right = operandStack.pop()
            left = operandStack.pop()
            result = operation(c, right, left)
            operandStack.push(result)
    return operandStack.pop()


def operation(op, op_r, op_l):
    if op == '+':
        return op_r + op_l
    elif op == '-':
        return op_r - op_l
    elif op == '*':
        return op_r * op_l
    elif op == '/':
        return op_r / op_l

if __name__ == '__main__':
    print(postfixEval('4 5 6 * +'))