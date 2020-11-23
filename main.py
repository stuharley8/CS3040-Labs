
from stepper import *
from turnstile import *

stepper = FsmlStepper(turnstile)
results = stepper.run(['ticket', 'pass', 'ticket', 'ticket'])

