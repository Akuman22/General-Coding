def Solution(P, K):
    flowerBloom = [0]*len(P)
    lastDay = calcLastDay(flowerBloom, P, 1, -1, K)
    return lastDay

def calcLastDay(flowerBloom, P, day, lastDay, K):
    if day <= len(P):
        flowerBloom[P[day - 1] - 1] = 1
        for i in range(day):
            if(groupLen(flowerBloom, P[i] - 1, 1, 0) == K):
                lastDay = day
        lastDay = calcLastDay(flowerBloom, P, day + 1, lastDay, K)
    return lastDay

def groupLen(flowerBloom, num, size, direc):
    if(num < len(flowerBloom)-1):
        if(flowerBloom[num + 1] == 1) and direc != 1:
            size += groupLen(flowerBloom, num + 1, 0, 2) + 1
    if(num > 0):
        if(flowerBloom[num - 1] == 1) and direc != 2:
            size += groupLen(flowerBloom, num - 1, 0, 1) + 1
    return size            
    
    
P = [3,1,5,2,4]
K = 1
print Solution(P, K)