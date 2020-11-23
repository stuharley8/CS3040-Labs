# BEGIN ...
from collections import defaultdict
# END ...

class FsmlException(Exception):
    # Base class for all FSML exceptions
    pass

class FsmlOkException(FsmlException):
    # Base class for all FsmlOk exceptions
    pass

class FsmlDistinctIdsException(FsmlOkException):
    pass

class FsmlDeterminismException(FsmlOkException):
    pass

class FsmlIllegalEventException(FsmlException):
    pass

class Fsm():
    def __init__(self):
        self.states = defaultdict(list)
        self.final_states = set()
        self.current = None
        self.initialState = None

    def add_state(self, id, is_final = False):
        #print("Adding state " + id)
        if not self.initialState:
            self.initialState = id
        self.current = id
        if id in self.states:
            raise FsmlDistinctIdsException
        self.states[id] = dict()
        if is_final:
            self.final_states.add(id)
        return self

    def add_transition(self, event, action, target):
        #print("  Adding transition on " + event + " going to " + target)
        if event in self.states[self.current]: 
            # machine not deterministic
            raise FsmlDeterminismException;
        self.states[self.current][event] = \
            (action, self.current if target is None else target)
        return self

    def add_transition_range(self, event_low, event_high, action, target):
        '''Add transitions for a range of characters going from event_low
        to event_high. Both the low and high must be a single character.
        Both the low and high values are included in the range. All events
        use the same action and target.'''
        transition_range = range(ord(event_low), ord(event_high) + 1)
        for trans in transition_range:
            self.add_transition(chr(trans), action, target)
        return self
    
    def is_final_state(self, state):
        return state in self.final_states
