"""Binary to Decimal and Back Converter by avinash-doddi"""

def binary_to_Decimal(binary):
    print(int(binary, 2))

def Decimal_to_binary(decimal):
    print(bin(decimal)[2:])
    
def main():
    try:
        print("Enter Binary to Convert Decimal to Binary, Enter Decimal to Convert Binary to Decimal")
        switch = input()
        if (switch == 'Binary' or switch == 'binary'):
            print("Enter the number:")
            Decimal_to_binary(int(input()))
        elif (switch == 'Decimal' or switch == 'decimal'):
            print("Enter the binary:")
            binary_to_Decimal(input())
        else:
            main()
    except ValueError:
        print("Entered Wrong value, Enter the Correct Value")
        main()
    except NameError:
        print("Entered Wrong value, Enter the Correct Value")
        main()
                
if __name__ == '__main__':
    main()
