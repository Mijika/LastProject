/*
    Action.h-로봇의 무빙과 라이트, 부저를 제어하는 라이브러리
    2020년 4월 13일 오리가미팀에서 개발
*/
#include "Action.h"


Action::Action() {
    //앞 바퀴 pwm 설정
    ledcSetup(MOVE_FRONT_MOTOR_RIGHT_PWM_CH, 5000, 8);
    ledcSetup(MOVE_FRONT_MOTOR_LEFT_PWM_CH, 5000, 8);
    ledcSetup(DIAMETER_FRONT_MOTORPWM_CH, 5000, 8);
    ledcAttachPin(MOVE_FRONT_MOTOR_RIGHT_PWM, MOVE_FRONT_MOTOR_RIGHT_PWM_CH);
    ledcAttachPin(MOVE_FRONT_MOTOR_LEFT_PWM, MOVE_FRONT_MOTOR_LEFT_PWM_CH);
    ledcAttachPin(DIAMETER_FRONT_MOTOR_PWM, DIAMETER_FRONT_MOTORPWM_CH);
    //뒷 바퀴 pwm 설정
    ledcSetup(MOVE_BACK_MOTOR_RIGHT_PWM_CH, 5000, 8);
    ledcSetup(MOVE_BACK_MOTOR_LEFT_PWM_CH, 5000, 8);
    ledcSetup(DIAMETER_BACK_MOTORPWM_CH, 5000, 8);
    ledcAttachPin(MOVE_BACK_MOTOR_RIGHT_PWM, MOVE_BACK_MOTOR_RIGHT_PWM_CH);
    ledcAttachPin(MOVE_BACK_MOTOR_LEFT_PWM, MOVE_BACK_MOTOR_LEFT_PWM_CH);
    ledcAttachPin(DIAMETER_BACK_MOTOR_PWM, DIAMETER_BACK_MOTORPWM_CH);
    //앞 바퀴 방향및 지름 모터 방향 설정
    pinMode(MOVE_FRONT_MOTOR_RIGHT_EN1, OUTPUT);       // Motor RIGHT 방향설정1
    pinMode(MOVE_FRONT_MOTOR_RIGHT_EN2, OUTPUT);       // Motor RIGHT 방향설정2
    pinMode(MOVE_FRONT_MOTOR_LEFT_EN1, OUTPUT);       // Motor LEFR 방향설정1
    pinMode(MOVE_FRONT_MOTOR_LEFT_EN2, OUTPUT);       // Motor LEFR 방향설정2
    pinMode(DIAMETER_FRONT_MOTOR_EN1, OUTPUT);       // 지름 모터 방향설정1
    pinMode(DIAMETER_FRONT_MOTOR_EN2, OUTPUT);       // 지름 모터 방향설정2
    //뒤 바퀴 방향및 지름 모터 방향 설정
    pinMode(MOVE_BACK_MOTOR_RIGHT_EN1, OUTPUT);       // Motor RIGHT 방향설정1
    pinMode(MOVE_BACK_MOTOR_RIGHT_EN2, OUTPUT);       // Motor RIGHT 방향설정2
    pinMode(MOVE_BACK_MOTOR_LEFT_EN1, OUTPUT);       // Motor LEFR 방향설정1
    pinMode(MOVE_BACK_MOTOR_LEFT_EN2, OUTPUT);       // Motor LEFR 방향설정2
    pinMode(DIAMETER_BACK_MOTOR_EN1, OUTPUT);       // 지름 모터 방향설정1
    pinMode(DIAMETER_BACK_MOTOR_EN2, OUTPUT);       // 지름 모터 방향설정2
}

//전방 라이트 함수
void Action::led_on() { //LED 전등 온
    digitalWrite(LED_RIGHT, HIGH);
    digitalWrite(LED_LEFT, HIGH);
}
void Action::led_off() { //LED 전등 오프
    digitalWrite(LED_RIGHT, LOW);
    digitalWrite(LED_LEFT, LOW);
}

