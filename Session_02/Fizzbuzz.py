
#Write a program that prints the numbers from 1 to 100 
#But for multiples of three it will print “Fizz” instead of the number.
#For the multiples of five it will print “Buzz” and For multiples
#of both three and five it will print “FizzBuzz” .

def print_number(n):
     ''' print 'Fizz'for multiples of three,print'Buzz'for multiples
of five and print 'FizzBuzz' for multiples of three and five'''
     
     for i in range(1,n):
         if i%3==0 and i%5==0:
              print("FizzBuzz")
         elif i%3==0:
               
               print("Fizz")
         elif i%5==0 :
              print("Buzz")
              
         else:
              print(i)
               
                 
        
                 
print_number(101)
