class MealyState:
    def __init__(self, name):
        self.name = name
    
    def transition(self, input_char):
        raise NotImplementedError("Subclasses must implement transition method")
    
    def __str__(self):
        return self.name


class StateA(MealyState):
    def __init__(self):
        super().__init__("A")
    
    def transition(self, input_char):
        if input_char == '0':
            return StateB(), 'b'
        else:
            return StateA(), 'b'


class StateB(MealyState):
    def __init__(self):
        super().__init__("B")
    
    def transition(self, input_char):
        if input_char == '0':
            return StateB(), 'b'
        else:
            return StateC(), 'a'


class StateC(MealyState):
    def __init__(self):
        super().__init__("C")
    
    def transition(self, input_char):
        if input_char == '0':
            return StateB(), 'b'
        else:
            return StateA(), 'b'


class MealyMachine:
    def __init__(self):
        self.current_state = StateA()
        self.transition_table = {
            'A': {'0': ('B', 'b'), '1': ('A', 'b')},
            'B': {'0': ('B', 'b'), '1': ('C', 'a')},
            'C': {'0': ('B', 'b'), '1': ('A', 'b')}
        }
    
    def show_transition_table(self):
        print("=" * 60)
        print("MEALY MACHINE TRANSITION TABLE (State / Input → Next State, Output)")
        print("=" * 60)
        print(f"{'State':<10}{'Input':<10}{'Next State':<15}{'Output':<10}")
        print("-" * 60)
        for state, transitions in self.transition_table.items():
            for inp, (next_state, out) in transitions.items():
                print(f"{state:<10}{inp:<10}{next_state:<15}{out:<10}")
        print("=" * 60)

    def process_input(self, input_string):
        if not all(char in ['0', '1'] for char in input_string):
            raise ValueError("Input string must contain only '0's and '1's")
        
        output_sequence = []
        state_path = [str(self.current_state)]
        
        print(f"\nInitial state: {self.current_state}")
        print(f"Input string: {input_string}")
        print("-" * 40)
        
        for i, char in enumerate(input_string):
            previous_state = str(self.current_state)
            self.current_state, output = self.current_state.transition(char)
            output_sequence.append(output)
            state_path.append(str(self.current_state))
            print(f"Step {i+1}: Input='{char}', State={previous_state}→{self.current_state}, Output='{output}'")
        
        print("-" * 40)
        print(f"State path: {' → '.join(state_path)}")
        return ''.join(output_sequence)
    
    def reset(self):
        self.current_state = StateA()


def main():
    mealy_machine = MealyMachine()
    
    # Display transition table
    mealy_machine.show_transition_table()

    # Example run
    mealy_machine.reset()
    output = mealy_machine.process_input("01")
    print(f"Final Output: {output}")
    print(f"Explanation: 'a' appears whenever '01' sequence is detected in the input.")

    print("\n" + "=" * 60)
    print("INTERACTIVE DEMO")
    print("=" * 60)
    
    mealy_machine.reset()
    while True:
        user_input = input("\nEnter a binary string (0s and 1s) or 'Exit' to exit: ")
        if user_input.lower() == 'exit':
            break
        
        mealy_machine.reset()
        output = mealy_machine.process_input(user_input)
        print(f"Final Output: {output}")


if __name__ == "__main__":
    main()
