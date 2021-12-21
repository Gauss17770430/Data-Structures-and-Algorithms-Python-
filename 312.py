from Deque import Deque

def palchecher(aString):
    chardeque = Deque()
    for ch in aString:
        chardeque.addRear(ch)
    stillEqual = True
    while chardeque.size() > 1 and stillEqual:
        front = chardeque.removeFront()
        rear = chardeque.removeRear()
        if front != rear:
            stillEqual = False
    return stillEqual

if __name__ == '__main__':
    print(palchecher('lsdkjfskf'))
    print(palchecher('radar'))