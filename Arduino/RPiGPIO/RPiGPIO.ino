// RPiGPIO.ino

uint8_t wires[5] = {13,12,11,10,9};
boolean change = false;

void setup() 
{
	Serial.begin(115200);
	for(int i=0;i<5;i++)
	{
		pinMode(wires[i],OUTPUT);
	}
}

void loop() 
{
	if(Serial.available()>0)
	{
		change = !change;
		digitalWrite(wires[0],change);
		for(int i=1;i<5;i++)
		{
			int value = random(0,2);
			digitalWrite(wires[i],value);
			Serial.print("wire ");
			Serial.print(wires[i]);
			Serial.print(" = ");
			Serial.println(value);
		}
	}
	while(Serial.available()>0)
	{
		Serial.read();
	}
}

