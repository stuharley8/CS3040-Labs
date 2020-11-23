# Author: Stuart Harley

from stepper import *
from real import *

stepper = FsmlStepper(real)
try:
    results = stepper.run(['6', 'e', '7', '.', '4'])
except FsmlIllegalEventException:
    print('Illegal input')