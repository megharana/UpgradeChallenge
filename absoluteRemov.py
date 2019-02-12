import time
resList = []


def calAbs(listToCalAbs):
    """
    func description: calculates  absolute difference of list passed as argument
    Return type: Integer
    param name1: 'listToCalAbs'  --> target list for which we need to calculate sum of absolute difference
    type name1: list
    """
    resultant = 0
    for x in range(len(listToCalAbs) - 1):
        resultant += abs(listToCalAbs[x] - listToCalAbs[x + 1])
    return resultant


def solve(A, N):
    """
    func description: to calculate minimum absolute 

    param name1: 'A'  --> calculates the minimum among the sums of absolute difference
    type name1: list

    param name2: 'N'  --> length of input string
    type name1: integer
    """
    for x in range(N):
        if (x == 0):
            resList.append(calAbs(A[1:N]))
        elif (x == N - 1):
            resList.append(calAbs(A[0:N - 1]))
        else:
            resList.append(calAbs(A[:x] + A[x + 1:]))
    end = time.time()
    print(min(resList))
    print(end - start)  #to calculate execution time


start = time.time()
T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(x) for x in input().split(" ")]
    solve(A, N)
