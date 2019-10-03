value1 = input("Enter a value: ")
while True:

    operator = input("Mathematical Operator: ")
    value2 = input("Enter another value: ")

    a = operator


    def add_op(value1, value2):
        result = int(value1) + int(value2)
        return result


    def sub_op(value1, value2):
        result = int(value1) - int(value2)
        return result


    def div_op(value1, value2):
        result = int(value1) / int(value2)
        return result


    def mul_op(value1, value2):
        result = int(value1) * int(value2)
        return result


    if a == "+":
        answer = add_op(value1, value2)
        print(answer)

    elif a == "-":
        answer = sub_op(value1, value2)
        print(answer)

    elif a == "/":
        answer = div_op(value1, value2)
        print(answer)

    elif a == "*":
        answer = mul_op(value1, value2)
        print(answer)

    value1 = answer
    b = input("To stop calculator please enter \"#\"")
    if b == "#":
        break
    else:
        continue
