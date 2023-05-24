import cyberpi as c 
from cyberpi import mbot2 as m 
import time

def no(): 
    m.servo_set(70, 3)
    time.sleep(0.2)
    m.servo_set(120, 3)
    time.sleep(0.2)
    
def frente(): 
    m.servo_set(90,3)

@c.event.is_press("a")
def callback():
    c.broadcast("happy")
    for i in range(10):
        no()
        
@c.event.receive("happy")
def happy():
    for i in range(10):
        c.ultrasonic2.play("happy", 1)
    
@c.event.is_press("b")
def callback2(): 
    while True:
        m.servo_set(10, 3)
        time.sleep(1)
        m.servo_set(170, 3)
        time.sleep(1)

@c.event.is_press("up")
def callback3():
    frente()
    
    