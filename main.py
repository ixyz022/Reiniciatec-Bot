import cyberpi as cp
from cyberpi import mbot2 as m 
import time 

#funcion para seguir lineas 
def seguidor_lineas(comprobacion):
    if (not comprobacion):
        m.drive_speed(0, 0)
    else :
        offset = cp.quad_rgb_sensor.get_offset_track(index = 1)  # Obtenemos el offset
        speed_adjustment = offset  # Ajustamos la velocidad basándonos en el offset
        # Configuramos la velocidad de los motores
        motor_right_speed = -50 + ((speed_adjustment/2)*-1)  # Ajustamos la velocidad del motor derecho
        motor_left_speed = 50 + ((speed_adjustment/2)*-1)  # Ajustamos la velocidad del motor izquierdo
        # Controlamos los motores
        m.drive_speed(motor_left_speed, motor_right_speed)
                
               
#mover un servo
def moverServo(posicion, servo):
    cp.mbot2.servo_set(posicion, servo)

# Realiza una vuelta 360
def giro360 (velocidad, tiempo):
    m.drive_speed(velocidad, velocidad)
    time.sleep(tiempo)
    m.drive_speed(0, 0)


# Mueve las ruedas una distancia que depende del tiempo y la velocidad
def moverCorto(velocidad, tiempo):
    m.drive_speed(velocidad, -velocidad)
    time.sleep(tiempo)
    m.drive_speed(0, 0)

# Movimientos iniciales
def etapa1():
    moverServo(90, 3) # Mover cabeza
    moverServo(90, 4) # Mover cuello
    moverServo(90, "em1") # brazo central en el medio
    moverServo(50, "em2") # abrir garra
    time.sleep(1) # espera para poner el prop
    moverServo(90, "em2") # cierra la garra
    time.sleep(0.5) # espera para poner el prop
    moverServo(70, "em1") # brazo central en el medio

# Sigue la linea hasta la zona de reciclaje dejando la garra a traves de la compuerta
def etapa2():
    comprobacion = True
    white = "0xffffff"
    while (True):
        #variable1 = cp.quad_rgb_sensor.get_color_sta(1, index = 1)
        variable1 = cp.quad_rgb_sensor.get_color(1, index = 1)
        comprobacion = False if variable1 != white else comprobacion
        #cp.console.println(variable1) 
        seguidor_lineas(comprobacion)
    moverCorto(30, 1) # Moverse hacia atras un segundo


def etapa3():
    moverServo(50, "em2") # abrir garra
    time.sleep(1) # espera para poner el prop
    moverServo(90, "em2") # cierra la garra
    cp.broadcast("levantar")
    moverCorto(-30, 1) # Moverse hacia atras un segundo
    giro360(40, 2.8)
    
def etapa4():
    giro360(40, 1.4)
    comprobacion = True
    white = "0xffffff"
    while (True):
        variable1 = cp.quad_rgb_sensor.get_color(1, index = 1)
        comprobacion = False if variable1 != white else comprobacion
        seguidor_lineas(comprobacion)
    

@cp.event.receive("levantar")
def etapa3dot5():
    moverServo(10, "em1") # brazo central en el medio

#rutina principal 
@cp.event.is_press('a')
def start(): 
    etapa1()

@cp.event.is_press('up')    
def start2():
    etapa2()

@cp.event.is_press('down')    
def start3():
    etapa3()
  
@cp.event.is_press('left')    
def all():
    etapa1()
    time.sleep(1) # espera
    etapa2()
    time.sleep(1) # espera
    etapa3()
    time.sleep(1) # espera
    etapa4()
##########################################################
