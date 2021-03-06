import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

class pin:
	def __init__(self, pin, IO = "IN"):
		self._pin = pin
		self._PWM = 0
		self._pwm_eneable = False
		if IO == "OUT":
			GPIO.setup(pin, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
		else:
			GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

	def set(self,status=True):
		GPIO.output(self._pin,status)

	def pwm(self,freq = 10, duty = 50):
		if self._pwm_eneable:
			self._PWM.ChangeFrequency(freq)
			self._PWM.ChangeDutyCycle(duty)
		else:
			self._pwm_eneable = True
			self._PWM = GPIO.PWM(_pin,freq)
			self._PWM.start(duty)

	def pwm_stop(self):
		if self._pwm_eneable:
			self._PWM.pwm_stop()
			self._pwm_eneable = False
