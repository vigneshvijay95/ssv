class prime_number:

            num = int(input("Enter the number:"))
            if num >1:
                for i in range(2,num):
                    if(num % i) ==0:
                        print(num,"is not a prime number")
                        print(i,"times",num//i,"i",num)
                        break
                    else:
                        print(num,"this is a prime number")
            else:
                print(num,"this is not a prime number")