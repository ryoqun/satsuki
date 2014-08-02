# ex: set ro:
# DO NOT EDIT.
# generated by smc (http://smc.sourceforge.net/)
# from file : satsuki.sm

import statemap


class TurnstileState(statemap.State):

    def Entry(self, fsm):
        pass

    def Exit(self, fsm):
        pass

    def keydown(self, fsm, event):
        self.Default(fsm)

    def keyup(self, fsm, event):
        self.Default(fsm)

    def Default(self, fsm):
        msg = "\n\tState: %s\n\tTransition: %s" % (
            fsm.getState().getName(), fsm.getTransition())
        raise statemap.TransitionUndefinedException, msg

class MainMap_Default(TurnstileState):
    pass

class MainMap_Normal(MainMap_Default):

    def keydown(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.name == "space"  :
            # No actions.
            pass
            fsm.pushState(SpaceMap.PreSpace)
            fsm.getState().Entry(fsm)
        elif  event.name == "slash"  :
            # No actions.
            pass
            fsm.pushState(ControlMap.PreSlashControl)
            fsm.getState().Entry(fsm)
        elif  event.name == "z"  :
            # No actions.
            pass
            fsm.pushState(ControlMap.PreZKeyControl)
            fsm.getState().Entry(fsm)
        else:
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.convert_and_emit(event)
            finally:
                fsm.setState(endState)


class MainMap(object):

    Normal = MainMap_Normal('MainMap.Normal', 0)
    Default = MainMap_Default('MainMap.Default', -1)

class SpaceMap_Default(TurnstileState):
    pass

class SpaceMap_PreSpace(SpaceMap_Default):

    def keydown(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.name == "slash"  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(SpaceMap.Space)
            fsm.getState().Entry(fsm)
            fsm.pushState(ControlMap.PreSlashControl)
            fsm.getState().Entry(fsm)
        elif  event.name == "z"  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(SpaceMap.Space)
            fsm.getState().Entry(fsm)
            fsm.pushState(ControlMap.PreZKeyControl)
            fsm.getState().Entry(fsm)
        elif  event.name == "space"  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(SpaceMap.Space)
            fsm.getState().Entry(fsm)
        else:
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.space_mode(True)
                ctxt.convert_and_emit(event)
            finally:
                fsm.setState(SpaceMap.Space)
                fsm.getState().Entry(fsm)


    def keyup(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.name == "space"  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.emit_space()
            finally:
                fsm.popState()
        else:
            SpaceMap_Default.keyup(self, fsm, event)
        
class SpaceMap_Space(SpaceMap_Default):

    def Entry(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.space_mode(True)

    def Exit(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.space_mode(False)

    def keydown(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.name == "slash"  :
            # No actions.
            pass
            fsm.pushState(ControlMap.PreSlashControl)
            fsm.getState().Entry(fsm)
        elif  event.name == "z"  :
            # No actions.
            pass
            fsm.pushState(ControlMap.PreZKeyControl)
            fsm.getState().Entry(fsm)
        else:
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.convert_and_emit(event)
            finally:
                fsm.setState(endState)


    def keyup(self, fsm, event):
        if  event.name == "space"  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.popState()
        else:
            # No actions.
            pass


class SpaceMap(object):

    PreSpace = SpaceMap_PreSpace('SpaceMap.PreSpace', 1)
    Space = SpaceMap_Space('SpaceMap.Space', 2)
    Default = SpaceMap_Default('SpaceMap.Default', -1)

class ShiftMap_Default(TurnstileState):
    pass

class ShiftMap(object):

    Default = ShiftMap_Default('ShiftMap.Default', -1)

class NumMap_Default(TurnstileState):
    pass

class NumMap(object):

    Default = NumMap_Default('NumMap.Default', -1)

class ControlMap_Default(TurnstileState):
    pass

class ControlMap_PreSlashControl(ControlMap_Default):

    def keydown(self, fsm, event):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.emit_control(event)
        finally:
            fsm.setState(ControlMap.SlashControl)
            fsm.getState().Entry(fsm)

    def keyup(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.name == "slash"  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.convert_and_emit(event)
            finally:
                fsm.popState()
        else:
            ControlMap_Default.keyup(self, fsm, event)
        
class ControlMap_PreZKeyControl(ControlMap_Default):

    def keydown(self, fsm, event):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.emit_control(event)
        finally:
            fsm.setState(ControlMap.ZKeyControl)
            fsm.getState().Entry(fsm)

    def keyup(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.name == "z"  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.convert_and_emit(event)
            finally:
                fsm.popState()
        else:
            ControlMap_Default.keyup(self, fsm, event)
        
class ControlMap_ZKeyControl(ControlMap_Default):

    def keyup(self, fsm, event):
        if  event.name == "z"  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.popState()
        else:
            ControlMap_Default.keyup(self, fsm, event)
        
class ControlMap_SlashControl(ControlMap_Default):

    def keyup(self, fsm, event):
        if  event.name == "slash"  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.popState()
        else:
            ControlMap_Default.keyup(self, fsm, event)
        
class ControlMap(object):

    PreSlashControl = ControlMap_PreSlashControl('ControlMap.PreSlashControl', 3)
    PreZKeyControl = ControlMap_PreZKeyControl('ControlMap.PreZKeyControl', 4)
    ZKeyControl = ControlMap_ZKeyControl('ControlMap.ZKeyControl', 5)
    SlashControl = ControlMap_SlashControl('ControlMap.SlashControl', 6)
    Default = ControlMap_Default('ControlMap.Default', -1)

class Turnstile_sm(statemap.FSMContext):

    def __init__(self, owner):
        statemap.FSMContext.__init__(self, MainMap.Normal)
        self._owner = owner

    def __getattr__(self, attrib):
        def trans_sm(*arglist):
            self._transition = attrib
            getattr(self.getState(), attrib)(self, *arglist)
            self._transition = None
        return trans_sm

    def enterStartState(self):
        self._state.Entry(self)

    def getOwner(self):
        return self._owner

# Local variables:
#  buffer-read-only: t
# End:
