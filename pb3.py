num = int(input("Enter a number greater than 0 : "))

if num <= 0 :
    print(f"{num} is not an invalid number")
    quit()

for i in range(num, 0, -1) :
    
    for k in range(0, i) :
        for j in range(0, k+1) :
            print("*", end="")
        print("")

    for k in range(i, 1, -1) :
        if( i > 2 ) :
            # Condition not to print the last 1 star as it's not the last two iteration
            if( k - 1 > 1) :
                for j in range(1, k) :
                    print("*", end="")
                print("")
        else :
            for j in range(1, k) :
                print("*", end="")
            print("")
        