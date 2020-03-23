import math


def find_number(i, j):
    if max(i, j) < 2:
        if 1 <= i <= j or i <= j < 1:
            return 0
        else:
            return 1
    now = 2**(math.floor(math.log2(max(i, j))))
    if i < now and j < now:
        return find_number(i, j)
    elif now <= i and now <= j:
        return find_number(i - now, j - now)
    elif i < now <= j:
        return find_number(i, j - now) + now
    else:
        return find_number(i - now, j) + now


def main():
    k = int(input())
    for i in range(k):
        i, j = [int(x) for x in input().split()]
        print(find_number(i, j))


if __name__ == '__main__':
    main()
