import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

class pin:
	def __init__(pin, IO = "IN"):
		_pin = pin
		_PWM = 0
		_pwm_eneable = False
		if IO == "OUT":
			GPIO.setup(pin,GPIO.OUT)
		else:
			GPIO.setup(pin,GPIO.IN)

	def set(I0 = True):
		GPIO.output(_pin,IO)

	def pwm(freq = 10, duty = 50):
		if pwm_eneable:
			_PWM.ChangeFrequency(freq)
			_PWM.ChangeDutyCycle(duty)
		else:
			_pwm_eneable = True
			_PWM = GPIO.PWM(_pin,freq)
			_PWM.start(duty)


out = pin(8,"OUT")

while true:
	command = raw_input("Command: ")
	if command == 'Set':
		out.set(bool(raw_input('Value 0/1: ')))
	if command == 'PWM'
		freq = int(raw_input('Frequency: '))
		duty = int(raw_input('DutyCycle: '))
		pin.pwm(freq,duty)
