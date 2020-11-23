# BEGIN ...
from fsm import Fsm
# END ...
turnstile = \
  Fsm() \
    .add_state("locked", is_final = True) \
      .add_transition("ticket", "collect", "unlocked") \
      .add_transition("pass", "alarm", "exception") \
    .add_state("unlocked") \
      .add_transition("ticket", "eject", "unlocked") \
      .add_transition("pass", None, "locked") \
    .add_state("exception") \
      .add_transition("ticket", "eject", "exception") \
      .add_transition("pass", None, "exception") \
      .add_transition("mute", None, "exception") \
      .add_transition_range('1', '5', 'punch', 'go') \
      .add_transition("release", None, "locked")
