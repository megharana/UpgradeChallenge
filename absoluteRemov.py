resList = []


def solve(A, N):
    absList = []
    absDict = {}
    for x in range(len(A) - 1):
        absList.append(abs(A[x] - A[x + 1]))
        absDict.update({abs(A[x] - A[x + 1]): max(A[x], A[x + 1])})

    del absDict[max(absDict.keys(), key=(lambda k: absDict[k]))]

    # return absDict
    resList.append(sum(absDict.keys()))


T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(x) for x in input().split(" ")]
    solve(A, N)
    # resList.append((sum(out_.keys()))
    # print((sum(out_.keys()))

for x in resList:
    print(x)
