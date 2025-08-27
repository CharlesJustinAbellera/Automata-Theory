def num1 (string):
    start = 'a'

    for ch in string:
        if start == 'a':
            if ch == '0':
                start = 'a'
            elif ch == '1':
                start = 'b'
            else:
                return None

        elif start == 'b':
            if ch == '0':
                start = '1'
            elif ch == '1':
                start = 'a'
            else:
                return None

        elif start == '1':
            if ch == '0':
                start = 'b'
            elif ch == '1':
                start = '1'
            else:
                return None
    
    return start == '1'

if __name__ == "__main__":
    while True:    
        string = input ("Enter binary digit/s: ").strip()
        result = num1(string)

        if result is None:
            print("Invalid")
        
        elif result:
            print ("Result: Accepted")

        else:
            print ("Result: Rejected")

        input_again = input ("Try again? (yes/no): ") .strip() .lower()
        if input_again != "y":
            print ("Sige")
            break


# Sample accepted: 101, 10100, 101111
# Sample rejected: 1001, 10101, 1101