/*
 * ex: set ro:
 * DO NOT EDIT.
 * generated by smc (http://smc.sourceforge.net/)
 * from file : satsuki.sm
 */

#ifndef _H_SATSUKI_SM
#define _H_SATSUKI_SM


#define SMC_USES_IOSTREAMS

#include <statemap.h>

namespace Turnstile
{
    // Forward declarations.
    class MainMap;
    class MainMap_Normal;
    class MainMap_Shift;
    class MainMap_Tenkey;
    class MainMap_PostSpace;
    class MainMap_NestedSpace;
    class MainMap_NestedZKeyControl;
    class MainMap_NestedSlashControl;
    class MainMap_PreSpace;
    class MainMap_Space;
    class MainMap_PreZKeyControl;
    class MainMap_PreSlashControl;
    class MainMap_SemiZKeyControl;
    class MainMap_SemiSlashControl;
    class MainMap_ZKeyControl;
    class MainMap_SlashControl;
    class MainMap_Default;
    class TurnstileState;
    class satsukiContext;
    class Turnstile;

    class TurnstileState :
        public statemap::State
    {
    public:

        TurnstileState(const char *name, int stateId)
        : statemap::State(name, stateId)
        {};

        virtual void Entry(satsukiContext&) {};
        virtual void Exit(satsukiContext&) {};

        virtual void keydown(satsukiContext& context, KeyEvent event);
        virtual void keyup(satsukiContext& context, KeyEvent event);

    protected:

        virtual void Default(satsukiContext& context);
    };

    class MainMap
    {
    public:

        static MainMap_Normal Normal;
        static MainMap_Shift Shift;
        static MainMap_Tenkey Tenkey;
        static MainMap_PostSpace PostSpace;
        static MainMap_NestedSpace NestedSpace;
        static MainMap_NestedZKeyControl NestedZKeyControl;
        static MainMap_NestedSlashControl NestedSlashControl;
        static MainMap_PreSpace PreSpace;
        static MainMap_Space Space;
        static MainMap_PreZKeyControl PreZKeyControl;
        static MainMap_PreSlashControl PreSlashControl;
        static MainMap_SemiZKeyControl SemiZKeyControl;
        static MainMap_SemiSlashControl SemiSlashControl;
        static MainMap_ZKeyControl ZKeyControl;
        static MainMap_SlashControl SlashControl;
    };

    class MainMap_Default :
        public TurnstileState
    {
    public:

        MainMap_Default(const char *name, int stateId)
        : TurnstileState(name, stateId)
        {};

    };

    class MainMap_Normal :
        public MainMap_Default
    {
    public:
        MainMap_Normal(const char *name, int stateId)
        : MainMap_Default(name, stateId)
        {};

        void keydown(satsukiContext& context, KeyEvent event);
    };

    class MainMap_Shift :
        public MainMap_Default
    {
    public:
        MainMap_Shift(const char *name, int stateId)
        : MainMap_Default(name, stateId)
        {};

        void Entry(satsukiContext&);
        void Exit(satsukiContext&);
        void keydown(satsukiContext& context, KeyEvent event);
        void keyup(satsukiContext& context, KeyEvent event);
    };

    class MainMap_Tenkey :
        public MainMap_Default
    {
    public:
        MainMap_Tenkey(const char *name, int stateId)
        : MainMap_Default(name, stateId)
        {};

        void Entry(satsukiContext&);
        void Exit(satsukiContext&);
        void keydown(satsukiContext& context, KeyEvent event);
        void keyup(satsukiContext& context, KeyEvent event);
    };

    class MainMap_PostSpace :
        public MainMap_Default
    {
    public:
        MainMap_PostSpace(const char *name, int stateId)
        : MainMap_Default(name, stateId)
        {};

        void keydown(satsukiContext& context, KeyEvent event);
        void keyup(satsukiContext& context, KeyEvent event);
    };

    class MainMap_NestedSpace :
        public MainMap_Default
    {
    public:
        MainMap_NestedSpace(const char *name, int stateId)
        : MainMap_Default(name, stateId)
        {};

        void Entry(satsukiContext&);
        void Exit(satsukiContext&);
        void keydown(satsukiContext& context, KeyEvent event);
        void keyup(satsukiContext& context, KeyEvent event);
    };

