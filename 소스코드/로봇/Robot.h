#ifndef _ROBOT_
#defind _ROBOT_

#include "arduino.h"
#include <SoftwareSerial.h>
#include <Wire.h>
#include <TinyGPS.h>
#include <Adafruit_BMP085_U.h>

#define GPS_RX_PIN 6
#define GPS_TX_PIN 5
#define GPS_BAUD 9600

class Robot {
public :
    class Sensor {
    private:
        String hardness = "0";      //경도값
        String latitude = "0";      //위도값
        String altitud_gps = "0";   //gps고도값
        String altitud = "0";       //고도값
        String temperature = "0";   //온도값

        int rate; //주변 센서와 통신 속도

        TinyGPS gps;
        SoftwareSerial uart_gps;
        Adafruit_BMP085_Unified bmp;

        String Sensing_gps_hardness();  //   gps 경도값 센싱
        String Sensing_gps_latitude();  //   gps 위도값 센싱
        String Sensing_gps_altitud_gps();    //gps고도값 센싱
        String Sensing_altitude_altitude();      //  고도 센서에서 고도값 센싱
        String Sensing_altitude_temperature();   //    고도 센서에서 온도값 센싱
    public :
        begin(int rate); //Sensor 클래스 초기화
        void sening(); //sening 해서 내부 필드에 값 저장

        String get_gps_hardness();  //   gps 경도값 가져오기
        String get_gps_latitude();  //   gps 위도값 가져오기
        String get_gps_altitud_gps();    //gps고도값 가져오기
        String get_altitude_altitude();      //  고도 센서에서 고도값 가져오기
        String get_altitude_temperature();   //    고도 센서에서 온도값 가져오기
    };
};

#endif
