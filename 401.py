def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])


if __name__ == '__main__':
    print(listsum([1, 3, 5, 7, 9]))