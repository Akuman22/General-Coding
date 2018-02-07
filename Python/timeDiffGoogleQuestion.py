def timeDiff(start, end):
    S = (int(start[2])*10)+int(start[3])+\
        (int(start[0])*10+int(start[1]))*60
    E = (int(end[2])*10)+int(end[3])+\
        (int(end[0])*10+int(end[1]))*60
    timeD = E - S
    return timeD if timeD<=0 else timeD+1440

def perm(string):
    if (len(string) <= 1):
        return string
    listOfPerms = []
    for i in range(len(string)):
        PermRet = perm(string[:i] + string[i+1:])
        try:
            listOfPerms.append([string[i] + _ for _ in sum(PermRet, [])])
        except:
            listOfPerms.append([string[i] + _ for _ in PermRet])
    return sum(listOfPerms, [])

def solution(S):
    time = S[0]+S[1]+S[3]+S[4]
    listOfTimes = perm(time)
    minDiff = 2000
    minTime = time
    for i in listOfTimes:
        if((int(i[0])*10 + int(i[1]))<24)and((int(i[2])*10 + int(i[3]))<60):
            if timeDiff(time, i) < minDiff:
                minDiff = timeDiff(time, i)
                minTime = i
    return minTime
    
print(solution("11:00"))
