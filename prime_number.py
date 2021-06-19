num = int(input("Enter an Integer: "))
if num > 1:
    for i in range(2 ,num):
        if (num%i) == 0:
            print("Not prime")
            break
    else:
        print("Prime") 
else:   
    print("not prime")