//모터 함수
void Action::move_forward() { //모터 전진
    //앞 바퀴
    digitalWrite(MOVE_FRONT_MOTOR_RIGHT_EN1, HIGH);
    digitalWrite(MOVE_FRONT_MOTOR_RIGHT_EN2, LOW);
    digitalWrite(MOVE_FRONT_MOTOR_LEFT_EN1, LOW);
    digitalWrite(MOVE_FRONT_MOTOR_LEFT_EN2, HIGH);
    ledcWrite(MOVE_FRONT_MOTOR_RIGHT_PWM_CH, MOVE_MOTOR_SPD);
    ledcWrite(MOVE_FRONT_MOTOR_LEFT_PWM_CH, MOVE_MOTOR_SPD);
    //뒷 바퀴
    digitalWrite(MOVE_BACK_MOTOR_RIGHT_EN1, HIGH);
    digitalWrite(MOVE_BACK_MOTOR_RIGHT_EN2, LOW);
    digitalWrite(MOVE_BACK_MOTOR_LEFT_EN1, LOW);
    digitalWrite(MOVE_BACK_MOTOR_LEFT_EN2, HIGH);
    ledcWrite(MOVE_BACK_MOTOR_RIGHT_PWM_CH, MOVE_MOTOR_SPD);
    ledcWrite(MOVE_BACK_MOTOR_LEFT_PWM_CH, MOVE_MOTOR_SPD);
}
void Action::move_reverse() { //모터 후진
    //앞 바퀴
    digitalWrite(MOVE_FRONT_MOTOR_RIGHT_EN1, LOW);
    digitalWrite(MOVE_FRONT_MOTOR_RIGHT_EN2, HIGH);
    digitalWrite(MOVE_FRONT_MOTOR_LEFT_EN1, HIGH);
    digitalWrite(MOVE_FRONT_MOTOR_LEFT_EN2, LOW);
    ledcWrite(MOVE_FRONT_MOTOR_RIGHT_PWM_CH, MOVE_MOTOR_SPD);
    ledcWrite(MOVE_FRONT_MOTOR_LEFT_PWM_CH, MOVE_MOTOR_SPD);
    //뒷 바퀴
    digitalWrite(MOVE_BACK_MOTOR_RIGHT_EN1, LOW);
    digitalWrite(MOVE_BACK_MOTOR_RIGHT_EN2, HIGH);
    digitalWrite(MOVE_BACK_MOTOR_LEFT_EN1, HIGH);
    digitalWrite(MOVE_BACK_MOTOR_LEFT_EN2, LOW);
    ledcWrite(MOVE_BACK_MOTOR_RIGHT_PWM_CH, MOVE_MOTOR_SPD);
    ledcWrite(MOVE_BACK_MOTOR_LEFT_PWM_CH, MOVE_MOTOR_SPD);
}
void Action::move_left_turn() { //모터 좌회전
    //앞 바퀴
    digitalWrite(MOVE_FRONT_MOTOR_RIGHT_EN1, HIGH);
    digitalWrite(MOVE_FRONT_MOTOR_RIGHT_EN2, LOW);
    digitalWrite(MOVE_FRONT_MOTOR_LEFT_EN1, HIGH);
    digitalWrite(MOVE_FRONT_MOTOR_LEFT_EN2, LOW);
    ledcWrite(MOVE_FRONT_MOTOR_RIGHT_PWM_CH, MOVE_MOTOR_SPD);
    ledcWrite(MOVE_FRONT_MOTOR_LEFT_PWM_CH, MOVE_MOTOR_SPD);
    //뒷 바퀴
    digitalWrite(MOVE_BACK_MOTOR_RIGHT_EN1, HIGH);
    digitalWrite(MOVE_BACK_MOTOR_RIGHT_EN2, LOW);
    digitalWrite(MOVE_BACK_MOTOR_LEFT_EN1, HIGH);
    digitalWrite(MOVE_BACK_MOTOR_LEFT_EN2, LOW);
    ledcWrite(MOVE_BACK_MOTOR_RIGHT_PWM_CH, MOVE_MOTOR_SPD);
    ledcWrite(MOVE_BACK_MOTOR_LEFT_PWM_CH, MOVE_MOTOR_SPD);
}
void Action::move_right_turn() { //모터 우회전
    //앞 바퀴
    digitalWrite(MOVE_FRONT_MOTOR_RIGHT_EN1, LOW);
    digitalWrite(MOVE_FRONT_MOTOR_RIGHT_EN2, HIGH);
    digitalWrite(MOVE_FRONT_MOTOR_LEFT_EN1, LOW);
    digitalWrite(MOVE_FRONT_MOTOR_LEFT_EN2, HIGH);
    ledcWrite(MOVE_FRONT_MOTOR_RIGHT_PWM_CH, MOVE_MOTOR_SPD);
    ledcWrite(MOVE_FRONT_MOTOR_LEFT_PWM_CH, MOVE_MOTOR_SPD);
    //뒷 바퀴
    digitalWrite(MOVE_BACK_MOTOR_RIGHT_EN1, LOW);
    digitalWrite(MOVE_BACK_MOTOR_RIGHT_EN2, HIGH);
    digitalWrite(MOVE_BACK_MOTOR_LEFT_EN1, LOW);
    digitalWrite(MOVE_BACK_MOTOR_LEFT_EN2, HIGH);
    ledcWrite(MOVE_BACK_MOTOR_RIGHT_PWM_CH, MOVE_MOTOR_SPD);
    ledcWrite(MOVE_BACK_MOTOR_LEFT_PWM_CH, MOVE_MOTOR_SPD);
}
void Action::move_stop() {
    //앞 바퀴
    digitalWrite(MOVE_FRONT_MOTOR_RIGHT_EN1, LOW);
    digitalWrite(MOVE_FRONT_MOTOR_RIGHT_EN2, LOW);
    digitalWrite(MOVE_FRONT_MOTOR_LEFT_EN1, LOW);
    digitalWrite(MOVE_FRONT_MOTOR_LEFT_EN2, LOW);
    ledcWrite(MOVE_FRONT_MOTOR_RIGHT_PWM_CH, 0);
    ledcWrite(MOVE_FRONT_MOTOR_LEFT_PWM_CH, 0);
    //뒷 바퀴
    digitalWrite(MOVE_BACK_MOTOR_RIGHT_EN1, LOW);
    digitalWrite(MOVE_BACK_MOTOR_RIGHT_EN2, LOW);
    digitalWrite(MOVE_BACK_MOTOR_LEFT_EN1, LOW);
    digitalWrite(MOVE_BACK_MOTOR_LEFT_EN2, LOW);
    ledcWrite(MOVE_FRONT_MOTOR_RIGHT_PWM_CH, 0);
    ledcWrite(MOVE_FRONT_MOTOR_LEFT_PWM_CH, 0);
}

