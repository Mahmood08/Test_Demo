
#Write a  program that draws a grid

def print_first(x):
    '''print number of ' + - - - - + 'for grid'''

    print("\n"'+', end=" ")
    
    for i in range (x):
        print("- - - - + ", end="")
        

    


def print_second(y):
    '''print number of '|  |  |' for grid'''
    
    print("\n"'|', end="")
    
    for i in range(y):
        
        print('         |', end="")




def grid_print(x,y):
    
    ''' print grid with specified number of rows and colums'''
    
    print_first(x)
    for i in range (y):
        for i in range (4):
            print_second(x)
        print_first(x)

x= int(input("enter column: "))
y= int(input("enter row :  "))

grid_print(x,y)
            
        
    
