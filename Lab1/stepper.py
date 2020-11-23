from fsm import FsmlIllegalEventException

class FsmlStepper():

    def __init__(self, machine):
        self.fsm = machine
        self.currentState = machine.initialState

    def run(self, input):
        saved_input = input
        input = list(input)
        output = []
        while input:
            symbol = input.pop(0)
            action, targetState = self.step(symbol)
            if action is not None: output.append(action)
        print("Final state of machine: " + self.currentState)
        if self.fsm.is_final_state(self.currentState):
            print("Machine accepted input " + str(saved_input))
        else:
            print("Machine REJECTED input " + str(saved_input))
        print("Machine output: " + str(output))
        return output

    def step(self, symbol):
        print("Taking step from " + str(self.currentState) + " on " + str(symbol))
        possible_transitions = self.fsm.states[self.currentState]
        if symbol not in possible_transitions:
            raise FsmlIllegalEventException
        (action, targetState) = possible_transitions[symbol]
        self.currentState = targetState
        return action, targetState
