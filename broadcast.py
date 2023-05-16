import cyberpi 
from cyberpi import mbot2 as m 
import time 

@cyberpi.event.start
def callback(): 
    cyberpi.console.println("hola")
    while True: 
        cyberpi.broadcast("a")

@cyberpi.event.receive("a")
def callback2():
    cyberpi.console.println("recibido")
