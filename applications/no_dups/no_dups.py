def no_dups(s):
    s = s.split()
    return ' '.join([i for n, i in enumerate(s) if i not in s[:n]])


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
