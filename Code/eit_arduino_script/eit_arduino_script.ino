//## Arduino script that handles vibrotactile actuators for CSE 598:EIT assignment-A2 ##
//#traceback: eit_test_script-3.ino#
//######################################################################################

//ERM motor pin assignment
const int lowerArm = 3; //yellow led
const int upperArm= 8; //red led

//vibration parameters
int Duration;
int SOA;

//time check
int t0;
int check;

void setup()
{
  Serial.begin(115200);
  
  pinMode(lowerArm, OUTPUT);
  pinMode(upperArm, OUTPUT);

}

void loop()
{
  while(Serial.available()==0){
    
    }
    
  Duration=Serial.readStringUntil(',').toInt();
  SOA=Serial.readStringUntil('\r').toInt();

  check= Duration-SOA;

  if (check>0){
    vibeFunction1(Duration,SOA);
    }
  else if (check<0){
    vibeFunction2(Duration,SOA);
    }
  else{
    vibeFunction3(Duration,SOA);
  }
      
}

void vibeFunction1(int Duration,int SOA){
    t0=millis(); digitalWrite(lowerArm,HIGH);
//    Serial.println(millis()-t0); 
    
    delay(SOA); digitalWrite(upperArm,HIGH);
//    Serial.println(millis()-t0);

    delay(Duration-SOA); digitalWrite(lowerArm,LOW);
//    Serial.println(millis()-t0); 

    delay(SOA); digitalWrite(upperArm,LOW);
//    Serial.println(millis()-t0); 
    
}

void vibeFunction2(int Duration,int SOA){
    t0=millis(); digitalWrite(lowerArm,HIGH);
//    Serial.println(millis()-t0); 
    
    delay(Duration); digitalWrite(lowerArm,LOW);
//    Serial.println(millis()-t0);

    delay(SOA-Duration); digitalWrite(upperArm,HIGH);
//    Serial.println(millis()-t0); 

    delay(Duration); digitalWrite(upperArm,LOW);
//    Serial.println(millis()-t0); 
    
}

void vibeFunction3(int Duration,int SOA){
  
    t0=millis(); digitalWrite(lowerArm,HIGH);
//    Serial.println(millis()-t0); 
    
    delay(Duration); digitalWrite(lowerArm,LOW); digitalWrite(upperArm,HIGH);
//    Serial.println(millis()-t0);

    delay(SOA); digitalWrite(upperArm,LOW);
//    Serial.println(millis()-t0); 
    
}
