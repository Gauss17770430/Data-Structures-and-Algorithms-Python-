def anagramSolution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)
    alist1.sort()
    alist2.sort()

    if alist1 == alist2:
        return True
    else:
        return False


if __name__ == '__main__':
    print(anagramSolution2('abcd', 'dcba'))