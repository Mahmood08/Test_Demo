def print_number(a):
     for i in range(1,a):
         if i%3==0 and i%5==0:
              print("FizzBuzz")
         elif i%3==0:
               
               print("Fizz")
         elif i%5==0 :
              print("Buzz")
              
         else:
              print(i)
               
                 
        
                 
print_number(101)
