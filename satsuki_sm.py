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
        if  event.is_space  :
            # No actions.
            pass
            fsm.pushState(MainMap.PreSpace)
            fsm.getState().Entry(fsm)
        elif  event.is_slash  :
            # No actions.
            pass
            fsm.pushState(MainMap.PreSlashControl)
            fsm.getState().Entry(fsm)
        elif  event.is_z  :
            # No actions.
            pass
            fsm.pushState(MainMap.PreZKeyControl)
            fsm.getState().Entry(fsm)
        elif  event.is_shift  :
            # No actions.
            pass
            fsm.pushState(MainMap.Shift)
            fsm.getState().Entry(fsm)
        elif  event.is_tenkey  :
            # No actions.
            pass
            fsm.pushState(MainMap.Tenkey)
            fsm.getState().Entry(fsm)
        else:
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.emit(event)
            finally:
                fsm.setState(endState)


class MainMap_Shift(MainMap_Default):

    def Entry(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.shift_mode(True)

    def Exit(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.shift_mode(False)

    def keydown(self, fsm, event):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.emit(event)
        finally:
            fsm.setState(endState)

    def keyup(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.is_shift  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.popState()
        else:
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.emit(event)
            finally:
                fsm.setState(endState)


class MainMap_Tenkey(MainMap_Default):

    def Entry(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.tenkey_mode(True)

    def Exit(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.tenkey_mode(False)

    def keydown(self, fsm, event):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.emit(event)
        finally:
            fsm.setState(endState)

    def keyup(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.is_tenkey  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.popState()
        else:
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.emit(event)
            finally:
                fsm.setState(endState)


class MainMap_PostSpace(MainMap_Default):

    def keydown(self, fsm, event):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.emit(event)
        finally:
            fsm.setState(endState)

    def keyup(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.is_space  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.pop_state()
            finally:
                fsm.popState()
        else:
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.emit(event)
            finally:
                fsm.setState(endState)


class MainMap_NestedSpace(MainMap_Default):

    def Entry(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.space_mode(True)

    def Exit(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.space_mode(False)

    def keydown(self, fsm, event):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.emit(event)
        finally:
            fsm.setState(endState)

    def keyup(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.is_space  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.pop_state()
            finally:
                fsm.popState()
        else:
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.emit(event)
            finally:
                fsm.setState(endState)


class MainMap_NestedZKeyControl(MainMap_Default):

    def Entry(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.control_mode(True)

    def Exit(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.control_mode(False)

    def keydown(self, fsm, event):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.emit(event)
        finally:
            fsm.setState(endState)

    def keyup(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.is_z  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.pop_state()
            finally:
                fsm.popState()
        else:
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.emit(event)
            finally:
                fsm.setState(endState)


class MainMap_PostSlashControl(MainMap_Default):

    def keydown(self, fsm, event):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.emit(event)
        finally:
            fsm.setState(endState)

    def keyup(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.is_slash  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.pop_state()
            finally:
                fsm.popState()
        else:
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.emit(event)
            finally:
                fsm.setState(endState)


class MainMap_PreSpace(MainMap_Default):

    def keydown(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.is_slash  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(MainMap.Space)
            fsm.getState().Entry(fsm)
            fsm.pushState(MainMap.PreSlashControl)
            fsm.getState().Entry(fsm)
        elif  event.is_z  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(MainMap.Space)
            fsm.getState().Entry(fsm)
            fsm.pushState(MainMap.PreZKeyControl)
            fsm.getState().Entry(fsm)
        elif  event.is_space  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(MainMap.Space)
            fsm.getState().Entry(fsm)
        else:
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.space_mode(True)
                ctxt.emit(event)
            finally:
                fsm.setState(MainMap.Space)
                fsm.getState().Entry(fsm)


    def keyup(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.is_space  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.emit_space()
            finally:
                fsm.popState()
        elif  event.is_slash  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.emit_slash()
            finally:
                fsm.setState(MainMap.PostSpace)
                fsm.getState().Entry(fsm)
        elif  event.is_z  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.emit_z()
            finally:
                fsm.setState(MainMap.PostSpace)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.keyup(self, fsm, event)
        
class MainMap_Space(MainMap_Default):

    def Entry(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.space_mode(True)

    def Exit(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.space_mode(False)

    def keydown(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.is_slash  :
            # No actions.
            pass
            fsm.pushState(MainMap.PreSlashControl)
            fsm.getState().Entry(fsm)
        elif  event.is_z  :
            # No actions.
            pass
            fsm.pushState(MainMap.PreZKeyControl)
            fsm.getState().Entry(fsm)
        elif  event.is_space  :
            # No actions.
            pass
        else:
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.emit(event)
            finally:
                fsm.setState(endState)


    def keyup(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.is_space  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.popState()
        elif  event.is_slash  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(MainMap.NestedSpace)
            fsm.getState().Entry(fsm)
        elif  event.is_z  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(MainMap.NestedSpace)
            fsm.getState().Entry(fsm)
        else:
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.emit(event)
            finally:
                fsm.setState(endState)


class MainMap_PreZKeyControl(MainMap_Default):

    def keydown(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.is_z  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(MainMap.ZKeyControl)
            fsm.getState().Entry(fsm)
        elif  event.is_space  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(MainMap.ZKeyControl)
            fsm.getState().Entry(fsm)
            fsm.pushState(MainMap.PreSpace)
            fsm.getState().Entry(fsm)
        else:
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.buffer(event)
            finally:
                fsm.setState(MainMap.SemiZKeyControl)
                fsm.getState().Entry(fsm)


    def keyup(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.is_z  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.emit_z()
            finally:
                fsm.popState()
        else:
            MainMap_Default.keyup(self, fsm, event)
        
class MainMap_PreSlashControl(MainMap_Default):

    def keydown(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.is_slash  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(MainMap.SlashControl)
            fsm.getState().Entry(fsm)
        elif  event.is_space  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(MainMap.SlashControl)
            fsm.getState().Entry(fsm)
            fsm.pushState(MainMap.PreSpace)
            fsm.getState().Entry(fsm)
        else:
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.buffer(event)
            finally:
                fsm.setState(MainMap.SemiSlashControl)
                fsm.getState().Entry(fsm)


    def keyup(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.is_slash  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.emit_slash()
            finally:
                fsm.popState()
        else:
            MainMap_Default.keyup(self, fsm, event)
        
class MainMap_SemiZKeyControl(MainMap_Default):

    def keydown(self, fsm, event):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.control_mode(True)
            ctxt.flush()
            ctxt.emit(event)
        finally:
            fsm.setState(MainMap.ZKeyControl)
            fsm.getState().Entry(fsm)

    def keyup(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.is_z  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.emit_z()
                ctxt.flush()
                ctxt.emit(event)
            finally:
                fsm.popState()
        else:
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.control_mode(True)
                ctxt.flush()
                ctxt.emit(event)
            finally:
                fsm.setState(MainMap.ZKeyControl)
                fsm.getState().Entry(fsm)


class MainMap_SemiSlashControl(MainMap_Default):

    def keydown(self, fsm, event):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.control_mode(True)
            ctxt.flush()
            ctxt.emit(event)
        finally:
            fsm.setState(MainMap.SlashControl)
            fsm.getState().Entry(fsm)

    def keyup(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.is_slash  :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.emit_slash()
                ctxt.flush()
                ctxt.emit(event)
            finally:
                fsm.popState()
        else:
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.control_mode(True)
                ctxt.flush()
                ctxt.emit(event)
            finally:
                fsm.setState(MainMap.SlashControl)
                fsm.getState().Entry(fsm)


class MainMap_ZKeyControl(MainMap_Default):

    def Entry(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.control_mode(True)

    def Exit(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.control_mode(False)

    def keydown(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.is_z  :
            # No actions.
            pass
        elif  event.is_space  :
            # No actions.
            pass
            fsm.pushState(MainMap.PreSpace)
            fsm.getState().Entry(fsm)
        else:
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.emit(event)
            finally:
                fsm.setState(endState)


    def keyup(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.is_z  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.popState()
        elif  event.is_space  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(MainMap.NestedZKeyControl)
            fsm.getState().Entry(fsm)
        else:
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.emit(event)
            finally:
                fsm.setState(endState)


class MainMap_SlashControl(MainMap_Default):

    def Entry(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.control_mode(True)

    def Exit(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.control_mode(False)

    def keydown(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.is_slash  :
            # No actions.
            pass
        else:
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.emit(event)
            finally:
                fsm.setState(endState)


    def keyup(self, fsm, event):
        ctxt = fsm.getOwner()
        if  event.is_slash  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.popState()
        elif  event.is_space  :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(MainMap.PostSlashControl)
            fsm.getState().Entry(fsm)
        else:
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.emit(event)
            finally:
                fsm.setState(endState)


class MainMap(object):

    Normal = MainMap_Normal('MainMap.Normal', 0)
    Shift = MainMap_Shift('MainMap.Shift', 1)
    Tenkey = MainMap_Tenkey('MainMap.Tenkey', 2)
    PostSpace = MainMap_PostSpace('MainMap.PostSpace', 3)
    NestedSpace = MainMap_NestedSpace('MainMap.NestedSpace', 4)
    NestedZKeyControl = MainMap_NestedZKeyControl('MainMap.NestedZKeyControl', 5)
    PostSlashControl = MainMap_PostSlashControl('MainMap.PostSlashControl', 6)
    PreSpace = MainMap_PreSpace('MainMap.PreSpace', 7)
    Space = MainMap_Space('MainMap.Space', 8)
    PreZKeyControl = MainMap_PreZKeyControl('MainMap.PreZKeyControl', 9)
    PreSlashControl = MainMap_PreSlashControl('MainMap.PreSlashControl', 10)
    SemiZKeyControl = MainMap_SemiZKeyControl('MainMap.SemiZKeyControl', 11)
    SemiSlashControl = MainMap_SemiSlashControl('MainMap.SemiSlashControl', 12)
    ZKeyControl = MainMap_ZKeyControl('MainMap.ZKeyControl', 13)
    SlashControl = MainMap_SlashControl('MainMap.SlashControl', 14)
    Default = MainMap_Default('MainMap.Default', -1)

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
