#  by Avinash Doddi

def main():
    while True:
        s = input("Enter a Word: ")
        if (len(s) > 1 and s.isalpha()):
            value = s[0:1]
            s = s[1:] + "-" + value + "ay"
            print("pyglatin word is " + s)
            quit = input("Enter 'quit' to quit, any other key to continue : ")
            if quit == 'quit': break
        else:
            print("Invalid Input, Please Try Again")
            
            
if __name__ == '__main__':
    main()
