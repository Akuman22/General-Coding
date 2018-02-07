'''
Given an array of N integers, can you find the sum of its elements?

Input Format

The first line contains an integer,N , denoting the size of the array. 
The second line contains N space-separated integers representing the array's elements.

Output Format

Print the sum of the array's elements as a single integer.

Sample Input

6
1 2 3 4 10 11
Sample Output

31
Explanation

We print the sum of the array's elements, which is: 1 + 2 + 3 + 4 + 10 + 11.
'''
#!/bin/python

import sys

def sum(ar, pos, n):
     return ar[pos] + sum(ar, pos+1, n) if pos < n else 0
    
def simpleArraySum(n, ar):
    return sum(ar, 0, n)

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)
