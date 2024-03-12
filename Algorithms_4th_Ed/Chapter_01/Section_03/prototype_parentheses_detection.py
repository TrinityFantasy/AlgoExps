# Algorithms, 4th Edition, Ch.1, Sec.3, Exe.1.3.04


def parenthesesCheck(str):
    l = len(str)
    if l == 1 or l == 0:
        return False

    check = []
    check.append(str[0])
    ic = 1

    for i in range(1, l):
        if str[i] == ")" and check[-1] == "(":
            check.pop()
            ic -= 1
        elif str[i] == "]" and check[-1] == "[":
            check.pop()
            ic -= 1
        elif str[i] == "}" and check[-1] == "{":
            check.pop()
            ic -= 1
        else:
            check.append(str[i])
            ic += 1

    if ic > 0:
        return False
    else:
        return True


if __name__ == "__main__":
    str1 = ["[", "(", ")", "]", "{", "}", "{", "[", "(", ")", "]", "(", ")", "}"]
    str2 = ["[", "(", "]", ")"]

    flag1 = parenthesesCheck(str1)
    flag2 = parenthesesCheck(str2)

    print(f"flag1 = {flag1}\n")
    print(f"flag2 = {flag2}\n")
