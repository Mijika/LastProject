/*
    Action.h-로봇의 무빙과 라이트, 부저를 제어하는 라이브러리
    2020년 4월 13일 오리가미팀에서 개발
*/
#ifndef _ACTION_
#define _ACTION_

#include "Arduino.h"



#define LED_RIGHT 5 //오른쪽 전등의 제어 핀
#define LED_LEFT 6 //왼쪽 전등의 제어 핀

//--------------------------------앞 바퀴-----------------------------
#define MOVE_FRONT_MOTOR_RIGHT_EN1 10 //앞쪽_오른쪽 모터의 방향 지시 핀 1
#define MOVE_FRONT_MOTOR_RIGHT_EN2 11 //앞쪽_오른쪽 모터의 방향 지시 핀 2
#define MOVE_FRONT_MOTOR_RIGHT_PWM 12 //앞쪽_오른쪽 모터의 pwm 핀
#define MOVE_FRONT_MOTOR_RIGHT_PWM_CH 0 //앞쪽_오른쪽 모터의 pwm 채널

#define MOVE_FRONT_MOTOR_LEFT_EN1 13 //앞쪽_왼쪽 모터의 방향 지시 핀 1
#define MOVE_FRONT_MOTOR_LEFT_EN2 14 //앞쪽_왼쪽 모터의 방향 지시 핀 2
#define MOVE_FRONT_MOTOR_LEFT_PWM 15 //앞쪽_왼쪽 모터의 pwm 핀
#define MOVE_FRONT_MOTOR_LEFT_PWM_CH 1 //앞쪽_왼쪽 모터의 pwm 채널

#define DIAMETER_FRONT_MOTOR_EN1 13 //앞쪽_바퀴 지름 제어 모터의 방향 지시 핀 1
#define DIAMETER_FRONT_MOTOR_EN2 14 //앞쪽_바퀴 지름 제어 모터의 방향 지시 핀 2
#define DIAMETER_FRONT_MOTOR_PWM 15 //앞쪽_바퀴 지름 제어 모터의 pwm 핀
#define DIAMETER_FRONT_MOTORPWM_CH 2 //앞쪽_지름 모터의 pwm 채널
//--------------------------------앞 바퀴-----------------------------

//--------------------------------뒤 바퀴-----------------------------
#define MOVE_BACK_MOTOR_RIGHT_EN1 16 //뒤쪽_오른쪽 모터의 방향 지시 핀 1
#define MOVE_BACK_MOTOR_RIGHT_EN2 17 //뒤쪽_오른쪽 모터의 방향 지시 핀 2
#define MOVE_BACK_MOTOR_RIGHT_PWM 18 //뒤쪽_오른쪽 모터의 pwm 핀
#define MOVE_BACK_MOTOR_RIGHT_PWM_CH 3 //뒤쪽_오른쪽 모터의 pwm 채널

#define MOVE_BACK_MOTOR_LEFT_EN1 19 //뒤쪽_왼쪽 모터의 방향 지시 핀 1
#define MOVE_BACK_MOTOR_LEFT_EN2 20 //뒤쪽_왼쪽 모터의 방향 지시 핀 2
#define MOVE_BACK_MOTOR_LEFT_PWM 21 //뒤쪽_왼쪽 모터의 pwm 핀
#define MOVE_BACK_MOTOR_LEFT_PWM_CH 4 //뒤쪽_왼쪽 모터의 pwm 채널

#define DIAMETER_BACK_MOTOR_EN1 22 //뒤쪽_바퀴 지름 제어 모터의 방향 지시 핀 1
#define DIAMETER_BACK_MOTOR_EN2 23 //뒤쪽_바퀴 지름 제어 모터의 방향 지시 핀 2
#define DIAMETER_BACK_MOTOR_PWM 24 //뒤쪽_바퀴 지름 제어 모터의 pwm 핀
#define DIAMETER_BACK_MOTORPWM_CH 5 //뒤쪽_지름 모터의 pwm 채널
//--------------------------------뒤 바퀴-----------------------------

#define MOVE_MOTOR_SPD 100 //이동 모터의 스피드
#define MOVE_DIAMETER_MOTOR_SPD 10 //지름 모터의 딜레이

class Action {
    public :
        //초기화 함수
        Action();

        //LED 모듈에 불 들어 오게하는 코딩
        void led_on(void); //LED 전등 온
        void led_off(void); //LED 전등 오프

        //이동 모터 4가지 모드 코딩(void전진, 후진, 왼쪽 턴, 오른쪽 턴)
        void move_forward(void); //모터 전진
        void move_reverse(void); //모터 후진
        void move_left_turn(void); //모터 좌회전
        void move_right_turn(void); //모터 우회전
        void move_stop(void); //모터 정지

        //지름 모터 앞, 뒷 2가지 모드 코딩(void지름 커짐, 작아짐)
        void front_diameter_up(void); // 지름 증가
        void front_diameter_down(void); // 지름 감소
        void back_diameter_up(void); // 지름 증가
        void back_diameter_down(void); // 지름 감소
};

#endif
