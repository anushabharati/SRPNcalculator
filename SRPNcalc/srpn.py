"""Code for Simple SRPN calculator"""
#This is your SRPN file. Make your changes here.
stack = []
max_num = 2147483647
min_num = -2147483648
checkvalue = []
operator = ['+','-','=','/','^','*','#']
#Function for splitting the input#
def process_command(command):
    flag = False
    c = command.split()
    for a in c:
        if a == '#' and flag is False:
            flag = True
        elif a == '#' and flag is True:
            flag = False
        elif flag is True:
            continue
        elif (len(a) > 1 and not a.isalnum()and not a.isalpha() and not a.isnumeric() and not (a.startswith("-") and a[1].isdigit())):
            index = 0
            while (index < (len(a)-1)):
                if a[index] in operator:
                    newstring = ' ' + a[index]+ ' '
                    a = a[:index] + newstring + a [(index + 1):]
                    index += 3
                else:
                    index += 1
            process_command(a)
        else:
            operation(a)
#Function for doing the operation on the input#
def operation(command):
    if (command.isdigit() or
    (command.startswith("-") and
    command[1:].isdigit())):
        command = int(command)
        if command < min_num:
            command = min_num
        elif command > max_num:
            command = max_num
        if len(stack) < 23:
            stack.append(command)
        else:
            print('Stack overflow.')
    elif command == 'd':
        for a in stack:
            print(a)

    elif command != '=':
        if len(stack) > 1:
            opr2 = int(stack.pop())
            opr1 = int(stack.pop())
            try:
                if command == "+":
                    result = opr1 + opr2
                elif command == "-":
                    result = opr1 - opr2
                elif command == "/":
                    if opr2 != 0:
                        result = int(opr1 / opr2)
                    else:
                        result = None
                        print('Divide by 0.')
                elif command == "*":
                    result = opr1 * opr2
                elif command == "%":
                    result = opr1 % opr2
                elif command == "^":
                    if opr2 > 0:
                        result = opr1 ** opr2
                    else:
                        result= None
                        stack.append(opr1)
                        stack.append(opr2)
                        print("Negative power.")
                if result is not None:
                    if int(result) < min_num:
                        result = min_num
                    elif int(result) > max_num:
                        result = max_num
                    if len(stack) < 23:
                        stack.append(result)
                    else:
                        print('Stack overflow.')
            except ValueError:
                print("Error")
            else:
                return None
        else:
            print("Stack underflow.")
    elif command == '=':
        print(stack[-1])

#This is the entry point for the program.
#Do not edit the below
if __name__ == "__main__":
    while True:
        try:
            cmd = input()
            pc = process_command(cmd)
            if pc is not None:
                print(str(pc))
        except:
            exit()
            