import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

wires = {'white':8,'grey':10,'violet':12,'blue':16,'green':18}

for wire in wires.keys():
	GPIO.setup(wires[wire], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0

print "----------------------------------------"

while counter < 10:
	GPIO.wait_for_edge(wires['white'], GPIO.BOTH)
	for wire in wires.keys():
		print 'Wire {} is {}'.format(wire,GPIO.input(wires[wire]))
	counter+=1
	print "----------------------------------------"
	
GPIO.cleanup()
