
import calculation as cal

def getnumber():
    numbers=[]

    while True:
        value = input("Enter a number or finish to proceed: ")

        if value.lower() == "finish":
            break
        elif value.isdigit():
         numbers.append(float(value))
        else: 
            print("syntax error")

    return numbers

def main():
    while True:
        choice = choice = int(input("1.addition\n2.subtraction\n3.multiplication\n4.division\n5.modulus\n6.clear \nEnter your choice:"))

        match choice:
            case 1:
                numbers = getnumber()
                if numbers:
                    print("addition:" , cal.add(numbers))

            case 2:
                numbers = getnumber()
                if numbers:
                    print("subtraction:", cal.sub(numbers))

            case 3:
                numbers = getnumber()
                if numbers:
                    print("multiplication:", cal.mul(numbers))

            case 4:
                 numbers = getnumber()
                 if len(numbers) >= 2:
                  result = cal.div(numbers)
                 if result is False:
                  print("Cannot divide by zero")
                 else:
                    print("Division:", result)
            
            case 5:
                numbers = getnumber()
                if len(numbers) >= 2:
                 result = cal.mod(numbers)
                if result is False:
                  print("Cannot calculate modulus with zero")
                else:
                  print("Modulus:", result)

            case 6: 
             print("close")
             break

            case _:
              print("Invalid choice")
              
if __name__ == "__main__":
    main()
