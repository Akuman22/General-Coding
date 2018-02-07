def BinSearch(array, obj):
    l = len(array)
    if  l <= 1:
        return int(obj == array[0])
    if(obj>array[l/2]):
        return BinSearch(array[l/2:], obj)
    if(obj<array[l/2]):
        return BinSearch(array[:l/2], obj)
    if(obj == array[l/2]):
        return 1
    
a = [1,2,3,4,5,6,7,8]
print(BinSearch(a, 3))