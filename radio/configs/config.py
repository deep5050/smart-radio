from threading import Event
global ctrl_c_exit

def init():
    global ctrl_c_exit
    ctrl_c_exit = Event()