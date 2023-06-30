import cyberpi as cp 
from cyberpi import mbot2 as m 
import time

#variables globales
velocidadBaile1 = 30

###########################################################
################# Definicion de funciones #################
###########################################################

# Mover unitariamente un servo 
def moverServo(posicion, servo):
    cp.mbot2.servo_set(posicion, servo)

@cp.event.is_press("eventoMoverServo")
def eventoMoverServo(posicion, servo):
    cp.mbot2.servo_set(posicion, servo)

# Unificacion de los de los motores
def motores(velocidad1, velocidad2 = None):
    if velocidad2 is None:
        velocidad2 = velocidad1
    cp.mbot2.EM_set_speed(velocidad1, "em1")
    cp.mbot2.EM_set_speed(velocidad2, "em2")


#agarrar
def agarrar():
    if m.servo_get(2) > 100: 
        m.servo_set(20, 2)
    else:
        m.servo_set(135, 2)

# Accion de afirmacion
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

#ajustar posición del robot respecto de la linea
def ajustar():
    offset = cp.quad_rgb_sensor.get_offset_track(index = 1)  # Obtenemos el offset
    while not(offset > -20 and offset < 20):
        if offset > -20: 
            m.drive_speed(-10, -10)
            offset = cp.quad_rgb_sensor.get_offset_track(index = 1) 
        if offset < 20: 
            m.drive_speed(10, 10)
            offset = cp.quad_rgb_sensor.get_offset_track(index = 1)
        offset = cp.quad_rgb_sensor.get_offset_track(index = 1)
    m.forward(0)
    
# Posicion inicial de performance 
def posicion_incial(): 
    m.servo_set(90, 1)
    m.servo_set(90, 2)
    m.servo_set(90, 3)
    m.servo_set(90, 4)
    cp.ultrasonic2.set_bri(0,"all", 1)
    cp.reset_yaw()
    cp.console.println(cp.get_yaw())
    
# Posicion para simular dormir
def posicion_dormir():
    m.servo_set(5, 1)
    m.servo_set(130, 2)
    m.servo_set(60, 3)
    m.servo_set(120, 4)
    
# Mover lentamente un servo
def servo_lento(incremento, target, delay, servo):
    estado = m.servo_get(servo)
    if target < estado :
        incremento = incremento*(-1)
    
    while target != estado: 
        m.servo_add(incremento, servo)
        estado = estado + incremento 
        time.sleep(delay)

# Cepillarse
def cepillar(iteracion): 
    for i in range(iteracion):
        m.servo_set(30, 1)
        time.sleep(0.2)
        m.servo_set(40, 1)
        time.sleep(0.2)

# Ducharse
def bañarse():
    time.sleep(1)
    m.servo_set(140, 4)
    time.sleep(1)
    cepillar(5)
    m.servo_set(90, 1)
    moverServo(60, 4) # Mover la cabeza hacia arriba
    cepillar(5)
    m.servo_set(90, 1)
    moverServo(160, 3) # Mirar hacia la izquierda
    cepillar(5)
    m.servo_set(90, 1)
    moverServo(20, 3) # Mirar hacia la derecha
    cepillar(5)
    m.servo_set(90, 1)
    moverServo(90, 3) # Mirar hacia el centro
    m.servo_set(70, 4)
    time.sleep(0.5)
    si(5)

# Subrutina del despertar del robot
def despertar(): 
    cp.broadcast("arriba")
    cp.broadcast("bajar_brazo")
    servo_lento(1, 90, 0.05, 3)
    time.sleep(1)
    for i in range(5):
        cp.ultrasonic2.play("happy")


#subrutina de que el robot va a encontrar el cepillo. #para estoy se utilizará el giroscopio. 
def ir_al_cepillo():
    
    while True:
        follow_line()
        if cp.quad_rgb_sensor.get_line_sta(1) == 0: 
            break
        
# Mueve las ruedas una distancia que depende del tiempo y la velocidad
def moverCorto(velocidad, tiempo):
    m.drive_speed(velocidad, -velocidad)
    time.sleep(tiempo)
    m.drive_speed(0, 0)

# Movimientos iniciales
def etapa1():
    moverServo(90, 3) # Mover cabeza
    moverServo(90, 4) # Mover cuello
    #moverServo(90, "em1") # brazo central en el medio
    #moverServo(50, "em2") # abrir garra
    #time.sleep(1) # espera para poner el prop
    #moverServo(90, "em2") # cierra la garra
    #time.sleep(0.5) # espera para poner el prop
    #moverServo(70, "em1") # brazo central en el medio

