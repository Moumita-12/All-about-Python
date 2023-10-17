for i in range(int(input())):
    n=int(input())
    if n%3 ==0:
        if(n<10):  print("NO") 
        else:  
            print("YES")
            print("1 4 " + str(n-5) )
    else:
        if(n<6):  print("NO") 
        else:  
            print("YES")
            print("1 2 " + str(n-3) )
