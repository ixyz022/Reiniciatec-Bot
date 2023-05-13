import cyberpi
import time
import event
import mbuild_modules.starter_shield as starter_shield

velocidad_giro =100
velocidad_giro_rapido = 150
velocidad_avanzar = 80
velocidad_retroceso = 50

#lista de estádos del sensor de color.
#izquierda = [3,7,11]
#derecha = [14,13,12]
#medio = [0,1,2,4,5,6,8,9,10] #quitar 0

izquierda = [8, 12, 4]
derecha = [1, 2, 3]
izquierdaRapido = [8]
izquierdaLento = [12, 4]
derechaRapido = [1]
derechaLento = [2, 3]
medio = [6, 15]


def seguidor_lineas():
    estado_linea = cyberpi.quad_rgb_sensor.get_line_sta(1)
    #si el sensor está viendo solo una linea a la derecha 
    if estado_linea in izquierda: 
        if estado_linea in izquierdaLento:
            cyberpi.mbot2.EM_set_speed(velocidad_avanzar, "em1")
            cyberpi.mbot2.EM_set_speed(-velocidad_giro, "em2")
        elif estado_linea in izquierdaRapido:
            cyberpi.mbot2.EM_set_speed(velocidad_giro_rapido, "em1")
            cyberpi.mbot2.EM_set_speed(-velocidad_avanzar, "em2")
    
    # si el sensor está viendo a la derecha
    if estado_linea in derecha: 
        if estado_linea in derechaLento:
            cyberpi.mbot2.EM_set_speed(velocidad_avanzar, "em1")
            cyberpi.mbot2.EM_set_speed(-velocidad_giro, "em2")
        elif estado_linea in derechaRapido:
            cyberpi.mbot2.EM_set_speed(velocidad_avanzar, "em1")
            cyberpi.mbot2.EM_set_speed(-velocidad_giro_rapido, "em2")
            
            
            
    #si el sensor va a la izquierda
    elif estado_linea in izquierda: 
        cyberpi.mbot2.EM_set_speed(-velocidad_giro, "em2")
        cyberpi.mbot2.EM_set_speed(velocidad_avanzar, "em1")
    #si el sensor está viendo a la derecha 
    elif estado_linea in derecha: 
        cyberpi.mbot2.EM_set_speed(velocidad_giro, "em1")
        cyberpi.mbot2.EM_set_speed(-velocidad_avanzar, "em2")
    #si el sensor no está viendo nada
    #else: 
     #   cyberpi.mbot2.EM_set_speed((-velocidad_retroceso), "em1")
      #  cyberpi.mbot2.EM_set_speed((velocidad_retroceso), "em2")

def ver_colores():
    if cyberpi.quad_rgb_sensor.is_color("r", "R1", 1) == True: 
        cyberpi.console.println("rojo")
    if cyberpi.quad_rgb_sensor.is_color("b", "R1", 1) == True: 
        cyberpi.console.println("azul")
    if cyberpi.quad_rgb_sensor.is_color("g", "R1", 1) == True: 
        cyberpi.console.println("verde")

def girar_robot(velocidad, aceleracion, duracion):
    # Aquí iría el código que hace girar al robot
    
    velocidad_giro = 0
    tiempo_inicial = time.time()
    
    while time.time() - tiempo_inicial < duracion:
        # Aumentamos gradualmente la velocidad de giro
        velocidad_giro += velocidad * aceleracion * (time.time() - tiempo_inicial)
        
        # Aquí iría el código que utiliza la velocidad de giro para hacer girar al robot
    
    # Aquí iría el código que finaliza el giro del robot
    
    return velocidad_giro

def ultrasonido(): 
    return cyberpi.ultrasonic2.get(1)
    
def abrazo():
    time.sleep(1)
    cyberpi.mbot2.servo_set(75, 1)
    cyberpi.mbot2.servo_set(105, 2)
    
def reset_brazos(): 
    time.sleep(1)
    cyberpi.mbot2.servo_set(180, 1)
    cyberpi.mbot2.servo_set(-180, 2)

    

@event.is_press('a')
def is_btn_press():
    time.sleep(1)
    while True:
        seguidor_lineas()
@event.is_press('b')
def is_btn_press1():
    reset_brazos()
    cyberpi.mbot2.forward(100, 1)
    abrazo()
    time.sleep(1)
    cyberpi.mbot2.turn(90, 100)
    cyberpi.mbot2.forward(100, 1)
    reset_brazos()
    cyberpi.mbot2.backward(100, 1)
    cyberpi.mbot2.turn(-90, 100)
    cyberpi.mbot2.backward(100, 1)
    return 0 
    