# Sigue la linea hasta la zona de reciclaje dejando la garra a traves de la compuerta
def etapa2():
    while cp.quad_rgb_sensor.is_color("purple","any") != True: 
        follow_line()
    m.forward(0)
    time.sleep(5)

def etapa3():
    m.servo_set(90, 1)
    m.forward(30, 1)
    moverServo(20, "em2") # abrir garra
    time.sleep(1) # espera para poner el prop
    cp.broadcast("levantar")
    moverCorto(-30, 1) # Moverse hacia atras un segundo
    moverServo(90, "em2") # cierra la garra
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

###########################################################
################## Definicion de eventos ##################
###########################################################      

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
        
###########################################################
########################## Actos ##########################
###########################################################            

#ACTO 1, 2 
def acto1(): 
    posicion_dormir()
    time.sleep(3)
    despertar()
    moverServo(20, 2) # cerrar garra
    ir_al_cepillo()
    m.drive_speed(0,0)
    m.straight(4, 30)
    ajustar()
    m.servo_set(110, 1)
    agarrar()
    #moverServo(130, 2) # cerrar garra
    time.sleep(0.5)
    bañarse()
    m.servo_set(40, 1)
    m.turn(90, 40)
    m.servo_set(90, 1)
    time.sleep(1)
    #moverServo(20, 2) # cerrar garra
    agarrar()
    time.sleep(1)
    m.servo_set(20, 1)
    m.turn(-90,40)
    while True: 
        follow_line()
        if cp.quad_rgb_sensor.get_line_sta(1) == 0:
            break
    m.drive_speed(0,0)

#acto 3 
def acto3():
    #el robot se acerca lentamente a el pez y lo toca
    m.servo_set(20,"S1")
    m.servo_set(130,"S2")
    m.servo_set(90,"S3")
    m.servo_set(120,"S4")
    time.sleep(1)
    m.forward(10, 2)
    ajustar()
    time.sleep(1)
    m.servo_set(20,"S1")
    for count in range(28):
        m.servo_add(2,"S1")
        time.sleep(0.1)

    m.servo_set(20,"S1")
    m.forward(0)
    time.sleep(1)
    m.turn(110, 50)
    m.servo_set(90,"S4")
    for count2 in range(7):
        m.servo_set(120,"S3")
        time.sleep(0.3)
        m.servo_set(60,"S3")
        time.sleep(0.3)
        
    m.turn(-120, 50)
    ajustar()
    m.servo_set(35,"S2")

    time.sleep(1)
    for count3 in range(22):
        m.servo_add(4,"S1")
        time.sleep(0.1)
        
    #el robot se acerca a tomar el pez
    m.straight(3,20)
    time.sleep(0.3)
    #m.servo_set(130,"S2")
    agarrar()
    time.sleep(0.7)
    m.servo_set(40, 1)
    m.servo_set(90, 3)
    time.sleep(0.5)
    m.servo_add(80, 3)
    time.sleep(1)
    m.servo_add(-160, 1)
    time.sleep(1)
    m.servo_set(90, 3)
    m.servo_set(120, 4)
    
    #sigue lineas hasta la curva
    ajustar()
    while True:
        follow_line()
        if cp.quad_rgb_sensor.is_line("l2", 1) == 1: 
            break
    #avanza lentamente hasta ver la curva
    m.straight(7, 30)
    time.sleep(0.2)
    m.turn(-50, 20)
    while True: 
        m.drive_speed(-30,-30)
        if cp.quad_rgb_sensor.is_line("r1", 1) == 1: 
            break
    ajustar()
    #time.sleep(1)
    
    
    #sigue lineas hasta el hospital
    while True: 
        follow_line()
        if cp.quad_rgb_sensor.get_line_sta(1) == 0:
            break
    m.drive_speed(0,0)
    time.sleep(1)
    m.straight(5, 40)
    
    for i in range(25):
        m.servo_add(2, 1)
        time.sleep(0.1)
    time.sleep(1)
    m.servo_set(20, 2)
    time.sleep(1)
    #m.straight(-5, 40)
    m.forward(0)
    time.sleep(1)
    
    #devolverse 
    m.straight(-4, 20)
    m.servo_set(5, 1)
    time.sleep(1)
    m.turn(-190, 40)

