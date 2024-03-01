import time as t


def intExam(a):
    tmp = str(a)
    l = len(tmp)

    if l & (l - 1) == 0:
        return True, l
    else:
        return False, l


def intSplit(a, l):
    tmp = str(a)
    ltmp = l // 2

    front = ""
    behind = ""
    for i in range(ltmp):
        front += tmp[i]
        behind += tmp[i + ltmp]
    m = ltmp * 2
    for i in range(m, l):
        behind += tmp[i]

    return int(front), int(behind), ltmp


def recIntMult(a, b, l):
    if l == 1:
        return a * b

    a_f, a_b, ltmpf = intSplit(a, l)
    b_f, b_b, ltmpf = intSplit(b, l)

    ac = recIntMult(a_f, b_f, ltmpf)
    ad = recIntMult(a_f, b_b, ltmpf)
    bc = recIntMult(a_b, b_f, ltmpf)
    bd = recIntMult(a_b, b_b, ltmpf)

    return 10**l * ac + 10 ** (l // 2) * (ad + bc) + bd


# The provided version of karatsuba test is only available when l = 2^n && len(p) == len(q) == l!
def karatsuba(a, b, l):
    if l == 1:
        return a * b

    a_f, a_b, ltmpf = intSplit(a, l)
    b_f, b_b, ltmpf = intSplit(b, l)

    p = a_f + a_b
    q = b_f + b_b
    ac = karatsuba(a_f, b_f, ltmpf)
    bd = karatsuba(a_b, b_b, ltmpf)
    pq = karatsuba(p, q, ltmpf)
    adbc = pq - ac - bd

    return 10**l * ac + 10 ** (l // 2) * adbc + bd


if __name__ == "__main__":
    # assume the length of a and b are the same, except the karatsuba algorithm
    a = 1024
    b = 1024

    flag1, la = intExam(a)
    flag2, lb = intExam(b)
    if not flag1 or not flag2:
        print("The length of each input integer must be the power of 2!")
        exit()

    s = t.time()
    res = a * b
    e = t.time()
    cost = e - s
    print(f"Result of normal way is: {res}, time cost is {cost} Sec.\n")

    s = t.time()
    res = recIntMult(a, b, la)
    e = t.time()
    cost = e - s
    print(f"Result of recIntMult is: {res}, time cost is {cost} Sec.\n")

    s = t.time()
    res = karatsuba(a, b, la)
    e = t.time()
    cost = e - s
    print(f"Result of karatsuba is: {res}, time cost is {cost} Sec.\n")
