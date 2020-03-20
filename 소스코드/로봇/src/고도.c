float bmp180(){
 sensors_event_t event;
  bmp.getEvent(&event);


  if (event.temperature)
  {

    Serial.print("Temperature: ");
    Serial.print(temperature);
    Serial.println(" C");

    float seaLevelPressure = 1020.5;
    Serial.print("Altitude:    ");
    Serial.print(bmp.pressureToAltitude(seaLevelPressure,
                                        event.pressure));

  Serial.println(" m");
    Serial.println("");
  }
  else
  {
    Serial.println("Sensor error");
  }
  delay(1000);
}
