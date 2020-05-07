#ifndef _SENSOR_
#define _SENSOR_

#include "Arduino.h"
#include <String.h>
#include <HardwareSerial.h>
#include <Wire.h>

#include <TinyGPS.h>
#include <Wire.h>
// #include <Adafruit_BMP085_U.h>

#define BAUD_RATE 11520 //ESP32 보드 통신 속도

#define GPS_RX_PIN 6 //GPS RX 핀
#define GPS_TX_PIN 5 //GPS TX 핀

class Sensor {
    private:
        String _hardness;      //경도값
        String _latitude;      //위도값
        String _altitud_gps;   //gps고도값
        String _altitud;       //고도값
        String _temperature;   //온도값

        TinyGPS _gps; //gps 신호를 해석하는 객체

         _serialGPS; //gps 신호를 읽어오는 객체
        // Adafruit_BMP085_Unified _bmp; //고도 센서를 처리하는 객체

        String Sensing_gps_hardness(void);  //   gps 경도값 센싱
        String Sensing_gps_latitude(void);  //   gps 위도값 센싱
        String Sensing_gps_altitud_gps(void);    //gps고도값 센싱
        // String Sensing_altitude_altitude(void);      //  고도 센서에서 고도값 센싱
        // String Sensing_altitude_temperature(void);   //    고도 센서에서 온도값 센싱
    public :
        Sensor();
        void begin(int rate); // 초기화
        void sening(void); //sening 해서 내부 필드에 값 저장

        String get_gps_hardness(void);  //   gps 경도값 가져오기
        String get_gps_latitude(void);  //   gps 위도값 가져오기
        String get_gps_altitud_gps(void);    //gps고도값 가져오기
        // String get_altitude_altitude(void);      //  고도 센서에서 고도값 가져오기
        // String get_altitude_temperature(void);   //    고도 센서에서 온도값 가져오기
};

#endif
