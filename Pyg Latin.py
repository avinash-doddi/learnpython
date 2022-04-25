#  by Avinash Doddi

def main():
    while True:
        s = input("Enter a Word: ")
        # checks whether the input is more than one character length and does it only contains alphabets.
        if (len(s) > 1 and s.isalpha()): 
            value = s[0:1] # to slice the starting alphabet of string,
            s = s[1:] + "-" + value + "ay" # modifying string.
            print("pyglatin word is " + s)
            quit = input("Enter 'quit' to quit, any other key to continue : ")
            if quit == 'quit': break
        else:
            print("Invalid Input, Please Try Again")
            
            
if __name__ == '__main__':
    main()
