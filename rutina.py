import cyberpi 
from cyberpi import mbot2 as m 
import time 


velocidad_giro = 150
velocidad_giro_rapido = 160
velocidad_avanzar = 50
velocidad_retroceso = 50

#lista de estádos del sensor de color.
izquierda = [3,7,11]
derecha = [14,13,12]
medio = [0,1,2,4,5,6,8,9,10]

def seguidor_lineas():
    estado_linea = cyberpi.quad_rgb_sensor.get_line_sta(1)
    #si el sensor está viendo solo una linea a la izquierda 
    if estado_linea in izquierda: 
        cyberpi.mbot2.EM_set_speed(-velocidad_giro, "em2")
        cyberpi.mbot2.EM_set_speed(velocidad_avanzar, "em1")
    #si el sensor está viendo solo al medio 
    elif estado_linea in medio: 
        cyberpi.mbot2.EM_set_speed(velocidad_avanzar, "em1")
        cyberpi.mbot2.EM_set_speed(-velocidad_avanzar, "em2")
    #si el sensor está viendo a la derecha 
    elif estado_linea in derecha: 
        cyberpi.mbot2.EM_set_speed(velocidad_giro, "em1")
        cyberpi.mbot2.EM_set_speed(-velocidad_avanzar, "em2")
    #si el sensor no está viendo nada
    else: 
        cyberpi.mbot2.EM_set_speed((-velocidad_retroceso), "em1")
        cyberpi.mbot2.EM_set_speed((velocidad_retroceso), "em2")
        
def leds_movement(): 
    cyberpi.console.println("han pasado 10 seg")
    
def mensaje(): 
    cyberpi.broadcast("a")


def eyes_colors(): 
    pass 

@cyberpi.event.start
def start(): 
    time.sleep(1)
    while True: 
        seguidor_lineas()
        cyberpi.broadcast("a")
    

@cyberpi.event.greater_than(1, 'timer')
def leds():
    leds_movement()

@cyberpi.event.receive("a")
def callback2():
    cyberpi.console.println("recibido")
    time.sleep(1)
