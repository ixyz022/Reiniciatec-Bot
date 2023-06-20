import cyberpi as cp 
from cyberpi import mbot2 as m 
import time

#variables globales
velocidadBaile1 = 30

#mover un servo
def moverServo(posicion, servo):
    cp.mbot2.servo_set(posicion, servo)

# Unificacion de la utilizacion de los motores
def motores(velocidad1, velocidad2 = None):
    if velocidad2 is None:
        velocidad2 = velocidad1
    cp.mbot2.EM_set_speed(velocidad1, "em1")
    cp.mbot2.EM_set_speed(velocidad2, "em2")

#mirar a la izquierda 
def mirar_izquierda(): 
    m.servo_set(160, 3)

#mirar al centro 
def mirar_centro(): 
    m.servo_set(90, 3)

#mirar a la derecha 
def mirar_derecha():
    m.servo_set(20, 3)

#mirar hacia arriba 
def mirar_arriba():
    m.servo_set(60, 4)
#mirar hacia abajo 
def mirar_abajo(): 
    m.servo_set(120, 4)

#mirar al frente 
def mirar_frente():
    m.servo_set(90, 4)

def si(iteracion):
    for i in range(iteracion):
        m.servo_set(95, 4)
        time.sleep(0.05)
        m.servo_set(85, 4)
        time.sleep(0.05)
        
# Movimientos a realizar dentro del baile
def movimientosBaile():
    # Inicial antes del baile
    cp.mbot2.servo_set(90,3)
    cp.mbot2.servo_set(10, 1)
    cp.broadcast("aplaudir")
    
    while True:
        motores(velocidadBaile1)
        time.sleep(0.7)
        motores(0)
        motores(velocidadBaile1, -velocidadBaile1)
        time.sleep(0.7)
        motores(0)
        motores(-velocidadBaile1)
        time.sleep(0.7)
        motores(0)
        motores(-velocidadBaile1, velocidadBaile1)
        time.sleep(0.7)
        motores(0)
        motores(-velocidadBaile1)
        time.sleep(0.7)
        motores(0)


#seguidor de lineas
def follow_line():
    offset = cp.quad_rgb_sensor.get_offset_track(index = 1)  # Obtenemos el offset
    speed_adjustment = offset  # Ajustamos la velocidad basándonos en el offset

    # Configuramos la velocidad de los motores
    motor_right_speed = -50 + ((speed_adjustment/2)*-1)  # Ajustamos la velocidad del motor derecho
    motor_left_speed = 50 + ((speed_adjustment/2)*-1)  # Ajustamos la velocidad del motor izquierdo

    # Controlamos los motores
    m.drive_speed(motor_left_speed, motor_right_speed)

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

#agarrar
def agarrar():
    if m.servo_get(2) > 100: 
        m.servo_set(20, 2)
    else:
        m.servo_set(135, 2)
    
#posición inicial 
def posicion_incial(): 
    m.servo_set(90, 1)
    m.servo_set(90, 2)
    m.servo_set(90, 3)
    m.servo_set(90, 4)
    cp.ultrasonic2.set_bri(0,"all", 1)
    cp.reset_yaw()
    cp.console.println(cp.get_yaw())
    
#posicion al dormir 
def posicion_dormir():
    m.servo_set(5, 1)
    m.servo_set(130, 2)
    m.servo_set(60, 3)
    m.servo_set(120, 4)
    
#mover un servo lentamente
def servo_lento(incremento, target, delay, servo):
    estado = m.servo_get(servo)
    if target < estado :
        incremento = incremento*(-1)
    
    while target != estado: 
        m.servo_add(incremento, servo)
        estado = estado + incremento 
        time.sleep(delay)

#cepillar 
def cepillar(iteracion): 
    for i in range(iteracion):
        m.servo_set(30, 1)
        time.sleep(0.2)
        m.servo_set(40, 1)
        time.sleep(0.2)

#bañarse
def bañarse():
    time.sleep(1)
    m.servo_set(140, 4)
    time.sleep(1)
    cepillar(5)
    m.servo_set(90, 1)
    mirar_arriba()
    cepillar(5)
    m.servo_set(90, 1)
    mirar_izquierda()
    cepillar(5)
    m.servo_set(90, 1)
    mirar_derecha()
    cepillar(5)
    m.servo_set(90, 1)
    mirar_centro()
    m.servo_set(70, 4)
    time.sleep(0.5)
    si(5)

#subrutina de que el robot despierta
def despertar(): 
    cp.broadcast("arriba")
    cp.broadcast("bajar_brazo")
    servo_lento(1, 90, 0.05, 3)
    time.sleep(1)
    for i in range(5):
        cp.ultrasonic2.play("happy")


#subrutina de que el robot va a encontrar el cepillo. #para estoy se utilizará el giroscopio. 
def ir_al_cepillo():
    while cp.quad_rgb_sensor.get_line_sta(0, 1):
        follow_line()
    
            

