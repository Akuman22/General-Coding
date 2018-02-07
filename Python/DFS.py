def DFS(grid, pos, value, loc):
    if(pos[0]+1<len(grid)):
        if(grid[pos[0]+1][pos[1]] == value) and [pos[0]+1, pos[1]] not in loc:
            loc.append([pos[0]+1, pos[1]])
            loc = DFS(grid, [pos[0]+1, pos[1]], value, loc)
    if(pos[1]+1<len(grid[0])):
        if(grid[pos[0]][pos[1]+1] == value) and [pos[0], pos[1]+1] not in loc:
            loc.append([pos[0], pos[1]+1])
            loc = DFS(grid, [pos[0], pos[1]+1], value, loc)
    if(pos[0]>0):
        if(grid[pos[0]-1][pos[1]] == value) and [pos[0]-1, pos[1]] not in loc:
            loc.append([pos[0]-1, pos[1]])
            loc = DFS(grid, [pos[0]-1, pos[1]], value, loc)
    if(pos[1]>0):
        if(grid[pos[0]][pos[1]-1] == value) and [pos[0], pos[1]-1] not in loc:
            loc.append([pos[0], pos[1]-1])
            loc = DFS(grid, [pos[0], pos[1]-1], value, loc)
    return loc

def findItem(grid, item):
    i = 0
    index = -1
    while(i<len(grid) and index == -1):
        try:
            index = grid[i].index(item)
        except:
            pass
        i+=1
    return DFS(grid, [i-1,index], item, [[i-1,index]]) if index != -1 else -1
    
        
grid = [[0,0,0,0,1,0,0,0,0,0,2],
        [0,0,0,0,1,0,0,0,0,2,2],
        [0,0,0,0,1,1,0,0,0,2,2],
        [0,0,3,0,1,0,0,0,0,0,0]]

a = findItem(grid, 1)
print a