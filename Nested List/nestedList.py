#"""Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line."""
#input
#The first line contains an integer, , the number of students. The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.
#output
#Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

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
