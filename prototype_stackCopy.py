# Algorithms, 4th Edition, Ch.1, Sec.3, Exe.1.3.12


def stackCopy(sarr):
    tmp = []
    cp = []

    for e in sarr:
        tmp.append(e)

    for e in tmp:
        cp.append(e)

    return cp


if __name__ == "__main__":
    s = "What is the purpose of this exercise?"
    input = []
    for e in s:
        input.append(e)
    print(f"Input: {input}\n")

    cp = stackCopy(s)
    print(f"Output: {cp}\n")
  