    class MainMap_NestedZKeyControl :
        public MainMap_Default
    {
    public:
        MainMap_NestedZKeyControl(const char *name, int stateId)
        : MainMap_Default(name, stateId)
        {};

        void Entry(satsukiContext&);
        void Exit(satsukiContext&);
        void keydown(satsukiContext& context, KeyEvent event);
        void keyup(satsukiContext& context, KeyEvent event);
    };

    class MainMap_NestedSlashControl :
        public MainMap_Default
    {
    public:
        MainMap_NestedSlashControl(const char *name, int stateId)
        : MainMap_Default(name, stateId)
        {};

        void Entry(satsukiContext&);
        void Exit(satsukiContext&);
        void keydown(satsukiContext& context, KeyEvent event);
        void keyup(satsukiContext& context, KeyEvent event);
    };

    class MainMap_PreSpace :
        public MainMap_Default
    {
    public:
        MainMap_PreSpace(const char *name, int stateId)
        : MainMap_Default(name, stateId)
        {};

        void keydown(satsukiContext& context, KeyEvent event);
        void keyup(satsukiContext& context, KeyEvent event);
    };

    class MainMap_Space :
        public MainMap_Default
    {
    public:
        MainMap_Space(const char *name, int stateId)
        : MainMap_Default(name, stateId)
        {};

        void Entry(satsukiContext&);
        void Exit(satsukiContext&);
        void keydown(satsukiContext& context, KeyEvent event);
        void keyup(satsukiContext& context, KeyEvent event);
    };

    class MainMap_PreZKeyControl :
        public MainMap_Default
    {
    public:
        MainMap_PreZKeyControl(const char *name, int stateId)
        : MainMap_Default(name, stateId)
        {};

        void keydown(satsukiContext& context, KeyEvent event);
        void keyup(satsukiContext& context, KeyEvent event);
    };

    class MainMap_PreSlashControl :
        public MainMap_Default
    {
    public:
        MainMap_PreSlashControl(const char *name, int stateId)
        : MainMap_Default(name, stateId)
        {};

        void keydown(satsukiContext& context, KeyEvent event);
        void keyup(satsukiContext& context, KeyEvent event);
    };

    class MainMap_SemiZKeyControl :
        public MainMap_Default
    {
    public:
        MainMap_SemiZKeyControl(const char *name, int stateId)
        : MainMap_Default(name, stateId)
        {};

        void keydown(satsukiContext& context, KeyEvent event);
        void keyup(satsukiContext& context, KeyEvent event);
    };

    class MainMap_SemiSlashControl :
        public MainMap_Default
    {
    public:
        MainMap_SemiSlashControl(const char *name, int stateId)
        : MainMap_Default(name, stateId)
        {};

        void keydown(satsukiContext& context, KeyEvent event);
        void keyup(satsukiContext& context, KeyEvent event);
    };

    class MainMap_ZKeyControl :
        public MainMap_Default
    {
    public:
        MainMap_ZKeyControl(const char *name, int stateId)
        : MainMap_Default(name, stateId)
        {};

        void Entry(satsukiContext&);
        void Exit(satsukiContext&);
        void keydown(satsukiContext& context, KeyEvent event);
        void keyup(satsukiContext& context, KeyEvent event);
    };

    class MainMap_SlashControl :
        public MainMap_Default
    {
    public:
        MainMap_SlashControl(const char *name, int stateId)
        : MainMap_Default(name, stateId)
        {};

        void Entry(satsukiContext&);
        void Exit(satsukiContext&);
        void keydown(satsukiContext& context, KeyEvent event);
        void keyup(satsukiContext& context, KeyEvent event);
    };

    class satsukiContext :
        public statemap::FSMContext
    {
    public:

        satsukiContext(Turnstile& owner)
        : FSMContext(MainMap::Normal),
          _owner(owner)
        {};

        satsukiContext(Turnstile& owner, const statemap::State& state)
        : FSMContext(state),
          _owner(owner)
        {};

        virtual void enterStartState()
        {
            getState().Entry(*this);
            return;
        }

        Turnstile& getOwner() const
        {
            return (_owner);
        };

        TurnstileState& getState() const
        {
            if (_state == NULL)
            {
                throw statemap::StateUndefinedException();
            }

            return (dynamic_cast<TurnstileState&>(*_state));
        };

        void keydown(KeyEvent event)
        {
            (getState()).keydown(*this, event);
        };

        void keyup(KeyEvent event)
        {
            (getState()).keyup(*this, event);
        };

    private:

        Turnstile& _owner;
    };
}


#endif // _H_SATSUKI_SM

/*
 * Local variables:
 *  buffer-read-only: t
 * End:
 */
