int BoxRelay1PIN = 13; //Relay1
int BoxRelay2PIN = 12; //Relay2
int BoxRelayToGrid = 27; //Relay to grid (safty)
double voltage = 0;
#define VoltageGridPIN A0 // Voltage reader Grid
char BatteryMode = 'Start';
char comando;


void disconnect(){

  digitalWrite(BoxRelayToGrid, HIGH);
  Serial.println("disconnect Box from Grid");
}

void connect(){

  digitalWrite(BoxRelayToGrid, LOW);
  Serial.println("disconnect Box from Grid");
}

void discharge(){

  Serial.println("discharge");
  connect();
  digitalWrite(BoxRelay1PIN, HIGH);
  digitalWrite(BoxRelay2PIN, HIGH);

}
void charge(){

  connect();
  digitalWrite(BoxRelay1PIN, LOW);
  digitalWrite(BoxRelay2PIN, LOW);
  Serial.println("charge");
}

double readVoltage(int reading){

  voltage = ((reading/4095) * 3.3);

  return voltage;
}


void setup() {
  // put your setup code here, to run once:
  pinMode(BoxRelay1PIN, OUTPUT);
  pinMode(BoxRelay2PIN, OUTPUT);
  pinMode(BoxRelayToGrid, OUTPUT);
  pinMode(VoltageGridPIN, INPUT);
  Serial.begin(115200);
  

}

void loop() {

    if (Serial.available() > 0) 
  {
    comando = Serial.read();
    
    if (comando == 'C') 
    {
      charge();
      BatteryMode = 'charge';
      delay(100);
    }
    else if (comando == 'D') 
    {
      discharge();
      BatteryMode = 'discharge';
      delay(100);
    }
    else if (comando == 'X') 
    {
      disconnect();
      BatteryMode = 'disconnected';
      delay(100);
    }
  }


/*
  // put your main code here, to run repeatedly:
  Serial.println("Charge 1, Discharge 2, disconnect 3");
  //Serial.print("Voltage Grid: "); Serial.print(readVoltage(analogRead(VoltageGridPIN))); Serial.println(" V");
  Serial.print("Voltage Grid: "); Serial.print(analogRead(VoltageGridPIN)); Serial.println(" V");

  while (Serial.available() == 0) {
  }

  int menuChoice = Serial.parseInt();

  if (menuChoice == 1){
    charge();
    delay(100);

    
  }
  else if (menuChoice == 2){

    discharge();
    delay(100);
  }
  else if (menuChoice == 3){

    disconnect();
    Serial.println("OFF");
    delay(100);
  } */
}
