def absent_number(n):
    all_nums = set([0,1,2,3,4,5,6,7,8,9])
    n = set([int(i) for i in n])
    n = n.symmetric_difference(all_nums)
    n = sorted(n)
    return n
if __name__ == "__main__":
    print(absent_number([9,7,9,1,3,9,6,5,9,1]))
    