def first(a):
    
    print("\n"'+', end=" ")
    
    for i in range (a):
        print("- - - - + ", end="")
        
#    print("- - - - + ")
    
a= int(input("enter column: "))
b= int(input("enter row :  "))
#first(a)

def second(b):
    
    print("\n"'|', end="")
    
    for i in range(b):
        
        print('         |', end="")
#    print("       |")    
#second(b)



def func(a,b):
    first(a)
    for i in range (b):
        for i in range (4):
            second(a)
        first(a)


func(a,b)
            
        
    
