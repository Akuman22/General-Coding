''' Question 1: Given a string A consisting of n characters 
and a string B consisting of m characters, write a function 
that will return the number of times A must be stated such that 
B is a substring of the repeated A. If B can never be a 
substring, return -1.

Example:
A = ‘abcd’
B = ‘cdabcdab’
The function should return 3 because after stating A 3 times, 
getting ‘abcdabcdabcd’, B is now a substring of A.

You can assume that n and m are integers in the range [1, 1000].
''' 

def solution(A, B):
    temp = A
    count = 0
    while len(temp)<(len(B)+2*len(A)):
        if temp.find(B) != -1:
            return count
        temp = temp + A
        count += 1
    return -1

A = 'abcd'
B = 'cdabcdab'
print solution(A,B)