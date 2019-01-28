#Calculate the fibonacci and Locus series

def fibonacci(n):
    """ Calculate the nth fibbonacci number"""
    

    
    
    first=0
    second=1
    if(n<0):
        return

    elif(n==0):
        return 0
      
    elif(n==1):
        return 1
    else:
        first=0
        second=1
        for i in range(2,n+1):
            next=first+second
            first=second
            second=next
               
        return next     
            
        

def Locus(n):
    """ Calculate the nth Locus number"""
    

    
    
    first=2
    second=1
    
    if(n<0):
        return 

    elif(n==0):
        return 2
      
    elif(n==1):
        return 1
    else:
       
        for i in range(2,n+1):
        
            next=first+second
            first=second
            second=next
        return next



def sum_series(n, first=0,second=1):
    
    """calculate the nth value of summation series"""
    

    if(n<0):
        return

    elif(n==0):
        return first
    elif(n==1):
        return second
    else:
        for i in range(2,n+1):
        
            next=first+second
            first=second
            second=next
        return next





n =int(input("Enter the input"))
    
print("print nth fibonacci Number")
print(fibonacci(n))

print("print nth Locus Number")
print(Locus(n))

print("print nth value of fibo summation series")
print(sum_series(n))

print("print nth value of Lucas summation series")
print(sum_series(n,2,1))





if __name__ == "__main__" :
    
    # run some tests
    print("run some test ")
    assert Locus(5)==11
    assert fibonacci(5)==5
    
    
  
    assert fibonacci(1)==1
    assert fibonacci(3)==2
    assert fibonacci(7)==13
    
    assert Locus(0)==2
    assert Locus(1)==1
    assert Locus(4)==7
    assert Locus(5)==11
    
# test if sum_series matched fibonacci
    assert sum_series(3)== fibonacci(3)
    
    
# test if sum_series matched lucas
    assert sum_series(5,2,1)==Locus(5) 
    print("test passed ")
  

    
        
    
    
    
    
          
