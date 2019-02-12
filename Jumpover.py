from operator import add
from itertools import accumulate
from operator import add


def cum_sum(l):
    """
    func description: cumulative sum
    Return value description : list

    param list: 'l'  --> list to get cumulative sum 
    type list: list
    """
    return accumulate(l, add)


T = int(input())
for x in range(T):
    N = int(input())
    val = [int(x) for x in input().split(" ")]
    h = [int(x) for x in input().split(" ")]
    M = int(input())
    I = [int(x) for x in input().split(" ")]
    min_I = [int(x) for x in input().split(" ")]

    height = 0
    total = 0
    heightList = list(cum_sum(h))

    for x in range(N):
        if x in I:
            if (heightList[x] < min_I[I.index(x)]):
                total = -1
                break
            else:
                if height < min_I[I.index(x)]:
                    height = heightList[x]
                else:
                    total += val[x]
        else:
            if (x + 1) in I:
                if height < min_I[I.index(x + 1)]:
                    if heightList[x] >= min_I[I.index(x + 1)]:  # need to chcek
                        height = heightList[x]
                    else:
                        total = -1
                        break

                else:
                    total += val[x]
            else:
                total += val[x]

    print(total)
