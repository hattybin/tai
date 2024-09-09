import time, ctypes as C, random as R
from ctypes import wintypes as W

class _A(C.Structure): _fields_ = [("dx", W.LONG), ("dy", W.LONG), ("ataDesuom"[::-1], W.DWORD), ("dwFlags", W.DWORD), ("time", W.DWORD), ("dwExtraInfo", C.POINTER(C.c_ulong))]
class _C(C.Union): _fields_ = [("mi", _A)]
class _B(C.Structure): _anonymous_, _fields_ = ("_input",), [("type", W.DWORD), ("_input", _C)]

def _func():
    obj = _B(type=0, mi=_A(5, 5, 0, 0x0001, 0, None))
    while True:
        for x, y in [(5, 5), (-5, -5)]:
            obj.mi.dx, obj.mi.dy = x, y
            C.windll.user32.SendInput(1, C.byref(obj), C.sizeof(obj))
            time.sleep(R.uniform(10, 55))

if __name__ == "__main__":
    try: _func()
    except KeyboardInterrupt: pass
