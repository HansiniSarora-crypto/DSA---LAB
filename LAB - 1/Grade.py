print("Enter mark:")
marks = int(input())
if marks >=91:
    print("The grade is O")
else:
    if marks >=86:
        print("The grade is A+")
    else:
        if marks >=81:
            print("The grade is A")
        else:
            if marks >=76:
                print("The grade is B+")
            else:
                if marks >=70:
                    print("The grade is B")
                else:
                    if marks >=60:
                        print("The grade is C")
                    else:
                        if marks <=50:
                            print("You are fail")
        
