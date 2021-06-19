# num = int(input("Enter an Integer: "))
# if num > 1:
#     for i in range(2 ,num):
#         if (num%i) == 0:
#             print("Not prime")
#             break
#     else:
#         print("Prime") 
# else:   
#     print("not prime")

# --------------------------------------------------------------------------------------------------------


# n = 20

# primes = [i for i in range(2, n + 1) if all(i%j != 0 for j in range(2, int(i ** 0.5) + 1))]

# print(primes)


# --------------------------------------------------------------------------------------------------------

lower = 2  
upper = 100 
  
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  