#ACTO 4 
def acto4():
    #El robot comienza con la garra el brazo a 90°, con la mirada hacia abajo, haciendo “no” con la cabeza. 
    m.servo_set(130, 4)
    m.servo_set(90, 3)
    m.servo_set(90, 1)
    m.servo_set(20, 2)
    time.sleep(1)
    cp.broadcast("no2")
    #el robot avanza lentamente por la linea
    while cp.quad_rgb_sensor.is_color("y",1) != True: 
        follow_line()
        if cp.quad_rgb_sensor.get_line_sta(1) == 0: 
            cp.stop_other()
            break
    m.servo_set(90, 3)
    m.servo_set(90, 4)
    m.forward(50, 0.2)    
    m.turn(-90, 20)
    while cp.quad_rgb_sensor.is_color("y",1) != True: 
        follow_line()
    m.forward(0)
    agarrar()
    time.sleep(1)
    #m.servo_set(20, 2)
    m.servo_set(40, 1)
    #m.backward(20, 1)
    m.turn(-70, 40)
    m.forward(40, 1)
    while True: 
        m.drive_speed(30,30)
        if cp.quad_rgb_sensor.is_line("any", 1):
            break
    m.forward(0)
    cp.console.println("llegué")

        
#ACTO 1, 2 
def acto1(): 
    posicion_dormir()
    time.sleep(3)
    despertar()
    agarrar()
    ir_al_cepillo()
    m.drive_speed(0,0)
    agarrar()
    bañarse()
    m.turn(90, 30)
    agarrar()
    m.servo_set(20, 1)
    m.turn(-90,30)
    while True: 
        follow_line()
    
    
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
    while (True):
        follow_line()
        if cp.quad_rgb_sensor.is_color("r","any", 1): 
            break
    m.drive_speed(0,0)

def etapa3():
    m.servo_set(90, 1)
    m.forward(30, 1)
    moverServo(50, "em2") # abrir garra
    time.sleep(1) # espera para poner el prop
    moverServo(90, "em2") # cierra la garra
    cp.broadcast("levantar")
    moverCorto(-30, 1) # Moverse hacia atras un segundo
    m.servo_set(20, 1)
    #giro360(40, 2.8)
    m.turn(360, 50)
    
def etapa4():
    #m.turn(-20, 20)
    m.forward(30, 1)
    while (True):
        follow_line()
        if cp.quad_rgb_sensor.is_color("y","any", 1): 
            break
    m.drive_speed(0,0)

#acto 5
def acto5():
    etapa2()
    time.sleep(1) # espera
    etapa3()
    time.sleep(1) # espera
    etapa4() 

#RUTINA
@cp.event.is_press("a")
def rutina(): 
    acto1()

    
@cp.event.is_press("b")
def callback2(): 
    cp.console.println(cp.get_yaw())
    
    
@cp.event.is_press("up")
def get_yaw(): 
    acto4()
    acto5()

#test
@cp.event.is_press("down")
def giro_giroscopio(): 
    cp.console.println(cp.quad_rgb_sensor.get_color_sta(2,1))
    
@cp.event.is_press('left')
def left(): 
    pass

"""
#obtener angulo yaw
@cp.event.is_press('right')
def right(): 
    #cp.reset_yaw()
    cp.console.println(cp.get_yaw())
"""

@cp.event.receive("arriba")
def arriba():
    for i in range(30):
        m.servo_add(-1, 4)
        time.sleep(0.05)
    
@cp.event.receive("bajar_brazo")
def bajar_brazo(): 
    for i in range(42):
        m.servo_add(2, 1)
        time.sleep(0.05)
    time.sleep(1)
    for i in range(3):
        m.servo_set(30, 2)
        time.sleep(0.5)
        m.servo_set(130,2)
        time.sleep(0.5)
        
#mover la cabeza al recibir la señal 
@cp.event.receive("cabeza")
def cabeza():
    servo_lento(5, 160, 0.05, 3 )
    time.sleep(1)
    servo_lento(5, 20, 0.05, 3 )
    time.sleep(1)
    servo_lento(5, 90, 0.05, 3)
    
@cp.event.receive("cabeza2")
def cabeza2():
    cp.mbot2.servo_set(120, 3)
    time.sleep(0.3)
    cp.mbot2.servo_set(60, 3)
    time.sleep(0.3)
    cp.mbot2.servo_set(90, 3)

@cp.event.receive("no")
def no(): 
    for i in range(10):
        m.servo_set(70, 3)
        time.sleep(0.2)
        m.servo_set(120, 3)
        time.sleep(0.2)
    m.servo_set(90, 3)


@cp.event.receive("aplaudir")
def aplaudir():
    while True:
        cp.mbot2.servo_set(145, 2)
        time.sleep(0.35)
        cp.mbot2.servo_set(90, 2)
        time.sleep(0.35)

@cp.event.receive("leds")
def leds(): 
    cp.led.play("rainbow")
  
  
@cp.event.receive("no2")
def no2(): 
    for i in range(10):
        servo_lento(10, 70, 0.05, 3 )
        time.sleep(0.1)
        servo_lento(10, 120, 0.05, 3 )
        time.sleep(0.1)
    
    """
    for i in range(10):
        m.servo_set(70, 3)
        time.sleep(0.8)
        m.servo_set(120, 3)
        time.sleep(0.8)
    m.servo_set(90, 3)
    """
