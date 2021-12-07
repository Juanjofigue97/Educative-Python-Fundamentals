def check_balance(brackets):  # The argument is a string
    a = 0
    for i in brackets:
        if  i == '[':
            a += 1
        elif i == ']':
            a -=1
        elif a < 0:
          break
    if a == 0:
      b = "The brackets are balance"
    else:
      b = "The brackets aren't balance"
    
    return b
print("--------Check Brackets--------")
print("how does it work: ")
print("check_balance('[][][[]]'): " + check_balance('[][][[]]'))
print("check_balance('[][[][[]]'): " + check_balance('[][[][[]]'))

A = input("Put your bracktes: ")

print(check_balance(A))
