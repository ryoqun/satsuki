  struct KeyEvent {
    char *name;
  };

#define True true
#define False false

namespace Turnstile {
  struct Turnstile {
    void buffer(KeyEvent) {};
    void flush() {};
    void emit(KeyEvent) {};
    void emit_z() {};
    void emit_space() {};
    void emit_slash() {};
    void space_mode(bool flag) {};
    void control_mode(bool flag) {};
    void shift_mode(bool flag) {};
    void tenkey_mode(bool flag) {};
  };
};
