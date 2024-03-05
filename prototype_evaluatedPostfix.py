def evaluatePostfix(sin):
    opds = []

    for e in sin:
        if e == "+":
            v2 = int(opds.pop())
            v1 = int(opds.pop())
            opds.append(v1 + v2)
        elif e == "-":
            v2 = int(opds.pop())
            v1 = int(opds.pop())
            opds.append(v1 - v2)
        elif e == "*":
            v2 = int(opds.pop())
            v1 = int(opds.pop())
            opds.append(v1 * v2)
        elif e == "/":
            v2 = int(opds.pop())
            v1 = int(opds.pop())
            opds.append(v1 / v2)
        else:
            opds.append(e)

    return opds.pop()


if __name__ == "__main__":
    str1 = "123*+4+"
    str2 = "12+42/*"

    res1 = evaluatePostfix(str1)
    res2 = evaluatePostfix(str2)

    print(f"The 123*+4+ is evaluated {res1 == (1+2*3+4)}, which is {res1}\n")
    print(f"The 12+42/* is evaluated {res2 == ((1+2)*(4/2))}, which is {res2}\n")
