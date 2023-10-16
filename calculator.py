first = input("enter 1st no: ")
op = input("enter operation: ")
second = input("enter 2nd no: ")

first = int(first)
second = int(second)

if op=="+":
    print(first + second)
elif op=="*":
    print(first * second)
elif op=="/":
    print(first / second)
elif op=="%":
    print(first % second)
elif op=="-":
    print(first - second)
