# Algorithms, 4th Edition, Ch.1, Sec.3, Exe.1.3.10


def top(arr):
    l = len(arr)
    if l == 1:
        return arr[0]
    else:
        return arr[l - 1]


def infixToPostfix(str):
    opds = []
    ops = []

    for s in str:
        if s == "(":
            continue
        elif s in "+-" and not ops:
            ops.append(s)
        elif s in "+-" and top(ops) in "+-":
            ops.append(s)
        elif s in "*/":
            ops.append(s)
        elif s in "+-" and top(ops) in "*/":
            sub = ""
            while opds:
                sub = sub + opds.pop()
            sub = sub[::-1]
            sub2 = ""
            while ops:
                sub2 = sub2 + ops.pop()
            sub = sub + sub2
            opds.append(sub)
            ops.append(s)
        elif s == ")":
            v2 = opds.pop()
            v1 = opds.pop()
            op = ops.pop()
            sub = ""
            sub = sub + v1 + v2 + op
            opds.append(sub)
        else:
            opds.append(s)

    if ops:
        v2 = opds.pop()
        v1 = opds.pop()
        sub = ""
        sub = sub + v1 + v2 + ops.pop()
        opds.append(sub)
    res = ""
    while opds:
        res = res + opds.pop()

    return res


if __name__ == "__main__":
    str1 = "A+B*C+D"
    str2 = "((1+2)*(4/2))"

    res1 = infixToPostfix(str1)
    print(f"The processed A+B*C+D is:\n{res1}\n")
    res2 = infixToPostfix(str2)
    print(f"The processed ((1+2)*(4/2)) is:\n{res2}\n")
  
