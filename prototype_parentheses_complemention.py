# Algorithms, 4th Edition, Ch.1, Sec.3, Exe.1.3.09


def parenthesesComp(str):
    opds = []
    ops = []

    for e in str:
        if e in "+-*/":
            ops.append(e)
        elif e == ")":
            op = ops.pop()
            opd2 = opds.pop()
            opd1 = opds.pop()
            substr = "(" + opd1 + op + opd2 + ")"
            opds.append(substr)
        else:
            opds.append(e)

    return opds.pop()


if __name__ == "__main__":
    str1 = "1+2)*3-4)*5-6)))"

    str1c = parenthesesComp(str1)

    print(f"str1 = {str1}\n")
    print(f"str1c = {str1c}\n")
