def anagramSolution1(s1, s2):
    alist = list(s2)
    pos1 = 0
    stillOK = True
    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
                alist[pos2] = 'None'
            else:
                pos2 += 1
        
        if not found:
            stillOK = False

        pos1 += 1
    
    return stillOK


if __name__ == '__main__':
    print(anagramSolution1('abcd', 'dcba'))