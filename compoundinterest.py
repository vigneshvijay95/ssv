def compoundinterest(principle,rate,time):
    Amount = principle * (pow((1 + rate / 100), time ))
    CI =  Amount -principle
    print("Compound interest is:", CI)
if __name__ == "__main__":
    compoundinterest(10000,10.25,12)