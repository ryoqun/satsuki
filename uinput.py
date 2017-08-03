from evdev import InputDevice, UInput, categorize, ecodes
import statemap
import satsuki_sm

class KeyEvent:
  def __init__(self, keyval):
    #print keyval
    self.keyval = keyval
    self.is_space = self.is_slash = self.is_period = self.is_z = self.is_tenkey = self.is_shift = False
    if self.keyval == ecodes.KEY_SPACE:
      self.name = "space"
      self.is_space = True
    #elif self.keyval == keysyms.slash:
    #  self.name = "slash"
    #  self.is_slash = True
    #elif self.keyval == keysyms.z:
    #  self.name = "z"
    #  self.is_z = True
    #elif self.keyval == keysyms.period:
    #  self.name = "slash"
    #  self.is_period = True
    #elif keyval == 65315 or keyval == 65329 or keyval == 65516:
    #  self.name = "shift"
    #  self.is_shift = True
    #elif keyval == 65314 or keyval == 65332 or keyval == 65515:
    #  self.name = "tenkey"
    #  self.is_tenkey = True
    else:
      self.name = "none"

class KeyDown(KeyEvent):
  pass

class KeyUp(KeyEvent):
  pass

class StateMachine(satsuki_sm.Turnstile_sm):
  def state_list(self):
    return self._state_stack + [self._state]

  def state_exit(self):
    self._state_stack[-1].Exit(self)
    return self._state_stack[-1]

class K:
  def __init__(self):
    self.sink = UInput()

  def emit(self, event):
    self.sink.write(ecodes.EV_KEY, ecodes.KEY_A, 1)
    self.sink.write(ecodes.EV_KEY, ecodes.KEY_A, 0)
    self.sink.syn()

state = StateMachine(K())

source = InputDevice('/dev/input/event5')
source.grab()
print(source)

for event in source.read_loop():
  if event.type == ecodes.EV_KEY:
    print(categorize(event))
    #sink.write(ecodes.EV_KEY, ecodes.KEY_A, 1)
    #sink.write(ecodes.EV_KEY, ecodes.KEY_A, 0)
    #sink.syn()
    state.keydown(KeyDown("aa"))
