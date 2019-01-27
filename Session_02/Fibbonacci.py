def fibbonacci(n):
    ''' Calculate the nth value of fibbonacci series'''
    
    print("print nth fibbonacci number")
    
    first=0
    second=1
    if(n<0):
        return
#       print("Incorrect input")
    elif(n==0):
        return 0
      
    elif(n==1):
        return 1
    else:
        
        for i in range(n-1):
            next=first+second
            first=second
            second=next
               
        return next     
            
          
          

def Locus(n):
    ''' Calculate the nth value of Locus seies'''
    
    print("print nth Locus Number")
    
    first= 2
    second = 1
    
    if(n<0):
        return
#       print("Incorrect input")
    elif(n==0):
        return 2
      
    elif(n==1):
        return 1
    else:
        for i in range(n-1):
        
            next=first+second
            first=second
            second=next
        return next



def fibbo_sum_series(n, first=0,second=1):
    
    '''calculate the series at a given index'''
    
    print(" print the fibbonacci series at a given index")
    
    if(n<0):
        return
 #       print("Incorrect input")
    elif(n==0):
        return first
    elif(n==1):
        return second
    else:
        for i in range(n-1):
        
            next=first+second
            first=second
            second=next
        return next


def Locus_sum_series(n,first,second):
    
    ''' Calculate the nth value of Locus seies'''
    
    print("print the Locus series at a given index")
   
    if(n<0):
        return 
#        print("Incorrect input")
    elif(n==0):
        return 2
      
    elif(n==1):
        return 1
    else:
        for i in range(n-1):
        
            next=first+second
            first=second
            second=next
        return next


n=int(input("Enter the input"))
print(Locus(n))    

print(fibbonacci(n))
print(fibbo_sum_series(n))
print(Locus_sum_series(n,2,1))




if__name__== '__main__':
    
    assert fibbonacci(0)==0
    assert fibbonacci(1)==1
  
    assert Locus(0)==0
    assert Locus(1)==1
    assert Locus(4)==7
    assert fibbo_sum_series(3)==fibbonacci(3)
    assert Locus_sum_series(4)==Locus(4)
    assert Locus_sum_series(5)==Locus(5)
    assert fibbo_sum_series(4)== fibbonacci(4)

    
        
    
    
    
    
          
