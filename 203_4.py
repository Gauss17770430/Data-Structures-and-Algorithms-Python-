def anagramSolution4(s1, s2):
    list1 = [0] * 26
    list2 = [0] * 26
    for i in range(len(s1)):
        list1[ord(s1[i]) - ord('a')] += 1
    for i in range(len(s2)):
        list2[ord(s2[i]) - ord('a')] += 1

    if list1 == list2:
        return True
    else:
        return False


if __name__ == '__main__':
    print(anagramSolution4('abcd', 'dcba'))