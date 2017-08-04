from evdev import InputDevice, UInput, categorize, events, ecodes
import statemap
import satsuki_sm

class KeyEvent:
  def __init__(self, event):
    #print event
    self.event = event
    self.is_space = self.is_slash = self.is_period = self.is_z = self.is_tenkey = self.is_shift = False
    if self.event.scancode == ecodes.KEY_SPACE:
      self.name = "space"
      self.is_space = True
    #elif self.event == keysyms.slash:
    #  self.name = "slash"
    #  self.is_slash = True
    #elif self.event == keysyms.z:
    #  self.name = "z"
    #  self.is_z = True
    #elif self.event == keysyms.period:
    #  self.name = "slash"
    #  self.is_period = True
    #elif event == 65315 or event == 65329 or event == 65516:
    #  self.name = "shift"
    #  self.is_shift = True
    #elif event == 65314 or event == 65332 or event == 65515:
    #  self.name = "tenkey"
    #  self.is_tenkey = True
    else:
      self.name = "none"
    print self.name

class KeyDown(KeyEvent):
  pass

class KeyUp(KeyEvent):
  pass

class StateMachine(satsuki_sm.Turnstile_sm):
  def state_list(self):
    return self._state_stack + [self._state]

  def state_exit(self):
    raise "aaaa"
    self._state_stack[-1].Exit(self)
    return self._state_stack[-1]

class K:
  def __init__(self):
    self.sink = UInput()
    self.reset_state()

  def emit(self, event):
    self.sink.write(ecodes.EV_KEY, ecodes.KEY_A, 1)
    self.sink.write(ecodes.EV_KEY, ecodes.KEY_A, 0)
    self.sink.syn()

  def emit_space(self):
    self.sink.write(ecodes.EV_KEY, ecodes.KEY_SPACE, 1)
    self.sink.write(ecodes.EV_KEY, ecodes.KEY_SPACE, 0)
    self.sink.syn()

  def reset_state(self):
    self.__buffer = None
    self.__space_mode = False
    self.__control_mode = False
    self.__meta_mode = False
    self.__tenkey_mode = False
    self.__shift_mode = False

  def space_mode(self, flag):
    print("spacd moe !!!!!!!i" + str(flag))
    self.__space_mode = flag

  def control_mode(self, flag):
    self.__control_mode = flag

  def meta_mode(self, flag):
    self.__meta_mode = flag

  def shift_mode(self, flag):
    self.__shift_mode = flag

  def tenkey_mode(self, flag):
    self.__tenkey_mode = flag


state = StateMachine(K())

source = InputDevice('/dev/input/event5')
source.grab()
print(source)

for event in source.read_loop():
  if event.type == ecodes.EV_KEY:
    key_event = categorize(event)
    print key_event
    print key_event.keystate
    #sink.write(ecodes.EV_KEY, ecodes.KEY_A, 1)
    #sink.write(ecodes.EV_KEY, ecodes.KEY_A, 0)
    #sink.syn()
    print(state.state_list())
    try:
      if key_event.keystate == events.KeyEvent.key_down:
        state.keydown(KeyDown(key_event))
      if key_event.keystate == events.KeyEvent.key_up:
        state.keyup(KeyUp(key_event))
    except Exception as exception:
      print "exception is caught"
      print exception
