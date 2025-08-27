def dfa2(string):
    # starts: q0 (start), q1, q2, q3 (final)
    start = 'q0'
    for ch in string:
        if ch not in ('a', 'b'):
            return None  # invalid input
        
        if start == 'q0':
            start = 'q1' if ch == 'a' else 'q2'
        elif start == 'q1':
            start = 'q0' if ch == 'a' else 'q3'
        elif start == 'q2':
            start = 'q3' if ch == 'a' else 'q0'
        elif start == 'q3':
            start = 'q2' if ch == 'a' else 'q1'
    
    return start == 'q3'  # Accept if ends in q3


if __name__ == "__main__":
    while True:
        string = input("Enter a string (a and b): ").strip()
        result = dfa2(string)

        if result is None:
            print("Invalid input: only 'a' and 'b' allowed")
        elif result:
            print("Result: ACCEPTED")
        else:
            print("Result: REJECTED")

        again = input("Try again? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

# Accepted: aaba, baabab, aaba
# Rejected: aba, baaba, aabb