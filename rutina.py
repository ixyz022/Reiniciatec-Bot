import cyberpi 
from cyberpi import mbot2 as m 
import time 

velocidad_giro = 60
velocidad_avanzar = 30
velocidad_retroceso = 20

#lista de estádos del sensor de color.
izquierda = [3,7,11]
derecha = [14,13,12]
medio = [0,1,2,4,5,6,8,9,10]

#función del seguidor de lineas
def seguidor_lineas():
    estado_linea = cyberpi.quad_rgb_sensor.get_line_sta(1)
    #si el sensor está viendo solo una linea a la izquierda 
    if estado_linea in izquierda: 
        cyberpi.mbot2.EM_set_speed(-velocidad_giro, "em2")
        cyberpi.mbot2.EM_set_speed(0, "em1")
    #si el sensor está viendo solo al medio 
    elif estado_linea in medio: 
        cyberpi.mbot2.EM_set_speed(velocidad_avanzar, "em1")
        cyberpi.mbot2.EM_set_speed(-velocidad_avanzar, "em2")
    #si el sensor está viendo a la derecha 
    elif estado_linea in derecha: 
        cyberpi.mbot2.EM_set_speed(velocidad_giro, "em1")
        cyberpi.mbot2.EM_set_speed(0, "em2")
    #si el sensor no está viendo nada
    else: 
        cyberpi.mbot2.EM_set_speed((-velocidad_retroceso), "em1")
        cyberpi.mbot2.EM_set_speed((velocidad_retroceso), "em2")

#definimos una lista con los brillos de los leds 
brillos = [100, 100, 100, 100, 100, 100, 100, 100]
def eyes_colors(): 
    cyberpi.ultrasonic2.led_show(brillos, 1)

#mover un servo lentamente
def servo_lento(incremento, target, delay, servo):
    estado = cyberpi.mbot2.servo_get(servo)
    if target < estado :
        incremento = incremento*-1
    
    while target != estado: 
        cyberpi.mbot2.servo_add(incremento, servo)
        estado = estado + incremento 
        time.sleep(delay)
        
def moverServo():
    cyberpi.mbot2.servo_set(145, 2)
        
velocidadBaile1 = 30

# Unificacion de la utilizacion de los motores
def motores(velocidad1, velocidad2 = None):
    if velocidad2 is None:
        velocidad2 = velocidad1
    cyberpi.mbot2.EM_set_speed(velocidad1, "em1")
    cyberpi.mbot2.EM_set_speed(velocidad2, "em2")

# Movimientos a realizar dentro del baile
def movimientosBaile():
    # Inicial antes del baile
    cyberpi.mbot2.servo_set(90,3)
    cyberpi.mbot2.servo_set(10, 1)
    cyberpi.broadcast("aplaudir")
    
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

        

