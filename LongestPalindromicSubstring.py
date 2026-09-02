def rev01(s):
    res = ""
    for i in range(0, len(s)):
        res = s[i] + res
    return res

if __name__ == "__main__":
    s = "malayalam"
    long_pal_sub = ""
    for i in range(0, len(s)):
        for j in range(0, len(s)):
            res = ""
            for k in range(i, j + 1):
                res += s[k]
            if res == rev01(res):
                if len(long_pal_sub) < len(res):
                    long_pal_sub = res
    print(res)
