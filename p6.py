'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

year=int(input())
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("yes")
        else:
            print("no")
    else:
        print("yes")
else:
    print("yes")
    
