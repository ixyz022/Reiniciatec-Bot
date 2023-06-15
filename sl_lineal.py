import cyberpi as cp 
from cyberpi import mbot2 as m 

#funcion para seguir lineas 
def follow_line():

    offset = cp.quad_rgb_sensor.get_offset_track(index = 1)  # Obtenemos el offset
    speed_adjustment = offset  # Ajustamos la velocidad basándonos en el offset

    # Configuramos la velocidad de los motores
    motor_right_speed = -50 + ((speed_adjustment/2)*-1)  # Ajustamos la velocidad del motor derecho
    motor_left_speed = 50 + ((speed_adjustment/2)*-1)  # Ajustamos la velocidad del motor izquierdo

    # Controlamos los motores
    m.drive_speed(motor_left_speed, motor_right_speed)

@cp.event.is_press("a")
def callback():
    while True: 
        follow_line()
        
@cp.event.is_press("b")
def callback2():
    cp.quad_rgb_sensor.set_led("w", 1)