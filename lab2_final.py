class MooreMachine:
    def __init__(self):
        # Define states with their transitions
        # Format: state: {input: (next_state, output)}
        self.transitions = {
            'A': {
                0: ('A', 'A'),  # Input 0: go to A, output A
                1: ('B', 'B')   # Input 1: go to B, output B
            },
            'B': {
                0: ('C1', 'A'), # Input 0: go to C1, output A
                1: ('D1', 'B')  # Input 1: go to D1, output B
            },
            'C1': {
                0: ('D2', 'C'), # Input 0: go to D2, output C
                1: ('B', 'B')   # Input 1: go to B, output B
            },
            'D1': {
                0: ('B', 'B'),  # Input 0: go to B, output B
                1: ('C2', 'C')  # Input 1: go to C2, output C
            },
            'C2': {
                0: ('D2', 'C'), # Input 0: go to D2, output C
                1: ('B', 'B')   # Input 1: go to B, output B
            },
            'D2': {
                0: ('B', 'B'),  # Input 0: go to B, output B
                1: ('C2', 'C')  # Input 1: go to C2, output C
            },
            'E': {
                0: ('D2', 'C'), # Input 0: go to D2, output C
                1: ('E', 'C')   # Input 1: go to E, output C
            }
        }
        self.current_state = 'A'
    
    def process_binary_string(self, binary_string):
        output_sequence = []
        self.current_state = 'A'  # Start from state A
        
        for char in binary_string:
            input_bit = int(char)
            current_state = self.current_state
            
            # Get transition info
            next_state, output = self.transitions[current_state][input_bit]
            
            # Add output to sequence
            output_sequence.append(output)
            
            # Move to next state for the next input
            self.current_state = next_state
        
        output_string = ''.join(output_sequence)
        print(f"Input: {binary_string} → Output: {output_string}")
        
        return output_string

# Main program
def main():
    machine = MooreMachine()
    
    print("=== MOORE MACHINE PROCESSOR ===")
    
    # Test samples
    print("\nTEST SAMPLES:")
    print("-" * 30)
    test_inputs = ["00110", "11001", "1010110", "101111"]
    
    for test_input in test_inputs:
        machine.process_binary_string(test_input)
    
    print("-" * 30)
    print("\nNow enter your own binary strings!")
    print("Type 'quit' to exit")
    
    while True:
        user_input = input("\nEnter binary string: ").strip()
        
        if user_input.lower() == 'quit':
            break
        
        if not user_input:
            continue
            
        # Validate input contains only 0s and 1s
        if all(char in '01' for char in user_input):
            machine.process_binary_string(user_input)
        else:
            print("Error: Input must contain only 0s and 1s")

if __name__ == "__main__":
    main()