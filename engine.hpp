struct KeyEvent {
  bool is_space, is_slash, is_z, is_tenkey, is_shift;
};

#define KEY_SPACE 0
#define KEY_SLASH 1
#define KEY_Z 2
#define KEY_SHIFT 3
#define KEY_TENKEY 4
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
