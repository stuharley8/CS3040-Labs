# Author: Stuart Harley

from fsm import Fsm

real = \
    Fsm() \
        .add_state("Start") \
            .add_transition_range("0", "9", None, "Before ./e") \
            .add_transition(".", None, "Decimal point") \
        .add_state("Before ./e", is_final=True) \
            .add_transition_range("0", "9", None, "Before ./e") \
            .add_transition(".", None, "Decimal point") \
            .add_transition("e", None, "E") \
        .add_state("Decimal point") \
            .add_transition_range("0", "9", None, "After .") \
        .add_state("After .", is_final=True) \
            .add_transition_range("0", "9", None, "After .") \
            .add_transition("e", None, "E") \
        .add_state("E") \
            .add_transition_range("0", "9", None, "After e") \
        .add_state("After e", is_final=True) \
            .add_transition_range("0", "9", None, "After e")
