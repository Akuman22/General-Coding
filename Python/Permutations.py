def perm(string):
    if (len(string) <= 1):
        return string
    listOfPerms = []
    temp = []
    for i in range(len(string)):
        PermRet = perm(string[:i] + string[i+1:])
        try:
            temp = [string[i] + _ for _ in sum(PermRet, [])]
        except:
            temp = [string[i] + _ for _ in PermRet]
        listOfPerms.append(temp)
    return sum(listOfPerms, [])

a = perm("abcd")
print a