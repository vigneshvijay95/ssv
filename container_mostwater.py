def init(self,height: list[int]):
    h = height  
    A = 0
    i,j=0,len(h)-1
    while j-i >0:
        if h[i] < h[j]:
            a = (j-i)*h[i]
            i +=1
    else:
        a = (j-i)*h[j]
        j -=1
    if a>A:
        A = a
    return A
if __name__ == "__main__":
    init(self,height, list[int])