class MooreState:
    def __init__(self, name, output):
        self.name = name
        self.output = output
    
    def transition(self, input_char):
        raise NotImplementedError("Subclasses must implement transition method")
    
    def __str__(self):
        return f"{self.name} (Output={self.output})"


class StateA(MooreState):
    def __init__(self):
        super().__init__("A", "0")

    def transition(self, input_char):
        if input_char == '1':
            return StateB()
        elif input_char == '0':
            return StateC()


class StateB(MooreState):
    def __init__(self):
        super().__init__("B", "0")

    def transition(self, input_char):
        if input_char == '1':
            return StateB()
        elif input_char == '0':
            return StateC()


class StateC(MooreState):
    def __init__(self):
        super().__init__("C", "1")

    def transition(self, input_char):
        if input_char == '0':
            return StateC()
        elif input_char == '1':
            return StateB()


class MooreMachine:
    def __init__(self):
        self.current_state = StateA()
        self.transition_table = {
            "A": {"0": "C", "1": "B", "output": "0"},
            "B": {"0": "C", "1": "B", "output": "0"},
            "C": {"0": "C", "1": "B", "output": "1"},
        }

    def show_transition_table(self):
        print("=" * 60)
        print("MOORE MACHINE TRANSITION TABLE (Output depends on state)")
        print("=" * 60)
        print(f"{'State':<10}{'Input':<10}{'Next State':<15}{'Output':<10}")
        print("-" * 60)
        for state, data in self.transition_table.items():
            for inp in ['0', '1']:
                print(f"{state:<10}{inp:<10}{data[inp]:<15}{data['output']:<10}")
        print("=" * 60)

    def process_input(self, input_string):
        if not all(char in ['0', '1'] for char in input_string):
            raise ValueError("Input string must contain only '0's and '1's")
        
        output_sequence = [self.current_state.output]  # Moore: output before processing input
        state_path = [self.current_state.name]
        
        print(f"\nInitial state: {self.current_state}")
        print(f"Input string: {input_string}")
        print("-" * 40)
        
        for i, char in enumerate(input_string):
            prev_state = str(self.current_state)
            self.current_state = self.current_state.transition(char)
            state_path.append(self.current_state.name)
            output_sequence.append(self.current_state.output)
            print(f"Step {i+1}: Input='{char}', State={prev_state} → {self.current_state}")

        print("-" * 40)
        print(f"State path: {' → '.join(state_path)}")
        print(f"Output sequence: {''.join(output_sequence)}")
        return ''.join(output_sequence)
    
    def reset(self):
        self.current_state = StateA()


def main():
    moore_machine = MooreMachine()
    
    # Show transition table
    moore_machine.show_transition_table()
    
    # Example run
    moore_machine.reset()
    output = moore_machine.process_input("1010")
    print(f"\nFinal Output: {output}")

    print("\n" + "=" * 60)
    print("INTERACTIVE DEMO")
    print("=" * 60)
    
    while True:
        user_input = input("\nEnter a binary string (0s and 1s) or 'Exit' to exit: ")
        if user_input.lower() == 'exit':
            break
        moore_machine.reset()
        moore_machine.process_input(user_input)


if __name__ == "__main__":
    main()
