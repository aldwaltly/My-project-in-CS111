def decimal_to_binary(decimal):
    x = 0
    mul = 1
    while decimal > 0:
        rem = decimal % 2
        x = x + (mul * rem)
        mul = mul * 10
        decimal //= 2
    print(f'The result in binary is {x}')
def decimal_to_octal(decimal):
    if decimal == 0:
        print(0)
    else:
        x = 0
        mul = 1
        rem = 0
        while decimal != 0:
            rem = int(decimal) % 8
            x = x + (mul * rem)
            mul *= 10
            decimal //= 8
        print(f'the result in octal {x}')
def decimal_to_hex(decimal):
        result=''
        while decimal!=0:
            rem=(decimal%16)
            if rem<10:
                decimal//=16
                result+=str(rem)
            elif rem>=10:
                if rem == 10:
                    decimal//=16
                    result+='A'
                elif rem == 11:
                    decimal//=16
                    result+='B' 
                elif rem==12:
                    decimal//=16
                    result+='C'
                elif rem==13:
                    result+='D'
                    decimal//=16
                elif rem==14:
                    result+='E'
                    decimal//=16
                elif rem== 15:
                    result+='F' 
                    decimal//=16
        result=result[::-1]  
        print(f'the result in hexadecimal {result}')
print("* numbering system converter *")
while True:
    print("A) Insert a new number")
    print("B) Exit program")

    start = input()
    if start == 'B'or start=='b':
        break
    elif start == 'A'or start =='a':
        while True:
            print("Please insert a number")
            the_number = input()

            print("* Please select the base you want to convert a number from *")
            print("A) Decimal")
            print("B) Binary")
            print("C) Octal")
            print("D) Hexadecimal")
            the_first_base = input()
            if the_first_base == 'A'or the_first_base=='a':
                if  any(digit not in {'0', '1','2','3','4','5','6','7','8','9','.'} for digit in str(the_number)):
                  print(f"{the_number} is not a valid number in base 10, please enter a valid number")
                  break
                else:
                    the_number=float(the_number)
                    decimal = int(the_number)
                    if decimal != the_number:
                        print(f"{the_number} is not a valid number in base 10, please enter a valid number")
                    else:
                     while True:
                        print("* Please select the base you want to convert a number to *")
                        print("A) Binary")
                        print("B) Octal")
                        print("C) Hexadecimal")
                        the_second_base = input()
                        if the_second_base == 'A'or the_second_base=='a':
                            decimal_to_binary(decimal) 
                            break
                        elif the_second_base == 'B'or the_second_base=='b':
                            decimal_to_octal(decimal)
                            break
                        elif the_second_base == 'C'or the_second_base=='c':
                            decimal_to_hex(decimal)        
                            break    
                        else:
                            print("Please select a valid choice")#it will appear in whhen user enter another choise
                            continue
                    break
                continue
            elif the_first_base == 'B'or the_first_base=='b':
                bin_int = str(the_number)
                if  any(digit not in {'0', '1'} for digit in str(bin_int)):
                  print(f"{the_number} is not a valid number in base 2, please enter a valid number")
                  break
                bin_int=int(the_number)
                decimal = 0
                count = 0
                while bin_int > 0:
                    last_digit = bin_int % 10
                    bin_int //= 10
                    decimal += last_digit * (2 ** count)
                    count += 1
                while True:
                    print("* Please select the base you want to convert a number to *")
                    print("A) Decimal")
                    print("B) Octal")
                    print("C) Hexadecimal")
                    the_second_base=input()
                    if the_second_base=='A'or the_second_base =='a':
                        print(f'the result in decimal is {decimal}')
                        break
                    elif the_second_base=='B'or the_second_base=='b':
                        x=0
                        decimal_to_octal(decimal)
                        break                    
                    elif the_second_base=='C'or the_second_base=='c':
                        decimal_to_hex(decimal)     
                        break 
                    else:
                        print('Please select a valid choice')   #it will appear in whhen user enter another choise
                        continue
                break            
            elif the_first_base == 'C'or the_first_base =='c':
                if any(digit not in {'0', '1','2','3','4','5','6','7'} for digit in str(the_number)):
                  print(f"{the_number} is not a valid number in base 8, please enter a valid number")
                  break
                oct_int = int(the_number)
                decimal = 0
                count = 0
                while oct_int > 0:
                    last_digit = oct_int % 10
                    oct_int //= 10
                    decimal += last_digit * (8 ** count)
                    count += 1
                while True:
                    print("* Please select the base you want to convert a number to *")
                    print("A) Decimal")
                    print("B) Binary")
                    print("C) Hexadecimal")
                    the_second_base=input()
                    if the_second_base=='A'or the_second_base=='a':
                        print(f'the result in decimal is {decimal}')
                        break
                    elif the_second_base=='B'or the_second_base=='b':
                        decimal_to_binary(decimal)       
                        break
                    elif the_second_base=='C'or the_second_base=='c':
                        decimal_to_hex(decimal)    
                        break 
                    else:
                        print('Please select a valid choice') #it will appear in whhen user enter another choise
                        continue
                break
            elif the_first_base == 'D' or the_first_base =='d':
                if any(digit not in {'0', '1','2','3','4','5','6','7','8','9','A','a','B','b','C','c','D','d','E','e','F','f'} for digit in str(the_number)):
                  print(f"{the_number} is not a valid number in base 16, please enter a valid number")
                  break
                else:
                    z = len(the_number)#to know how many iits and characters in hexadecimal
                    the_number = the_number[::-1]#i needd to flip this string to make the operation from right to left
                    decimal = 0
                    for i in range(0, z, 1):
                        if any(digit in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'} for digit in the_number[i]):#to check every character an assign it to et its value
                            decimal += int(the_number[i]) * 16 ** i
                        elif the_number[i] == 'A' or the_number[i] == 'a':
                            decimal += 10 * 16 ** i
                        elif the_number[i] == 'B' or the_number[i] == 'b':
                            decimal += 11 * 16 ** i
                        elif the_number[i] == 'C' or the_number[i] == 'c':
                            decimal += 12 * 16 ** i
                        elif the_number[i] == 'D' or the_number[i] == 'd':
                            decimal += 13 * 16 ** i
                        elif the_number[i] == 'E' or the_number[i] == 'e':
                            decimal += 14 * 16 ** i
                        elif the_number[i] == 'F' or the_number[i] == 'f':
                            decimal += 15 * 16 ** i
                    while True:
                        print("* Please select the base you want to convert a number to *")
                        print("A) Decimal")
                        print("B) Binary")
                        print("C) Octal") 
                        the_second_base=input()
                        if the_second_base == 'A' or the_second_base=='a':
                            print(f'the result in decimal is {decimal}')
                            break
                        elif the_second_base == 'B'or the_second_base=='b':
                            decimal_to_binary(decimal)    
                            break 
                        elif the_second_base=='C'or the_second_base=='c':
                            decimal_to_octal(decimal)
                            break 
                        else:
                            print('Please select a valid choice')
                            continue
                    break                                      
            else:
                print("Please select a vaalid choice")
                break
    else:
        print("Please select a valid choice")  