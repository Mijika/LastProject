#include "Robot.h"

void Robot::Sensor::begin(int rate) { //Robot 클래스 초기화
    Serial.println("센서들 초기화 중....");
    uart_gps.begin(BAUD_RATE);
    if(!bmp.begin(BMP085_ULTRAHIGHRES)) {
        Serial.println("BMP180 센서를 찾을 수 없습니다. 연결을 확인해 주세요!");
        return
    }
    if()

    Serial.println("센서들 초기화 완료....");
}

void Robot::Sensor::sening() { //sening 해서 내부 필드에 값 저장
    Serial.println("센싱중... ");
    delay(300);
    hardness = Sensing_gps_hardness();
    latitude = Sensing_gps_latitude();
    altitud_gps = Sensing_gps_altitud_gps();
    altitud = Sensing_altitude_altitude();
    temperature = Sensing_altitude_temperature();
    Serial.println("센싱 완료... ");
}

String Robot::Sensor::Sensing_gps_hardness() {  //gps 경도값 센싱
    /*    gps 경도값 가져오기
       return : (String)경도값
       // float 형의 값을 string 형으로 변환에서 리턴
    */
    float hardness, latitude; // 위도, 경도값을 전달할 변수

    if(uart_gps.available()) {  //버퍼에 데이터가 있는지 확인
        int c = uart_gps.read(); //버퍼에 들어가 있는 값을 c에 저장
        gps.encode(c); // gps 레퍼런스에 gps값 삽입
    }
    else { //없을 경우 오류 메세지 리턴
        return "gps 수신 오류";
    }

    gps.f_get_position(&hardness, &latitude); //위도, 경도갑을 변수에 삽입

    return String.valueOf(hardness); //경도값을 string 형으로 형 변환 하여 리턴
}

String Robot::Sensor::Sensing_gps_latitude() { //gps 위도값 센싱
    /*    gps 위도값 가져오기
       return : (String)위도값
       // float 형의 값을 string 형으로 변환에서 리턴
    */
    float hardness, latitude; // 위도, 경도값을 전달할 변수

    if(uart_gps.available()) {  //버퍼에 데이터가 있는지 확인
        int c = uart_gps.read(); //버퍼에 들어가 있는 값을 c에 저장
        gps.encode(c); // gps 레퍼런스에 gps값 삽입
    }
    else { //없을 경우 오류 메세지 리턴
        return "gps 수신 오류";
    }

    gps.f_get_position(&hardness, &latitude); //위도, 경도갑을 변수에 삽입

    return String.valueOf(latitude); //위도값을 string 형으로 형 변환 하여 리턴
}
String Robot::Sensor::Sensing_gps_altitud() {
    /*    gps 고도값 가져오기
       return : (String)고도값
       // float 형의 값을 string 형으로 변환에서 리턴
    */
    if(uart_gps.available()) {  //버퍼에 데이터가 있는지 확인
        int c = uart_gps.read(); //버퍼에 들어가 있는 값을 c에 저장
        gps.encode(c); // gps 레퍼런스에 gps값 삽입
    }
    else { //없을 경우 오류 메세지 리턴
        return "gps 수신 오류";
    }

    return String.valueOf(gps.f_altitude()); // gps 고도값을 string 형으로 형 변환 하여 리턴
}
String Robot::Sensor::Sensing_altitude_altitude() { //고도 센서에서 고도값 센싱
    /*  고도 센서에서 고도값 가져오기
        //기상청에서 우리나라 해면 기압 확인해서 코드에 반영한다.
            -이유: 고도센서에서 설정한 디폴트 값이 우리 나라의 해면 기압이 아니라서 오차 있음
        return : (String)고도값
        // float 형의 값을 string 형으로 변환에서 리턴
    */
    return String.valueOf(bmp.readAltitude(100560));
}
String Robot::Sensor::Sensing_altitude_temperature() { //고도 센서에서 온도값 센싱
    /*  고도 센서에서 온도값 가져오기
        return : (String)온도값
        // float 형의 값을 string 형으로 변환에서 리턴
    */
     return String.valueOf(bmp.readTemperature());
}

