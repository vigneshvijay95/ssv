class fibannoci_series():
    def n_terms():
        n_terms = int(input("how many terms do u want?:"))
        n1 = 0
        n2 = 1
        count = 2
        if n_terms<1:
            print("enter the postive integer")
        elif n_terms ==1:
            print("fibannoci sequence:")
            print(n1)
        else:
            print("fibannoci sequence:")
            print(n1,n2,end=',')
        while count<n_terms:
            nth = n1+n2
            print(nth,end=',')
            n1 = n2
            n2 = nth
            count +=1

           