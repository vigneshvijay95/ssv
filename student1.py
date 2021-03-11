class student:
    def __init__ (self, name, rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
    def accept(self,Name,Rollno,marks1,marks2):
        ob = student(Name,Rollno,marks1,marks2)
        ls.append(ob)
    def display(self,ob):
        print("Name :",ob.name)
        print("Rollno :",ob.rollno)
        print("marks1 :",ob.m1)
        print("marks2 :",ob.m2)
        print("\n")
    def search(self,rn):
        for i in range (ls.__len__()):
            if (ls[i].rollno == rn):
                return i

                                      
    def delete(self, rn):
        i = obj.search(rn)   
        del ls[i] 
  
        
    def update(self, rn, No): 
        i = obj.search(rn) 
        roll = No 
        ls[i].rollno = roll
ls =[]
obj = student('', 0, 0, 0)


print("\nOperations used: ") 
print("\n1.Accept Student details\n2.Display Student Details\n" 
        "3.Search Details of a Student\n4.Delete Details of Student" 
        "\n5.Update Student Details\n6.Exit") 

#ch = int(input("Enter the choice:")) 
#if (ch == 1):
obj.accept("vignesh", 1, 90, 78)
obj.accept("Ram", 2, 85, 90)
obj.accept("Bala", 3, 65, 70)
#elif (ch == 2):
print("\n") 
print("\nList of Students\n") 
for i in range(ls.__len__()):
    obj.display(ls[i]) 
             
#elif(ch == 3):
print("\n Student Found, ") 
s = obj.search(2) 
obj.display(ls[s])
#elif(ch == 4):
obj.delete(2) 
print(ls.__len__()) 
print("List after deletion") 
for i in range(ls.__len__()):
    obj.display(ls[i])
#elif (ch == 5):
obj.update(3, 2) 
print(ls.__len__()) 
print("List after updation") 
for i in range(ls.__len__()):
    obj.display(ls[i])
#else:
print("Thank You !")      

f = open("student.txt","r")
my_data = f.readlines()
print(type(my_data))
f = open("sv.txt","w")
f.write("Hi welcome to svs web portal:\n")
f.write("This is student details")
f.close()
