from Stack import Stack

def baseConverter(decNumber, base):
    digits = '0123456789ABCDEF'
    s = Stack()
    while decNumber != 0:
        s.push(decNumber % base)
        decNumber //= base
    r = []
    for i in range(s.size()):
        r.append(digits[s.pop()])
    return ''.join(r)


if __name__ == '__main__':
    print(baseConverter(25, 2))
    print(baseConverter(25, 16))