from Stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not match(top, symbol):
                    balanced = False
        index += 1
    
    if balanced and s.isEmpty():
        return True
    else:
        return False

def match(s1, s2):
    l1 = '([{'
    l2 = ')]}'
    return l1.index(s1) == l2.index(s2)

if __name__ == '__main__':
    print(parChecker('((()))'))