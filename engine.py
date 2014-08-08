import gobject
import pango
import ibus
from ibus import keysyms
from ibus import modifier
import statemap
import satsuki_sm

class KeyEvent:
  def __init__(self, keyval, keycode, state):
    self.keyval = keyval
    self.keycode = keycode
    self.state = state
    self.is_space = self.is_slash = self.is_z = self.is_tenkey = self.is_shift = False
    if self.keyval == keysyms.space:
      self.name = "space"
      self.is_space = True
    elif self.keyval == keysyms.slash:
      self.name = "slash"
      self.is_slash = True
    elif self.keyval == keysyms.z:
      self.name = "z"
      self.is_z = True
    elif keyval == 65315 or keyval == 65329:
      self.name = "shift"
      self.is_shift = True
    elif keyval == 65314 or keyval == 65332:
      self.name = "tenkey"
      self.is_tenkey = True
    else:
      self.name = "none"

class KeyDown(KeyEvent):
  pass

class KeyUp(KeyEvent):
  pass

class StateMachine(satsuki_sm.Turnstile_sm):
  pass

class Engine(ibus.EngineBase):
  __tenkey_mode_map = {
    'q': [ord('1'),   2, 0],
    'w': [ord('2'),   3, 0],
    'e': [ord('3'),   4, 0],
    'r': [ord('4'),   5, 0],
    't': [ord('5'),   6, 0],
    'y': [ord('6'),   7, 0],
    'u': [ord('7'),   8, 0],
    'i': [ord('8'),   9, 0],
    'o': [ord('9'),  10, 0],
    'p': [ord('0'),  11, 0],

    'a': [65289,     15, 0], # tab
    's': [65535,    111, 0], # delete
    'd': [65288,     14, 0], # backspace
    'f': [65307,      1, 0],
    # 'g': unmapped
    'h': [65361,    105, 0],
    'j': [65364,    108, 0],
    'k': [65362,    103, 0],
    'l': [65363,    106, 0],
    ';': [65293,     28, 0],
  }

  __space_mode_map = {
    'q': [ord('!'),   2, 1],
    'w': [ord('@'),   3, 1],
    'e': [ord('#'),   4, 1],
    'r': [ord('$'),   5, 1],
    't': [ord('%'),   6, 1],
    'y': [ord('^'),   7, 1],
    'u': [ord('&'),   8, 1],
    'i': [ord('*'),   9, 1],
    'o': [ord('('),  10, 1],
    'p': [ord(')'),  11, 1],

    'a': [ord('_'),  12, 1],
    's': [ord('-'),  12, 0],
    'd': [ord('['),  26, 0],
    'f': [ord(']'),  27, 0],
    'g': [ord('\''), 43, 0],
    'h': [ord('"'),  40, 1],
    'j': [ord('{'),  26, 1],
    'k': [ord('}'),  27, 1],
    'l': [ord('~'),  41, 1],
    ';': [ord(':'),  39, 1],

    'x': [ord('`'),  41, 0],
    'c': [ord('\\'), 43, 0],
    'v': [ord('='),  13, 0],
    'b': [ord('|'),  43, 1],
    'n': [ord('+'),  13, 1],
    'm': [ord(' '),  57, 0],
    ',': [ord('<'),  51, 1],
    '.': [ord('>'),  52, 1],
    '/': [ord('?'),  53, 1],
  }

  def __init__(self, bus, object_path):
      super(Engine, self).__init__(bus, object_path)
      self.__state = StateMachine(self)
      self.reset_state()

  def reset_state(self):
    self.__buffer = None
    self.__space_mode = False
    self.__control_mode = False
    self.__tenkey_mode = False
    self.__shift_mode = False

  def emit(self, event):
    #print self.__state.getState()
    #print event
    print "space: " + str(self.__space_mode) + ", tenkey: " + str(self.__tenkey_mode) + ", shift: " + str(self.__shift_mode) + ", control: " + str(self.__control_mode)
    if self.__space_mode:
      result = self.__space_mode_map[chr(event.keyval)]
      event.keyval = result[0]
      event.keycode = result[1]

    if self.__tenkey_mode:
      result = self.__tenkey_mode_map[chr(event.keyval)]
      event.keyval = result[0]
      event.keycode = result[1]

    if self.__shift_mode:
      event.keyval = ord(chr(event.keyval).upper())
      event.state = event.state | 1

    if self.__control_mode:
      event.state = event.state | modifier.CONTROL_MASK

    if not self.__is_pressed(event.state):
      event.state = event.state | 1073741824

    self.do_emit(event)

  def emit_space(self):
    self.do_emit(KeyDown(keysyms.space, 57, 0))
    self.do_emit(KeyUp(keysyms.space, 57, modifier.RELEASE_MASK))

  def emit_z(self):
    self.do_emit(KeyDown(keysyms.z, 44, 0))
    self.do_emit(KeyUp(keysyms.z, 44, modifier.RELEASE_MASK))

  def emit_slash(self):
    self.do_emit(KeyDown(keysyms.slash, 53, 0))
    self.do_emit(KeyUp(keysyms.slash, 53, modifier.RELEASE_MASK))

  def emit_control_down(self):
    pass

  def emit_control_up(self):
    pass

  def buffer(self, event):
    self.__buffer = event

  def flush(self):
    if self.__buffer:
      self.emit(self.__buffer)
    self.__buffer = None

  def do_emit(self, event):
    print "emit"
    print "name: " + str(event.name) + " keyval: " + str(event.keyval) + " keycode: " + str(event.keycode) + " state: " + str(event.state)
    self.__forward_key_event(event.keyval, event.keycode, event.state)

  def space_mode(self, flag):
    self.__space_mode = flag

  def control_mode(self, flag):
    self.__control_mode = flag

  def shift_mode(self, flag):
    self.__shift_mode = flag

  def tenkey_mode(self, flag):
    self.__tenkey_mode = flag

  def process_key_event(self, keyval, keycode, state):
    print "aaa"
    try:
      if keyval == 0 and keycode == 89:
        self.reset_state()

      if self.__is_pressed(state):
        self.__state.keydown(KeyDown(keyval, keycode, state))
      else:
        self.__state.keyup(KeyUp(keyval, keycode, state))

    except Exception as exception:
      print exception

    return True

  def __is_pressed(self, state):
    return ((state & modifier.RELEASE_MASK) == 0)

  def __forward_key_event(self, keyval, keycode, state):
    self.forward_key_event(keyval, keycode, state)
