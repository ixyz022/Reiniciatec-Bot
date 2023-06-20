import mbot2, event, time, cyberpi

@event.is_press('a')
def is_btn_press():
    mbot2.turn(110) #gira para mirar hacia el publico
    mbot2.servo_set(90,"S4")
    time.sleep(0.5)
    mbot2.servo_set(20,"S1")
    for count in range(7):
        mbot2.servo_set(120,"S3")
        time.sleep(0.3)
        mbot2.servo_set(60,"S3")
        time.sleep(0.3)

    mbot2.turn(-110) #gira de vuelta a su posición inicial
    mbot2.servo_set(80,"S1")
    cyberpi.stop_all()
