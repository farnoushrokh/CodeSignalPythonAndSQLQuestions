#First Soluiton

def solution(n):
    if n == int(n) :
        return n % 2
    else:
        return -1

#second Soluiton

def solution1(n):
    if isinstance(n, int) :
        return n % 2
    else:
        return -1
#third Solution

def solution2(n):
    if n%1==0 :
        return n % 2
    else:
        return -1