#ACTO 4 
def acto4():
    #El robot comienza con la garra el brazo a 90°, con la mirada hacia abajo, haciendo “no” con la cabeza. 
    m.servo_set(130, 4)
    m.servo_set(90, 3)
    m.servo_set(20, 1)
    m.servo_set(20, 2)
    time.sleep(1)
    cp.broadcast("no2")
    #el robot avanza lentamente por la linea
    while True: 
        follow_line()
        if cp.quad_rgb_sensor.get_line_sta(1) == 0: 
            cp.stop_other()
            break
    #luego de ver la linea se pone en posición inicial y gira a la derecha. 
    m.forward(0)
    m.servo_set(90, 3)
    m.servo_set(90, 4)
    #antes de girar mirá hacia los barriles
    m.servo_set(90, 1)
    time.sleep(0.5)
    m.servo_set(170, 3)
    m.servo_set(90, 4)
    time.sleep(1)
    cp.broadcast("mirar")
    #gira hacia los barriles
    m.forward(50, 0.2)
    m.forward(0)
    time.sleep(1)
    m.turn(-100, 20)
    #sigue la linea hasta ver el color amarillo
    while cp.quad_rgb_sensor.is_color("y",1) != True: 
        follow_line()
    m.forward(0)
    m.servo_set(110, 1)
    m.straight(5, 20)
    agarrar()
    time.sleep(0.7)
    #m.straight(-10,20)
    
    m.servo_set(30, 1)
    
    time.sleep(0.5)
    #m.servo_set(20, 2)
    
    #m.backward(20, 1)
    #m.turn(-70, 40)
    #m.forward(40, 1)
    """
    while True: 
        #m.drive_speed(30,30)
        if cp.quad_rgb_sensor.is_line("any", 1):
            break
    """



# ACTO 5
def acto5():
    while True: 
        m.drive_speed(-30, -30)
        if cp.quad_rgb_sensor.is_line("r1", 1) == 1: 
            break
    while cp.quad_rgb_sensor.is_color("purple","any") != True: 
        follow_line()
    m.forward(0)
    time.sleep(0.5)
    m.servo_set(110, 1)
    m.forward(30, 1)
    moverServo(20, "em2") # abrir garra
    time.sleep(1) # espera para poner el prop
    moverCorto(-30, 1) # Moverse hacia atras un segundo
    moverServo(90, "em2") # cierra la garra
    m.servo_set(20, 1)
    #giro360(40, 2.8)
    #m.turn(360, 50)
    time.sleep(1) # espera
    """
    m.turn(-70, 40)
    while True: 
        m.drive_speed(30, -30)
        if cp.quad_rgb_sensor.is_line("r1", 1) == 1: 
            break
    """
#acto 6
def acto6(): 
    while True: 
        follow_line()
        if cp.quad_rgb_sensor.get_line_sta(1) == 0: 
            break
    m.forward(0)
    ajustar()
    m.servo_set(20,2)
    time.sleep(1)
    for count3 in range(22):
        m.servo_add(4,"S1")
        time.sleep(0.1)
        
    #el robot se acerca a tomar el pez
    m.straight(3,20)
    time.sleep(0.3)
    #m.servo_set(130,"S2")
    agarrar()
    time.sleep(0.7)
    m.servo_set(30, 1)
    time.sleep(0.5)
    m.turn(-70, 40)
    m.straight(45, 60)
    for i in range(35):
        m.servo_add(2, 1)
        time.sleep(0.1)
    time.sleep(0.5)
    agarrar()
    m.straight(-10, 60)
    movimientosBaile()
    
    
    """
    m.straight(8, 15)
    m.turn(-60, 15)
    m.straight(4, 15)
    ajustar()
    m.straight(3,15)
    ajustar()
    m.straight(2, 15)
    ajustar()
    m.forward(0)
    m.servo_set(20, 2)
    for i in range(35):
        m.servo_add(2, 1)
        time.sleep(0.05)
    m.servo_set(130, 2)
    time.sleep(1)
    m.servo_set(20, 1)
    m.straight(-20, 20)
    m.turn(-60, 20)
    m.straight(40, 40)
    movimientosBaile()
    """
    
    

    
###########################################################
################## Eventos de la rutina ###################
###########################################################      

#RUTINA
@cp.event.is_press("a")
def rutina(): 
    acto1()
    acto3()
    acto4()
    acto5()
    acto6()
    #ponemos la posición para pasar al acto 3 
    

    
@cp.event.is_press("b")
def callback2(): 
    acto3()
    
    
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

@cp.event.receive("mirar")
def mirar_izq():
    for i in range(20):
        m.servo_add(-4, 3)
        time.sleep(0.1)
        
"""
#obtener angulo yaw
@cp.event.is_press('right')
def right(): 
    #cp.reset_yaw()
    cp.console.println(cp.get_yaw())
"""
