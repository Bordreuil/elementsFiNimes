
// Bibliotheque a telecharger
#include "HX711.h"

// HX711.DOUT  - pin #A1
// HX711.PD_SCK - pin #A0

HX711 scale(A1, A0);    // parameter "gain" is ommited; the default value 128 is used by the library

// variables pour la lecture sur le port serie
//  du microcontroleur

boolean   stringComplete = false;
String     inputString         = "";


void setup() 
{
  // Initialisation du port serie
  Serial.begin(9600);
  inputString.reserve(200);
  
  
  
};

void initMeasure()
{
  Serial.println("----------------------------------------Initialisation------------------------------------------");
  Serial.println("Lecture avant reglage du offset:");
  Serial.print("lecture: \t\t");
  Serial.println(scale.read());      // print a raw reading from the ADC

  Serial.print("lecture moyenne sur 20 mesures: \t\t");
  Serial.println(scale.read_average(20));   // print the average of 20 readings from the ADC

  Serial.print("valeur sur 5 mesures: \t\t");
  Serial.println(scale.get_value(5));   // print the average of 5 readings from the ADC minus the tare weight (not set yet)

  Serial.print("get units: \t\t");
  Serial.println(scale.get_units(5), 1);  // print the average of 5 readings from the ADC minus tare weight (not set) divided 
            // by the SCALE parameter (not set yet)  

  scale.set_scale(-1140.f);                      // this value is obtained by calibrating the scale with known weights; see the README for details
  scale.tare();               // reset the scale to 0

  Serial.println("Mesure apres tarage et reglage du offset:");

  Serial.print("lecture une mesure: \t\t");
  Serial.println(scale.read());                 // print a raw reading from the ADC

  Serial.print("lecture 20 mesure: \t\t");
  Serial.println(scale.read_average(20));       // print the average of 20 readings from the ADC

  Serial.print("mesure 5 valeur avec le offset sans le tarage: \t\t");
  Serial.println(scale.get_value(5));   // print the average of 5 readings from the ADC minus the tare weight, set with tare()

  Serial.print("idem avec le tarage: \t\t");
  Serial.println(scale.get_units(5), 1);        // print the average of 5 readings from the ADC minus tare weight, divided 
            // by the SCALE parameter set with set_scale
  
};
void measure()
{
  scale.power_up();
  delay(200);
  Serial.print("une mesure:\t");
  Serial.print(scale.get_units(), 1);
  Serial.print("\t| moyenne de 10 valeurs:\t");
  Serial.print(scale.get_units(10), 1);
  Serial.println("\t micro deformation");
  scale.power_down();              // put the ADC in sleep mode


}
//////////////////////////////////////////////////////////////////////////////////////////////////
//
//
//      Dialogue Port Serie
//
//
// Ici, on recupere le buffer provenant du port seroe
// et on affecte les variables du micro controleur
/*
  M1     Initialisation
  M2     Mesure
*/


void checkParameters()
// Verifier des codes pour le port serie
{  
 
   if(stringComplete)
   {
     // M100: On lance les POM
     if(inputString.startsWith("M1"))
       {
         initMeasure();
       }
       if(inputString.startsWith("M2"))
       {
         measure();
         
       }       
                       
      inputString       = "";
      stringComplete = false;
   } 
};

  
void loop()
{
  // Dans cette fonction on gere directement certaines variables
  // Directement a partir du port serie
  // Vitesse Table
  
  // Soudage
  checkParameters();
  //vérifie l'état de fin de course et pom
 
  
}



/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read(); 
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    } 
  }
}
