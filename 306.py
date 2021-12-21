from Stack import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    prec[')'] = 1
    
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for c in tokenList:
        if c in '0123456789':
            postfixList.append(c)
        elif c == '(':
            opStack.push(c)
        elif c == ')':
            pop = opStack.pop()
            while pop != '(':
                postfixList.append(pop)
                pop = opStack.pop()
        elif c in '+-*/':
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[c]:
                postfixList.append(opStack.pop())
            opStack.push(c)
    
    for i in range(opStack.size()):
        postfixList.append(opStack.pop())

    return ' '.join(postfixList)


if __name__ == '__main__':
    print(infixToPostfix('( 1 + 2 ) * 3'))