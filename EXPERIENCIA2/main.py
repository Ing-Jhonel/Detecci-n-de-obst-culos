#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile

ev3 = EV3Brick()

ev3 = EV3Brick()
md = Motor(Port.B)
mi = Motor(Port.C)
diametro_rueda = 55.5
distancia_entre_ruedas = 104
robot = DriveBase(md, mi, diametro_rueda, distancia_entre_ruedas)

ultrasonido = UltrasonicSensor(Port.S4)

velocidad=200
ev3.light.on(Color.GREEN)
c=0
  
while True:
    distancia = ultrasonido.distance()
    robot.drive(velocidad, 0)
    if distancia <= 200:
        robot.stop()
        ev3.light.on(Color.RED)
        ev3.screen.draw_text(50, 50, "¡DISPAROO!")
        ev3.speaker.beep(1000, 100)
        wait(1000)
        ev3.speaker.beep(800, 100)
        wait(500)
        robot.straight(-500)


    
