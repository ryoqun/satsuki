from evdev import InputDevice, UInput, categorize, ecodes

source = InputDevice('/dev/input/event5')
sink = UInput()
print(source)
source.grab()
for event in source.read_loop():
  if event.type == ecodes.EV_KEY:
    print(categorize(event))
    sink.write(ecodes.EV_KEY, ecodes.KEY_A, 1)
    sink.write(ecodes.EV_KEY, ecodes.KEY_A, 0)
    sink.syn()
