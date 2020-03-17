#ifndef _ROBOT_
#defind _ROBOT_

#include "arduino.h"
#include <SoftwareSerial.h>
#include <Wire.h>
#include <TinyGPS.h>
#include <Adafruit_BMP085_U.h>

#define BAUD_RATE 11520 //ESP32 보드 통신 속도

#define GPS_RX_PIN 6 //GPS RX 핀
#define GPS_TX_PIN 5 //GPS TX 핀

#define LED_RIGHT 5 //오른쪽 lED 전등의 제어 핀
#define LED_LEFT 6 //오른쪽 lED 전등의 제어 핀

#define MOVE_MOTOR_RIGHT_EN1 10 //오른쪽 모터의 방향 지시 핀 1
#define MOVE_MOTOR_RIGHT_EN2 11 //오른쪽 모터의 방향 지시 핀 2
#define MOVE_MOTOR_RIGHT_PWM 12 //오른쪽 모터의 pwm 핀
#define MOVE_MOTOR_RIGHT_PWM_CH 0 //오른쪽 모터의 pwm 채널

#define MOVE_MOTOR_LEFT_EN1 13 //왼쪽 모터의 방향 지시 핀 1
#define MOVE_MOTOR_LEFT_EN2 14 //왼쪽 모터의 방향 지시 핀 2
#define MOVE_MOTOR_LEFT_PWM 15 //왼쪽 모터의 pwm 핀
#define MOVE_MOTOR_LEFT_PWM_CH 1 //왼쪽 모터의 pwm 채널

#define MOVE_MOTOR_SPD 100 //이동 모터의 스피드
#define MOVE_MOTOR_DEL 10 //이동 모터의 딜레이

#define DIAMETER_MOTOR_EN1 13 //바퀴 지름 제어 모터의 방향 지시 핀 1
#define DIAMETER_MOTOR_EN2 14 //바퀴 지름 제어 모터의 방향 지시 핀 2
#define DIAMETER_MOTOR_PWM 15 //바퀴 지름 제어 모터의 pwm 핀
#define DIAMETER_MOTORPWM_CH 2 //지름 모터의 pwm 채널

#define MAIN_UART_RX 1 //ESP32-CMA 과 UART 통신에 사용되는 RX 핀
#define MAIN_UART_TX 2 //ESP32-CMA 과 UART 통신에 사용되는 TX 핀

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
        Adafruit_BMP085_Unified bmp;
        SoftwareSerial uart_gps(GPS_RX_PIN, GPS_TX_PIN);

        String Sensing_gps_hardness();  //   gps 경도값 센싱
        String Sensing_gps_latitude();  //   gps 위도값 센싱
        String Sensing_gps_altitud_gps();    //gps고도값 센싱
        String Sensing_altitude_altitude();      //  고도 센서에서 고도값 센싱
        String Sensing_altitude_temperature();   //    고도 센서에서 온도값 센싱
    public :
        void begin(int rate); //Sensor 클래스 초기화
        void sening(); //sening 해서 내부 필드에 값 저장

        String get_gps_hardness();  //   gps 경도값 가져오기
        String get_gps_latitude();  //   gps 위도값 가져오기
        String get_gps_altitud_gps();    //gps고도값 가져오기
        String get_altitude_altitude();      //  고도 센서에서 고도값 가져오기
        String get_altitude_temperature();   //    고도 센서에서 온도값 가져오기
    };

    class Action {
    public :
        void begin();
        //LED 모듈에 불 들어 오게하는 코딩
        void led_on(); //LED 전등 온
        void led_off(); //LED 전등 오프
        //이동 모터 4가지 모드 코딩(전진, 후진, 왼쪽 턴, 오른쪽 턴)
        void move_forward(); //모터 전진
        void move_reverse(); //모터 후진
        void move_left_turn(); //모터 좌회전
        void move_right_turn(); //모터 우회전
        void move_stop(); //모터 정지
        //지름 모터 2가지 모드 코딩(지름 커짐, 작아짐)
        void diameter_up(); // 지름 증가
        void diameter_down(); // 지름 감소
    };

    class Uart_Communication {
        private :

        public :

    };
};

#endif