String Robot::Sensor::get_gps_hardness() { //gps 경도값 가져오기
    return hardness;
}
String Robot::Sensor::get_gps_latitude() { //gps 위도값 가져오기
    return latitude;
}
String Robot::Sensor::get_gps_altitud_gps() { //gps고도값 가져오기
    return altitud_gps;
}
String Robot::Sensor::get_altitude_altitude() { //고도 센서에서 고도값 가져오기
    return altitud;
}
String Robot::Sensor::get_altitude_temperature() { //고도 센서에서 온도값 가져오기
    return temperature;
}


//--------------------------------Action--------------------//
void Robot::Action::begin() {
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

void Robot::Action::led_on() { //LED 전등 온
    digitalWrite(LED_RIGHT, HIGH);
    digitalWrite(LED_LEFT, HIGH);
}
void Robot::Action::led_off() { //LED 전등 오프
    digitalWrite(LED_RIGHT, LOW);
    digitalWrite(LED_LEFT, LOW);
}

void Robot::Action::move_forward() { //모터 전진
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
    ledcWrite(MOVE_BACK_MOTOR_RIGHT_PWM_CH, MOVE_BACK_MOTOR_SPD);
    ledcWrite(MOVE_BACK_MOTOR_LEFT_PWM_CH, MOVE_BACK_MOTOR_SPD);
}
void Robot::Action::move_reverse() { //모터 후진
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
    ledcWrite(MOVE_BACK_MOTOR_RIGHT_PWM_CH, MOVE_BACK_MOTOR_SPD);
    ledcWrite(MOVE_BACK_MOTOR_LEFT_PWM_CH, MOVE_BACK_MOTOR_SPD);
}
void Robot::Action::move_left_turn() { //모터 좌회전
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
    ledcWrite(MOVE_BACK_MOTOR_RIGHT_PWM_CH, MOVE_BACK_MOTOR_SPD);
    ledcWrite(MOVE_BACK_MOTOR_LEFT_PWM_CH, MOVE_BACK_MOTOR_SPD);
}
void Robot::Action::move_right_turn() { //모터 우회전
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
    ledcWrite(MOVE_BACK_MOTOR_RIGHT_PWM_CH, MOVE_BACK_MOTOR_SPD);
    ledcWrite(MOVE_BACK_MOTOR_LEFT_PWM_CH, MOVE_BACK_MOTOR_SPD);
}
void Robot::Action::move_stop() {
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
void Robot::Action::front_diameter_up() { // 지름 증가
    digitalWrite(DIAMETER_FRONT_MOTOR_EN1, HIGH);
    digitalWrite(DIAMETER_FRONT_MOTOR_EN2, LOW);
    ledcWrite(DIAMETER_FRONT_MOTORPWM_CH, MOVE_DIAMETER_MOTOR_SPD);
}
void Robot::Action::front_diameter_down() { // 지름 감소
    digitalWrite(DIAMETER_FRONT_MOTOR_EN1, LOW);
    digitalWrite(DIAMETER_FRONT_MOTOR_EN2, HIGH);
    ledcWrite(DIAMETER_FRONT_MOTORPWM_CH, MOVE_DIAMETER_MOTOR_SPD);
}
void Robot::Action::back_diameter_up() { // 지름 증가
    digitalWrite(DIAMETER_MOTOR_EN1, HIGH);
    digitalWrite(DIAMETER_MOTOR_EN2, LOW);
    ledcWrite(DIAMETER_BACK_MOTORPWM_CH, MOVE_DIAMETER_MOTOR_SPD);
}
void Robot::Action::back_diameter_down() { // 지름 감소
    digitalWrite(DIAMETER_BACK_MOTOR_EN1, LOW);
    digitalWrite(DIAMETER_BACK_MOTOR_EN2, HIGH);
    ledcWrite(DIAMETER_BACK_MOTORPWM_CH, MOVE_DIAMETER_MOTOR_SPD);
}