#rutina principal 
@cyberpi.event.is_press("a")
def start(): 
    time.sleep(1)
    #prender las luces de los ojos
    for i in range(3):
        cyberpi.ultrasonic2.play("happy", 1)
    #bajamos el brazo lentamente
    servo_lento(1, 90, 0.01, 1)
    cyberpi.broadcast("cabeza2")
    for i in range(2):
        cyberpi.mbot2.servo_set(120, 2)
        time.sleep(0.5)
        cyberpi.mbot2.servo_set(60, 2)
        time.sleep(0.5)
    #avanzar hasta ver la linea
    line = 15
    while line == 15: 
        line = cyberpi.quad_rgb_sensor.get_line_sta(1)
        cyberpi.mbot2.EM_set_speed(velocidad_avanzar, "em1")
        cyberpi.mbot2.EM_set_speed(-velocidad_avanzar, "em2")
    cyberpi.broadcast("cabeza")
    while True: 
        seguidor_lineas()
        if cyberpi.quad_rgb_sensor.is_color("g", "any", 1):
            break
    cyberpi.mbot2.drive_power(0,0)
    time.sleep(1)
    cyberpi.mbot2.drive_power(20, -20)
    time.sleep(0.7)
    cyberpi.mbot2.drive_power(0, 0)
    cyberpi.mbot2.servo_set(110, 2)
    time.sleep(0.5)
    cyberpi.mbot2.servo_set(20, 1)
    cyberpi.broadcast("no")
    time.sleep(0.5)
    #subir brazo
    servo_lento(5, 90, 0.05, 1)
    time.sleep(1)
    cyberpi.mbot2.servo_set(50, 1)
    #moverse a la izquierda
    cyberpi.mbot2.drive_power(-50, -50)
    time.sleep(1)
    cyberpi.mbot2.servo_set(50, 2)
    cyberpi.mbot2.drive_power(0, 0)
    #moverse a la derecha 
    cyberpi.mbot2.drive_power(50, 50)
    time.sleep(1.1)
    cyberpi.mbot2.drive_power(0, 0)
    cyberpi.mbot2.servo_set(90, 1)
    time.sleep(1)
    
    #tomar el coral 
    while True: 
        seguidor_lineas()
        if cyberpi.quad_rgb_sensor.is_color("g", "any", 1):
            break
    cyberpi.mbot2.drive_power(0,0)
    time.sleep(1)
    cyberpi.mbot2.drive_power(20, -20)
    time.sleep(0.7)
    cyberpi.mbot2.drive_power(0, 0)
    cyberpi.mbot2.servo_set(130, 2)
    time.sleep(0.5)
    cyberpi.mbot2.servo_set(40, 1)
    time.sleep(0.5)
    cyberpi.mbot2.servo_set(10, 3)
    for i in range(3):
        cyberpi.ultrasonic2.play("thinking", 1)
    for i in range(2):
        cyberpi.mbot2.servo_set(90, 3)
        time.sleep(0.7)
        cyberpi.mbot2.servo_set(170, 3)
        time.sleep(0.7)
    cyberpi.mbot2.servo_set(90, 3)
    cyberpi.mbot2.turn(-130, 30)
    cyberpi.mbot2.straight(25, 30)
    m.servo_set(90, 1)
    time.sleep(0.5)
    m.servo_set(20, 2)
    time.sleep(0.5)
    m.backward(20, 1)
    m.turn(-130, 60)
    movimientosBaile()
        
    
#mover la cabeza al recibir la señal 
@cyberpi.event.receive("cabeza")
def cabeza():
    servo_lento(5, 160, 0.05, 3 )
    time.sleep(1)
    servo_lento(5, 20, 0.05, 3 )
    time.sleep(1)
    servo_lento(5, 90, 0.05, 3)
    
@cyberpi.event.receive("cabeza2")
def cabeza2():
    cyberpi.mbot2.servo_set(120, 3)
    time.sleep(0.3)
    cyberpi.mbot2.servo_set(60, 3)
    time.sleep(0.3)
    cyberpi.mbot2.servo_set(90, 3)

@cyberpi.event.receive("no")
def no(): 
    for i in range(10):
        m.servo_set(70, 3)
        time.sleep(0.2)
        m.servo_set(120, 3)
        time.sleep(0.2)
    m.servo_set(90, 3)

#estado inicial 
@cyberpi.event.is_press('b')
def estado_inicial():
    cyberpi.mbot2.servo_set(90,3)
    cyberpi.mbot2.servo_set(10, 1)
    cyberpi.mbot2.servo_set(90, 2)

#al presionar el botón arriba 
@cyberpi.event.is_press('up')
def arriba(): 
    for i in range(5): 
        cyberpi.led.play("rainbow")
    """cyberpi.led.play("rainbow")
    cyberpi.led.play("spoondrift")
    cyberpi.led.play("meteor_blue")
    cyberpi.led.play("meteor_green")
    cyberpi.led.play("flash_red")
    cyberpi.led.play("firefly")"""

@cyberpi.event.is_press('down')
def abajo(): 
    cyberpi.mbot2.servo_set(50, 2)
    
@cyberpi.event.is_press('left')
def left(): 
    cyberpi.mbot2.servo_set(90, 1)

@cyberpi.event.is_press('right')
def right(): 
    movimientosBaile()


@cyberpi.event.receive("aplaudir")
def aplaudir():
    while True:
        cyberpi.mbot2.servo_set(145, 2)
        time.sleep(0.35)
        cyberpi.mbot2.servo_set(90, 2)
        time.sleep(0.35)

@cyberpi.event.receive("leds")
def leds(): 
    cyberpi.led.play("rainbow")