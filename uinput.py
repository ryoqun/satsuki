from evdev import InputDevice, UInput, categorize, events, ecodes
import statemap
import satsuki_sm

class KeyEvent:
  def __init__(self, event):
    #print(event)
    self.event = event
    self.is_space = self.is_slash = self.is_period = self.is_z = self.is_tenkey = self.is_shift = False
    if self.event.scancode == ecodes.KEY_SPACE:
      self.name = "space"
      self.is_space = True
    elif self.event.scancode == ecodes.KEY_SLASH:
      self.name = "slash"
      self.is_slash = True
    elif self.event.scancode == ecodes.KEY_Z:
      self.name = "z"
      self.is_z = True
    #elif self.event.scancode == keysyms.period:
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
    #print(self.name)

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
  __space_mode_map = {
    ecodes.KEY_1: [ecodes.KEY_1, True],
    ecodes.KEY_2: [ecodes.KEY_2, True],
    ecodes.KEY_3: [ecodes.KEY_3, True],
    ecodes.KEY_4: [ecodes.KEY_4, True],
    ecodes.KEY_5: [ecodes.KEY_5, True],
    ecodes.KEY_6: [ecodes.KEY_6, True],
    ecodes.KEY_7: [ecodes.KEY_7, True],
    ecodes.KEY_8: [ecodes.KEY_8, True],
    ecodes.KEY_9: [ecodes.KEY_9, True],
    ecodes.KEY_0: [ecodes.KEY_0, True],

    ecodes.KEY_Q: [ecodes.KEY_1, True],
    ecodes.KEY_W: [ecodes.KEY_2, True],
    ecodes.KEY_E: [ecodes.KEY_3, True],
    ecodes.KEY_R: [ecodes.KEY_4, True],
    ecodes.KEY_T: [ecodes.KEY_5, True],
    ecodes.KEY_Y: [ecodes.KEY_6, True],
    ecodes.KEY_U: [ecodes.KEY_7, True],
    ecodes.KEY_I: [ecodes.KEY_8, True],
    ecodes.KEY_O: [ecodes.KEY_9, True],
    ecodes.KEY_P: [ecodes.KEY_0, True],

    ecodes.KEY_A: [ecodes.KEY_MINUS, True],
    ecodes.KEY_S: [ecodes.KEY_MINUS, False],
    ecodes.KEY_D: [ecodes.KEY_LEFTBRACE, False],
    ecodes.KEY_F: [ecodes.KEY_RIGHTBRACE, False],
    ecodes.KEY_G: [ecodes.KEY_APOSTROPHE, False],
    ecodes.KEY_H: [ecodes.KEY_APOSTROPHE, True],
    ecodes.KEY_J: [ecodes.KEY_LEFTBRACE, True],
    ecodes.KEY_K: [ecodes.KEY_RIGHTBRACE, True],
    ecodes.KEY_L: [ecodes.KEY_GRAVE, True],
    ecodes.KEY_SEMICOLON: [ecodes.KEY_SEMICOLON, True],

    #ecodes.KEY_Z: used for control mode!
    ecodes.KEY_X: [ecodes.KEY_GRAVE, False],
    ecodes.KEY_C: [ecodes.KEY_BACKSLASH, False],
    ecodes.KEY_V: [ecodes.KEY_EQUAL, False],
    ecodes.KEY_B: [ecodes.KEY_BACKSLASH, True],

    ecodes.KEY_N: [ecodes.KEY_EQUAL, True],
    ecodes.KEY_M: [ecodes.KEY_SPACE, False],
    ecodes.KEY_COMMA: [ecodes.KEY_COMMA, True],
    ecodes.KEY_DOT: [ecodes.KEY_DOT, True],
    ecodes.KEY_SLASH: [ecodes.KEY_SLASH, True],
  }

  def __init__(self):
    self.sink = UInput()
    self.reset_state()
    self.buffered_event = None

  def emit_with_space_mode(self, event):
    if event.event.scancode in self.__space_mode_map:
      translated_event = self.__space_mode_map[event.event.scancode]
      if translated_event[1]:
        self.sink.write(ecodes.EV_KEY, ecodes.KEY_LEFTSHIFT, 1)
        self.sink.write(ecodes.EV_KEY, ecodes.KEY_LEFTSHIFT, 2)
        self.sink.write(ecodes.EV_KEY, translated_event[0], 1)
        self.sink.write(ecodes.EV_KEY, translated_event[0], 0)
        self.sink.write(ecodes.EV_KEY, ecodes.KEY_LEFTSHIFT, 0)
      else:
        self.sink.write(ecodes.EV_KEY, translated_event[0], 1)
        self.sink.write(ecodes.EV_KEY, translated_event[0], 0)
    else:
      self.sink.write(ecodes.EV_KEY, event.event.scancode, 1)
      self.sink.write(ecodes.EV_KEY, event.event.scancode, 0)

  def emit_with_normal_mode(self, event):
    self.sink.write(ecodes.EV_KEY, event.event.scancode, event.event.keystate)

  def emit(self, event):
    if self.__space_mode and event.event.keystate == events.KeyEvent.key_down:
      self.emit_with_space_mode(event)
    if self.__control_mode and event.event.keystate == events.KeyEvent.key_down:
      self.emit_with_control_mode(event)
    else:
      self.emit_with_normal_mode(event)

    self.sink.syn()

  def emit_space(self):
    self.sink.write(ecodes.EV_KEY, ecodes.KEY_SPACE, 1)
    self.sink.write(ecodes.EV_KEY, ecodes.KEY_SPACE, 0)
    self.sink.syn()

  def emit_z(self):
    self.sink.write(ecodes.EV_KEY, ecodes.KEY_Z, 1)
    self.sink.write(ecodes.EV_KEY, ecodes.KEY_Z, 0)
    self.sink.syn()

  def emit_slash(self):
    self.sink.write(ecodes.EV_KEY, ecodes.KEY_SLASH, 1)
    self.sink.write(ecodes.EV_KEY, ecodes.KEY_SLASH, 0)
    self.sink.syn()

  def emit_as_buffered(self, event):
    self.buffered_event = event

  def emit_buffered(self):
    self.emit(self.buffered_event)
    self.buffered_event = None

  def buffer(self, event):
    self.emit_as_buffered(event)

  def flush(self):
    self.emit_buffered()

  def reset_state(self):
    self.__buffer = None
    self.__space_mode = False
    self.__control_mode = False
    self.__meta_mode = False
    self.__tenkey_mode = False
    self.__shift_mode = False

  def space_mode(self, flag):
    self.__space_mode = flag

  def control_mode(self, flag):
    self.__control_mode = flag

  def meta_mode(self, flag):
    self.__meta_mode = flag

  def shift_mode(self, flag):
    self.__shift_mode = flag

  def tenkey_mode(self, flag):
    self.__tenkey_mode = flag

  def close(self):
    self.sink.close()
   
k = K()
state = StateMachine(k)

source = InputDevice('/dev/input/event5')
source.grab()
print(source)

try:
  for source_event in source.read_loop():
    if source_event.type == ecodes.EV_KEY:
      key_event = categorize(source_event)
      #print(key_event)
      #print(key_event.keystate)
      #sink.write(ecodes.EV_KEY, ecodes.KEY_A, 1)
      #sink.write(ecodes.EV_KEY, ecodes.KEY_A, 0)
      #sink.syn()
      print(state.state_list())
      if key_event.keystate == events.KeyEvent.key_down:
        state.keydown(KeyDown(key_event))
      if key_event.keystate == events.KeyEvent.key_up:
        state.keyup(KeyUp(key_event))
finally:
  k.close()
