if __name__ == '__main__':
    mark = []
    scoreList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mark.append([name,score])
        scoreList.append(score)
    mark.sort(key = lambda x :x[1])
    scoreList.sort()
    temp = scoreList[0]
    for i in scoreList:
        if i > temp:
            temp = i
            break;          
    nameList = []
    for i,j in mark:
        if j == temp:
            nameList.append(i)
    nameList.sort()
    for i in nameList:
        print(i)
