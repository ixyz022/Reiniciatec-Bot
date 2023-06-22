#estas partes de código deben ser agregagas donde sea pertinente

#llevar al amigo pez a una zona segura, zona B
while not cyberpi.quad_rgb_sensor.is_color("g", "R1", 1) == True:
  follow_line():
m.servo_set(20,2)


#acto 6
#el robot se desplaza al centro de la pista
cyberpi.mbot2.servo_set(120,4)
cyberpi.mbot2.servo_set(130,2)
cyberpi.mbot2.servo_set(5,1)
    
motores(80, 80)
time.sleep(0.7)
motores(80, -80)
time.sleep(0.6)
cyberpi.mbot2.servo_set(90,4)
time.sleep(0.1)

#baile 1
#luces al recibir la señal
@cyberpi.event.receive("luz_ojos")
def luz_ojos():
    cyberpi.ultrasonic2.play("happy", 1)
    
    
#mover cabeza al recibir señal
@cyberpi.event.receive("cabeza")
def cabeza():
    cyberpi.mbot2.servo_set(60,3)
    time.sleep(0.1)
    cyberpi.mbot2.servo_set(130,2)
    time.sleep(0.1)
    cyberpi.mbot2.servo_set(5,1)
    time.sleep(0.1)
    cyberpi.mbot2.servo_set(90,3)
    time.sleep(0.1)
    cyberpi.mbot2.servo_set(60,4)
    time.sleep(0.2)
    cyberpi.mbot2.servo_set(90,1)
    time.sleep(0.1)
    cyberpi.mbot2.servo_set(30,2)
    time.sleep(0.1)
    cyberpi.mbot2.servo_set(90,4)
    time.sleep(0.1)
    cyberpi.mbot2.servo_set(120,3)
    time.sleep(0.1)
    cyberpi.mbot2.servo_set(130,2)
    time.sleep(0.1)
    
#mover cuerpo al recibir la señal
@cyberpi.event.receive("cuerpo")
def cuerpo():
    motores(-10,-30)
    time.sleep(0.2)
    motores(0)
    time.sleep(0.1)
    motores(10,30)
    time.sleep(0.2)
    motores(30,10)
    time.sleep(0.2)
    motores(0)
    time.sleep(0.1)
    
while True:
        cyberpi.broadcast("luz_ojos")
        cyberpi.broadcast("cabeza")
        cyberpi.broadcast("cuerpo")
