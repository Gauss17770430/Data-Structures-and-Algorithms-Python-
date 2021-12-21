from Stack import Stack

def divideBy2(decNumber):
    s = Stack()
    while decNumber != 0:
        s.push(decNumber % 2)
        decNumber //= 2
    r = []
    for i in range(s.size()):
        r.append(str(s.pop()))
    return ''.join(r)


if __name__ == '__main__':
    print(divideBy2(42))