//지름 모터
void Action::front_diameter_up() { // 지름 증가
    digitalWrite(DIAMETER_FRONT_MOTOR_EN1, HIGH);
    digitalWrite(DIAMETER_FRONT_MOTOR_EN2, LOW);
    ledcWrite(DIAMETER_FRONT_MOTORPWM_CH, MOVE_DIAMETER_MOTOR_SPD);
}
void Action::front_diameter_down() { // 지름 감소
    digitalWrite(DIAMETER_FRONT_MOTOR_EN1, LOW);
    digitalWrite(DIAMETER_FRONT_MOTOR_EN2, HIGH);
    ledcWrite(DIAMETER_FRONT_MOTORPWM_CH, MOVE_DIAMETER_MOTOR_SPD);
}
void Action::back_diameter_up() { // 지름 증가
    digitalWrite(DIAMETER_BACK_MOTOR_EN1, HIGH);
    digitalWrite(DIAMETER_BACK_MOTOR_EN2, LOW);
    ledcWrite(DIAMETER_BACK_MOTORPWM_CH, MOVE_DIAMETER_MOTOR_SPD);
}
void Action::back_diameter_down() { // 지름 감소
    digitalWrite(DIAMETER_BACK_MOTOR_EN1, LOW);
    digitalWrite(DIAMETER_BACK_MOTOR_EN2, HIGH);
    ledcWrite(DIAMETER_BACK_MOTORPWM_CH, MOVE_DIAMETER_MOTOR_SPD);
}
