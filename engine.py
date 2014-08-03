# vim:set et sts=4 sw=4:
#
# satsuki - The Input Bus satsuki Engine
#
# Copyright (c) 2007-2011 Peng Huang <shawn.p.huang@gmail.com>
# Copyright (c) 2011 Ryo Onodera <ryoqun@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

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
    if self.keyval == keysyms.space:
      self.name = "space"
    elif self.keyval == keysyms.slash:
      self.name = "slash"
    elif self.keyval == keysyms.z:
      self.name = "z"
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
      self.__space_mode = False
      self.__space_mode_used = False
      self.__control_mode = False
      self.__control_mode_used = False
      self.__tenkey_mode = False
      self.__shift_mode = False
      self.__state = StateMachine(self)
      #print "aaaaa"

  def convert_and_emit(self, event):
    #print self.__state.getState()
    print "convderrt"
    print event.name
    print event.keyval
    print event.keycode
    print event.state
    #print event
    if self.__space_mode:
      result = self.__space_mode_map[chr(event.keyval)]
      state = 0
      if self.__is_pressed(state):
        state = result[2]
      else:
        state = result[2] | 1073741824
      event.keyval = result[0]
      event.keycode = result[1]
      event.state = state

    if self.__control_mode:
      event.state = event.state | modifier.CONTROL_MASK

    self.emit(event)

  def emit_space(self):
    self.emit(KeyDown(keysyms.space, 57, 0))
    self.emit(KeyUp(keysyms.space, 57, modifier.RELEASE_MASK))

  def emit_z(self):
    self.emit(KeyDown(keysyms.z, 44, 0))
    self.emit(KeyUp(keysyms.z, 44, modifier.RELEASE_MASK))

  def emit_slash(self):
    self.emit(KeyDown(keysyms.slash, 53, 0))
    self.emit(KeyUp(keysyms.slash, 53, modifier.RELEASE_MASK))

  def emit_control_down(self):
    pass

  def emit_control_up(self):
    pass

  def emit(self, event):
    print "emit"
    self.__forward_key_event(event.keyval, event.keycode, event.state)

  def space_mode(self, flag):
    self.__space_mode = flag

  def control_mode(self, flag):
    self.__control_mode = flag

  def process_key_event(self, keyval, keycode, state):
      try:
        #print "before"
        #print keyval
        #print keycode
        #print state
        #print "end"
        print self.__state.getState()
        if self.__is_pressed(state):
          self.__state.keydown(KeyDown(keyval, keycode, state))
        else:
          self.__state.keyup(KeyUp(keyval, keycode, state))

        #processed = self.__update_space_mode(keyval, keycode, state)
        #if processed:
        #  return True

        #processed = self.__update_control_mode(keyval, keycode, state)
        #if processed:
        #  return True

        processed = self.__update_tenkey_mode(keyval, keycode, state)
        if processed:
          return True

        processed = self.__update_shift_mode(keyval, keycode, state)
        if processed:
          return True

        #if self.__space_mode:
        #  self.__forward_space_mode_key_event(keyval, keycode, state)
        #  return True

        #if self.__control_mode:
        #  self.__forward_control_mode_key_event(keyval, keycode, state)
        #  return True

        if self.__tenkey_mode:
          self.__forward_tenkey_mode_key_event(keyval, keycode, state)
          return True

        if self.__shift_mode:
          self.__forward_shift_mode_key_event(keyval, keycode, state)
          return True

      except Exception as exception:
        print exception

      return True

  def __update_tenkey_mode(self, keyval, keycode, state):
    if keyval == 65314 or keyval == 65332:
      if self.__is_pressed(state):
        self.__tenkey_mode = True
      else:
        self.__tenkey_mode = False

      return True

  def __update_shift_mode(self, keyval, keycode, state):
    if keyval == 65315 or keyval == 65329:
      if self.__is_pressed(state):
        self.__shift_mode = True
      else:
        self.__shift_mode = False

      return True

  def __update_space_mode(self, keyval, keycode, state):
    if keyval == keysyms.space:
      if self.__is_pressed(state):
        #if self.__space_mode:
        #  return False
        #else:
        #  self.__space_mode = True
        #  return True
        #self.__space_mode = True
        return True
      else:
        space_mode_used = self.__space_mode_used
        #self.__space_mode = False
        self.__space_mode_used = False

        if space_mode_used:
          processed = True
        else:
          self.__forward_key_event(keysyms.space, 57, 0)
          processed = False

        return processed

  def __update_control_mode(self, keyval, keycode, state):
    if keyval == keysyms.slash or keyval == keysyms.z:
      if self.__is_pressed(state):
        if not self.__shift_mode and not self.__space_mode and not self.__control_mode:
          self.__control_mode = True
          self.__control_mode_trigger_key = [keyval, keycode, state]
          return True
        if self.__control_mode and keyval == self.__control_mode_trigger_key[0]:
          return True
      else:
        if self.__control_mode and keyval == self.__control_mode_trigger_key[0]:
          control_mode_used = self.__control_mode_used
          self.__control_mode = False
          self.__control_mode_used = False

          if control_mode_used:
            processed = True
          else:
            key = self.__control_mode_trigger_key
            self.__forward_key_event(key[0], key[1], key[2])
            processed = False

          return processed


  def __is_pressed(self, state):
    return ((state & modifier.RELEASE_MASK) == 0)

  def __forward_space_mode_key_event(self, keyval, keycode, state):
    event = self.__space_mode_map[chr(keyval)]
    if self.__is_pressed(state):
      self.__space_mode_used = True
      state = event[2]
    else:
      state = event[2] | 1073741824

    if self.__control_mode:
      self.__control_mode_used = True
      state = state | modifier.CONTROL_MASK

    self.__forward_key_event(event[0], event[1], state)

  def __forward_tenkey_mode_key_event(self, keyval, keycode, state):
    event = self.__tenkey_mode_map[chr(keyval)]
    if self.__is_pressed(state):
      state = event[2]
    else:
      state = event[2] | 1073741824

    if self.__control_mode:
      self.__control_mode_used = True
      state = state | modifier.CONTROL_MASK

    self.__forward_key_event(event[0], event[1], state)

  def __forward_shift_mode_key_event(self, keyval, keycode, state):
    keyval = ord(chr(keyval).upper())
    state = state | 1
    self.__forward_key_event(keyval, keycode, state)

  def __forward_control_mode_key_event(self, keyval, keycode, state):
    self.__control_mode_used = True
    state = state | modifier.CONTROL_MASK
    self.__forward_key_event(keyval, keycode, state)

  def __forward_key_event(self, keyval, keycode, state):
    self.forward_key_event(keyval, keycode, state)
